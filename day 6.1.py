# Exercise 13: Print multiplication table from 1 to 10

for i in range(1, 11):
    for j in range(1, 11):
        print(j * i, end=" ")
    print(end="\n")