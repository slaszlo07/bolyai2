a=15
if a%2==0:
	print("Páros")
else:
	print("Páratlan")


szo = input("írjon be egy szót:")
if szo == "tűzliliom":
    print("Ezt ismerem,csodaszp virág!")
else:
    print("Ez egy nagyon szép szó!")

kereset =(float(input("Írja be a keresetét:")))
if kereset < 14400:
    print("Nem kell adót fizetni")
elif (kereset >= 14400) and (kereset< 34000):
    print("19% adó kell fizetni")
elif kereset >= 34000:
    print("29% adót kell fizetni")