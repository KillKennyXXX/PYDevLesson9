from random import randint


class Card:
    def __init__(self):
        self.name = 'Компьютер'  # Имя игрока
        self._barrels = set()  # Множество боченков игрока
        self._cardList = [[0 for j in range(9)] for i in range(3)]  # Карточка игрока
        [self._barrels.add(randint(1, 90)) for i in range(1000) if len(self._barrels) < 15]
        self._barrels = list(self._barrels)
        self._barrels.sort()
        count = 0
        for i in range(3):
            nums = 0
            while nums < 5:
                y = randint(0, 8)
                if self._cardList[i][y] == 0:
                    self._cardList[i][y] = self._barrels[count]
                    nums += 1
                    count += 1
        # print(self._cardList)

    @property
    def barrels(self):
        return self._barrels

    @property
    def cardList(self):
        return self._cardList

    def __str__(self):
        strA = '*' * int(15 - len(self.name) / 2) + ' ' + self.name + ' ' + '*' * int(15 - len(self.name) / 2)
        strC = '*' * 31 + '\n'
        strB = ''
        for i in range(3):
            strB += '\n'
            for j in range(9):
                strB += f' {self._cardList[i][j]} ' if self._cardList[i][j] else '   '
        strB += '\n'

        return strA + strB + strC

    def set_name(self):
        f = input('Как к вам обращаться? ')
        self.name = f if len(f) < 30 and len(f) else 'Игрок'

    def dell_card(self, barrel):
        self._barrels.remove(barrel)
        for i in range(3):
            for j in range(9):
                if self._cardList[i][j] == barrel:
                    self._cardList[i][j] = 0
                    break

    def check_card(self, barrel):
        if barrel in self._barrels:
            self.dell_card(barrel)
            if len(self) >= 1:
                return 1
            else:
                return 2
        else:
            return 0

    def __len__(self):
        return len(self._barrels)

    def __eq__(self, other):
        if self.name == other.name and len(self) == len(other):
            count = len(self)
            while count:
                if self.barrels[count] != other.barrels[count]:
                    return False
                count -= 1
            return True

    def __ne__(self, other):
        return not self == other


class Bag:
    def __init__(self):
        self._barrels = set()
        self._barrel = 0

    @property
    def barrels(self):
        return self._barrels

    @property
    def barrel(self):
        return self._barrel

    def new_barrel(self):
        nums = len(self)
        while nums == len(self):
            barrel = randint(1, 90)
            self._barrels.add(barrel)
        self._barrel = barrel

    def __str__(self):
        return f'\nНовый бочонок {self._barrel}, осталось {90 - len(self)} бочонков.'

    def __len__(self):
        return len(self._barrels)

    def __eq__(self, other):
        if len(self) == len(other):
            count = len(self)
            while count:
                if self.barrels[count] != other.barrels[count]:
                    return False
                count -= 1
            return True

    def __ne__(self, other):
        return not self == other



def game():
    card_user = Card()
    card_user.set_name()
    card_comp = Card()
    bag_new = Bag()
    print('Начинаем игру.')

    while True:
        bag_new.new_barrel()
        print(bag_new)
        print('Ваши карточки:')
        print(card_user)
        print(card_comp)
        user_choice = input('Вычеркиваем бочонок? (Да): ').upper()
        if user_choice == 'ДА':
            check = card_user.check_card(bag_new.barrel)
            if check == 0:
                print('Вы проиграли!')
                break
            elif check == 1:
                print(f'{card_user.name} зачеркнул бочонок {bag_new.barrel}')
            elif check == 2:
                print('Вы выиграли!')
                break
        elif bag_new.barrel in card_user.barrels:
            print('Вы проиграли!')
            break

        if bag_new.barrel in card_comp.barrels:
            check = card_comp.check_card(bag_new.barrel)
            print(f'Компьютер зачеркнул бочонок {bag_new.barrel}')
            if check == 2:
                print('Компьютер выиграл!')
                break



if __name__ == '__main__':
    game()


