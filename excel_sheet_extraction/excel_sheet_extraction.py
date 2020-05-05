import pandas as pd

excelfile = pd.ExcelFile('excel_file.xlsx')

sales = excelfile.parse('sales')
sales.to_csv('sales.csv', sep=',')

invoice = excelfile.parse('invoice')
invoice.to_csv('invoice.csv', sep=',')

salary = excelfile.parse('salary')
salary.to_csv('salary.csv', sep=',')

jo_sells = excelfile.parse('jo_sells')
jo_sells.to_csv('jo_sells.csv', sep=',')

product = excelfile.parse('product')
product.to_csv('product.csv', sep=',')

mariah = excelfile.parse('mariah')
mariah.to_csv('mariah.csv', sep=',')

order = excelfile.parse('order')
order.to_csv('order.csv', sep=',')

person = excelfile.parse('person')
person.to_csv('person.csv', sep=',')

emails = excelfile.parse('emails')
emails.to_csv('emails.csv', sep=',')

trips = excelfile.parse('sales')
trips.to_csv('trips.csv', sep=',')