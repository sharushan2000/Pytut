from django.shortcuts import render

# Create your views here.
def tutorial(request):
    name = request.path
    print(name)
    if name == '/tutorial/':
        return render(request , 'intro.html',{})
    sp = name.split('/')
    html = sp[2].strip('/')
    name = html+('.html')
    return render (request , name,{})
