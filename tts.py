import pyttsx3

# Initialize engine once
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text: str):
    """Speak text using pyttsx3"""
    print(f"🤖 Astra: {text}")  # Only print here
    engine.say(text)
    engine.runAndWait()
