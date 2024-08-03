# Shipping Form Generator

I originally wrote this small app as a stop-gap to a persistent problem with a shipping system that did not provide a 
user interface module for a kiosk use case.

### Purpose
- Generate a shipping form that can intake shipper and recipient data and provide mail processors the ability to injest
that data into the user interface provided by the shipping software 

### Challenges 
- No API access to perform data transfer programmatically
- Prevent as much repeat data entry as possible for the mail processor
- Must run locally on machine
- Must not retain history
- Best data entry method available is a barcode scanner attached to mail processor's machine

### App Details
- App is written in Python
- Generates two barcodes, one for user alias id and one for the recipient data
- Exports a PDF file from an HTML template 
- Sends a "print" command to the system to print the resulting PDF to its default printer

### Packages Used
- NiceGUI
- pylibdmtx
- pdfkit
- jinja
- wkhtmltopdf
