import datetime
import random


class House:
    # Статические поля
    default_id = ''
    default_number = 'No phone'
    default_tarea = 'No faculty'
    default_usearea = 'No course'
    default_floor = 'No group'
    default_rooms = ''
    default_street = 'No street'
    default_typehouse = 'No address'
    default_year = ''
    __typehouse = ("Kirpich", "Panel")
    __street = ("M.Bogdanovicha", "V.Horuzhey")
    __id = ("500/456849", "500/456258", "500/456000")

    def __init__(self, id, number, tarea, usearea, floor, rooms, street, typehouse, year):
        self.id = id
        self.number = number
        self.tarea = tarea
        self.usearea = usearea
        self.floor = floor
        self.rooms = rooms
        self.street = street
        self.typehouse = typehouse
        self.year = year
        #print('New object created!')

    def get_id(self):
        return self.id

    def get_number(self):
        return self.number

    def get_tarea(self):
        return self.tarea

    def get_usearea(self):
        return self.usearea

    def get_floor(self):
        return self.floor

    def get_rooms(self):
        return self.rooms

    def get_street(self):
        return self.street

    def get_typehouse(self):
        return self.typehouse

    def get_year(self):
        return self.year

    def house_age(self, curr_year=2023):
        if (curr_year - self.get_year()) > 50:
            print('VNIMANIE! Neobhodim kapitalnij remont!')
        return curr_year - self.get_year()

    def setBaseParametersOfHouse(self, id, number, tarea, usearea, floor, rooms, street, typehouse, year):
        try:
            if tarea <= usearea:
                raise ValueError("area exception")
            if rooms > 6:
                raise ValueError("too much rooms exception")
            if not isinstance(year, int) or year > datetime.datetime.now().year or year < 1900:
                raise ValueError("year exception")
            self.id = id
            self.number = number
            self.tarea = tarea
            self.usearea = usearea
            self.floor = floor
            self.rooms = rooms
            self.street = street
            self.typehouse = typehouse
            self.year = year
            print('New object created!')
        except ValueError as e:
            print("Base parameters exception: " + str(e))
            return

    @staticmethod
    def getRandomHouse():
        id = '500/000000'
        number = random.randint(1, 132)
        tarea = random.randint(45, 150)
        usearea = 0.7 * tarea
        floor = random.randint(1, 11)
        rooms = random.randint(1, 6)
        street = House.__street[(random.randint(0, len(House.__street) - 1))]
        typehouse = House.__typehouse[(random.randint(0, len(House.__typehouse) - 1))]
        year = random.randint(1986, 2022)
        # newHouse = House()
        newHouse = House(id, number, tarea, usearea, floor, rooms, street, typehouse, year)
        return newHouse

    def __str__(self):
        return f"Street: {self.street}, Year og building: {self.year}, Type of walls: {self.typehouse}, InvNumber: {self.id}, \n" \
               f"Number of flat: {self.number}, Count of rooms: {self.rooms}"

    def __hash__(self):
        return hash((self.id, self.tarea, self.year))

    def __gt__(self, other):
        return self.year > other.year

    def __lt__(self, other):
        return self.year < other.year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year


def info(item):
    print(f'Number of flat: {Allhouses[item].get_number()}')
    print(f'Total area: {Allhouses[item].get_tarea()} sq.m.')
    print(f'Useable area: {Allhouses[item].get_usearea()} sq.m.')
    print(f'Floor of flat: {Allhouses[item].get_floor()}')
    print(f'Number of rooms: {Allhouses[item].get_rooms()}')
    print(f'Street: {str(Allhouses[item].get_street())}')
    print(f'Type of building: {str(Allhouses[item].get_typehouse())}')
    print(f'House age: {Allhouses[item].house_age()}')
    print(f'House id: {Allhouses[item].get_id()}')
    print('---------------')


Allhouses = [House('500/244251', 23, 45, 18, 4, 1, 'M.Bogdanovicha', 'Panel', 2012),
             House('500/225694', 24, 64, 27, 4, 2, 'M.Bogdanovicha', 'Panel', 2007),
             House('500/345557', 25, 57, 30, 5, 2, 'M.Bogdanovicha', 'Panel', 2012),
             House('500/349427', 26, 64, 49, 5, 3, 'M.Bogdanovicha', 'Panel', 2012),
             House('500/345892', 27, 75, 58, 6, 3, 'M.Bogdanovicha', 'Panel', 2002),
             House('500/248754', 28, 84, 65, 6, 4, 'M.Bogdanovicha', 'Panel', 2012),
             House('500/456849', 29, 45, 18, 7, 1, 'M.Bogdanovicha', 'Panel', 2012),
             House('500/256389', 30, 40, 17, 8, 1, 'V.Horuzhey', 'Kirpich', 1995),
             House('500/257893', 23, 40, 17, 7, 3, 'V.Horuzhey', 'Kirpich', 1995),
             House('500/257893', 23, 40, 17, 1, 4, 'V.Horuzhey', 'Kirpich', 1965),
             House('500/257893', 23, 40, 17, 3, 2, 'V.Horuzhey', 'Kirpich', 1995),
             House('500/257893', 23, 40, 17, 6, 1, 'V.Horuzhey', 'Kirpich', 1975),
             House('500/257893', 23, 40, 17, 5, 3, 'V.Horuzhey', 'Kirpich', 1995),
             House('500/145287', 24, 58, 25, 9, 2, 'V.Horuzhey', 'Kirpich', 1968),
             House('500/145287', 27, 75, 37, 7, 3, 'V.Horuzhey', 'Kirpich', 1995)]


def search_group_houses(g):
    for i in range(len(Allhouses)):
        if Allhouses[i].get_typehouse() == g:
            info(i)


def search_year_houses(f):
    for i in range(len(Allhouses)):
        if Allhouses[i].get_year() == f:
            info(i)


def search_numberrooms_houses(n):
    for i in range(len(Allhouses)):
        if Allhouses[i].get_rooms() == n:
            info(i)


def search_nrooms_rangefloor(nr, a, b):
    for i in range(len(Allhouses)):
        if Allhouses[i].get_rooms() == nr and (Allhouses[i].get_floor() >= a and Allhouses[i].get_floor() <= b):
            info(i)


print(Allhouses[1])
print("\n")
print(f"Реализация метода __hash__: {hash(Allhouses[1])}")
print("\n")
print(f"Реализация метода __gt__: {Allhouses[1].__gt__(Allhouses[10])}")
print("\n")
print(f"Реализация метода __lt__: {Allhouses[1].__lt__(Allhouses[10])}")
print("\n")
print(f"Реализация метода __eq__: {Allhouses[1].__eq__(Allhouses[10])}")
print("\n")
print(f"Реализация метода __ne__: {Allhouses[1].__ne__(Allhouses[10])}")