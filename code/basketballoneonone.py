x = input()
score = {'A':0, 'B':0}
for i in range(0,len(x),2):
    score[x[i]] += int(x[i+1])
print('A') if score['A'] > score['B'] else print('B')