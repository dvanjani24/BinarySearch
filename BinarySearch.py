
def binary_search(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        if target > array[mid]:
            start = mid + 1
        elif target < array[mid]:
            end = mid - 1
        else: 
            return -1
binary_search([1,2,3,4,5,6,7,8], 5)
