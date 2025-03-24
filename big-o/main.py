# O(n)
def print_items(n):
    for i in range(n):
        print(i)
    
    # it still O(n) not O(2n)
    # for j in range(n):
    #     print(j)

if __name__ == '__main__':
    print_items(10)

