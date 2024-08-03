import os
from nicegui.elements.mixins.value_element import ValueElement
import shipping_form as sf
from pylibdmtx.pylibdmtx import encode
import jinja2
import pdfkit
import PIL.Image as Image


def reset(recipient_grid, shipper_grid):
# resets all form fields to a blank value
    for child in recipient_grid.default_slot.children:
        if isinstance(child, ValueElement):
            child.value = None
    for child in shipper_grid.default_slot.children:
        if isinstance(child, ValueElement):
            child.value = None


def generate_form(user_path):
# generates the printable form and barcodes from user input data
    T = '\t'
    # shipper alias barcode generation
    shipper_alias_barcode = encode(data=sf.shipper_alias.value.encode("utf8"))
    shipper_alias_barcode_img = Image.frombytes('RGB',
                                                (shipper_alias_barcode.width, shipper_alias_barcode.height),
                                                shipper_alias_barcode.pixels)
    shipper_alias_barcode_img.save(user_path + r'\Documents\Barcodes\alias_barcode.jpg')
    # recipient barcode generation from the concatenation of the recipient data values
    recipient_barcode_concat = sf.recipient_company.value + T + sf.recipient_name.value + T + sf.recipient_address_line1.value + T + sf.recipient_address_line2.value + T + sf.recipient_address_line3.value + T + sf.recipient_city.value + T + T + T + sf.recipient_zip.value + T + sf.recipient_phone.value + T + sf.recipient_email.value
    recipient_barcode = encode(data=recipient_barcode_concat.encode("utf8"))
    recipient_barcode_img = Image.frombytes('RGB',
                                            (recipient_barcode.width, recipient_barcode.height),
                                            recipient_barcode.pixels)
    recipient_barcode_img.save(user_path + r'\Documents\Barcodes\recipient_barcode.jpg')

    # data elements used for display wothin html template
    data_elements = {
        'alias': sf.shipper_alias.value,
        'ship_from_name': sf.shipper_name.value,
        'ship_from_phone': sf.shipper_phone.value,
        'company_name': sf.recipient_company.value,
        'city': sf.recipient_city.value,
        'contact_name': sf.recipient_name.value,
        'address_line1': sf.recipient_address_line1.value,
        'address_line2': sf.recipient_address_line2.value,
        'address_line3': sf.recipient_address_line3.value,
        'country': sf.recipient_country.value,
        'state': sf.recipient_state.value,
        'zip_code': sf.recipient_zip.value,
        'phone': sf.recipient_phone.value,
        'email': sf.recipient_email.value
    }

    # jinja loader for html template
    template_loader = jinja2.FileSystemLoader(user_path + r'\Documents\Barcodes')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template('pdf_html.html')

    output_text = template.render(data_elements)

    # pdf generation from rendered html template
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe")
    pdfkit.from_string(output_text, user_path + r'\Documents\Barcodes\pdf_generated.pdf', configuration=config,
                       options={"enable-local-file-access": ""})

    os.startfile(user_path + r'\Documents\Barcodes\pdf_generated.pdf', "print")
