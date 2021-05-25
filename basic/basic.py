"""
x = input()
x = input().split()
N = int(input())
x = [int(x) for x in input().split()]
l = [int(input()) for i in range(N)]

while True:
    try:
        line = input()
    except EOFError:
        break
    if line == '0': # for me to be able to stop it (instead of EOF)
        break

import sys
<< sys.stdin.readline().strip() >> instead of << input() >> for faster code
"""
