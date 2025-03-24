# O(n)
def print_items(n):
    for i in range(n):
        print(i)
    
    # it still O(n) not O(2n)
    # for j in range(n):
    #     print(j)

# O(n^2)
def print_items_2(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

if __name__ == '__main__':
    print_items_2(10)

