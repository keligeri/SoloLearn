# Tulajdonképpen törölhetek vele elemeket, de gyakorlatilag nem töröl, hanem
# a kért elemeket adja vissza

nums = [x for x in range(0, 51)]


number = list(filter(lambda x: x % 5 == 0, nums))

print (number)
