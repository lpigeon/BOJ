# 그룹 단어 체커

result = 0
for i in range(int(input())):
    s = input()
    if list(s) == sorted(s, key=s.find):
        result += 1
print(result)