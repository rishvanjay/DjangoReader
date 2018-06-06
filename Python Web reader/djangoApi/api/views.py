from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
import urllib
import json
# from . import reader

# make message queue



# Create your views here.
# class HomePageView(TemplateView):
def index(request):
    return render(request, 'index.html', context=None)

def reader(request):
    link = request.GET['link']
    
    # response = requests.get(link)
    # url = response.json()
    html = readMethod(link)
    html = str(html)
    return render(request, 'index.html', {'url': json.dumps(html)})

@csrf_exempt
def readApi(request):
    # link = request.POST['url', False]
    strn = json.loads(request.body)
    strn = strn['Input']['url']
    html = readMethod(strn)
    return HttpResponse(json.dumps(html), content_type='application/json')

    # print(json.dump(strn))
    # response = requests.get(link)
    # url = response.json()
    # html = readMethod(link)
    # html = str(html)
    # return render(request, 'index.html', {'url': html})

def readMethod(url):
    # add a header to define a custon User-Agent
    HEADERS = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
    contentJson = ""

    req = urllib.request.Request(url, headers=HEADERS)
    try:
        response = urllib.request.urlopen(req).read()
    except urllib.error.HTTPError as e:
        # print("error")
        response = ""

        ContentJson = json.dumps({
            'url':url, 
            'error': {'errorNo':"MS0101",'errorMessage':"URL does not exist"},
            'data': ""
        })

        # print(ContentJson)
    # print response
    except urllib.error.URLError as e:
        response = ""

        ContentJson = json.dumps({
            'url':url,
            'error': {'errorNo':"MS0101",'errorMessage':"URL does not exist"},
            'data': ""
        })

    else: 
        ContentJson = json.dumps({
            'url':url,
            'error': {'errorNo':"",'errorMessage':""}, 
            'data':response.decode('utf-8'),
        })

        # print(ContentJson)

    return ContentJson

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    except TypeError as e:
        return False
    return True 