#python function to reverse words in a sentence

def reversing_words():
    # base code
    '''sentence = input("Enter the sentence:")
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    print (reversed_sentence)
    '''
    # optimize code
    '''sentence = input("Enter the sentence:")
    print(' '.join(sentence.split()[::-1]))'''
    # more optimized 
    reversed_sentence = print(' '.join(input("Enter Sentence: ").split()[::-1]))

reversing_words()