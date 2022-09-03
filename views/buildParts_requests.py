BUILDPARTS = [
    {
        "id": 1,
        "partId": 1,
        "buildId": 1
    },
    {
        "id": 2,
        "partId": 2,
        "buildId": 1
    },
    {
        "id": 3,
        "partId": 3,
        "buildId": 2
    }
]

def get_all_buildParts():
    return BUILDPARTS

def get_single_buildPart(id):
    requested_buildPart = None

    for buildPart in BUILDPARTS:
        if buildPart["id"] == id:
            requested_buildPart = buildPart

    return requested_buildPart

def delete_buildPart(id):
    buildPart_index = -1

    for index, buildPart in enumerate(BUILDPARTS):
        if buildPart["id"] == id:
            buildPart_index = index

    if buildPart_index >= 0:
        BUILDPARTS.pop(buildPart_index)