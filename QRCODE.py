import qrcode

url = input("Digite a URL do site: ")
qr = qrcode.make(url)
qr.save("qrcode_url.png")
print("QR Code gerado e salvo como 'qrcode_url.png'.")