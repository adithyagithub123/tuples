def palindrome(t):
    length = len(t) - 1
    i = 0
    while(i < length):
        if (t[i] != t[length]):
            return False
        length = length - 1
        i = i + 1
    return True

tuple_1 = (1,2,3,3,2,1)
if (palindrome(tuple_1)) :
    print("it is a flip flop !!")

else :
    print("It isnt a flip flop")