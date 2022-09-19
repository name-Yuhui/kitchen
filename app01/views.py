from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from app01 import mongo_handle
import pymongo
import time
from datetime import datetime
import json
import datetime
# import pandas as pd
# pd.set_option('display.max_rows',None)#取消行限制
# pd.set_option('display.max_columns',None)#取消列限制
# pd.set_option('display.width',1000)#增加每行的宽度
# Create your views here.
def auth(request):
    username = dict(request.session).get("username", None)
    return username


def index(request):
    kitchenDB = mongo_handle.kitchenDB()
    recp = kitchenDB.recipes
    carousel = list(recp.find().sort("date", pymongo.DESCENDING).limit(3))
    # 新秀菜谱，最新发布的菜谱
    new_recipes = list(recp.find().sort("date", pymongo.DESCENDING).limit(6))
    # 最近流行
    recent = list(recp.find().sort("date", pymongo.DESCENDING).limit(6))

    username = auth(request)

    return render(request, 'index.html',
                  {"carousel": carousel, "username": username,"new_recipes":new_recipes,
                   "recent":recent,"recipe_url_prefix":"/recipe/"})


def logout(request):
    print(">>>>>>\n", dict(request.session))

    if dict(request.session):
        request.session.flush()
        print(">>>>>>", dict(request.session))

    return redirect("/")


def login(request):
    kitchenDB = mongo_handle.kitchenDB()
    if request.method == "POST":
        user_name = request.POST.get("username")
        pwd = request.POST.get("password")
        result = kitchenDB.users.find({"name": user_name, "pwd": pwd}, {"name": 1})
        # print(list(result))
        if not list(result):
            ret = redirect("/")
            # 设置cookie和session
            ret.set_cookie("username", user_name, 10)
            request.session["username"] = user_name
            request.session.set_expiry(0)

            return ret
    return render(request, "login.html")


def regitser(request):
    kitchenDB = mongo_handle.kitchenDB()
    users = kitchenDB.users
    data = request.POST
    user_json = {
        "id": users.estimated_document_count(),
        "name": data.get("username"),
        "pwd": data.get("password"),
        "address": "",
        "gender": "男",
        "occupation": "",
        "fans": "",
        "fans_num": 0,
        "attentions": "",
        "attentions_num": 0,
        "image": "",
        "collections": "",
    }
    users.insert_one(user_json)
    return redirect("/index")


def get_img(request, z):
    path = request.path
    file_one = open(path, "rb")
    return HttpResponse(file_one.read(), content_type='image/jpg')


def category(request):
    username = auth(request)
    return render(request, "category.html", {"username": username})


def publish(request):
    username = auth(request)
    # 获取最新id
    kitchenDB = mongo_handle.kitchenDB()
    recipes = kitchenDB.recipes
    if request.method == "POST":
        print(request.POST)
        # 整理数据
        data = {
            "id": recipes.estimated_document_count(),
            "title": request.POST.get("title"),
            # "author": request.POST.get("author"),
            "author": "lin",
            "score": 0,
            "type": request.POST.get("type"),
            "description": request.POST.get("desc"),
            "use_foods": json.loads(request.POST.get("use_list")),
            "steps":  json.loads(request.POST.get("steps_list")),
            "img_src": "/recipe_imgs/" + request.FILES.get("main_img").name ,
            "collected_nums": 0,
            "done_nums": 0,
            "date": datetime.now(),
        }
        # 把菜谱的所有图片下载到位
        for k, v in dict(request.FILES).items():
            print("is >>>>>>>>>", k)
            if k != "main_img" and k:
                data["steps"][int(k)-1]["img_src"] = "/recipe_imgs/"+v[0].name
            with open('/recipe_imgs/' + v[0].name, 'wb') as fp:
                fp.write(v[0].read())
        print('data>>>>',data)
        kitchenDB.recipes.insert_one(data)
        return JsonResponse({"core": 0})
        # return render(request, "publish.html", {"username": username})

    else:
        return render(request, "publish.html", {"username": username})


def works(request):
    username = auth(request)
    return render(request, "works.html", {"username": username})


def menu(request):
    kitchenDB = mongo_handle.kitchenDB()
    recp = kitchenDB.recipes

    username = auth(request)
    key = request.GET.get('key')
    recipes_list = list(recp.find({"$or": [{"title": {'$regex': key}},{"use_foods.name": {'$regex': key}}]})) if key else None
    return render(request, "menu.html", {"username": username,"recipes_list":recipes_list,"recipe_url_prefix":"/recipe/"})


def recipe(request,recipe_id):
    username = auth(request)
    kitchenDB = mongo_handle.kitchenDB()
    recp = kitchenDB.recipes
    id = int(recipe_id)
    info = list(recp.find({"id": id}))[0]
    print(info)
    # 作者名字
    author = info.get("author")
    # print(info)

    # 通过名字获取作者信息
    users = kitchenDB.users
    user_info = list(users.find({"name": author}))[0] if list(users.find({"name": author})) else None
    # print(user_info)
    return render(request, "recipe.html", {"info": info, "user_info": user_info, "username": username})
