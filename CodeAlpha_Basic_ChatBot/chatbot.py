# ── Rule-Based Chatbot ──────────────────────────────────────────

def get_reply(user_input):
    """Return a predefined reply based on the user's input."""
    text = user_input.lower().strip()

    if "hello" in text or "hi" in text or "hey" in text:
        return "Hi there! How can I help you today?"

    elif "how are you" in text or "how r you" in text:
        return "I'm doing great, thanks for asking! How about you?"

    elif "your name" in text or "who are you" in text:
        return "I'm ChatBot, your friendly rule-based assistant!"

    elif "help" in text or "what can you do" in text:
        return "I can respond to greetings, questions, and goodbyes!"

    elif "joke" in text:
        return "Why do programmers prefer dark mode? Light attracts bugs!"

    elif "thanks" in text or "thank you" in text:
        return "You're welcome! Anything else I can help with?"

    elif "good morning" in text:
        return "Good morning! Hope your day is off to a great start!"

    elif "good night" in text:
        return "Good night! Sleep well!"

    elif "bye" in text or "goodbye" in text or "see you" in text:
        return "Goodbye! Have a wonderful day!"

    else:
        return "Hmm, I didn't catch that. Try 'hello', 'how are you', or 'bye'!"


def run_chatbot():
    """Main loop — keeps chatting until the user says bye."""
    print("ChatBot: Hello! I'm ChatBot. Type something to get started!")
    print("         (Type 'bye' to exit)\n")

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            continue

        reply = get_reply(user_input)
        print(f"ChatBot: {reply}\n")

        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            break


# ── Entry point ─────────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()