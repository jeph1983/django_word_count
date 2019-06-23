from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):

    return render(request, 'home.html', {'firstname':'Eliazar','lastname':'Florian'})



def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    worddictionnary={}
    for word in wordlist:
        if word in worddictionnary:
            worddictionnary[word]+=1
        else:
            worddictionnary[word]=1
    sortedwords=sorted(worddictionnary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})




def about(request):
    return render(request, 'about.html',{'first':'Zaza','last':'Junior'})
