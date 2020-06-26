def even(numbers):
    result=[]
    for a in numbers:
        if a % 2 == 0:
            result.append(a)
    return result 

def sum_up_list(numbers):
    result=[]
    for a in numbers:   
        result.append(a)
    return sum(result)

def return_maximum(numbers):
    result=[]
    for a in numbers:   
        result.append(a)
    return max(result)
        
    
print(even[1,2,3,4,5,6,7,8,9]) 
print(sum_up_list[1,2,3,4,5,6,7,8,9]) 
print(return_maximum[1,2,3,4,5,6,7,8,9])  