food = float (input ("Enter your food amount: "))
tip = int (input ("Enter your tip %: "))
tax = 0.8

tip_amt = food * tip/100
tax_amt = food * tax
total = food + tip_amt + tax_amt

print(f"Your food is ${food} and your tip is ${tip_amt}.")
print(f"Your total with tax was {total}.")