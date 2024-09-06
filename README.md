# Post-Apocalyptic Zork Game
## Overview
### This project is a text-based Zork-style game set in a post-apocalyptic Washington D.C. 200 years after a nuclear war. The player, a descendant of survivors living in a bunker, must explore, collect items, and solve puzzles while facing dangers such as locked doors and creatures. The game involves a 3D soundscape using OpenAL for spatialized audio effects that enhance the player’s experience based on in-game events. The goal is to survive, uncover the truth about the player's father, and make a critical decision at the end, influenced by the player's choices throughout the game.

## Team Members
### Carlos Orduz

## Description
### The project consists of two main Python files:

#### prueba.py - This file manages the logic behind audio execution using OpenAL. It loads .wav files and applies 3D spatialization to create immersive audio experiences, adjusting properties like pitch, gain, and position based on player actions.
#### Juego.py - This file contains the core game logic. It handles the narrative, player actions, and the mechanics of the game world, including movement between rooms, inventory management, and interaction with objects. Audio effects from prueba.py are triggered during specific events such as moving, picking up items, or encountering enemies.
#### Key Features
#### Text-Based Gameplay: Players interact with the game using text commands such as "move," "examine," and "collect."
#### Audio Integration with OpenAL: Every action is accompanied by spatialized sound. For example, players hear doors closing or enemies growling from specific directions based on their position.
#### Narrative Structure: The game features a story that unfolds as the player progresses, with a clear beginning, middle, and multiple possible endings depending on the player's decisions.
#### Item Collection and Puzzle Solving: Players must gather items like a key, a lever, and a bullet to unlock doors and defeat enemies.
#### Multiple Endings: The outcome of the game depends on whether the player collects all the notes scattered throughout the bunker, leading to different epilogues.

## Audio Files
### The game makes extensive use of .wav audio files located in the /audio folder. These sounds are crucial for creating the atmosphere and assisting the player with cues. Below is a mapping of audio file usage in the game:

#### titulo.wav: Played at the game's start.
#### newquest.wav: Played when the player receives a new objective.
#### caminar.wav: Played when the player moves between rooms.
#### murometal.wav: Played when the player encounters an inaccessible direction.
#### puertacerrada.wav: Played when the player tries to open a locked door without the necessary item.
#### disparo.wav: Played when the player shoots an enemy.
#### muerte.wav: Played when the player dies.
#### nota.wav: Played when the player examines or picks up a note.
#### recoger.wav: Played when the player collects an item.
#### And many more, including sound effects for final decisions and endings.

### Justification
#### I included over 50 lines of text in the game, but I decided not to assign a unique audio effect to each line. This was to avoid disrupting the flow of gameplay with too many sound interruptions. Instead, I reused some sound effects where they fit naturally in different situations. To keep things organized and easier to manage, I implemented the sound functions in a separate file (prueba.py). This file controls how audio is played based on the distance from the player, which allows me to make adjustments without affecting the main game code.
#### Inspired by the Fallout series, I used a mix of serious and humorous sound effects to match the game’s atmosphere. The gameplay lasts over 5 minutes, thanks to the multiple possible endings, each with its own epilogue, which adds replay value for players to discover different outcomes.
#### I kept the comments in the code simple, mostly to validate the 50+ lines of text and explain specific functions. I also structured the project into clear sections to make it easier to understand and navigate.
