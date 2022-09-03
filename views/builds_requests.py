BUILDS = [
    {
        "id": 1,
        "title": "Build 1",
        "builder": 1,
        "img": "https://www.gamingscan.com/wp-content/uploads/2020/07/Best-Custom-PC-Builders.jpg",
        "price": 1000,
        "rating": 5,
    },
    {
        "id": 2,
        "title": "Build 2",
        "builder": 2,
        "img": "https://www.gamingscan.com/wp-content/uploads/2020/07/Best-Custom-PC-Builders.jpg",
        "price": 1500,
        "rating": 5,
    }
]

def get_all_builds():
    return BUILDS

def get_single_build(id):
    requested_build = None

    for build in BUILDS:
        if build["id"] == id:
            requested_build = build

    return requested_build