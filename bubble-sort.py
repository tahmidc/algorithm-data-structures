## This is a demo bubble sort algorithm ##
## Complexity of O(n^2) ##

def bubble_sort(l):
    switched = True
    while switched:
        #print(l)
        switched=False
        for x in range(len(l)-1):
            if l[x] > l[x+1]:
                switched=True
                l[x], l[x+1] = l[x+1], l[x]
    print(l)

unsorted_list = [9,4,20,1,6,3,11,8,7]                
bubble_sort(unsorted_list)
    
