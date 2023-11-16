import sys


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items


def check_palindrome(sentence):
    stack = Stack()

    # Prepare the original sentence by filtering non-alphanumeric characters and converting to lowercase
    original_sentence = "".join(word.lower() for word in sentence if word.isalnum())

    for word in original_sentence:
        stack.push(word)

    # Reverse the sentence by popping characters from the stack
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()

    # Return the original sentence and its reversed form
    return original_sentence, reversed_str


def main():
    while True:
        print("------------------- Welcome to Palindrome Palooza! -------------------")

        # Ask the user to input a word or sentence that will be checked whether it is a palindrome or not
        sentence = input("Enter a sentence: ")

        # We are assigning the variables: original and reverse to the value of check_palindrome() since it will return the corresponding outputs of original and reversed form of the word
        original, reverse = check_palindrome(sentence)

        # We have a conditional statement that will check whether the value of the variables original and reverse are the same
        if original == reverse:
            print(f"The sentence '{sentence}' is a palindrome.\n")
        else:
            print(f"The sentence '{sentence}' is not a palindrome.\n")

        # After stating if the sentence is a palindrome or not, our code will then show how the original and reversed sentences differ
        print("-----------------------------------------")
        print(f"Original sentence: '{original}'")
        print(f"Reversed sentence: '{reverse}'")
        print("-----------------------------------------\n")

        # Once we are done with the Palindrome Palooza, there's a loop that will ask if we want to try again or not
        while True:
            prompt = input("Do you want to try again? [y]/[n]: ").lower()
            if prompt == "y":
                print()
                break
            elif prompt == "n":
                print()
                print("Thank you for using Palindrome Palooza!")
                sys.exit()
            else:
                print("Invalid Input. Please type [y] or [n].")


if __name__ == "__main__":
    main()
