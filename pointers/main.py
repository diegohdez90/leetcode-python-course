if __name__ == '__main__':

    num1 = 11
    num2 = num1
    
    print(num1)
    print(num2)
    
    print(f'num1 points to {id(num1)}')
    print(f'num2 points to {id(num2)}')
    num2 = 22
    
    print(num1)
    print(num2)
    
    print(f'num1 points to {id(num1)}')
    print(f'num2 points to {id(num2)}')