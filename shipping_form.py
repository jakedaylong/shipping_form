from nicegui import ui
import os
import directory_creation as dc
import button_functions as bf

user_path = os.path.expanduser('~')
dc.check_directory(user_path)
dc.mkfile(user_path)

with ui.grid(columns=7).classes('w-full'):
    with ui.column().classes('col-span-7'):
        ui.label('Mail and Shipping Form').style('font-size: 24px; font-weight: bold')
with ui.grid(columns=7).classes('w-full'):
    with ui.column().classes("col-span-1"):
        ui.label('Ship From:').style('font-size: 20px; font-weight: bold')
    with ui.grid(columns=3).classes('col-span-5') as shipper_grid:
        shipper_alias = ui.input(label='Alias', placeholder='type your alias', value='')
        shipper_name = ui.input(label='Name', placeholder='type your name', value='')
        shipper_phone = ui.input(label='Phone', placeholder='enter you phone number', value='')

ui.separator()

with ui.grid(columns=7).classes('w-full') as shipto_grid:
    with ui.column().classes("col-span-1"):
        ui.label('Ship To:').style('font-size: 20px; font-weight: bold')
    with ui.grid(columns=3).classes('col-span-5') as recipient_grid:
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

ui.button('Reset', on_click=lambda: bf.reset(recipient_grid, shipper_grid))
ui.button('Generate Form', on_click=lambda: bf.generate_form(user_path))


ui.run(title='Mail and Ship Form', favicon='package.png')
# ui.run(native=True, window_size=(400, 300), fullscreen=False, title='Mail and Ship Form', favicon='th.jpg')