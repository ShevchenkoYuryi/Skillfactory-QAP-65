def sort_list(array):
    count = 0
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                count += 1
                array[j], array[j - 1] = array[j - 1], array[j]
    print(f'Отсортированный список: {array}')
    print(f'Число перестановок = {count}')
    print('------------------------------------------')
    return array

def binary_search(array, item):
    start = 0
    fin = len(array) - 1

    while start <= fin:
        middle = (fin + start) // 2
        print(middle)
        if array[middle] == item:
            return middle
        elif item < array[middle]:
            fin = middle - 1
        elif array[middle] < item < array[middle + 1]:
            return print(array.index(array[middle]), array.index(array[middle + 1]))
        else:
            start = middle + 1
    return None


user_nums = input("Введите числа через пробел: ")
num = int(input("Введите число: "))
user_nums = list(map(int, user_nums.split()))
print(f'Первоначальный список: {user_nums}')
print('------------------------------------------')

sort_user_nums = sort_list(user_nums)
binary_search(sort_user_nums, num)