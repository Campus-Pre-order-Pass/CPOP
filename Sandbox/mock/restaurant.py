def get_mock_r_current():
    return {"current_number": 2, "wait_number": 9}


def get_mock_menu(count=1):
    data = []
    props = ["水餃", "豆漿"]
    prop_2 = ["staples", "beverages"]
    for i in range(count):
        data.append(
            {
                "id": i,
                "type": prop_2[i],
                "title": props[i],
                "price": 5,
                "hot": False,
                "menu_img_url": f"http://127.0.0.1:8000/static/img/r/{i}/menu/1.jpg",
                "desc": "這是好吃水餃",
                "promotions": "買100送1"
            }
        )

    return data


def get_mock_r(count=1):
    data = []
    props = ["麥當勞", "水餃店"]
    for i in range(count):
        data.append(
            {
                "id":  i,
                "name": props[i],
                "status": get_mock_r_current(),
                "r_image_url": f"http://127.0.0.1:8000/static/img/r/{i}/r.jpg",
                "ratings": 3.5,
                "contact": "0987111222",
                "menu": get_mock_menu(count=2),
                "address": "台北市",
                "detail": {
                    "desc": "位於學餐廳",
                    "promotions": "特殊優惠",
                    "specialties": get_mock_menu(),
                    "r_url": "http//123:8000/api/static....",
                    "ig_url": "http//123:8000/api/static....",
                    "fd_url": "http//123:8000/api/static....",
                }
            }
        )

    return data
