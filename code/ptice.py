N = int(input())
answers = input()

adrian = 'ABC'; count_A = 0
bruno ='BABC'; count_B = 0
goran = 'CCAABB'; count_G = 0
for i, c in enumerate(answers):
    if c == adrian[i%3]:
        count_A += 1
    if c == bruno[i%4]:
        count_B += 1
    if c == goran[i%6]:
        count_G += 1
maximum = max([count_A, count_B, count_G])
print(maximum)
print('Adrian') if count_A == maximum else None
print('Bruno') if count_B == maximum else None
print('Goran') if count_G == maximum else None
