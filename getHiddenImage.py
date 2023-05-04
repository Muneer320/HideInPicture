import PIL.Image as I
import io


with open('ReferenceImage.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)

    newImg = I.open(io.BytesIO(f.read()))
    newImg.save('NewImage.jpg')