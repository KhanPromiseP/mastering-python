def linear_search_recursive():
    def linear_search(arr, target,i):
        if i >= len(arr):
            return -1
        elif arr[i] == target:
            return i
        return linear_search(arr,target,i+1)
    arr = [4, 7, 78, 8, 23]
    result = print(linear_search(arr, 7, 0))

linear_search_recursive()
