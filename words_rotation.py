#python function for words rotation

#base code
def words_rotation():
    '''def are_rotations(word1, word2):
        index = word2.index(word1[0])
        for i in range(len(word1)):
            if word2[index] != word1[i]:
            return False
            index = (index + 1) % len(word1)
        return True 
    print(are_rotations("ABCD", "ACDB"))'''
    
    # work 2
    def are_rotation(word1, word2):
        if len(word1) != len(word2):
            return False
        return sorted(word1) == sorted(word2)
    print(are_rotation("ABCD", "BCAD"))

words_rotation()