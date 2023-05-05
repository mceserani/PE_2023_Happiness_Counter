"""Calcolatore di felicità"""

n, m = map(int,input().split())

L = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))

H = 0
for i in L:
    if i in A:
        H += 1
    elif i in B:
        H -= 1

print(H)

# test_case expected output: 15
# test_case_long expected output: -100
