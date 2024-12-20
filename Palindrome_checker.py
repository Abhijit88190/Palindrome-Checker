def is_palindrome(s):
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is the same as its reverse
    return cleaned == cleaned[::-1]

# Main program
if __name__ == "__main__":
    # Prompt the user for input
    user_input = input("Enter a word, sentence, or phrase: ")
    # Check if it's a palindrome
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')