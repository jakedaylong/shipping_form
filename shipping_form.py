from nicegui import ui

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
            recipient_email.value = None

        def generate_form():
            recipient_country_form = recipient_country.value.lower()

ui.button('Reset', on_click=reset)
ui.button('Generate Form', on_click=generate_form)

ui.run(title='Mail and Ship Form', favicon='package.png')
#ui.run(native=True, window_size=(400, 300), fullscreen=False, title='Mail and Ship Form', favicon='th.jpg')