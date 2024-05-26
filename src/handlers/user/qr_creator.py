import os
from qrcode import make


def create_qrcode(text: str, path: str, filename: str) -> None:
    img = make(text)
    fullname = path + '\\' + filename
    if not os.path.exists(path):
        os.mkdir(path)
    img.save(fullname)
