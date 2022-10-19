from random import randint


class Card:
    def __init__(self):
        self.name = 'Компьютер'  # Имя игрока
        self.barrels = set()  # Множество боченков игрока
        self.cardList = [[0 for j in range(9)] for i in range(3)]  # Карточка игрока
        [self.barrels.add(randint(1, 90)) for i in range(1000) if len(self.barrels) < 15]
        self.barrels = list(self.barrels)
        self.barrels.sort()
        count = 0
        for i in range(3):
            nums = 0
            while nums < 5:
                y = randint(0, 8)
                if self.cardList[i][y] == 0:
                    self.cardList[i][y] = self.barrels[count]
                    nums += 1
                    count += 1

    def view(self):
        print('*' * int(15 - len(self.name) / 2) + ' ' + self.name + ' ' + '*' * int(15 - len(self.name) / 2))
        for i in range(3):
            strA = ''
            for j in range(9):
                strA += f' {self.cardList[i][j]} ' if self.cardList[i][j] else '   '
            print(strA)
        print('*' * 31)

    def get_name(self):
        f = input('Как к вам обращаться? ')
        self.name = f if len(f) < 30 and len(f) else 'Игрок'

    def dell_card(self, barrel):
        self.barrels.remove(barrel)
        for i in range(3):
            for j in range(9):
                if self.cardList[i][j] == barrel:
                    self.cardList[i][j] = 0
                    break

    def check_card(self, barrel):
        if barrel in self.barrels:
            self.dell_card(barrel)
            if len(self.barrels) >= 1:
                return 1
            else:
                return 2
        else:
            return 0


class Bag:
    def __init__(self):
        self.barrels = set()

    def new_barrel(self):
        nums = len(self.barrels)
        while nums == len(self.barrels):
            barrel = randint(1, 90)
            self.barrels.add(barrel)
        return barrel

    def view(self, barrel):
        return f'Новый боченок {barrel}, осталось {90 - len(self.barrels)} бочонков.'


def game():
    card_user = Card()
    card_user.get_name()
    card_comp = Card()
    bag_new = Bag()
    print('Начинаем игру.')

    while True:
        barrel = bag_new.new_barrel()
        print(bag_new.view(barrel))
        print('Ваши карточки:')
        card_user.view()
        card_comp.view()
        user_choice = input('Вычеркиваем боченок? (Да): ').upper()
        if user_choice == 'ДА':
            check = card_user.check_card(barrel)
            if check == 0:
                print('Вы проиграли!')
                break
            elif check == 1:
                print(f'{card_user.name} зачеркнул боченок {barrel}\n')
            elif check == 2:
                print('Вы выиграли!')
                break
        elif barrel in card_user.barrels:
            print('Вы проиграли!')
            break


        if barrel in card_comp.barrels:
            check = card_comp.check_card(barrel)
            print(f'Компьютер зачеркнул боченок {barrel}')
            if check == 2:
                print('Компьютер выиграл!')
                break
        print()

if __name__ == '__main__':
    game()


