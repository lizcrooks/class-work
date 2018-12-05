def computepay(a,b):
        if a <= 40.0 :
            pay = a * b
        else :
            pay = b * 40 + (b * 1.5 * (a - 40))
        return pay
        
hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)
   
p = computepay(h,r)
print p
