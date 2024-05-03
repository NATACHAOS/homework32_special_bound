class House:
    """ДОМ"""

    def __init__(self):
        self.numberOfFloors = 0  # задаём атрибут этажности

    def setNewNumberOfFloors(floors):  # изменим атрибут этажности на floors и выведем на консоль
        floors.numberOfFloors = 10
        print(floors.numberOfFloors)


my_house = House()
my_house.setNewNumberOfFloors()