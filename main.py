from sample_library import SMARTPHONE
from sample_library import DESKTOP

from scanner import merge
from devices import group_by_device
from album import create_albums
from duplicates import find_duplicates
from gallery import summary
from output import show

collection = merge(
    SMARTPHONE,
    DESKTOP
)

devices = group_by_device(collection)

albums = create_albums(collection)

duplicates = find_duplicates(collection)

info = summary(collection)

show(
    devices,
    albums,
    duplicates,
    info
)
