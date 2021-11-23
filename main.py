from typing import Union, Any

Menu = {'Yum Burger': .99, 'Yum Fries': .79, 'Yum Soda': 1.09}
tax_percent = 0.6
total_burgers = 0
total_fries = 0
total_sodas = 0
sub_total = 0
taxes = 0.0
total_cost = 0.0

print('Menu')
print(' Yum Burger: 0.99$\n', 'Yum Fries: 0.79$\n', 'Yum Soda : 1.09$\n')


def input_int(prompt, default_value):
    value = input(prompt)
    try:
        int_value = int(value)
    except:
        int_value = default_value
    return int_value


def new_order():
    global total_burgers
    global total_fries
    global total_sodas
    global sub_total
    global taxes
    global total_cost

    total_burgers = input_int('How many burgers would you like? ', 0) + total_burgers
    total_fries = input_int('How many fries would you like? ', 0) + total_fries
    total_sodas = input_int('How many sodas would you like? ', 0) + total_sodas
    sub_total = total_burgers * Menu['Yum Burger'] + total_fries * Menu['Yum Fries'] + total_sodas * Menu['Yum Soda']
    taxes = sub_total * tax_percent
    total_cost = sub_total * tax_percent + sub_total


def plurals(value, one_of, other):
    if value == 1:
        return one_of
    else:
        return other


def receipt():
    print('\nReceipt')
    print('',
          total_burgers, plurals(total_burgers, 'Burger\n', 'Burgers\n'),
          total_fries, plurals(total_fries, 'Fry\n', 'Fries\n'),
          total_sodas, plurals(total_sodas, 'Soda\n', 'Sodas\n')
          )

    print('Sub-Total:', "{:.2f}".format(sub_total))
    print('Taxes 6%:', "{:.2f}".format(taxes))
    print('Total:', "{:.2f}".format(total_cost), '$')


def keep_going(value):
    return not(value == 'N' or value == 'No' or value == 'n' or value == 'no')


def customer_order():
    continue_order = ''

    while keep_going(continue_order):
        new_order()
        continue_order = input('Would you like anything else (Y/N)? ')
    receipt()


customer_order()
