age = int(input('Сколько Вам полных лет? '))
print(age)

mylist = ['Учиться в деском саду', 'Учиться в школе', 'Учиться в ВУЗе', 'Работает']

def employment_age(age, mylist):
    if age <= 6:
        print(mylist[0])
    elif age <= 17:
        print(mylist[1])
    elif age <= 23:
        print(mylist[2])
    elif age >= 23:
        print(mylist[3])


employment_age(age, mylist)
