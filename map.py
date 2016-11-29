# megadhatok neki egy functiont első paraméterként és egy iterable-t (listát, tuple, dict ..)
# második paraméterként

nums = [x for x in range(10, 100) if x % 11 == 0]

number = list(map(lambda x: x / 2, nums))

print (number)
