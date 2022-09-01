unit=int(input("enter unit:"))
if(unit>=0 and unit <=0):
    unit = unit*5
    cgst = unit*12.5/100
    sgst = unit*12.5/100
    pay = unit+cgst+sgst
    print("unit = {}".format(unit))
    print("unit = {}".format(cgst))
    print("unit = {}".format(sgst))
    print("unit = {}".format(pay))
elif(unit>=101 and unit<=200):
    unit = unit*8
    cgst = unit*12.5/100
    sgst = unit*12.5/100
    pay = unit+cgst+sgst
    print("unit = {}".format(unit))
    print("unit = {}".format(cgst))
    print("unit = {}".format(sgst))
    print("unit = {}".format(pay))
elif(unit>=201 and unit<=300):
    unit = unit*10
    cgst = unit*12.5/100
    sgst = unit*12.5/100
    pay = unit+cgst+sgst
    print("unit = {}".format(unit))
    print("unit = {}".format(cgst))
    print("unit = {}".format(sgst))
    print("unit = {}".format(pay))
else:
    unit = unit*12
    cgst = unit*12.5/100
    sgst = unit*12.5/100
    pay = unit+cgst+sgst
    print("unit = {}".format(unit))
    print("unit = {}".format(cgst))
    print("unit = {}".format(sgst))
    print("unit = {}".format(pay))
    
    
    
    
    
    
