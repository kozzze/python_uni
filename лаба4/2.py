'''18. Дан целочисленный массив. Необходимо найти элементы,
расположенные перед первым минимальным.'''
array=[5,6,7,6,5,6,3,7,6,56,7,5]
min=min(array)
for i in range(len(array)+1):
    ind=0
    if array[i]==min:
        ind=i
        break
for i in range(ind+1):
    print(array[i])
