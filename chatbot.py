# modules/chatbot.py
from llama_cpp import Llama

# Load the local GGUF model
llm = Llama(
    model_path="models/orca-mini-3b-gguf2-q4_0.gguf",  # your model path
    n_ctx=2048,
    n_threads=6   # adjust based on CPU cores
)

def chat_response(prompt: str) -> str:
    try:
        output = llm(
            prompt,
            max_tokens=200,
            stop=["User:", "Astra:"],
            echo=False
        )
        return output["choices"][0]["text"].strip()
    except Exception as e:
        return f"Error generating response: {e}"
