from typing import Counter


intro_msg=['**************************************','**    Welcome to the Snakes Cafe!   **','**    Please see our menu below.    **','**','** To quit at any time, type "quit" **','**************************************']
for i in intro_msg:
    print(i)
   
print('')

menu=[
    {
        "name":"Appetizers",
        "items":['Wings','Cookies','Spring Rolls'],
    },
        {
        "name":"Entrees",
        "items":['Salmon','Steak','Meat Tornado','A Literal Garden'],
    },
        {
        "name":"Desserts",
        "items":['Ice Cream','Cake','Pie'],
    },
        {
        "name":"Drinks",
        "items":['Coffee','Tea','latte'],
    }
]

for i in menu:
    print(i['name'])
    print('----------')
    for x in i['items']:
        print(x)
    print('')
orders=[]
print("""***********************************
** What would you like to order? **
***********************************
    """)

while True:
    order=input('> ')
    order=order.capitalize()
    if order=='Quit':
        break
    else:
        orders.append(order)
        c=Counter(orders)
        if c[order]==1:
             print(f"** {c[order]} order of {order} added to your meal **")
             print('')
        else:
            print(f"** {c[order]} orders of {order} added to your meal **")
            print('')

 


 
