import qrcode
from PIL import Image
import os

# URL que deseas convertir en código QR
url = "https://github.com/Hoyos-Dev"

# Crear objeto QRCode con configuración para mayor durabilidad
qr = qrcode.QRCode(
    version=1,  # Controla el tamaño del QR (1-40), mayor número = más datos
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Nivel alto de corrección de errores (30%)
    box_size=10,  # Tamaño de cada "caja" del QR
    border=4,  # Borde alrededor del QR
)

# Agregar datos al QR
qr.add_data(url)
qr.make(fit=True)

# Crear una imagen del código QR
qr_img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen
output_file = "codigo_qr_permanente.png"
qr_img.save(output_file)

# Mostrar la ruta completa donde se guardó el archivo
ruta_completa = os.path.abspath(output_file)
print(f"Código QR generado y guardado en: {ruta_completa}")