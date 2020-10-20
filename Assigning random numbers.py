import random
b=[]
for i in range(50):
    a= random.randint(1,6)
    if a not in b:
        b.append(a)
    else:
        continue
print(b)
