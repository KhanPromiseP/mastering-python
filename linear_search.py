def linear_search():   
    size = int(input("Enter the size of the array:\n"))
    my_list = []
    for i in range(size):
        arr_elements = int(input("Enter an element:"))
        my_list.append(arr_elements)
    target_element = int(input("Enter target element:\n"))
    for j in range(len(my_list)):
        if my_list[j] == target_element:
            print(f"The target element {target_element} is found at index {j}")
        break 
    else:   
        print(f"{-1}\n Element not found!!!")  

linear_search()