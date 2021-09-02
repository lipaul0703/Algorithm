# import time
def number_keyin(j):
    global number_list
    i = 1
    number_array = [0] * 11
    number_list = []
    print(number_array)
    for i in range(j):
        x = int(input("請輸入數字_%d = " % i))
        number_list.append(x)
        i += 1
    print("輸入數字為:", number_list)
    for i in number_list:
        number_array[i] += 1
    return number_array


def bucket_sort_as(list_input):  # in ascending order
    i = 0
    number_sort = []
    for j in list_input:
        for k in range(j):
            number_sort.append(i)
            k += 1
        i += 1
    return number_sort


def bucket_sort_des(list_input):  # in descending order
    i = 10
    list_input = list_input[::-1]
    number_sort = []
    for j in list_input:
        for k in range(j):
            number_sort.append(i)
            k += 1
        i -= 1
    return number_sort


if __name__ == '__main__':
    number_list = number_keyin(5)
    print("各數字出現次數:", number_list)
    number_sort_as = bucket_sort_as(number_list)
    print("由小排序到大:", number_sort_as)
    number_sort_des = bucket_sort_des(number_list)
    print("由大排序到小:", number_sort_des)
