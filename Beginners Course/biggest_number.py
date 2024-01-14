def max_num(num, num2, num3):
    if num >= num2 and num >= num3:
        return num
    elif num2 >= num and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(3, 10, 5))
        
