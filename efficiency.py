# Hello World: My Version
from random import randint, seed

file = open("seeds.txt","r")
count = int(file.readlines()[-1])
file.close()

def generate():
    """Generates the seed that returns the number at the correct placement"""
    global count
    seed(count)
    number = randint(0,100000)
    while number != 72727:
        count+=1
        seed(count)
        number = randint(0,100000)

file = open("seeds.txt","a+")
for i in range(10000):
    count+=1
    generate()
    print(i+1,"\t",count)
    file.write(str(count)+"\n")
