import streamlit as st
import io
import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader

def generate_rate_confirmation_memory(data, logo_path="gflogo.png", target_page_size=(612, 792)):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=target_page_size)
    width, height = target_page_size

    # Naslov
    c.setFont("Helvetica-Bold", 6.2)
    c.drawString(30, height - 40, "TRUCKLOAD RATE CONFIRMATION")
    
    # Informacije o kompaniji
    c.setFont("Helvetica", 6.2)
    c.drawString(30, height - 70, "Gray Falcon United")
    c.drawString(30, height - 85, "MC # 1040945")
    c.drawString(30, height - 115, "1431 Opus Pl Ste 110")
    c.drawString(30, height - 130, "DOWNERS GROVE, IL 60515")
    
    # Dodavanje logotipa (ako fajl postoji)
    if os.path.exists(logo_path):
        img = ImageReader(logo_path)
        image_width = 100
        image_height = 100
        c.drawImage(img, width - image_width - 90, height - image_height - 30, image_width, image_height)
    
    # Informacije o carrier-u i tovaru
    c.setFont("Helvetica-Bold", 6.2)
    c.drawString(30, height - 165, "Carrier Name:")
    c.setFont("Helvetica", 6.2)
    c.drawString(75, height - 165, data['carrier_name'])
    
    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(30, height - 180, "Pickup Date:")
    c.setFont("Helvetica", 6.27)
    c.drawString(74, height - 180, data['pickup_date'])

    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(30, height - 195, "Delivery Date:")
    c.setFont("Helvetica", 6.27)
    c.drawString(76, height - 195, data['delivery_date'])

    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(30, height - 210, "Service Level:")
    c.setFont("Helvetica", 6.27)
    c.drawString(76, height - 210, data['service_level'])

    # Shipper Information Section
    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(30, height - 240, "Shipper Information:")
    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(50, height - 255, "Name:")
    c.setFont("Helvetica", 6.27)
    c.drawString(95, height - 255, data['shipper_name'])
    
    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(50, height - 270, "Address:")
    c.setFont("Helvetica", 6.27)
    c.drawString(95, height - 270, data['shipper_address'])
    c.drawString(95, height - 285, data['shipper_place'])
    
    # Consignee Information Section
    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(30, height - 315, "Additional Stop Information:")
    
    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(50, height - 330, "Name:")
    c.setFont("Helvetica", 6.27)
    c.drawString(95, height - 330, data['consignee_name'])
    
    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(50, height - 345, "Address:")
    c.setFont("Helvetica", 6.27)
    c.drawString(95, height - 345, data['consignee_address'])
    c.drawString(95, height - 360, data['consignee_place'])
    
    # Pickup and Delivery Times
    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(30, height - 390, "Scheduled:")
    c.setFont("Helvetica", 6.27)
    c.drawString(66, height - 390, f"{data['delivery_date']} FCFS")

    # Right Section
    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(340, height - 165, "Load#:")
    c.setFont("Helvetica", 6.27)
    c.drawString(362, height - 165, data['load_number'])
    
    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(340, height - 180, "Customer PO:")
    c.drawString(340, height - 195, "Shipper Ref#:")
    c.drawString(340, height - 210, "Trailer Type/Size:")
    c.setFont("Helvetica", 6.27)
    c.drawString(395, height - 210, data['trailer_type'])
    
    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(340, height - 240, "Contact:")
    c.drawString(340, height - 255, "Phone:")
    c.drawString(340, height - 285, "Pickup Date & Time:")
    c.setFont("Helvetica", 6.27)
    c.drawString(404, height - 285, f"{data['pickup_date']} FCFS")
    
    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(340, height - 315, "Contact:")
    c.drawString(340, height - 330, "Phone:")
    c.drawString(340, height - 345, "Email:")
    c.drawString(340, height - 360, "Appointment:")
    c.setFont("Helvetica", 6.27)
    c.drawString(384, height - 360, f"{data['delivery_date']} FCFS")
    
    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(340, height - 390, "Contact:")
    c.drawString(340, height - 405, "Phone:")
    c.drawString(340, height - 420, "Delivery Date & Time:")
    c.setFont("Helvetica", 6.27)
    c.drawString(406, height - 420, data['delivery_date'])
    
    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(340, height - 560, "Rate:")
    c.setFont("Helvetica", 6.27)
    c.drawString(520, height - 560, data['rate'])
    
    c.setFont("Helvetica-Bold", 6.27)
    c.drawString(340, height - 575, "Total:")
    c.setFont("Helvetica", 6.27)
    c.drawString(520, height - 575, data['rate'])
    
    # Tabela
    table_data = [
        ["Handling Units", "Package Type", "Pieces", "HAZMAT", "List of Items", "Total Weight"],
        ["0", "Pallet", "1", " ", "FAK", "37,000"]
    ]
    table = Table(table_data, colWidths=[90, 90, 90, 90, 90, 90], rowHeights=12)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6.27),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    table.wrapOn(c, width, height)
    table.drawOn(c, 30, height - 480)
    
    c.setFont("Helvetica-Bold", 6.2)
    c.drawString(30, height - 500, "PICKUP INSTRUCTION:")
    c.drawString(340, height - 500, "DELIVERY INSTRUCTION:")
    
    c.save()
    packet.seek(0)
    return packet

def merge_pdfs_memory(first_pdf_bytesio, second_pdf_path):
    first_reader = PdfReader(first_pdf_bytesio)
    second_reader = PdfReader(second_pdf_path)
    second_page_size = second_reader.pages[0].mediabox
    
    writer = PdfWriter()
    first_page = first_reader.pages[0]
    first_page.mediabox = second_page_size
    writer.add_page(first_page)
    
    for page in second_reader.pages:
        writer.add_page(page)
        
    output_packet = io.BytesIO()
    writer.write(output_packet)
    output_packet.seek(0)
    return output_packet

# --- STREAMLIT UI ---
st.set_page_config(page_title="RC Generator", layout="wide")
st.title("📄 Rate Confirmation Generator")

st.info("Logo (gflogo.png) i Carrier Confirmation (CarrierConfirmation_121586049.pdf) se automatski povlače iz foldera.")

# Unos podataka
col1, col2, col3 = st.columns(3)
with col1:
    carrier_name = st.text_input("Carrier Name:", value="Example Carrier")
    load_number = st.text_input("Load Number:", value="121586049")
    trailer_type = st.text_input("Trailer Type/Size:", value="Van / Full")
    rate = st.text_input("Rate:", value="USD $1,000.00")
    service_level = st.text_input("Service Level:", value="Normal")

with col2:
    pickup_date = st.text_input("Pickup Date:", value="1/8/2025")
    shipper_name = st.text_input("Shipper Name:", value="UFLOOR Systems Inc.")
    shipper_address = st.text_input("Shipper Address:", value="200 Garrison Oak Dr, ")
    shipper_place = st.text_input("Shipper City/State/Zip:", value="Dover, DE 19901")

with col3:
    delivery_date = st.text_input("Delivery Date:", value="1/13/2025")
    consignee_name = st.text_input("Consignee Name:", value="Blakely Products Company")
    consignee_address = st.text_input("Consignee Address:", value="13891 Stephens Rd,  ")
    consignee_place = st.text_input("Consignee City/State/Zip:", value="Warren, MI 48089")

st.divider()

# NOVO: Polje za prilagođeni naziv fajla
st.subheader("Podešavanja fajla")
custom_filename = st.text_input("Unesite naziv fajla za preuzimanje (npr. Storm Smith 1-1-26):", value="", help="Ako ostavite prazno, fajl će se zvati Final_RC_[LoadNumber].pdf")

if st.button("Generiši Spojeni RC", type="primary"):
    second_page_file = "CarrierConfirmation_121586049.pdf"
    
    if not os.path.exists(second_page_file):
        st.error(f"Fajl '{second_page_file}' nije pronađen u folderu. Dodaj ga pre generisanja.")
    else:
        data = {
            "carrier_name": carrier_name,
            "load_number": load_number,
            "trailer_type": trailer_type,
            "delivery_date": delivery_date,
            "pickup_date": pickup_date,
            "shipper_name": shipper_name,
            "shipper_address": shipper_address,
            "shipper_place": shipper_place,
            "consignee_name": consignee_name,
            "consignee_address": consignee_address,
            "consignee_place": consignee_place,
            "rate": rate,
            "service_level": service_level,
        }

        first_page_io = generate_rate_confirmation_memory(data, logo_path="gflogo.png")
        final_pdf_io = merge_pdfs_memory(first_page_io, second_page_file)

        st.success("Rate Confirmation uspešno kreiran!")
        
        # Logika za odabir imena fajla
        if custom_filename.strip():
            final_name = f"{custom_filename.strip()}.pdf"
        else:
            final_name = f"Final_RC_{load_number}.pdf"
            
        st.download_button(
            label="⬇️ Preuzmi Finalni RC PDF",
            data=final_pdf_io,
            file_name=final_name,
            mime='application/pdf'
        )
