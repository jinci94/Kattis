"""
list_github.txt - the list containing completed exercises from github, separated by |
list_kattis.txt - the list containing completed exercises from kattis, separated by \t
"""

def from_kattis():
    file = open('list_kattis.txt', 'r')
    uppg = file.readlines()
    uppg_lst = [x.strip().split('\t') for x in uppg]
    for u in uppg_lst:
        print(f'| [{u[0]}]() | [Python 3]() | {u[-1]} |')
#from_kattis()
# --------------------------------------------------------------
def sorting_by_name(lst):
    return sorted(lst, key=lambda x:x[0])

def sorting_by_difficulty(lst):
    def sorting(x):
        if '-' in x[2]:
            xi = x[2].split('-')[1]
            return xi
        else:
            return x[2]
    return sorted(lst, key=sorting)

def from_github():
    file = open('list_github.txt', 'r')
    uppg = file.readlines()
    uppg_lst = [x.strip().split('|')[1:-1] for x in uppg]
    #sorted_lst = sorting_by_name(uppg_lst)
    sorted_lst = sorting_by_difficulty(uppg_lst)
    for u in sorted_lst:
        print(f'|{u[0]}|{u[1]}|{u[2]}|')
from_github()