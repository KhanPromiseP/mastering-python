def binary_search(): 
    my_list = []
    arr_size = int(input("Enter array lenght:\n"))
    for i in range(arr_size):
        elements = int(input("Enter and element:"))
        my_list.append(elements)
    my_list.sort()
    target_element = int(input("Enter the target element:\n")) 
    low, high = 0, len(my_list)-1
    while low <= high:
        mid = (high +low)//2
        if my_list[mid] == target_element:
            print(f"The target element {target_element} found at index {mid}")
            break
        elif my_list[mid] < target_element:
            low = mid + 1
        else:
            high = mid - 1
    else:
        print("-1")

binary_search()