tuple_1 = (1,0,0,0,1,1,0)
sunny = 0
rainy = 0
for i in range(0,7) :
    if (tuple_1[i] == 0):
        sunny = sunny + 1
    else :
        rainy = rainy + 1

if (sunny > rainy) :
    print("Its a sunny weather")
else :
    print("its a rainy weather")
