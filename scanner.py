def merge(phone, desktop):

    collection = []

    for photo in phone:
        collection.append({
            "device": "Smartphone",
            "file": photo
        })

    for photo in desktop:
        collection.append({
            "device": "Desktop",
            "file": photo
        })

    return collection
