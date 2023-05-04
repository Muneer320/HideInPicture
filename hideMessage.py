with open('Picture2.jpg', 'ab') as f:
    message = bytes(input("Message to hide >>> "), 'utf-8')
    f.write(message)

print("Done!")