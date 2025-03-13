from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

def dibuja_icono(icon_code):
    if icon_code.endswith('d'):
        fill_color = Color('orange')
    elif icon_code.endswith('n'):
        fill_color = Color('gray')
        fill_color = Color('white')

    with Drawing() as draw:
        draw.stroke_color = Color('black')
        draw.stroke_width = 2
        draw.fill_color = fill_color

        if icon_code in ['01d', '01n']:  # Cielo despejado
            draw.circle((200, 150), (100, 150))  # Un círculo
        elif icon_code in ['02d', '02n']:  # Pocas nubes
            draw.rectangle(left=100, top=50, right=300, bottom=250)  # Un rectángulo
        elif icon_code in ['03d', '03n', '04d', '04n']:  # Nubes dispersas
            draw.ellipse((200, 150), (150, 100))  # Una elipse
        elif icon_code in ['09d', '09n']:  # Llovizna
            draw.line((50, 150), (350, 150))  # Una línea horizontal
        elif icon_code in ['10d', '10n']:  # Lluvia ligera
            draw.line((100, 100), (300, 200))  # Una línea diagonal
        elif icon_code in ['11d', '11n']:  # Tormenta eléctrica
            draw.polygon([(100, 150), (200, 50), (300, 150)])  # Un triángulo
        elif icon_code in ['13d', '13n']:  # Nieve
            draw.arc((100, 100), (300, 200), 0, 360)  # Un arco circular
        elif icon_code in ['50d', '50n']:  # Niebla
            draw.bezier([(50, 150), (150, 50), (250, 250), (350, 150)])  # Una curva bezier
        else:
            draw.text(100, 150, "Icono desconocido")

        with Image(width=400, height=300, background=Color('lightblue')) as image:
            draw(image)
            image.format = 'png'
            png_bin = image.make_blob()
            return png_bin