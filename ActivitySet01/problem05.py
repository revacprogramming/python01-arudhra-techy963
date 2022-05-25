def computepay(h, r):
    
    if h <= 40:
    	p = h * r
    
    elif h > 40:
        p = 40*r + (h - 40 ) *1.5 *r

    return p


hrs = int(input("Enter Hours:"))
rate = float(input("Enter rate: "))

pay = computepay(hrs, rate)
print("Pay", pay)


        