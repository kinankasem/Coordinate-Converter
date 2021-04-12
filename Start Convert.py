print("Wellcome to Converter Tool, Let's Start..!")
en = input("If you want convert DMS to Decimal Degree, Enter 1\nIf you want convert Decimal Degree to DMS, Enter 2 ")
if en == '1':
    from tools import DMS_to_DD
elif en == '2':
    from tools import DD_to_DMS