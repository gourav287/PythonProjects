try:
    import nltk
    from nltk.corpus import words
except ImportError:
    print("nltk is not installed. Please install it using 'pip install nltk'.")

def generateSource(filepath='inputfile.txt'):
    # Download the words dataset if not already downloaded
    try: 
        nltk.data.find('corpora/words.zip')
    except:
        nltk.download('words')

    # Get the list of words
    word_list = words.words()

    five_letter_words = [
        word for word in word_list
        if len(word) == 5
    ]

    # Sort the words alphabetically
    five_letter_words.sort()

    # Join the words with a single space
    output = ' '.join(five_letter_words)

    # Write to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(output)

if __name__ == '__main__':
    generateSource()