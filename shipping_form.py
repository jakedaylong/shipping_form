from nicegui import ui
import PIL.Image as Image
from pylibdmtx.pylibdmtx import encode
import jinja2
import os
import pdfkit

user_path = os.path.expanduser('~')

with ui.grid(columns=7).classes('w-full'):
    with ui.column().classes('col-span-7'):
        ui.label('Mail and Shipping Form').style('font-size: 24px; font-weight: bold')
with ui.grid(columns=7).classes('w-full'):
    with ui.column().classes("col-span-1"):
        ui.label('Ship From:').style('font-size: 20px; font-weight: bold')
    with ui.grid(columns=3).classes('col-span-5'):
        shipper_alias = ui.input(label='Alias', placeholder='type your alias', value='')
        shipper_name = ui.input(label='Name', placeholder='type your name', value='')
        shipper_phone = ui.input(label='Phone', placeholder='enter you phone number', value='')

ui.separator()

with ui.grid(columns=7).classes('w-full'):
    with ui.column().classes("col-span-1"):
        ui.label('Ship To:').style('font-size: 20px; font-weight: bold')
    with ui.grid(columns=3).classes('col-span-5') as shipTo_grid:
        recipient_company = ui.input(label='Company', placeholder='company name', value='')
        recipient_name = ui.input(label='Name', placeholder='contact name', value='')
        recipient_phone = ui.input(label='Phone', placeholder='contact phone', value='')

        recipient_address_line1 = ui.input(label='Address Line 1', value='')
        recipient_address_line2 = ui.input(label='Address Line 2', value='')
        recipient_address_line3 = ui.input(label='Address Line 3', value='')

        recipient_city = ui.input(label='City', placeholder='city', value='')
        recipient_state = ui.input(label='State', placeholder='state', value='')
        recipient_country = ui.input(label='Country', placeholder='country', value='')

        recipient_zip = ui.input(label='Zip', placeholder='zip', value='')
        recipient_email = ui.input(label='Email', placeholder='contact email', value='')


        def reset():
            shipper_phone.value = None
            shipper_name.value = None
            shipper_alias.value = None
            recipient_company.value = None
            recipient_name.value = None
            recipient_phone.value = None
            recipient_address_line1.value = None
            recipient_address_line2.value = None
            recipient_address_line3.value = None
            recipient_city.value = None
            recipient_state.value = None
            recipient_country.value = None
            recipient_zip.value = None
            recipient_email.value = None


        data_elements = {
            'alias': shipper_phone.value,
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
            'email': recipient_email.value
        }

        template_loader = jinja2.FileSystemLoader(user_path + r'\Documents\Barcodes')
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template('pdf_html.html')

        output_text = template.render(data_elements)

        # config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe")
        pdfkit.from_string(output_text, user_path + r'\Documents\Barcodes\pdf_generated.pdf', configuration=config,
                           options={"enable-local-file-access": ""})

        os.startfile(user_path + r'\Documents\Barcodes\pdf_generated.pdf', "print")

        def generate_form():
            T = '\t'
            shipper_alias_barcode = encode(data=shipper_alias.value.encode("utf8"))
            shipper_alias_barcode_img = Image.frombytes('RGB',
                                                        (shipper_alias_barcode.width, shipper_alias_barcode.height),
                                                        shipper_alias_barcode.pixels)
            shipper_alias_barcode_img.save('alias_barcode.jpg')

            recipient_barcode = recipient_company.value + T + recipient_name.value + T + recipient_address_line1.value + T + recipient_address_line2.value + T + recipient_address_line3.value + T + recipient_city.value + T + T + T + recipient_zip.value + T + recipient_phone.value + T + recipient_email.value
            recipient_barcode_img = Image.frombytes('RGB',
                                                    (recipient_barcode.width, recipient_barcode.height),
                                                    recipient_barcode.pixels)
            recipient_barcode_img.save('recipient_barcode.jpg')

ui.button('Reset', on_click=reset)
ui.button('Generate Form', on_click=lambda: generate_form())

ui.run(title='Mail and Ship Form', favicon='package.png')
# ui.run(native=True, window_size=(400, 300), fullscreen=False, title='Mail and Ship Form', favicon='th.jpg')
