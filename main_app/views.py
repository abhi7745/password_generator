import password_generator
from django.shortcuts import render


import random
# Create your views here.


def index(request):

    return render(request,'index.html',{})


# main password generator condition
def generator(request):

    if request.method=='POST':
        length=int(request.POST.get('pass_length'))
        uppercase=request.POST.get('uppercase')
        numbers=request.POST.get('numbers')
        symbols=request.POST.get('symbols')
        print(length)
        print(uppercase)
        print(numbers)
        print(symbols)

        chars = list('abcdefghijklmnopqrstuvwxyz')
        if uppercase:
            chars.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if numbers:
            chars.extend('1234567890')
        if symbols:
            chars.extend('!@#$%^&*()<>?')

        pass_char=''
        for i in range(length):
            pass_char+=random.choice(chars)

        
        # print(pass_char)

        return render(request,'output.html',{'password':pass_char})


    return render(request,'index.html',{})



# unsecured way- because of form method="get" 
# def generator(request):

#     length=int(request.GET.get('pass_length'))
#     uppercase=request.GET.get('uppercase')
#     numbers=request.GET.get('numbers')
#     symbols=request.GET.get('symbols')

#     chars = list('abcdefghijklmnopqrstuvwxyz')
#     if uppercase:
#         chars.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     if numbers:
#         chars.extend('1234567890')
#     if symbols:
#         chars.extend('!@#$%^&*()<>?')

#     pass_char=''
#     for i in range(length):
#         pass_char+=random.choice(chars)

#     return render(request,'output.html',{'password':pass_char})
