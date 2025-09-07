# Voice Assistant

A real-time AI voice assistant built with Python using the [ElevenLabs Conversational AI API](https://elevenlabs.com/). Speak naturally, get lifelike responses, and customise prompts, schedules, and user info. It is useful for exploring conversational AI, Python audio, and interactive voice applications.

---

## Features

- Real-time speech recognition and synthesis  
- Customisable assistant prompts and first message  
- Easy configuration with a `.env` file  
- Works on Windows with PyAudio  

---

## Getting Started

### 1. Clone the repository

"git clone https://github.com/Deeksha1709/voice_assistant.git"  
"cd voice_assistant"

### 2. Create and activate a virtual environment
"python -m venv .venv"    
".\.venv\Scripts\Activate.ps1"   #Windows PowerShell

### 3. Install required Python packages
"pip install --upgrade pip"  
"pip install python-dotenv elevenlabs[pyaudio]"

### 4. Configure environment variables
- Copy the example environment file:  
"copy .env.example .env"
- Open .env in a text editor and add your AGENT_ID and API_KEY from ElevenLabs.
- Optional: set USER_NAME and SCHEDULE to personalise your assistant.

### 5. Run the voice assistant
"python voice_assistant.py"  
- Speak into your microphone and the assistant will respond in real time.

---

## Tips

- Make sure your microphone is set as the default recording device in Windows.
- Close other apps that might be using your microphone to avoid PyAudio errors.
- Customise the first message and system prompt in voice_assistant.py to change the assistant’s behavior.
