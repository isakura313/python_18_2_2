

names = []
salarys = []

amount = 0
amount_of_members = input("Введите количество членов семьи: ")
aom = int(amount_of_members)

for i in range(aom):
    names.append(input("Введите имя "+ str(i+1) + " человека: "))

for i in range(aom):
    salarys.append(input("Доход "+ str(i+1) + " человека: "))


сredit = input("введите сумму кредита")
how_long = input("на какой срок кредит в месяцах")
procent = input("введите процент")

pay_per_month = (int(сredit) / int(how_long) )+ ((int(сredit)/100 * int(procent))/ 12)

print("Платеж за месяц", pay_per_month)

for salary in salarys:
    amount += int(salary)

mean = (amount - pay_per_month)/aom
# mean = mean - pay_per_month
mean = str(mean)
for name in names:
    print(name.title() + " может потратить " + mean)






# print("privet User!")
# name = input("Введите ваше имя!: ")
# name = name.strip()
# print("Добро пожаловать " + name.title())
# entry1 = input("введите первое число: ")
# entry2 = input("введите второе число: ")
# print(int(entry1) + int(entry2))