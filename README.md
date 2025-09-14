#AstraAI Offline Voice Assistant

This project is an offline voice assistant powered by Python and a local GGUF model. It can recognize voice commands, answer general questions, search Wikipedia, open websites, play YouTube music, and respond through text-to-speech.

💡 #Features:

🗨️ Voice-based interaction using speech-to-text and text-to-speech
🌐 Wikipedia search with summarized answers
🎵 Play YouTube songs (including trending and Bollywood hits)
🔗 Open popular websites like Google, YouTube, LinkedIn, GitHub
⏰ Tell current time
🧠 Local GGUF model (Orca-Mini 3B) for general chatbot responses
🔄 Prevents duplicate commands for a smoother experience
🛠️ Modular design for easy customization and scalability

 🛠️ #Tech Stack:

Technology	Role / Usage
Python 3.10	Core programming language
pyttsx3	Text-to-speech engine for voice output
speech_recognition	Speech-to-text engine for capturing user input
wikipedia	Wikipedia API for search queries
pywhatkit	Play YouTube videos directly from voice command
webbrowser	Open websites in default browser
random, datetime	Select random songs and handle time functions
.gguf	Local GGUF model file for offline chatbot responses


AstraAI/
│
├── main.py                     # Main program: CLI voice assistant
├── requirements.txt            # Python dependencies
│
├── modules/                    # Core modules
│   ├── stt.py                  # Speech-to-text
│   ├── tts.py                  # Text-to-speech
│   ├── wikipedia_search.py     # Wikipedia search module
│   ├── music_player.py         # Play music on YouTube
│   ├── chatbot.py              # Local GGUF model chat
│   └── web_browser.py          # Open websites module
│
├── models/                     # AI models
│   └── orca-mini-3b-gguf2-q4_0.gguf
│
└── assets/                     # Optional: GUI images, icons, avatars
    └── avatar.png

