PART_TYPES = [
    {
      "id": 1,
      "label": "cpu"
    },
    {
      "id": 2,
      "label": "motherboard"
    },
    {
      "id": 3,
      "label": "memory"
    },
    {
      "id": 4,
      "label": "storage"
    },
    {
      "id": 5,
      "label": "gpu"
    },
    {
      "id": 6,
      "label": "case"
    },
    {
      "id": 7,
      "label": "psu"
    },
    {
      "id": 8,
      "label": "os"
    },
    {
      "id": 9,
      "label": "monitor"
    }
]

def get_all_partTypes():
    return PART_TYPES

def get_single_partType(id):
    requested_partType = None

    for partType in PART_TYPES:
        if partType["id"] == id:
            requested_partType = partType

    return requested_partType