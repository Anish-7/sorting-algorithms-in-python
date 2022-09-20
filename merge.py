def merge_sort(list):

    if len(list)<=1: # stoping condition for recursive function (last stack of return)
        return list
    
    mid = len(list)//2      # divides the list in middle

    left_half = list[ :mid]
    right_half = list[mid: ]

   
    left = merge_sort(left_half)        # recursive function till all the elements are arrays of single element
    right = merge_sort(right_half)      # and that single element is returned at end of the stack of calls 

    return merge(left,right)            
                                        #and from that last call it is returned to last but one return that is merge return
def merge(left,right):                  #hence so on the recursive return call are statisfied
    s = []
    i=0
    j=0
    
    while i <len(left) and j< len(right):  # run till all elments are the end index
       
        if left[i]<right[j]:
            s.append(left[i])              #compare one element of one array to another array both are sorted at higher order
            i+=1                           
        else:
            s.append(right[j])
            j+=1
        

    s +=left[i:]                              # if any one of the array lenght is shorter add the remaining array to the list as it is already sorted
    s +=right[j:]

    return s            

arr =[8,7,6,5,4,3,2,1]

print(merge_sort(arr))