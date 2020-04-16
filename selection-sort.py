## This is a demo selection sort algorithm ##
## Complexity of O(n^2) ##

def selection_sort(l):
    spot_marker = 0
    while spot_marker < len(l):
        for num in range(spot_marker, len(l)):
            if l[num] < l[spot_marker]:
                l[spot_marker], l[num] = l[num], l[spot_marker]
        spot_marker +=1
        print(l)
        

unsorted_list = [9,4,20,1,6,3,11,8,7]                
bubble_sort(unsorted_list)
    
