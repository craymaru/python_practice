# def add_animal_for_list(animal_name, animal_list=None):
#
#     if animal_list is None:
#         animal_list = []
#
#     animal_list.append(animal_name)
#     return animal_list


def add_animal_for_list(animal_name, animal_list=[]):

    animal_list.append(animal_name)
    return animal_list


cat_list = add_animal_for_list("Meow")
print(cat_list)

add_animal_for_list("マンチカン", cat_list)
print(cat_list)

dog_list = add_animal_for_list("Wan")
print(dog_list)

add_animal_for_list("わんわんお", dog_list)
print(dog_list)

kirin_list = []
add_animal_for_list("Super Kirin", kirin_list)
print(kirin_list)

add_animal_for_list("Legendaly Kirin", kirin_list)
print(kirin_list)