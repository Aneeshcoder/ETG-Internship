import json

fd = open("record.json",'r')
r = fd.read()
fd.close()

fs = open("sales.json",'r')
s = fs.read()
fd.close()

records = json.loads(r)
sales = json.loads(s)

ui_prod  = str(input("Enter the product_Id: "))

if ui_prod in records.keys():
  ui_quant = int(input("Enter the quantity: "))
  if records[ui_prod]['qn']>=ui_quant:
    print("Product: ", records[ui_prod]['name'])
    print("Price: ", records[ui_prod]['pr'])
    print("Billing Amount: ", records[ui_prod]['pr'] * ui_quant)
    records[ui_prod]['qn'] = records[ui_prod]['qn'] - ui_quant
    ui_name = records[ui_prod]['name']
    if ui_name in sales.keys():
      sales[ui_name]['qn']=+ui_quant
      sales[ui_name]['amount']=+records[ui_prod]['pr']*ui_quant
    else:
      sales[ui_name] = {'qn':ui_quant,'amount':records[ui_prod]['pr']*ui_quant}
  else:
    print("This much Quantity is not available !")
else: 
  print("Product Not Available !")

js = json.dumps(records)
jsale = json.dumps(sales)

fd = open("record.json",'w')
fd.write(js)
fd.close()

fs = open("sales.json",'w')
fs.write(jsale)
fs.close()

