def move_zeros(array):
    #your code here
    non_zeros = []
    zeros = []
    
    for a in array:
        print(a)
        if a != 0 or type(a) == bool:
            non_zeros.append(a)
        else:
            zeros.append(0)
        
    non_zeros.extend(zeros)
    return non_zeros