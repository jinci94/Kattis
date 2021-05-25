binary = input()
binary = '0'*((3-len(binary)%3)%3) + binary
octal = ''
for i in range(0,len(binary),3):
    part = binary[i:i+3]
    count = sum([int(n)*2**(2-i) for i,n in enumerate(part)])
    octal += str(count)
print(octal)
