# Countdown
def countdown(num):
    countdown_list = []
    for i in range(num, -1, -1):
        countdown_list.append(i)
    print(countdown_list)


countdown(5)


# Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]


p_r = print_and_return([1, 2])
print(p_r)


# First Plus Length
def first_plus_length(list):
    return list[0] + len(list)


f_p_l = first_plus_length([1, 2, 3, 4, 5])
print(f_p_l)


# Values Greater than Second
def values_greater_than_second(list):
    new_list = []
    greater_than = 0
    for i in list:
        if len(list) < 2:
            return False
        elif i > list[1]:
            new_list.append(i)
            greater_than += 1
    print(greater_than)
    return new_list


vgts1 = values_greater_than_second([5, 2, 3, 2, 1, 4])
vgts2 = values_greater_than_second([3])

print(vgts1)
print(vgts2)


# This length, That Value
def length_and_value(size, value):
    list = []
    while len(list) < size:
        list.append(value)
    return list


l_v1 = length_and_value(4, 7)
l_v2 = length_and_value(6, 2)

print(l_v1)
print(l_v2)
