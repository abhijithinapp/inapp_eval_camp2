def totalPrice(basePrice, gstRate):
    priceAfterCGSTorSGST = basePrice + ((gstRate/2)/100)*basePrice
    print("Actual price of item: %.2f" %(basePrice))
    print("Price after CGST: %.2f" %(priceAfterCGSTorSGST ))
    print("Price after SGST: %.2f" %(priceAfterCGSTorSGST ))
    print("Total price with GST: %.2f" %(priceAfterCGSTorSGST * 2 ))
    

basePrice = int(input("Enter base price: "))
gstRate = int(input("Enter gst rate: "))
totalPrice(basePrice,gstRate)

