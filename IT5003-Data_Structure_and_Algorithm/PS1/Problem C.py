pension_f = float(input())
property_f = float(input())
money = []
year_salaries = 0
exemption = 59665
tax_base = 0
for i in range(12):
    money.append(float(input()))

for i in range(12):
    tax = 0
    funds = int(money[i] * pension_f * 0.01) + int(money[i] * property_f * 0.01)
    tax_base =int(money[i]) - funds
    if tax_base <= 0:
        tax = 0
    elif tax_base <= 409986:
        tax = int(tax_base * 0.3145)
    elif tax_base <= 1151012:
        tax = int(409986 * 0.3145 + (tax_base - 409986) * 0.3795)
    else:
        tax = int((tax_base - 1151012) * 0.4625 + 409986 * 0.3145 + (1151013 - 409987)* 0.3795)
    if tax <= exemption:
        year_salaries += money[i] - funds
        exemption += 59665 - tax
    else:
        year_salaries += money[i] - funds - (tax - exemption) 
        exemption = 59665
print(int(year_salaries))
    
#666
