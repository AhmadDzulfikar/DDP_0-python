n = -1

while n < 3:
    print(n)
    n +=1

    if n > 1:
        print(n**2)
        break
    else:
        continue

else:
    print(n)