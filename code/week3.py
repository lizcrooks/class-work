hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)
if h > 40.0 :
    overtime = (h - 40)
    reghrs = h - overtime
    gross_pay = (reghrs * r) + (overtime * (r * 1.5))
print gross_pay
