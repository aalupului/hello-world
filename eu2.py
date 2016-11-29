x = 1
y = x + x
list = []

while y < 4000000:
    if x < y:
        if x % 2 == 0:
            list.append(x)
        all.append(x)
        x = x + y
        # print "X = ", x, "and Y = ", y
    elif x > y:
        if y % 2 == 0:
            list.append(y)
        all.append(y)
        # print "Y = ", y, "and X = ", x
        y = x + y

print all

print list

print "and the sum is: ", sum(list)
