class House:
    def __init__(self, name, num_flor):
        self.name = name
        self.numbers_of_floors = num_flor


    def __len__(self):
        return self.numbers_of_floors


    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.numbers_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)

print(len(h1))
print(len(h2))
#print(f' Я живу в {self.name} на {self.numbers_of_floors} ')