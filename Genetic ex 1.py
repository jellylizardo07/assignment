import random

# Fitness function
def fitness(x):
    return x**2

# Generate population
population = [random.randint(0, 10) for _ in range(6)]

for generation in range(10):
    population = sorted(population, key=fitness, reverse=True)
    
    # Select top 2
    parent1, parent2 = population[0], population[1]
    
    # Crossover
    child = (parent1 + parent2) // 2
    
    # Mutation
    if random.random() < 0.2:
        child += random.randint(-1, 1)
    
    population[-1] = child

print("Best solution:", population[0])