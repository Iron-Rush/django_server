from time import ctime

import simplejson as simplejson
import sys
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp.models import AllInfo
import requests
import json
# Create your views here.
def hello(request):
    return HttpResponse("你爸爸！！")
def testLottie(request):
    info = 'Data log save success'
    status_code = 200
    all = []
    try:
        if request.method == 'POST':
            req = simplejson.loads(request.raw_post_data)
            print('req:', req)
            type = req['action']
            page = req['page']
            print(type, page)
            index = page*10+1
            end = index + 10
            if type == 'seletcted':
                allInfo = AllInfo.objects.filter(lottieid__gte=index, lottieid__lt=end, type='featured')
            # tempDict.clear()
            elif type == 'new':
                index += 30000
                end += 30000
                allInfo = AllInfo.objects.filter(lottieid__gte=index, lottieid__lt=end, type='recent')
            # hot
            elif type == 'hot':
                index += 15000
                end += 15000
                allInfo = AllInfo.objects.filter(lottieid__gte=index, lottieid__lt=end, type='popular')
            else:
                allInfo = AllInfo.objects.filter(lottieid__gte=1, lottieid__lt=10)
                status_code = 400
        for info in allInfo:
            tempDict = {}
            tempDict['lottie'] = info.lottie
            tempDict['userimg'] = info.userimg
            tempDict['username'] = info.username
            all.append(tempDict)
    except:
        info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
        status_code = 400
    if len(all) == 0:
        status_code = 400
    jr = JsonResponse({'status': status_code, 'data': all, 'info': info})
    print(jr)
    return jr

def lottie(request):
    # featured:1-14999 popular:15000-29999 recent:30000
    # json_in = json.load(request.body)
    # type = json_in['action']
    # page = json_in['page']
    # print(type, page)
    # type = request.POST.get('action')
    # page = request.POST.get('page')
    type = 'new'
    page = 1
    status_code = 200
    all = []
    index = page*10+1
    end = index + 10
    if type == 'seletcted':
        allInfo = AllInfo.objects.filter(lottieid__gte=index, lottieid__lt=end, type='featured')
            # tempDict.clear()
    elif type == 'new':
        index += 30000
        end += 30000
        allInfo = AllInfo.objects.filter(lottieid__gte=index, lottieid__lt=end, type='recent')
    # hot
    elif type == 'hot':
        index += 15000
        end += 15000
        allInfo = AllInfo.objects.filter(lottieid__gte=index, lottieid__lt=end, type='popular')
    else:
        allInfo = AllInfo.objects.filter(lottieid__gte=1, lottieid__lt=10)
        status_code = 400
    for info in allInfo:
        tempDict = {}
        tempDict['lottie'] = info.lottie
        tempDict['userimg'] = info.userimg
        tempDict['username'] = info.username
        all.append(tempDict)
    # data_json = json.dumps({'status': 200, 'data': all})
    # print(data_json)
    # print(all)
    if len(all) == 0:
        status_code = 400
    jr = JsonResponse({'status': status_code, 'data': all})
    print(jr)
    return jr
    # return render(request, "LottieInfo.html", {"allInfo": all})

# def lottiePost(request):


def datasave(request):
    dict = {}
    info = 'Data log save success'
    try:
        if request.method == 'POST':
            req = simplejson.loads(request.raw_post_data)
            username = req['username']
            password = req['password']
            datas = req['datas']
            game_id1 = datas[0]['game_id']
    except:
        info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
    dictInfo = dict()
    dictInfo['message']= info
    dictInfo['create_at']= str(ctime())
    json=simplejson.dumps(dictInfo)
    return HttpResponse(json)

def Index(request):
    return render(request, "Json.html")
    # return render(request, "index.html")

def index(request):     #HttpRequest
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        print(request.method)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'wcnnnd' and password == '123':
            return HttpResponse('登陆成功')
        else:
            return HttpResponse('登陆失败')
    # url_json = 'http://httpbin.org/post'
    # data_json = json.dumps({'key1': 'value1', 'key2': 'value2'})  # dumps：将python对象解码为json数据
    # r_json = requests.post(url_json, data_json)
    return render(request, 'login.html')

    # print(request.GET)  #<QueryDict: {'username': ['wcnnnd'], 'password': ['123']}>
    # username = request.GET.get('username')
    # password = request.GET.get('password')
    # print(username, password)
    # if username == 'wcnnnd' and password == '123':
    #     return HttpResponse("登陆成功")
    # # elif (len(username) == 0 and len(password) == 0):
    # #     return HttpResponse("登陆失败")
    # else:
    #     return render(request, 'login.html')
