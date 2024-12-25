#Ultimate solution for capitalizing all first letters in a paragraph

def first_letter_capitalizing():            
    '''sentence = input("Enter the sentence:")
    words = sentence.split()
    capitalized_words = (word.capitalize()for word in words)
    capitalized_sentence = ' '.join(capitalized_words)
    print(capitalized_sentence)'''

    # OR
    sentence = input("Enter Sentence: ")
    str= print(' '.join(leter.capitalize()for leter in sentence.split()))
    
first_letter_capitalizing()