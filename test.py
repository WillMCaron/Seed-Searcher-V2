from random import randint, seed
seed_nums = open("seeds.txt").readlines()
rangeMax = len(seed_nums)-1
seed_num = int(seed_nums[randint(0,rangeMax)])
seed(seed_num)
print(seed_num, randint(0,100000))
