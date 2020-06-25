# Onyx-Audio-Looper

## Goal
Allows simultaneous recording & playback/looping for multiple audio clips.  
Provides interface to audio files with playback controls.

## Current Status
Implemented basic GUI for starting and stopping audio recording (saves to CWD as *output.wav*).  
Added placeholder for audio file display.

## Architectural Decision Records (ADRs)
- Python as main development language 
    - Experience in Python and wide availability of audio libraries
    - Compatibility with PyCharm IDE
- Kivy Python Framework
    - Simple and easy design match simple GUI requirements for fast implementation
    - Cross-platform for future expansion to Android
    - Requires Kivy virtual environment to run
    > *For Windows setup instructions, visit https://kivy.org/doc/stable/installation/installation-windows.html#install-win-dist*