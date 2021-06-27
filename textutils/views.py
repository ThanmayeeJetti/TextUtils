from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'Thanmayee','place':'Guntur'}
    return render(request,'index.html',params)
    # return HttpResponse('''<h1>This is Home</h1> <a href="https://www.codewithharry.com/">CWH</a>''')

def analyze(request):

    text=request.POST.get('text','This is default text')
    removepunc=request.POST.get('removepunc','off')
    upper=request.POST.get('uppercase','off')
    extraspace=request.POST.get('extraspace','off')
    nl=request.POST.get('nlremove','off')
    p=request.POST.get('counter','off')

    if removepunc=="on":
        punctuations=''' !()-[]{};:'"\,<>./?@#$%^&*_~ '''
        ans=""
        for i in text:
            if i not in punctuations:
                ans=ans+i
        text=ans
        params={'purpose':'removepunc','analyzed_text':ans}
        text=ans
    if p=="on": 
        d={}
        for i in text:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        print(d)
        params={'purpose':'counter','analyzed_text':d}
    if extraspace=="on":
        ans=""
        for idx,char in enumerate(text):
            if text[idx]==" " and text[idx+1]==" ":
                pass
            else:
                ans=ans+char
        text=ans
        params={'purpose':'extraspace','analyzed_text':ans}
    if nl=="on":
        ans=""
        for char in text:
            if char!="\n" and char!="\r":
                ans=ans+char

        text=ans
        params={'newline':ans,'purpose':'newlineremoval'}
    if upper=="on":
        ans=""
        for char in text:
            ans=ans+char.upper()
        text=ans
        params={'uppertext':ans,'purpose':'changetouppercase'}
    if (removepunc!="on"  and p!="on" and extraspace!="on" and nl!="on" and upper!="on"):
        return HttpResponse("Error")
    return render(request,'analyze.html',params)
    