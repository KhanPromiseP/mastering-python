def are_palindrome():
    def palindrome_check(word):
        word = word.replace(" ","").lower()
        if word == word[::-1]:
            return True
        else:
            return False
    input_word = input("Enter the word: ")
    print(palindrome_check(input_word)) 

are_palindrome()