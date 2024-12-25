def bubble_sort():
    arr = []
    size = int(input("Enter the array lenght:\n"))
    for element in range(size):
        elements = int(input("Enter an element:"))
        arr.append(elements)
    for i in range(size-1):
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("The sorted array is:\n", arr)   

bubble_sort()