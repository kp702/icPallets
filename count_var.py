gall_run = input("how many gallons are being run?")
siz_run = input("pints, 56, or tubs?")
print("you are running {gall_run} of {siz_run} today?")

pints = 8 * gall_run #8 pints per gallon
half_gal = 128 / 56 #128 ounces per gallon
tubs = gall_run / 3 #3 gallons per tub

    if siz_run = "pints":
        print(f"{gall_run} gallons will be approximatly {pints} total pints.")
    elif siz_run = "half_gal":
        print(f"{gall_run} gallons will be approximatly {half_gal} total 56 ounce containers.")
    elif siz_run = "tubs":
        print(f"{gall_run} gallons will be approximatly {tubs} total tubs.")
    else:
        print("enter a valid selection")
        
        
        
