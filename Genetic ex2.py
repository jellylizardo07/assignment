import random

def fitness(individual):
    return sum(individual)  # maximize number of 1s

# Initialize population
population = [[random.randint(0, 1) for _ in range(5)] for _ in range(6)]

for _ in range(20):
    population.sort(key=fitness, reverse=True)
    
    parent1, parent2 = population[0], population[1]
    
    # Crossover
    crossover_point = 2
    child = parent1[:crossover_point] + parent2[crossover_point:]
    
    # Mutation
    if random.random() < 0.1:
        idx = random.randint(0, 4)
        child[idx] = 1 - child[idx]
    
    population[-1] = child

print("Best:", population[0])