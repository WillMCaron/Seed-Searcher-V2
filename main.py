# Hello World: My Version
from random import randint, seed

def search(seed_num, maxnum, placement=1):
    """Returns a number from a random seed from a desired placement"""
    seed(seed_num)
    for o in range(placement):
        number = randint(0,maxnum)
    return number

def generate(count, maxnum, goal, placement = 1):
    """Generates the seed that returns the number at the correct placement"""
    number = randint(0,maxnum)
    while number != goal:
        count+=1
        number = search(count,maxnum,placement)
    return count - 1

def main():
    file = open("seeds.txt","r")
    count = int(file.readlines()[-1])
    file.close()
    file = open("seeds.txt","a+")
    for i in range(300):
        count = generate(count+2,100000,72727,1)
        print(count)
        file.write(str(count)+"\n")

main()
