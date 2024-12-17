'''54. Для введенного списка построить список из элементов,
встречающихся в исходном более трех раз.'''

ar=[]
while True:
        value = input("Введите значение (или нажмите Enter для завершения): ")
        if value == "":  # Если введена пустая строка, выходим из цикла
            break
        else:
            ar.append(int(value))

mas=[]
for i in ar:
    if ar.count(i)>3:mas.append(i)
print(ar)
print(set(mas))