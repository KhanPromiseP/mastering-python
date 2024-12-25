#python function to count the maximum frequent letter in a sentence

def max_frequant_letter():
    sentence = input("Enter the Sentence: ")
    sentence = sentence.lower()
    highest_frequent_letter = []
    highest_frequency = 0
    for letter in sentence:
        if letter.isalpha:
            friquency = sentence.count(letter)
        if friquency > highest_frequency:
            highest_frequency = friquency
            highest_frequent_letter = [letter]
        elif friquency == highest_frequency:
            highest_frequent_letter.append(letter)
    if len(highest_frequent_letter) == 1:
        print("The highest friquent letter is: ", highest_frequent_letter[0])
    else:
        result = set(highest_frequent_letter)
        print("The highest friquent letters are: ",", ".join(result ))

max_frequant_letter()