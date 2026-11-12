"""Joseph Duran
Chapter 10
This program will show you how to send messages.
8/10
"""
def show_messages(messages):
    """Print each message in the list."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Move each message to the sent messages list."""
    while messages:
        sent_messages.append(messages.pop(0))

messages = ['Hello, world!', 'How are you?', 'I am fine, thank you.']
sent_messages = []

show_messages(messages)

send_messages(messages, sent_messages)

print("\nThe following messages have been sent:")
print("Sent messages:", sent_messages)

