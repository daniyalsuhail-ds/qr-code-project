import qrcode

url = input("Enter URL :")
image = qrcode.make(url)
image.save('1.png')
