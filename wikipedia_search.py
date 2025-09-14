# modules/wikipedia_search.py
import wikipedia
from modules.tts import speak

# Optional: set language
wikipedia.set_lang("en")

def search_wikipedia(query: str) -> str:
    """
    Search Wikipedia and return a short summary.
    Handles disambiguation and page errors gracefully.
    """
    if not query:
        return "Please provide a topic to search."

    try:
        # Try to get a summary of 2 sentences
        summary = wikipedia.summary(query, sentences=2)
        return summary

    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:5]  # show first 5 options
        option_list = ", ".join(options)
        message = f"Multiple results found for '{query}'. Did you mean: {option_list}?"
        return message

    except wikipedia.exceptions.PageError:
        return f"Sorry, I could not find information on '{query}'."

    except Exception as e:
        return f"An error occurred: {str(e)}"
