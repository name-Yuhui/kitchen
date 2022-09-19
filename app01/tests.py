def auth(func):
    def wrapper():
        # username = dict(request.session).get("username", None)
        username = 'aaa'
        return func(username)

    return wrapper

@auth
def index(*args, **kwargs):
    print(">>>>", args)
    print(">>>>", kwargs)

index()


# from django.test import TestCase
#
# # Create your tests here.
# user = {
#     "id": 0,
#     "name": "lin",
#     "password": "123456",
#     "address": "广东汕头",
#     "gender": "男",
#     "occupation": "lin",
#     "fans": "",
#     "fans_num": 0,
#     "attentions": "",
#     "attentions_num": 0,
#     "image": "",
#     "collections": "",
# }
#
# recipe = {
#     "id": 0,
#     "title": "佛跳槽", "author": "lin",
#     "score": 8.8, "type": "炖",
#     "description": "这是一道食材丰富，色香味俱全的中国传统大锅炖",
#     "use_foods": [
#         {"name": "海参", "g": "4只"},
#         {"name": "鲍鱼", "g": "6只"},
#         {"name": "素翅", "g": "35g"},
#         {"name": "鸽蛋", "g": "4个"},
#         {"name": "瑶柱", "g": "12个"},
#         {"name": "花菇", "g": "4个"},
#         {"name": "花胶", "g": "8片"}
#     ],
#     "steps": [
#         {"ord": 1, "cont": "准备炖盅，底铺火腿薄片，然后是鱼翅。",
#          "img_src": "/recipe_imgs/a63b64d61d2b406295d08e3032d88b09_1472w_1104h.jpg"},
#         {"ord": 2, "cont": "准备炖盅，底铺火腿薄片，然后是鱼翅。", "img_src": "/imgs/1.jpg"},
#         {"ord": 3, "cont": "准备炖盅，底铺火腿薄片，然后是鱼翅。", "img_src": "/imgs/1.jpg"},
#         {"ord": 4, "cont": "准备炖盅，底铺火腿薄片，然后是鱼翅。", "img_src": "/imgs/1.jpg"},
#         {"ord": 5, "cont": "准备炖盅，底铺火腿薄片，然后是鱼翅。", "img_src": "/imgs/1.jpg"}
#     ],
#     "img_src": "/imgs/0.jpg",
#     "collected_nums": 0,
#     "title": "",
# }
# r = {
#     "id": 0,
#     "title": "蛤蜊蒸蛋",
#     "author": "lin",
#     "score": 8.8,
#     "type": ["蒸蛋","快手菜","早餐"],
#     "description": "招待小朋友们时，一盘蛤蜊蒸蛋遭疯抢，家长要求留个菜谱。",
#     "use_foods": [
#         {
#             "name": "蛤蜊",
#             "g": "10余个"
#         },
#         {
#             "name": "鸡蛋",
#             "g": "2个"
#         },
#         {
#             "name": "盐",
#             "g": "2g"
#         },
#         {
#             "name": "香菜",
#             "g": "2根"
#         },
#         {
#             "name": "姜",
#             "g": "2片"
#         },
#         {
#             "name": "生抽",
#             "g": "1勺"
#         }
#     ],
#     "steps": [
#         {
#             "ord": 1,
#             "cont": "蒸蛋我家常做，要蒸出细嫩爽滑的蛋，关键是蛋必须彻底打匀并滤去泡沫与沉淀物",
#             "img_src": "/recipe_imgs/6fb7fd0d3ae4422d97bd403e5fb366dc_1081w_811h.jpg"
#         },
#         {
#             "ord": 2,
#             "cont": "材料：蛤蜊、蛋",
#             "img_src": "/recipe_imgs/c80b8d84d9ff49168703a6a8161993a0_1280w_960h.jpg"
#         },
#         {
#             "ord": 3,
#             "cont": "水煮沸后，姜片、葱结连同蛤蜊一起下锅",
#             "img_src": "/recipe_imgs/3a649e623548470da9a5645ff224e60b_480w_384h.jpg"
#         },
#         {
#             "ord": 4,
#             "cont": "蛤蜊开口时间不同步，开口一个捞出一个",
#             "img_src": "/recipe_imgs/989324a6a9314e19a89d0d217115c3a7_1280w_960h.jpg"
#         },
#         {
#             "ord": 5,
#             "cont": "用冷水将蛤蜊冲洗干净",
#             "img_src": "/recipe_imgs/1f545ee79e3d424c8e944ed8843134cb_1280w_960h.jpg"
#         },
# {
#             "ord": 6,
#             "cont": "将蛤蜊放入盘中",
#             "img_src": "/recipe_imgs/5b55ec88e3f44bc78ca770250c2f789e_1280w_959h.jpg"
#         }
#     ],
#     "img_src": "/recipe_imgs/bdc0132c66b24156827af09654f0d8a1_1280w_960h.jpg",
#     "collected_nums": 0,
#     "done_nums": 0,
#     "date": {
#         "$date": {
#
#         }
#     }
# }
