# Archived Messages
def send_messages(messages, sent_messages):
    """ Print a series of short text messages and moves each message to a new list as it’s printed. """
    messages.reverse()
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


messages = ['a', 'b', 'c', 'd']
sent_messages = []
send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)
