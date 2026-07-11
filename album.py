def create_albums(collection):

    albums = {
        "Vacation": [],
        "Family": []
    }

    for photo in collection:

        filename = photo["file"].lower()

        if "trip" in filename or "img" in filename:
            albums["Vacation"].append(photo)

        if "cat" in filename:
            albums["Family"].append(photo)

    return albums
