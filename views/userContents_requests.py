USERCONTENTS = [
    {
        "id": 1,
        "builderId": 1,
        "title": "TEST TITLE",
        "content": "TEST CONTENT"
    },
    {
        "id": 2,
        "builderId": 2,
        "title": "TEST TITLE 2",
        "content": "TEST CONTENT 2"
    }
]

def get_all_userContents():
    return USERCONTENTS

def get_single_userContent(id):
    requested_userContent = None

    for userContent in USERCONTENTS:
        if userContent["id"] == id:
            requested_userContent = userContent

    return requested_userContent