def show(devices, albums, duplicates, info):

    print("=" * 35)
    print("IMAGE GALLERY")
    print("=" * 35)

    for device, photos in devices.items():
        print(f"{device:<11}: {len(photos)} photos")

    print("\nAlbums")
    print("-" * 15)

    for album, photos in albums.items():
        print(f"{album} ({len(photos)})")

    print("\nDuplicate files")
    print("-" * 15)

    if duplicates:
        for photo in duplicates:
            print(photo)
    else:
        print("No duplicates")

    print("\nTotal Photos:", info["photos"])
