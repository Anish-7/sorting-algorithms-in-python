
def bubble_sort(list):

    sorted = False                                      #lets assume that list is unsorted to get into while
    
    while sorted is False:                              # this loop will run untill list is not sorted
        sorted = True                                   # exit condition when list is sorted
        
        for i in range(len(list)-1):                    # continue condtion if any one pair of numbers are not sorted sorted flag is set to false
                                           
            if list[i]>list[i+1]:
                list[i],list[i+1] =  list[i+1],list[i]
                sorted = False

    return list            
 
arr =[7,6,5,4,3,2,1]

print(bubble_sort(arr))