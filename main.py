# main.py
from modules.stt import take_command
from modules.tts import speak
from modules.chatbot import chat_response
from modules.wikipedia_search import search_wikipedia
from modules.web_browser import open_website
import datetime
import pywhatkit
import random

print("AstraAI is running... Speak something!")
speak("Hello! I am Astra, your assistant. How can I help you?")

last_command = None  # Track previous command to prevent duplicates

while True:
    query = take_command()

    if query is None or len(query.strip()) == 0:
        continue

    query = query.lower().strip()

    # Skip duplicate commands
    if query == last_command:
        continue
    last_command = query

    print(f"You said: {query}")

    # -------------------------
    # Exit condition
    # -------------------------
    if any(word in query for word in ["exit", "quit", "stop"]):
        speak("Goodbye! Have a nice day.")
        break

    # -------------------------
    # Wikipedia search
    # -------------------------
    elif "wikipedia" in query or "who is" in query or "tell me about" in query:
        topic = query.replace("wikipedia", "").replace("who is", "").replace("tell me about", "").strip()
        if topic:
            result = search_wikipedia(topic)
            speak(result)
        else:
            speak("Please tell me a topic to search on Wikipedia.")

    # -------------------------
    # Current time
    # -------------------------
    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    # -------------------------
    # Play music on YouTube
    # -------------------------
    elif query.startswith("play "):
        song = query.replace("play", "").replace("on youtube", "").strip()

        # Predefined trending options
        if song.lower() in ["music", "bollywood"]:
            trending_songs = [
                "Bollywood top hits 2025",
                "Arijit Singh best songs",
                "Party mashup songs"
            ]
            song = random.choice(trending_songs)

        if song:
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)
        else:
            speak("Please tell me the song name to play.")

    # -------------------------
    # Open websites
    # -------------------------
    elif query.startswith("open "):
        site_name = query.replace("open", "").strip()
        message = open_website(site_name)
        speak(message)

    # -------------------------
    # Default → Local chatbot
    # -------------------------
    else:
        response = chat_response(query)
        speak(response)
