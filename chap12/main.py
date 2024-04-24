student = {
  'name' : 'Maria',
  'id_number' : 1234,
  'scores' : [90, 95, 88]
}

animal_info = {}

print(student)
print(student['name'])

print(animal_info)

print("*****************************")

favorite_ic_flavors = {
   'Mom' : 'vanilla',
   'Jerry' : 'Cherry Garcia',
   'Ben' : 'Chocolate Fudge Brownie',
   'Jenny' : 'Mint Chocolate Chip',
   'Odd choice' : 'pickled mango',
   'teachher' : 'Rocky Road'
}

print(favorite_ic_flavors)


favorite_ic_flavors["Mom"] = "chocolate chip"
favorite_ic_flavors["Klee"] = "reeses penut butter ice cream"
del(favorite_ic_flavors["Odd choice"])
favorite_ic_flavors["teacher"] = favorite_ic_flavors["teachher"]
del(favorite_ic_flavors["teachher"])

print(favorite_ic_flavors)

print("*****************************")


text = "What does the fox say?"
words = ['What', 'does', 'the', 'fox', 'say?']
state_capitals = {
   'MO' : 'Jefferson City',
   'CA' : 'Sacramento',
   'TX' : 'Austin',
   'HI' : 'Honolulu'
}

print(len(text))
print(len(words))
print(len(state_capitals))

print("*****************************")

num_animals = {
   'lions' : 3,
   'tigers' : 2,
   'bears' : 8,
   'pigeons' : 3000,
   'snakes' : 37,
   'Koalas' : 3
}

print(min(num_animals))
print(min(num_animals.items()))
print(max(num_animals.values()))