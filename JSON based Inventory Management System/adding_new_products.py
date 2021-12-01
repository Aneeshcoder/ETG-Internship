import json

fd = open("record.json",'r')
r = fd.read()
fd.close()

record = json.loads(r)

prod_id = str(input("Enter the prod ID: "))

if prod_id in record.keys():
  qn = int(input("Enter the prod quantity: ")) #quantity
  record[prod_id]['qn']+=qn

else:
  name = str(input("Enter the prod name: "))
  pr = int(input("Enter the prod price: ")) #price
  qn = int(input("Enter the prod quantity: ")) #quantity
  record[prod_id] = {'name':name,'pr':pr,'qn':qn}

js = json.dumps(record)
fd = open("record.json",'w')
fd.write(js)
fd.close()

fd = open("record.json",'r')
r = fd.read()
fd.close()

record = json.loads(r)
record
