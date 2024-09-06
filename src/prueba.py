import os
import sys
import time
import wave
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from openal import al, alc

def run(sound, distance):
    if len(sys.argv) < 2:
        dirname = os.path.dirname(__file__)
        fname = os.path.join(dirname, sound)
    else:
        fname = sys.argv[1]

    wavefp = wave.open(fname)
    channels = wavefp.getnchannels()
    bitrate = wavefp.getsampwidth() * 8
    samplerate = wavefp.getframerate()
    wavbuf = wavefp.readframes(wavefp.getnframes())
    formatmap = {
        (1, 8) : al.AL_FORMAT_MONO8,
        (2, 8) : al.AL_FORMAT_STEREO8,
        (1, 16): al.AL_FORMAT_MONO16,
        (2, 16) : al.AL_FORMAT_STEREO16,
    }
    alformat = formatmap[(channels, bitrate)]

    device = alc.alcOpenDevice(None)
    context = alc.alcCreateContext(device, None)
    alc.alcMakeContextCurrent(context)

    source = al.ALuint(0)
    al.alGenSources(1, source)

    al.alSourcef(source, al.AL_PITCH, 1)
    al.alSourcef(source, al.AL_GAIN, 1)
    al.alSource3f(source, al.AL_POSITION, distance, 0, 0)
    al.alSource3f(source, al.AL_VELOCITY, 0, 0, 0)
    al.alSourcei(source, al.AL_LOOPING, 0)  

    buf = al.ALuint(0)
    al.alGenBuffers(1, buf)

    al.alBufferData(buf, alformat, wavbuf, len(wavbuf), samplerate)
    al.alSourceQueueBuffers(source, 1, buf)
    al.alSourcePlay(source)

    state = al.ALint(0)
    while True:
        al.alGetSourcei(source, al.AL_SOURCE_STATE, state)
        if state.value != al.AL_PLAYING:
            break
        time.sleep(0)

    al.alDeleteSources(1, source)
    al.alDeleteBuffers(1, buf)
    alc.alcDestroyContext(context)
    alc.alcCloseDevice(device)