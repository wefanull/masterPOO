from dibujarClima import consulta_clima, genera_imagen

# Consulta el clima para una ciudad
ciudad = "Toluca"
datos_clima = consulta_clima(ciudad)

# Genera la imagen
imagen_blob = genera_imagen(datos_clima)

# Guarda la imagen en un archivo
with open("clima.png", "wb") as f:
    f.write(imagen_blob)

print("Imagen generada como 'clima.png'")