states = ["A", "B"]
actions = ["left", "right"]

# Rewards
rewards = {
    ("A", "right"): 10,
    ("A", "left"): 0,
    ("B", "right"): 0,
    ("B", "left"): 5,
}

# Initialize values
V = {s: 0 for s in states}
gamma = 0.9

for _ in range(10):
    new_V = {}
    for s in states:
        values = []
        for a in actions:
            values.append(rewards.get((s, a), 0) + gamma * V[s])
        new_V[s] = max(values)
    V = new_V

print(V)