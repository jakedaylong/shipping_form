import os


def check_directory(user_path):
    """checks for existing directory at the below path"""
    if not os.path.exists(user_path + r'\Documents\Barcodes'):
        os.mkdir(user_path + r'\Documents\Barcodes')


def mkfile(user_path):
    """checks for existing pdf_html.html file and creates it from the below code if necessary
    currently html file needs to be edited after creation to correct img paths. will correct later"""
    user_path_html = os.path.join('"' + user_path, 'Documents\\Barcodes\\pdf_html.html' + '"')
    if not os.path.exists(user_path_html):
        html_str = """
        <h2>Please fill out the form with applicable Ship From and Ship To information, Print and Clear the
        form, then bring it to the Customer Service Counter</h2>
    
        <p><h2>Ship From:</h2></p>
        <table style="border-collapse: collapse; width: 100%;">
            <tbody>
                <tr>
                    <td>Alias:</td>
                    <td>{{alias}}</td>
                    <td>Name:</td>
                    <td>{{ship_from_name}}</td>
                    <td>Phone:</td>
                    <td>{{ship_from_phone}}</td>
                </tr>
            </tbody>
        </table>
        <br>
        <br>
        <br>
        <p><h2>Ship To:</h2></p>
        <table style="border-collapse: collapse; width: 100%;">
            <tbody>
                <tr>
                    <td>Company Name:</td>
                    <td justify-content="start">{{company_name}}</td>
                    <td>Contact Name:</td>
                    <td>{{contact_name}}</td>
                    </tr>
                <tr>
                    <td>Address Line 1:</td>
                    <td>{{address_line1}}</td>
                    <td>Address Line 2:</td>
                    <td>{{address_line2}}</td>
                </tr>
                <tr>
                    <td>Address Line 3:</td>
                    <td>{{address_line3}}</td>
                    <td>City:</td>
                    <td>{{city}}</td>
                </tr>
                <tr>
                    <td>Country:</td>
                    <td>{{country}}</td>
                    <td>State:</td>
                    <td>{{state}}</td>
                    <td>Zip Code:</td>
                    <td>{{zip_code}}</td>
                </tr>
                <tr>
                    <td>Phone:</td>
                    <td>{{phone}}</td>
                    <td>Email:</td>
                    <td>{{email}}</td>
                </tr>
            </tbody>
        </table>
        <br>
        <br>
        <br>
    
        <table style="border-collapse: collapse; width: 100%;">
            <tbody>
            <tr>
                <td align="center">Recipient Barcode</td>
                </tr>
            <tr>
                <td colspan="2" align="center"><img src={{recipient_path}} alt=""></td>
            </tr>
        </tbody>
        </table>
        
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        
        <table style="border-collapse: collapse; width: 100%;">
            <tbody>
            <tr>
                <td colspan="2" align="center">Alias</td>
            </tr>
            <tr>
                <td colspan="2" align="center"><img src={{alias_path}}></td>
            </tr>
        </tbody>
        </table>
        """
        with open(user_path + r'\Documents\Barcodes\pdf_html.html', 'w') as html_file:
            html_file.write(html_str)
