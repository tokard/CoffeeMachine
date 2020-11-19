class CoffeeMachine:
    def __init__(self, milk, water, beans, cups, money):
        self.milk = milk
        self.water = water
        self.beans = beans
        self.cups = cups
        self.money = money

    def print_res(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')
        print()

    def buy_coffee(self):
        print('What do you want to buy?')
        print('1. Espresso')
        print('2. Latte')
        print('3. Cappuccino')
        print('back - to main menu')
        choice = input()
        if choice.isdigit():
            choice = int(choice)
        if choice == 1:
            if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
            elif self.water < 250:
                print('Sorry, not enough water')
            elif self.beans < 16:
                print('Sorry, not enough beans')
            elif self.cups < 1:
                print('Sorry, not enough cups')
        elif choice == 2:
            if self.water >= 350 and self.beans >= 20 \
                    and self.cups >= 1 and self.milk >= 75:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
            elif self.water < 350:
                print('Sorry, not enough water')
            elif self.beans < 20:
                print('Sorry, not enough beans')
            elif self.cups < 1:
                print('Sorry, not enough cups')
            elif self.milk < 75:
                print('Sorry, not enough milk')
        elif choice == 3:
            if self.water >= 200 and self.beans >= 12 \
                    and self.cups >= 1 and self.milk >= 100:
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
            elif self.water < 200:
                print('Sorry, not enough water')
            elif self.beans < 12:
                print('Sorry, not enough beans')
            elif self.cups < 1:
                print('Sorry, not enough cups')
            elif self.milk < 100:
                print('Sorry, not enough milk')
        print()

    def take_money(self):
        print(f'I gave you {self.money}')
        self.money = 0

    def fill(self):
        water_add = int(input('Write how many ml of water do you want to add: '))
        milk_add = int(input('Write how many ml of milk do you want to add: '))
        beans_add = int(input('Write how many grams of coffee beans do you want to add: '))
        cups_add = int(input('Write how many disposable cups of coffee do you want to add: '))
        self.milk += milk_add
        self.water += water_add
        self.beans += beans_add
        self.cups += cups_add
        print()

    def action(self):
        while True:
            act = input('Write action (buy, fill, take, remaining, exit): ')
            if act == 'buy':
                self.buy_coffee()
            elif act == 'fill':
                self.fill()
            elif act == 'take':
                self.take_money()
            elif act == 'remaining':
                self.print_res()
            else:
                break


coffee = CoffeeMachine(540, 400, 120, 9, 550)
coffee.action()