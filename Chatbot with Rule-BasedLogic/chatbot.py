import random
from datetime import datetime

# Color support for terminal (Windows-friendly)
try:
    from colorama import init, Fore, Style
    init()
    use_colors = True
except ImportError:
    use_colors = False

# Chatbot greeting
def colorful(text, color=None):
    if not use_colors:
        return text
    return getattr(Fore, color.upper(), Fore.WHITE) + text + Style.RESET_ALL

def chatbot():
    print(colorful("🤖 RuleBot is online! Type 'exit' to leave the chat.", "cyan"))
    print(colorful("✨ I'm friendly, a bit sarcastic, and know the time and date!", "magenta"))

    chat_history = []

    while True:
        user_input = input(colorful("You: ", "green")).lower().strip()
        chat_history.append(f"You: {user_input}")
        
        if user_input == "exit":
            print(colorful("RuleBot: Bye! Hope I was at least mildly helpful. 😎", "yellow"))
            break

        elif any(greet in user_input for greet in ["hi", "hello", "hey", "yo"]):
            responses = ["Hey there! 👋", "Hi! Need something?", "Hello, human! 🤖"]
            reply = random.choice(responses)

        elif "your name" in user_input:
            reply = "I'm RuleBot, version 2.0. I'm not famous yet, but I'm working on it. 😎"

        elif "how are you" in user_input:
            reply = "I'm 100% CPU-powered and emotionally stable. Thanks for asking! 😄"

        elif "time" in user_input:
            now = datetime.now().strftime("%I:%M %p")
            reply = f"The current time is {now} ⏰"

        elif "date" in user_input:
            today = datetime.now().strftime("%A, %B %d, %Y")
            reply = f"Today is {today} 📅"

        elif "help" in user_input:
            reply = "Try asking me about the time, date, or say hi! I'm here to entertain."

        elif "joke" in user_input:
            jokes = [
                "Why did the computer show up late to work? It had a hard drive. 😆",
                "I would tell you a UDP joke, but you might not get it. 😂",
                "Debugging: Being the detective in a crime movie where you are also the murderer. 🕵️‍♂️"
            ]
            reply = random.choice(jokes)

        else:
            reply = "Umm... I didn’t quite get that. I'm still learning 🧠"

        print(colorful(f"RuleBot: {reply}", "yellow"))
        chat_history.append(f"RuleBot: {reply}")

    # Save chat history (optional)
    with open("chat_history.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(chat_history))

# Run it
chatbot()
