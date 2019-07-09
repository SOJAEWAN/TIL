
#import  random
#webbrowser.open('https://google.com')   

import webbrowser
idors = ['소녀시대', '레드벨벳', '트와이스', 'IU']

for idor in idors:
    print(type(idor))
    webbrowser.open(f'https://search.naver.com/search.naver?query={idor}')