# Tulajdonképpen törölhetek vele elemeket, de gyakorlatilag nem töröl, hanem
# a kért elemeket adja vissza
"""sdfsdf
sadfsadf
s
adf
as
sdfsdf
dsfsef
"""
nums = [x for x in range(0, 101)]


number = list(filter(lambda x: x % 4 == 0, nums))

print (number)
