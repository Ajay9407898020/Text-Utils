# I have created this file -Ajay 

from django.http import HttpResponse
from django.shortcuts import render



# def index(request):
#     params={'name' : 'Ajay','place' : 'Earth'}
#     return render(request,'index.html',params)
    # return HttpResponse('Home')

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removePunc = request.POST.get('removepunc','off')
    fullCaps = request.POST.get('fullcaps','off')
    newLineRemover = request.POST.get('newLineRemover','off')
    extraSpaceRemover = request.POST.get('extraSpaceRemover','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    if removePunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char

        params = {'purpose':'Removed Punctuation','analyzed_text':analyzed}
        djtext = analyzed
    if(fullCaps == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Upper Case','analyzed_text':analyzed}
        djtext = analyzed

    if(newLineRemover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed = analyzed+char
        params = {'purpose':'New Line Remove','analyzed_text':analyzed}
        djtext = analyzed
    
    if(extraSpaceRemover=='on'):
        analyzed = ''
        for index,char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed+char
        params = {'purpose':'Extra space Remove','analyzed_text':analyzed}
        djtext = analyzed
    return render(request,'analyze.html',params)
