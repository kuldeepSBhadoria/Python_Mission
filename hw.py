Items = [('Shoes', 20.0), ('Banana', .5), ('Shirt', 5), ('Coffee', 3), ('Egg', 1), ('Watch', 50) , ('bag', 99), ('book', 8), ('Bulb', 11), ('Lamp',23)] 

while True:
    affordable = []
    
    user_ip = (input(' Enter any Price : '))
    if not user_ip:
        print(' ...Exit .. ')
        break
    for t in Items:
        try:
            if( float(user_ip) >= float(t[1])):
                affordable.append(t[0])
        except ValueError:
            print('Please Enter Numeric  Only')
            break
            
    print ('\t You can Afford {}'.format(affordable))
