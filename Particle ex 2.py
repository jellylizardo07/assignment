import random

def fitness(x, y):
    return x**2 + y**2

particles = [[random.uniform(-5, 5), random.uniform(-5, 5)] for _ in range(5)]
velocities = [[0, 0] for _ in range(5)]

pbest = particles[:]
gbest = min(particles, key=lambda p: fitness(p[0], p[1]))

for _ in range(30):
    for i in range(5):
        for d in range(2):
            velocities[i][d] += random.random() * (pbest[i][d] - particles[i][d]) + \
                                random.random() * (gbest[d] - particles[i][d])
            
            particles[i][d] += velocities[i][d]

        if fitness(*particles[i]) < fitness(*pbest[i]):
            pbest[i] = particles[i]

    gbest = min(pbest, key=lambda p: fitness(p[0], p[1]))

print("Best:", gbest)