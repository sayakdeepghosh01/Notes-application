#this is convert mongodb files to python dictonary

def noteEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "title": item["title"],
        "desc": item["desc"],
        "important": item["important"],
    }

#

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]




