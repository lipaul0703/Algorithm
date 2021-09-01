def binary_search(x, y):
    x_low = 0
    x_high = len(x) - 1
    while x_low <= x_high:
        x_mid = (x_low+x_high) // 2
        if x[x_mid] == y:
            return True, x_mid
        elif x[x_mid] < y:
            x_low = x_mid+1
        elif x[x_mid] > y:
            x_high = x_mid-1
        else:
            return None


if __name__ == '__main__':
    y = -1
    list = [1, 3, 4, 7, 9, 11, 14, 17]
    y_index = binary_search(list, y)
    print(y_index)
