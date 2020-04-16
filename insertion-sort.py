## This is a demo insertion sort algorithm ##
## Complexity of O(n^2) ##

def insertion_sort(arr):
    for key in range(1, len(arr)):
        if arr[key] < arr[key-1]:
            j = key
            while j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1

l = [6,1,8,4,10,-1,-0.5555555]
insertion_sort(l)
print(l)

    
