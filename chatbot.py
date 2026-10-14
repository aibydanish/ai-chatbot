# Project by @aibydanish | AI Engineer

def ai_chatbot():
    print("AI Chatbot by Danish | Type 'bye' to exit")
    print("-" * 45)
    while True:
        user = input("\nYou: ").lower()
        if user in ['bye', 'exit', 'quit']:
            print("Bot: Goodbye! Thanks for chatting.")
            break
        elif 'hello' in user or 'hi' in user:
            print("Bot: Hello! I'm your AI assistant made by Danish.")
        elif 'your name' in user:
            print("Bot: I'm Danish's AI Bot.")
        else:
            print(f"Bot: You said '{user}' - Tell me more!")

if __name__ == "__main__":
    ai_chatbot()
