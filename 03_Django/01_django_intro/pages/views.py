from django.shortcuts import render
from datetime import datetime
import random
import requests

#1. 기본로직
def index(request):
    return render(request,'pages/index.html')

def introduce(request):
    return render(request, 'pages/introduce.html')

def image(request):
    return render(request, 'pages/image.html')

#2. Template Variable(템플릿 변수)    
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick' : pick}
    return render(request, 'pages/dinner.html', context)

#3. Variable Routing(동적 라우팅)
def hello(request, name, age):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    # names = ['justin', 'john', 'jason', 'juan', 'zzulu']
    
    # name = random.choice(names)
    context = {
        'name': name, 
        'age': age, 
        'pick': pick,
    }
    return render(request, 'pages/hello.html', context)

#4. 실습
#4-1. 동적 라이팅을 활용해서(name과 age를 인자로 받아) 자기소개 페이지
def introduce2(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'pages/introduce2.html', context)

#4-2. 두개의 숫자를 인자로 받아(num1, num2) 곱세 결과를 출력
def multiple(request, num1, num2):
    result = num1 * num2
    context = {
       'result': result
    }
    return render(request, 'pages/multiple.html', context)

#4-3. 반지름(r)를 인자로 받아 원의 넓이(area)를 구하시오.
def get_area(request, r):
    area = 3.14 *(r**2)
    context = {
        'r': r,
        'area': area,
    }
    return render(request, 'pages/get_area.html', context)

#5. DTL(Django Template Language)
def template_language(request):
    menus = ['짜장면', '짬퐁', '양장피', '탕수육']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = ['하하하하']

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }

    return render(request, 'pages/template_language.html', context)

    #6. 실습
    #6-1. isbirth
def isbirth(request):
    today = datetime.now()
    month = today.month
    day = today.day
    print(today.month)
    print(today.day)
    context = {
        'month': month,
        'day': day,
        'True': True,
        'False': False,
    }
    return render(request, 'pages/isbirth.html', context)

    #6-2. 회문판별
    # 회문이면 회문입니다.
    # 회문이 아니면 '회문이 아닙니다.'
def ispal(request, word):
    if list(word) == list(reversed(word)):
        result = '회문입니다'
    else:
        result = '회문이 아닙니다.'

    context = {
        'result': result,
    }

    return render(request, 'pages/ispal.html', context)




    #6-3. 로또 번호 추첨
    # lottos -> 1 ~45번까지의 번호 중 6개를 랜덤으로 pick한 리스트
    # real_lottos ->[21, 24, 30, 32, 40, 42]
    #1. 1ottos 번호를 하나씩 출력(DTL-for문)
    #2. 컴시기가 뽑은 로또 번호와 실제 로또 당첨 번호를 비교해보기(DTL-if문)
def lottos(request):
    lottos = sorted(random.sample(range(1, 46),6))
    real_lottos = [21, 24, 30, 32, 40, 42]
    

    context = {
        'lottos': lottos,
        'real_lottos': real_lottos,
    }

    return render(request, 'pages/lottos.html', context)


#7. Form - GET

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message': message,
        'message2': message2,
    }
    return render(request, 'pages/catch.html', context)


def ping(request):
    return render(request, 'pages/ping.html')

def pong(request):
    heart = request.GET.get('heart')
    heart2 = request.GET.get('heart2')

    context = {
        'heart': heart,
        'heart2': heart2,
    }

    return render(request, 'pages/pong.html', context)

#8. Form - GET 실습(아스키 아티)
def art(request):
    return render(request, 'pages/art.html')

def result(request):
    #1. form으로 날린 데이터를 받는다.(GET)
    word = request.GET.get('word')

    #2. ARTII api로 요청을 보낸 응답 결과를 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    #3. fonts(str)를 fonts(list)를 바꾼다.
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서 
    # font라는 변수에 저장
    font = random.choice(fonts)
    
    #5. 위에서 사용자에게 받은 word와 font를 가지고 다시 
    # 요청을 보낸다. 그리고 응답 결과를 result에 저장한다. 
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    context = {
        'result': result,
    }

    return render(request, 'pages/result.html', context)

    #9. Form - POST
def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'password': pwd,
    }
    return render(request, 'pages/user_create.html', context)

#10. 정적 파일
def static_example(request):
    return render(request, 'pages/static_example.html')
    