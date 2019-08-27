# tar_list = []
# low = 0
# high = len(tar_list)-1
# mid = (high - low)/2


def binary_search(list0, item):
    low = 0
    high = len(list0)-1

    while low < high:
        mid = (high - low)//2
        print(mid)

        guess = list0[mid]
        print(guess)
        # print(guess)
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1
        if guess == item:
            return mid
    return None


if __name__ == "__main__":
    list1 = list(range(100))
    print(list1)
    index = binary_search(list1, 53)
    print(index)
