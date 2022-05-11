largest = 0
smallest = 0

while True:
    
    try:
        
        num = input("Enter a number: ")
        if num == "done":
            break
        
        n = int(num)
        largest = n if largest < n or largest == 0 else largest
        smallest = n if smallest > n or smallest == 0 else smallest
        
    except:
        print("Invalid input")
        
        
print("Maximum is", largest)
print("Minimum is", smallest)