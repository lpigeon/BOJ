from collections import Counter
import sys

n = int(sys.stdin.readline().rstrip())
n_card = sys.stdin.readline().rstrip().split()
n_card = [int(i) for i in n_card]
m = int(sys.stdin.readline().rstrip())
m_card = sys.stdin.readline().rstrip().split()
m_card = [int(i) for i in m_card]

n_card_count = Counter(n_card)
n_card = list(set(n_card))
n_card.sort()
results = []

def binary_search(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return False

for x in m_card:
    result = binary_search(x, n_card)
    if result == True:
        results.append(n_card_count[x])
    else:
        results.append(0)

print(*results)