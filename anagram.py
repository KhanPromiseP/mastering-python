def are_anagram():               
    def anagram_check(word1, word2):
        word1 = word1.replace(" ","").lower()
        word2 = word2.replace(" ","").lower()
        if len(word1) != len(word2):
            return False
        sorted_word1 = sorted(word1)
        sorted_word2 = sorted(word2)
        if sorted_word1 == sorted_word2:
            return True
        else:
            return False
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")
    print(anagram_check(word1, word2))

are_anagram()