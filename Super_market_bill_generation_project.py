from datetime import datetime
user_name = input("Please enter your name: ")
greeting_msg = "Hello {} thank you for choosing Appaji Mart."
print(greeting_msg.format(user_name))

groceries_list = '''
1.Rice                                   Rs:60.23/KG
2.Sunflower oil                          Rs:120.09/L
3.Grountnut oil                          Rs:160.56/L
4.Salt                                   Rs:25.50/KG
5.Home Paper Napkins(100 Pcs)            Rs:35.70/-
6.Vim Diswash Bar                        Rs:80.90/-
7.Maggie                                 Rs:14.99/-
8.Cinthol Bath Soaps 150g (pack of 4)    RS:234.76/-
9.Wheat Atta                             Rs:50.89/-
10.SurfExcel                             Rs:250.56/-
11.Green Elachi 10g                      Rs:70.78/-
12.Bru 100g                              Rs:300.90/-
13.Sugar                                 Rs:50.45/kg
14.Harpic Toilet Cleaner                 Rs:350.32/L
15.Washed Gota Urad Dal                  Rs:130.90/KG
16.Idly Ravva                            Rs:50.89/KG
17.Lapsi Ravva                           Rs:50.45/KG
18.Bombay Sooji                          Rs:50.90/KG
19.Jangery                               Rs:70.99/KG
'''

groceries_set = {"Rice": 60.23,
"Sunflower oil":120.09,
"Grountnut oil":160.56,
"Salt":25.50,
"Home Paper Napkins(100 Pcs)":35.70,
"Vim Diswash Bar":80.90,
"Maggie":14.99,
"Cinthol Bath Soaps 150g (pack of 4)":234.76,
"Wheat Atta":50.89,
"SurfExcel":250.56,
"Green Elachi 10g":70.78,
"Bru 100g":300.90,
"Sugar" :50.45,
"Harpic Toilet Cleaner":350.32,
"Washed Gota Urad Dal":130.90,
"Idly Ravva":50.89,
"Lapsi Ravva":50.45,
"Bombay Sooji": 50.90,
"Jangery":70.99
}

cart = []
total_price = 0
loop = True
again_loop = False
for i in range (2):
    option = int(input("If you would like to buy groceries Press 1: "))
    if option == 1:
        loop = False
        print(groceries_list)
        total_len = len(groceries_list)
        status = "No"
        for i in range(total_len):
            if status == "No":
                again_loop = True
                if i == 0:
                    keys = int(input("Press the item key what would you like to buy, Please press groccery ID: "))
                    quantity = int(input("How much quantity do you want: "))
                if keys == 1: 
                    price = quantity * int(groceries_set["Rice"])
                    total_price += price
                    cart.append((keys,"Rice",quantity,price))
                    total_len += 1
                elif keys == 2: 
                    price = quantity * groceries_set["Sunflower oil"]
                    total_price += price
                    cart.append((keys,"Sunflower oil",quantity,price))
                    total_len += 1
                elif keys == 3: 
                    price = quantity * groceries_set["Grountnut oil"]
                    total_price += price
                    cart.append((keys,"Grountnut oil",quantity,price))
                    total_len += 1
                elif keys == 4: 
                    price = quantity * groceries_set["Salt"]
                    total_price += price
                    cart.append((keys,"Salt",quantity,price))
                    total_len += 1
                elif keys == 5: 
                    price = quantity * groceries_set["Home Paper Napkins(100 Pcs)"]
                    total_price += price
                    cart.append((keys,"Home Paper Napkins(100 Pcs)",quantity,price))
                    total_len += 1
                elif keys == 6: 
                    price = quantity * groceries_set["Vim Diswash Bar"]
                    total_price += price
                    cart.append((keys,"Vim Diswash Bar",quantity,price))
                    total_len += 1
                elif keys == 7: 
                    price = quantity * groceries_set["Maggie"]
                    total_price += price
                    cart.append((keys,"Maggie",quantity,price))
                    total_len += 1
                elif keys == 8: 
                    price = quantity * groceries_set["Cinthol Bath Soaps 150g (pack of 4)"]
                    total_price += price
                    cart.append((keys,"Cinthol Bath Soaps 150g (pack of 4)",quantity,price))
                    total_len += 1
                elif keys == 9: 
                    price = quantity * groceries_set["Wheat Atta"]
                    total_price += price
                    cart.append((keys,"Wheat Atta",quantity,price))
                    total_len += 1
                elif keys == 10: 
                    price = quantity * groceries_set["SurfExcel"]
                    total_price += price
                    cart.append((keys,"SurfExcel",quantity,price))
                    total_len += 1
                elif keys == 11: 
                    price = quantity * groceries_set["Green Elachi 10g"]
                    total_price += price
                    cart.append((keys,"Green Elachi 10g",quantity,price))
                    total_len += 1
                elif keys == 12: 
                    price = quantity * groceries_set["Bru 100g"]
                    total_price += price
                    cart.append((keys,"Bru 100g",quantity,price))
                    total_len += 1
                elif keys == 13: 
                    price = quantity * groceries_set["Sugar"]
                    total_price += price
                    cart.append((keys,"Sugar",quantity,price))
                    total_len += 1
                elif keys == 14:
                    price = quantity * groceries_set["Harpic Toilet Cleaner"]
                    total_price += price
                    cart.append((keys,"Harpic Toilet Cleaner",quantity,price))
                    total_len += 1
                elif keys == 15:
                    price = quantity * groceries_set["Washed Gota Urad Dal"]
                    total_price += price
                    cart.append((keys,"Washed Gota Urad Dal",quantity,price))
                    total_len += 1
                elif keys == 16:
                    price = quantity * groceries_set["Idly Ravva"]
                    total_price += price
                    cart.append((keys,"Idly Ravva",quantity,price))
                    total_len += 1
                elif keys == 17:
                    price = quantity * groceries_set["Lapsi Ravva"]
                    total_price += price
                    cart.append((keys,"Lapsi Ravva",quantity,price))
                    total_len += 1
                elif keys == 18:
                    price = quantity * groceries_set["Bombay Sooji"]
                    total_price += price
                    cart.append((keys,"Bombay Sooji",quantity,price))
                    total_len += 1
                elif keys == 19:
                    price = quantity * groceries_set["Jangery"]
                    total_price += price
                    cart.append((keys,"Jangery",quantity,price))
                    total_len += 1
                print("Your item has been added into cart sucessfully!")
                a = input("If you would like to add some more items Press 'Yes' (or) If you would like to generate your bill Press 'No': " )
                if a == "yes" or a == "Yes" or a == "YES":
                    keys = int(input("Press the item key what would you like to buy, Please press groccery ID: "))
                    quantity = int(input("How much quantity do you want: "))
                elif a == "no" or a == "No" or a == "No":
                    status = "Yes"
                    print("- " * 75)
                    print("Date and Time: ", datetime.now())
                    print("- " * 75)
                    print(" " * 3,"ID"," " * 15,"Items"," " * 33,"Quantity"," " * 8,"Price")
                    print("- " * 75)
                    for ids,item,quantity,price in cart:
                        print((2 - len((str(ids)))) * " ", (1 * " "),ids, " " * 16,item,(40 - len(item)) * " ",quantity,(" " * (15 - (len(str(quantity))))),round(price,2))
                    print("- " * 75)
                    print("Total Amount"," " * 68, str(round(total_price,2)))
                    print("- " * 75)
                    print("Thank you for shopping at Appaji Mart,Please Visit again!")
                    break
                else:
                    print("Enter correct value") 
        if again_loop:
            break                 
    else:
        if i == 1 and (loop is True):
            print("You entered wrong key again, please try after some time, Thank you!")
            break
        print("You entered wrong key, please press correct key!")  