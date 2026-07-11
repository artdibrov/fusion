from collections import defaultdict


def group_by_device(collection):

    devices = defaultdict(list)

    for photo in collection:
        devices[photo["device"]].append(photo["file"])

    return devices
