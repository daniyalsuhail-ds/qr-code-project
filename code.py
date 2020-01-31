import qrcode

url = input("Enter URL :")
image = qrcode.make(url)
