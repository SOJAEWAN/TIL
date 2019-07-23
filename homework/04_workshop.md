# 04_workshop

## 01_문제

```python
val = int(input())
result = 0

def sgrt(s, e, count):
    if val < s*s or val > e*e:
        return
    if count > 11:
        global result
        result= (s + e) / 2
        return
    sgrt(s, (s+e)/2, count+1)
    sgrt((s+e)/2, e, count+1)

for i in range(1,val):
    if i * i > val:
        sgrt(i-1, i, 0)
        break
    elif i * i == val:
        result = i
        break
print(result)
```





