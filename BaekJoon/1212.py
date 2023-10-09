from math import pow
octa = input()
octa = octa[::-1]

#print(pow(3,2))
deci = 0
for i in range(len(octa)):
    deci += int(octa[i]) * int(pow(8,i))
binary =''
while deci:
    binary +=str(deci%2)
    #print(deci %2)
    deci = deci //2    

print(binary[::-1])

print(bin(int(input(), 8))[2:])