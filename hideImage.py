import PIL.Image as I
import io

loc = input('Location of picture to be hidden >>> ')
img = I.open(loc)
byte_arr = io.BytesIO()
img.save(byte_arr, format='PNG')

with open('ReferenceImage.jpg', 'ab') as f:
    f.write(byte_arr.getvalue())

print("Done!")