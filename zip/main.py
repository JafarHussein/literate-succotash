#zip()= Combines multiple iterables into a single iterator

names=["Spongebob", "Patrick", "Squirdward"]
ages=[25,30,35]
jobs=["frycook","unemployed","cashier"]

data=tuple(zip(names, ages, jobs))
print(data)
print()
print()

for name, age, job in data:
    print(f"{name} is a {age} year old {job}")
