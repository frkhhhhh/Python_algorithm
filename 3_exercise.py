numbers=[2,4,7,9,8,5]

def buble_sort(unsorted_list):
    n=len(unsorted_list)
    for i in range(n):
        for a in range(0, n-1):
        
          if unsorted_list[a]>unsorted_list[a+1]:
                unsorted_list[a], unsorted_list[a+1]=unsorted_list[a+1],unsorted_list[a]
                
                
                return unsorted_list, 


print(buble_sort(numbers))
