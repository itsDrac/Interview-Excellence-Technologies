
def main():
    from random import shuffle, randint
    l = [0]*randint(0,5)+[1]*randint(0,9)
    shuffle(l)
    print(l)
    print(count(l))

def count(l):
    if not l:
        return 0
    ones = 1
    counter = 1
    for i in range(len(l) - 1):
        if l[i] == 1:
            if l[i+1] == 1:
                counter += 1
            else :
                counter = 1
        ones = max(ones, counter)


    return ones


if __name__ == '__main__':
    main()
