# 03_workshop

## 01_문제

```python
  i = input()
def palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:     
            return False
        else:
            return True
print(palindrome(i))            



# def is_palindrome(word):
#     if word == word[::-1]:
    
#         return True
#     else:
#         return False
# print(is_palindrome('level'))
# print(is_palindrome('asd'))



# def is_palindrome(word):
#     list_word = list(word)
#     for i in range(len(list_word) // 2):
#         if list_word[i] != list_word[-i-1]:
#             return False
#     return True

# print(is_palindrome('level'))
# print(is_palindrome('asdf'))
```





