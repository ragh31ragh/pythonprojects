import openpyxl
inv_file = openpyxl.load_workbook("inventory.xlsx")
print(type(inv_file))
product_list = inv_file["Sheet1"]
print(type(product_list))