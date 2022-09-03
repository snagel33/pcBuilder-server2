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

def create_userContent(userContent):
    max_id = USERCONTENTS[-1]["id"]
    new_id = max_id + 1
    userContent["id"] = new_id
    USERCONTENTS.append(userContent)
    return userContent

def delete_userContent(id):
    userContent_index = -1

    for index, userContent in enumerate(USERCONTENTS):
        if userContent["id"] == id:
            userContent_index = index

    if userContent_index >= 0:
        USERCONTENTS.pop(userContent_index)