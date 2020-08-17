greet = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""
print(greet)
menu = {"Wings":0,"Coockies":0,"Spring Rolls":0,"Salmon":0,"Steak":0,"Meat Tornado":0,"A Literal Garden":0,"Ice Cream":0,"Cake":0,"Pie":0,"Coffee":0,"Tea":0,"Unicorn Tears":0}


def customerOrder():
    while True:
        order = input()
        if order == "quit":
            break
        elif order in menu:
            menu[order]+=1
            print(f"** {menu[order]} order of {order} have been added to your meal **")
        else:print("Not a valid order")

customerOrder()

