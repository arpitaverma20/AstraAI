import pywhatkit

def play_song(song_name: str = None, category: str = None) -> str:
    try:
        if category:
            if category.lower() == "bollywood":
                song_name = "latest Bollywood songs"
            elif category.lower() == "party":
                song_name = "party songs"
        if song_name:
            pywhatkit.playonyt(song_name)
            return f"Playing {song_name} on YouTube..."
        else:
            return "No song specified."
    except Exception as e:
        return f"Error playing song: {str(e)}"
