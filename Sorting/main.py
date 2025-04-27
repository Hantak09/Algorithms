import random




def main():
    x = [i for i in range(10)]
    random.shuffle(x)
    print(x)
    print(quicksort(x))


if __name__ == '__main__':
    main()
