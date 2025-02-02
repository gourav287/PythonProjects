"""
As per the latest budget (2025) by Indian FM N. Sitharaman, there will be no taxes for
individuals earning below ₹12Lac per annum
For people earning above ₹12Lac in an year, here are the slabs:
₹0-4Lac          - No tax
₹4-8Lac          - 5%
₹8-12Lac         - 10%
₹12-16Lac        - 15%
₹16-20Lac        - 20%
₹20-24Lac        - 25%
₹24Lac and above - 30%

This is a basic tax simulator that simply tells you your taxes based on your exact salary
The numbers will vary based on other factors like allowances, investments, dividends, etc.
"""

salary = int(input("Please enter your yearly compensation: "))

tax_percent = 0
total_tax = 0
distribution = 400000

if salary > distribution*3:
    for i in range(7):
        if salary <= 0:
            break
        elif i == 6 or salary <= distribution:
            total_tax += (tax_percent * salary) / 100
            break
        else:
            total_tax += (tax_percent * distribution) / 100
            salary -= distribution
            tax_percent += 5

print("You will pay Rs.", total_tax, "in taxes")