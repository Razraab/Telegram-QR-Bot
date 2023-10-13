import qrcode


def create(text: str, path: str) -> None:
    img = qrcode.make(text)
    img.save(path)
