import random

chromosome1=[1,0,1,0,0,0,0,0]
chromosome2=[0,0,0,0,0,0,0,1]

def genetic(chromosome1, chromosome2, prev):
    flag=False
    while not flag:
        i=random.randint(0, 7)
        child=chromosome1[0: i] + chromosome2[i:]
        if (sum(child)>=sum(chromosome1)):
            flag=True
    mp=random.randint(0, 7)
    child[mp]=1
    if sum(child)>prev:
        print(child)
        print(f"Fitness: {sum(child)}")
        prev=sum(child)
    if sum(child)<8:
        chromosome1=child
        genetic(chromosome1,chromosome2,prev)

print(f"Chromosome 1: {chromosome1}")
print(f"Chromosome 2: {chromosome2}")
print("The solution of genetic algorithm are: ")
genetic(chromosome1,chromosome2,0)

    
