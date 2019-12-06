from class_monster import *

#Setup

monster1 = Monster('Paul', ['scary', 'hairy', 'loud'])
print(type(monster1.skills))
print(monster1.skills)
print(monster1.name)

#testing scare_attack()

print('checking if monster can scare_attack properly')
print(monster1.scare_attack())

print('///')
(monster1.add_skills('aaaaa'))
print(monster1.skills)