with open('Picture.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)

    with open('newFile.exe', 'wb') as e:
        e.write(f.read())

print("Done!")