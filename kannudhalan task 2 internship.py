def count_words(text):
    """Counts the number of words in the given text."""
    words = text.split()  
    return len(words) 

"""Main function to handle user input and output."""
print("Welcome to the Word Counter!")
    
text = input("Enter a sentence or paragraph: ").strip()
    
if not text:
    print("Error: No text provided. Please enter some text.")
else:
    word_count = count_words(text)
    print(f"Word Count: {word_count}")