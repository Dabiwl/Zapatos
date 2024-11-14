from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def crear_pdf_factura(libro):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Encabezado de la factura
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, height - 72, "Factura de Compra")

    # Datos del libro
    c.setFont("Helvetica", 12)
    c.drawString(72, height - 100, f"Título: {libro.titulo}")
    c.drawString(72, height - 120, f"Descripción: {libro.descripción}")
    c.drawString(72, height - 140, f"Precio: ${libro.precio:.2f}")

    # Total de la compra
    c.drawString(72, height - 180, f"Total: ${libro.precio:.2f}")

    # Pie de página
    c.drawString(72, height - 220, "Gracias por su compra.")

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer
