
degree_sign = u"\N{DEGREE SIGN}"

print('Wellcome to Convert DMS to Decimal Degree Tool.')

d_input = input('Enter Degree: ')
m_input = input('Enter Minutes: ')
s_input = input('Enter Seconds: ')

dms = str(d_input)+degree_sign+' '+str(m_input)+"' "+str(s_input)+"\""


m_decimal = int(m_input)/60
s_decimal = int(s_input)/3600
sum_decimal = m_decimal+s_decimal

decimal_d = int(d_input)+sum_decimal

print('Your DMS is '+str(dms) )
print('The decimal Drgree is '+str(decimal_d))
