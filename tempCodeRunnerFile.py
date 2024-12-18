import emoji

def print_emoji_message():
    """
    Prints a message with emojis using the emoji library.
    """
    message = emoji.emojize("Hello, World! :earth_americas: :smile:", language='alias')
    print(message)

    # Custom usage
    custom_message = emoji.emojize("Python is fun! :snake: :sparkles:", language='alias')
    print(custom_message)

# Run the function
if __name__ == "__main__":
    print_emoji_message()
