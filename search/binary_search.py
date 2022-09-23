
def binary_search(list,key):
    
    start_index=0
    end_index =len(list)-1
    
    while start_index<=end_index:

        mid=(start_index+end_index)//2

        if list[mid] == key:
            return mid
        elif key <list[mid]:
            end_index=mid-1

        else:
            start_index = mid 

    return None  

ar =[1,2,3,4,5]
print(binary_search(ar,1))
