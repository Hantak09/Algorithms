import random
import sorting


def main():
    x = [i for i in range(10)]
    random.shuffle(x)
    print(x)
    sorting.quicksort_inplace(x, 0 , len(x) - 1)
    print(x)

if __name__ == '__main__':
    main()
