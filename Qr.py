import qrcode
data=input("Enter Any Thing To Make QR ")
img=qrcode.make(data)
img.save("new.png")