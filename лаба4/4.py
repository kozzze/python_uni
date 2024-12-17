'''42. Дан целочисленный массив. Найти все элементы, которые
меньше
среднего арифметического элементов массива.'''
array=[1,2,3,4,5,6,7,8,9,10]
sr=sum(array)/len(array)
print(sr)
for i in range(len(array)):
    if array[i]<sr:
        print (array[i])