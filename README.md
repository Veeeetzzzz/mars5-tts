# MARS5 Text-To-Speech (TTS) Deep Clone

This is a Python implementation for the [MARS5 TTS repo](https://github.com/Camb-ai/MARS5-TTS) that allows you to clone a voice with a command line interface.

Try the [online demo here](https://6b1a3a8e53ae.ngrok.app/) for a quickstart or follow the instructions below to run this project locally/offline

# Installation

Install [Python](https://www.python.org/downloads/)

Clone directory/download [.zip file](https://github.com/Veeeetzzzz/mars5-tts/archive/refs/heads/main.zip)

Open CMD/Powershell in directory and run      
                              
    pip install -r requirements.txt

# Usage

## Visual Studio Code

Download/clone this repo and open the folder in Visual Studio Code

![image](https://github.com/Veeeetzzzz/mars5-tts/assets/40268197/09059ae7-cdfe-4c47-a6a3-07143849377f)

Find your Terminal and run 

    python tts.py # where tts.py is the file name of the Python script

![image](https://github.com/Veeeetzzzz/mars5-tts/assets/40268197/6f525c5c-0c98-4642-961c-82c4d3712e5a)

You'll be taken through the steps to start cloning - fill in your own values or press ENTER for default.

![image](https://github.com/Veeeetzzzz/mars5-tts/assets/40268197/0b4bed6b-2aa0-459e-b765-a45320919cce)


## Command Line/PowerShell

Download/clone this repo and open Command Line/PowerShell from the folder (File -> Open PowerShell Window)

![image](https://github.com/Veeeetzzzz/mars5-tts/assets/40268197/2e1e6077-1d0f-4009-898d-fad2a7b3d386)

There's no impact on us whether we use Command Line or PowerShell. They look the same in terms of input/output.

    python tts.py

![image](https://github.com/Veeeetzzzz/mars5-tts/assets/40268197/ba1fae6e-b614-4ff6-95da-e176717652f4)

# Notes

- Keep reference voice between 6-10 seconds
- Tune config to get optimal output
- Provide transcript when possible
- Use sample provided for ease

# Known issues

- System won't lock up but CPU usage remains at 100% throughout processing stage
- Results will vary - this is not a one shot model but seems far more impressive than ElevenLabs, Speechify at the cost of processing time

# Things to add

- PyTorch CUDA support to reduce procesing times
- Local front end to upload files and preview results
