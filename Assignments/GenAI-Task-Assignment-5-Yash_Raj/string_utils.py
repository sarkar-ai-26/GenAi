#Method to return text with each word capitalized
def capitalize_words(text):
    return text.upper()

#Method to return the reverse of string provided
def reverse_string(text):
    return text[::-1]

#Method to return the count of the text provided
def word_count(text):
    newText = text.strip()
    return len(newText)
