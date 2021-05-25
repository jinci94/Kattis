N = int(input())

def distance(w1, w2):
    keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    for i, line in enumerate(keyboard):
        if w1 in line:
            x1 = i; y1 = line.index(w1)
        if w2 in line:
            x2 = i; y2 = line.index(w2)
    return abs(x1-x2)+abs(y1-y2)

for i in range(N):
    words = {}
    word1, n = input().split()
    for j in range(int(n)):
        word2 = input(); count = 0
        for w1, w2 in zip(word1, word2):
            count += distance(w1, w2)
        words[word2] = count
    lst = sorted(words.items(), key=lambda x:(x[1], x[0]), reverse=False)
    for word, nr in lst:
        print(word, nr)

