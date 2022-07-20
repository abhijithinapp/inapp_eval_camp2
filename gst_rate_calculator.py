def totalPrice(basePrice, gstRate):
    priceAfterCGSTorSGST = basePrice + ((gstRate/2)/100)*basePrice
    print("Actual price of item: %d" %(basePrice))
    print("Price after CGST: %d" %(priceAfterCGSTorSGST ))
    print("Price after SGST: %d" %(priceAfterCGSTorSGST ))
    print("Total price with GST: %d" %(priceAfterCGSTorSGST * 2 ))
    

basePrice = int(input("Enter base price: "))
gstRate = int(input("Enter gst rate: "))
totalPrice(basePrice,gstRate)

