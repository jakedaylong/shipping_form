import os
from nicegui.elements.mixins.value_element import ValueElement
from pylibdmtx.pylibdmtx import encode
import jinja2
import pdfkit
import PIL.Image as Image


def reset(recipient_grid, shipper_grid):
    """resets all form fields to a blank value"""
    for child in recipient_grid.default_slot.children:
        if isinstance(child, ValueElement):
            child.value = None
    for child in shipper_grid.default_slot.children:
        if isinstance(child, ValueElement):
            child.value = None


def generate_form(user_path,
                 shipper_alias,
                 shipper_name,
                 shipper_phone,
                 recipient_company,
                 recipient_city,
                 recipient_name,
                 recipient_address_line1,
                 recipient_address_line2,
                 recipient_address_line3,
                 recipient_country,
                 recipient_state,
                 recipient_zip,
                 recipient_phone,
                 recipient_email):
    """generates the printable form and barcodes from user input data"""
    T = '\t'
    """shipper alias barcode generation"""
    shipper_alias_barcode = encode(data=shipper_alias.value.encode("utf8"))
    shipper_alias_barcode_img = Image.frombytes('RGB',
                                                (shipper_alias_barcode.width, shipper_alias_barcode.height),
                                                shipper_alias_barcode.pixels)
    shipper_alias_barcode_img.save(user_path + r'\Documents\Barcodes\alias_barcode.jpg')
    """recipient barcode generation from the concatenation of the recipient data values"""
    recipient_barcode_concat = recipient_company.value + T + recipient_name.value + T + recipient_address_line1.value + T + recipient_address_line2.value + T + recipient_address_line3.value + T + recipient_city.value + T + T + T + recipient_zip.value + T + recipient_phone.value + T + recipient_email.value
    recipient_barcode = encode(data=recipient_barcode_concat.encode("utf8"))
    recipient_barcode_img = Image.frombytes('RGB',
                                            (recipient_barcode.width, recipient_barcode.height),
                                            recipient_barcode.pixels)
    recipient_barcode_img.save(user_path + r'\Documents\Barcodes\recipient_barcode.jpg')

    alias_path = os.path.join('"' + user_path, 'Documents\\Barcodes\\alias_barcode.jpg' + '"')
    recipient_path = os.path.join('"' + user_path, 'Documents\\Barcodes\\recipient_barcode.jpg' + '"')
    """data elements used for display within html template"""
    data_elements = {
        'alias': shipper_alias.value,
        'ship_from_name': shipper_name.value,
        'ship_from_phone': shipper_phone.value,
        'company_name': recipient_company.value,
        'city': recipient_city.value,
        'contact_name': recipient_name.value,
        'address_line1': recipient_address_line1.value,
        'address_line2': recipient_address_line2.value,
        'address_line3': recipient_address_line3.value,
        'country': recipient_country.value,
        'state': recipient_state.value,
        'zip_code': recipient_zip.value,
        'phone': recipient_phone.value,
        'email': recipient_email.value,
        'alias_path': alias_path,
        'recipient_path': recipient_path
    }

    """jinja loader for html template"""
    template_loader = jinja2.FileSystemLoader(user_path + r'\Documents\Barcodes')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template('pdf_html.html')

    output_text = template.render(data_elements)

    """pdf generation from rendered html template"""
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe")
    pdfkit.from_string(output_text, user_path + r'\Documents\Barcodes\pdf_generated.pdf', configuration=config,
                       options={"enable-local-file-access": ""})

    os.startfile(user_path + r'\Documents\Barcodes\pdf_generated.pdf', "print")
