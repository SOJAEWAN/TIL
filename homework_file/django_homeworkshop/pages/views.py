from django.shortcuts import render

def info(request):
    return render(request, 'info.html')

def student(request, name):
    context = {
        'name': name,
    }

    return render(request, 'student.html', context)


def push(request):
    return render(request, 'push.html')

def pull(request):
    num = request.GET.get('num')
    context = {
        'num': num,
    }
    return render(request, 'pull.html', context)

def one(request):
    return render(request, 'one.html')

def two(request):
    return render(request, 'two.html')