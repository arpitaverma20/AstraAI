# modules/stt.py
import speech_recognition as sr

def take_command():
    """Listen to user voice and return clean text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
        except sr.WaitTimeoutError:
            return None

    try:
        # Recognize using Google Speech Recognition
        transcript = recognizer.recognize_google(audio)
        return transcript.lower().strip()  # Return only clean string

    except sr.UnknownValueError:
        return None  # Could not understand audio
    except sr.RequestError:
        return None  # API was unreachable
