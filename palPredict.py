print("\nWELCOME TO MY ICE CREAM PALLET PREDICTOR!\n " * 4)
#ask what product is being run
product = input("What product are we going to run? (pints, halfs, or tubs) ")

# !!NEED A BREAK FOR INCCORRECT INPUT!!

#ask how many gallons will be run
gallons = input(f"How many gallons of {product} are we running? ")

#pint calculations
pints = int(gallons) * 8
pintPk = pints // 6
pintLyr = pintPk //20
pintPal = pintLyr / 14

#half calculations
gal = int(gallons) * 168 #gallons to ounces
halfs = gal // 56
halfPk = halfs // 6
halfLyr = halfPk // 12
halfPal = halfLyr / 11


#tubs calculations
tubs = int(gallons) / 3 #3 gallons per tub
tubsLyr = tubs / 20
tubsPal = tubsLyr / 5


#output statements
if product == "pints":
    print(f"There should be about {round(pintPal,1)} pallet(s) or {pintLyr} total layers of pints.")
elif product == "halfs":
    print(f"There should be about {round(halfPal,1)} pallet(s) or {halfLyr} total layers of halfs.")
elif product == "tubs":
    print(f"There should be about {tubsPal} pallet(s) or {tubsLyr} total layers of tubs.")
else: #only works after both inputs
    print("Please enter 'pints, halfs, or tubs' to continue")
