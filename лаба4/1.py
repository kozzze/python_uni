#Вариант 6. Задачи 6, 18, 30, 42, 54
'''6. Дан целочисленный массив. Необходимо осуществить
циклический
сдвиг элементов массива влево на три позиции.'''
def shift_left(arr):
    return arr[3:] + arr[:3]
array = [1, 2, 3, 4, 5, 6, 7]
shifted_array = shift_left(array)
print(shifted_array)