from qrcode import make


def create(text: str, path: str) -> None:
    img = make(text)
    img.save(path)
