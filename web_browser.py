# modules/web_browser.py
import webbrowser
from modules.tts import speak

# Predefined websites
WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "linkedin": "https://www.linkedin.com",
    "instagram": "https://www.instagram.com",
    "github": "https://www.github.com"
}

def open_website(site_name):
    site_name = site_name.lower()
    if site_name in WEBSITES:
        url = WEBSITES[site_name]
        webbrowser.open(url)
        message = f"Opening {site_name}"
        speak(message)  # Astra speaks
        return message
    else:
        message = f"Sorry, I don't know how to open {site_name}"
        speak(message)  # Astra speaks error
        return message
