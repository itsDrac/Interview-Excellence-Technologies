from random import randint
def main():
    l = [randint(1,101) for _ in range(10)]
#    l = []
#    while True:
#        n = input("Enter a number for list or type q to exit\n")
#        if n.lower() == 'q':
#            break
#        elif n.isdigit():
#            l.append(int(n))
#        else :
#            print("Invalid Input\nTry again")
#
    print('Sum of numbers', *l ,'is', add_list(l))


def add_list(l):
    return sum(l)

if __name__ == '__main__':
    main()
