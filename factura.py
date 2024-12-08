import pdfkit
import jinja2
from datetime import datetime

client_name = "Juan Emiliani"
item1 = "TV"
item2 = "Mueble"
item3 = "Lavadora"
subtotal1 = 500
subtotal2 = 300
subtotal3 = 250
total = subtotal1 + subtotal2 + subtotal3

today_date = datetime.today().strftime("%d %b, %Y")
month = datetime.today().strftime("%B")

context = {'client_name': client_name, 'today_date': today_date, 'total': f'${total:.2f}', 'month': month,
           'item1': item1, 'subtotal1': f'${subtotal1:.2f}',
           'item2': item2, 'subtotal2': f'${subtotal2:.2f}',
           'item3': item3, 'subtotal3': f'${subtotal3:.2f}'
           }

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'plantilla.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='C:\\Users\\Eco\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
output_pdf = 'factura.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config, css='estilo.css')



