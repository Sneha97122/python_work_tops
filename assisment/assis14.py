orders=[]
tax_rate=0.18

def book_orders():
    name=input("enter customer name:-")
    device=input("enter the name of device:-")
    issue=input("enter the issue of the device:-")
    date=input("enter the date :-")

    order={
        "customer":name,
        "device":device,
        "issue":issue,
        "date":date
    }

    orders.append(order)
    print("data is insert")
    print("----------------------")

def bill_genrate():
    if not orders:
        print("no order is found")
        return

    for i, order in enumerate(orders):
            print(f"{i+1} :-{order['customer']}-{order['device']}")

    num=int(input("select order number:-"))-1
    order=orders[num]

    parts_cost=float(input("parts cost: "))
    repair_fee=float(input("repair fee: "))
    discount =float(input("discount :"))

    subtotal=parts_cost + repair_fee
    tax=subtotal* tax_rate
    total =subtotal + tax - discount

    print("\n---------- FIXTRACK BILL ----------")
    print("Customer:", order["customer"])
    print("Device:", order["device"])
    print("Issue:", order["issue"])
    print("Parts Cost:", parts_cost)
    print("Repair Fee:", repair_fee)
    print("Tax (18%):", tax)
    print("Discount:", discount)
    print("Final Amount:", total)
    print("------------------------------------")

def display():
    if not orders:
        print("no order is found")
        return

    for i, order in enumerate(orders):
         print(f"{i+1}.{order['customer']}-{order['device']}")

def main():
    while True:
        print("------------------------")
        print("1. adding the data")
        print("2.showing data")
        print("3.genrate bill")
        print("4. exit")
        print("------------------------")

        choise=int(input("enter your choise(1/2/3/4)"))

        if choise == 1:
            book_orders()
        elif choise == 2:
            display()
        elif choise == 3:
           bill_genrate()
        elif choise == 4:
            print("goodbyy")
            break
        else:
            print("invalid choise")

main()


