lunch ={
    '양자강': '02-123-1234',
    '새마을식당': '051-123-1234',
    '남다른 감자탕': '010-4104-6770'
}

#1. 방법 1 (csv로 글쓰기)

with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():
        f.write(f'{item[0]}, {item[1]}\n')
