def quick(list):

    if len(list)<=1:                          # exit condition of the recursive function it splits untill its one element array
        return list
    
    pivot = list[0]
    
    less_half,great_half = split(list)        #it will take first element as pivot and divides into less than array and greater than array
    
    less= quick(less_half)
    great=quick(great_half)

    return less+[pivot]+great                 #lastly merge all the elements into the same array  as pviot as mid point



def split(list):
    less_half=[]
    great_half=[]

    for i in range(1,len(list)):              # compare from the 1st element as the first element is pivot
        if list[i]<list[0]:
            less_half.append(list[i])
        else:
            great_half.append(list[i])
    
    return less_half ,great_half              # return the both the halfs 

arr =[8,7,6,5,4,3,2,1]

print(quick(arr))
