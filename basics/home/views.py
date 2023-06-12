from django.http import HttpResponseRedirect
from django.shortcuts import  render
from django.urls import reverse
import array
import random

# Create your views here.

def index(request): 
    return render(request, "home/index.html") 

def char(request):
    length = int(request.GET.get('length'))
    characters = request.GET.get('characters')
    numbers = request.GET.get('numbers')
    sp = request.GET.get('sp')
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
            '*', '(', ')', '<']
    
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    COMBINED_LIST = []
    if characters=="on":
        COMBINED_LIST += UPCASE_CHARACTERS + LOCASE_CHARACTERS
        temp_pass = rand_upper + rand_lower
    if numbers=="on":
        COMBINED_LIST += DIGITS
        temp_pass = rand_digit
    if sp=="on":
        COMBINED_LIST += SYMBOLS
        temp_pass = rand_symbol
    for x in range(length):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
            password = password + x
    password = password[slice(length)]

    print(password)


    return render(request, 'home/char.html' ,{'char':password})


"""
def char(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = 8
    pass1 = ''
    for x in range(length):
        pass1 += random.choice(characters)
    return render(request,'home/char.html',{'char':pass1})
"""
"""
def num(request):    
    numbers = list('1234567890')
    length = 8
    pass1 = ''
    for x in range(length):
        pass1 += random.choice(numbers)
    return render(request,'home/num.html',{'num':pass1})
"""
"""def spl(request):   
    sp = list('!@#$%^&*')
    length = 8
    pass1 = ''
    for x in range(length):
        pass1 += random.choice(sp)
    return render(request,'home/spl.html',{'spl':pass1})
"""
"""def ran(request):    
    randoms = list('!@#$%^&*1234567890abcdefghijklmnopqrstuvwxyz')
    length = 8
    pass1 = ''
    for x in range(length):
        pass1 += random.choice(randoms)
    return render(request,'home/ran.html',{'ran':pass1})
"""

