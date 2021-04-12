degree_sign = u"\N{DEGREE SIGN}" 
a='.'       # For identify the decimal number.
d_n=0       # For identify the count numbers before '.'
print('Wellcome to Convert Decimal Degree to DMS Tool.')

decimal_d = input('Enter Decimal Degree: ')   # Enter Coordinate like (42.3698)

s=list(decimal_d)           # Convert the Decimal Degree to List

for i in s:                 # for loop for count the numbers.
    d_n = d_n + 1
    if a in i:
        break

d_n = d_n - 1

d = decimal_d[:d_n]         # Select the Degree number
m = '0'+decimal_d[d_n:]     # Select the Decimal Number

float_m = float(m) * 60     # Convert from String to Float 
mi = str(float_m)[:2]       # Then convert to String to identify the Minutes

s = '0.'+str(float_m)[3:]   
float_s = float(s) * 60     # Identify the Scondes

dms = str(d)+degree_sign+' '+str(mi)+"' "+str(float_s)+"\""
print(dms)
