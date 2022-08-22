import random

for i in range(3):
    print(random.randint(1, 99))

members = ["Kim", "Goh", "Alick"]
leader = random.choice(members)
print(leader)
