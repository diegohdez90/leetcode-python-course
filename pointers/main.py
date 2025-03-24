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
    
    dict1 = {
        'value': 11
    }
    
    dict2 = dict1
    
    print(dict1)
    print(dict2)
    
    print(f'dict1 points to {id(dict1)}')
    print(f'dict2 points to {id(dict2)}')
    
    dict2['value'] = 22
    print(dict1)
    print(dict2)
    
    print(f'dict1 points to {id(dict1)}')
    print(f'dict2 points to {id(dict2)}')