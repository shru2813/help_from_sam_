score=int(input())
alex=1
count=1
while alex < score:
    if alex *2 <=score:
        alex *= 2
    else:
        alex+=1
        count +=1
print(count)
