# Basics
for i in range(151):
    print(i)

# Multiple of Five
for i in range(5, 1005, 5):
    print(i)

# Counting, the Dojo Way
for i in range(1, 101):
    if i % 10 == 0:
        print("CodingDojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Whoa. That Sucker's Huge
sum = 0
for i in range(1, 500000, 2):
    sum += i
print(sum)

# Countdown by Fours
for i in range(2018, 0, -4):
    print(i)

# Flexible Counter
low_num = 2
high_num = 33
mult = 3
for i in range(low_num, high_num + mult):
    if i % mult == 0:
        print(i)
