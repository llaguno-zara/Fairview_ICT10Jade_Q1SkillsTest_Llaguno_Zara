from pyscript import document, display

def place_order(e):
    document.getElementById("output1").innerHTML = " " # clears previous result
    prod1 = document.getElementById("item1") #get item1
    prod2 = document.getElementById("item2") #get item2
    prod3 = document.getElementById("item3") #get item3
    prod4 = document.getElementById("item4") #get item4
    prod5 = document.getElementById("item5") #get item5

    drinktot = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked + float(prod5.value) * prod5.checked

    size = document.querySelector("input[name='size']:checked")
    sizpr = float(size.value)
    grandtot = drinktot + sizpr

    extras = document.getElementById("coffee")
    extras_price = float(extras.value)

    fixed = grandtot + extras_price
    tax = fixed * 0.12 #vat 12%
    taxpr = fixed + tax # order total + tax

    final = taxpr

    display(f"Subtotal: ₱{fixed}", target="output1")
    display(f"Tax: ₱{tax}", target="output1", append=True)
    display(f"Total: ₱{final}", target="output1", append=True)
    display("--------------------------", target="output1", append=True)
    display("Thank you for ordering!", target="output1", append=True)
