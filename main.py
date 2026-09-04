import qrcode

img = qrcode.make(input("Insira o valor para ser exibido junto ao QR Code: "))
type(img)  # qrcode.image.pil.PilImage
img.save(r".\qrcode_gen\qrcode.png")

if img == True:
    print("QR Code gerado com sucesso!")
else:
    print("Erro ao gerar QR Code!")