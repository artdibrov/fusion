def summary(collection):

    return {
        "photos": len(collection),
        "devices": len(
            set(
                photo["device"]
                for photo in collection
            )
        )
    }
