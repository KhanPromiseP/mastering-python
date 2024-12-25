def binary_search_recursive():
    def binary_search(arr, target_value,low,high):
        if low <= high:
            mid = (high+low)//2
            if arr[mid] == target_value:
                return mid
            elif arr[mid] > target_value:
                return binary_search(arr, target_value, low, mid - 1)
            else:
                return binary_search(arr, target_value, mid+1, high)
        return -1
    arr = [7, 2, 6, 4]
    arr.sort()
    result = print(binary_search(arr, 4 ,0,len(arr)-1))

binary_search_recursive()