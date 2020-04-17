import random
limit = input("Выбер предел рандома: ")
limit = int(limit)
def game():
    print("Пора проверить свою удачу! ")
    guess_number = input("Выберите любое число до предела: ")
    random_number = random.randint(1, limit)
    if random_number == int(guess_number):
        print("вы выйграли")
        return
    else:
        print("сегодня вам не везет ")
        print("Выйгрышное число было", random_number)
    game()

game()