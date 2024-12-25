#python counting vowels function
def counting_vowels():
    string = input("Input sentence:\n")
    count = 0
    vowels = (('a','e','i','o','u'))
    for i in string:
        if i in vowels:
            count+=1
    print(f"The number of vowels is {count}") 

counting_vowels()