from pyscript import document, display

tax = 0.12
subtax = tax * subtotal
grandtot = subtotal + price

def add_num(e): #put e for the event handler
    document.getElementById("output1").innerHTML = "" #clears previous result
    num1 = float(document.getElementById("input1").value) #get input value
    num2 = float(document.getElementById("input1").value) #get input value
result = num1 + num2 #use operator
display(result, target="output1") #display result

def create_order(e):
    document.getElementById("output2").innerHTML = "" #clears previous result
    prod1=document.getElementById("item1") #get item 1 id
    #Calcuclate
    subtotal = float(prod1.value) * prod1.checked
    size = document.querySelector("input[name= 'size']: checked")
    price = float(size.value)
    grandtotal = subtotal + price
    display (grandtotal, target="output2")

def place_order(e):
    document.getElementById("output3").innerHTML = "" #clear previous result

    coffee = document.getELementById("coffee")
    coffee_price = float(coffee.value)
    display(coffee_price, target = "output3")

def show_order(e):
    document.getElementById("output4").innerHTML = "" #clears previous result
    prod1=document.getElementById("prod1") #get item 1 id
    subtotal = float(prod1.value) * prod1.checked
    size = document.querySelector("input[name= 'size']: checked")
    price = float(size.value)
    grandtotal = subtotal + price
    final_order = grandtotal + coffee_price
    display(f'You have to pay a total of {final_order}', target="output4")

subtotal = (float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked
)

display(f"Subtotal: {Subtotal}.", target="output1")
display(f"Tax: {tax}.", target="output1", append=True)
display(f"Total: {total}.", target="output1", append=True)
display("Thank you for your order!", target="output1", append=True)
