# O(n*3)
def ncr(n,r):
    if r > n:
        return 0
    if r > n -r:
        r = n - r
    res = 1
    # print(n,r)
    for i in range(r):
        res *= (n-i)
        res //= (i+1)
    return res

n = 5
ans = []
for i in range(n):
    temp = []
    for j in range(i):
        temp.append(ncr(i, j))
    temp.append(1)
    ans.append(temp)
print(ans)



# O(n^2)
def generate_pascals_triangle(n):
    ans = []
    for i in range(n):
        row = [1] * (i + 1)   # first and last element are always 1
        for j in range(1, i): # fill middle values
            row[j] = ans[i-1][j-1] + ans[i-1][j]
        ans.append(row)
    return ans

n = 5
print(generate_pascals_triangle(n))
