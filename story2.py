from time import sleep
greeting=input('Welcome to The Restaurant. Would you like to order something?: ')

def greeting2(greeting):
    if greeting.lower()=='yes' or greeting.lower()=='y' or greeting=='1':
        pizza_burger=input('Do you want a pizza or a burger?: ')
        pizza_burger2(pizza_burger)
    else:
        print('Okay bye.')
        sleep(1)
        exit()

#---------------------------------------------------------------------------------------------------------------------------------------------------------

def pizza_burger2(pizza_burger):
    if pizza_burger.lower()=='pizza' or pizza_burger=='1':
        a='pizza'
        small_medium_large=input('Do you want a small, medium, or large?: ')
        small_medium_large2(small_medium_large, pizza_burger)      
    elif pizza_burger.lower()=='burger' or pizza_burger=='2':
        a='burger'
        burger_meat=input('Do you want a cheeseburger or a hamburger?: ')
        burger_meat2(burger_meat, pizza_burger)
    else:
        print("That's not an option.")
        sleep(.5)
        greeting2(greeting)

#---------------------------------------------------------------------------------------------------------------------------------------------------------

def burger_meat2(burger_meat, pizza_burger):
    if burger_meat.lower()=='cheeseburger' or burger_meat=='1':
        b='cheeseburger'
        lettuce=input('Would you like lettuce on your ' + b + '?: ')
        lettuce2(lettuce, burger_meat, pizza_burger)
    elif burger_meat.lower()=='hamburger' or burger_meat=='2':
        b='hamburger'
        lettuce=input('Would you like lettuce on your ' + b + '?: ')
        lettuce2(lettuce, burger_meat, pizza_burger)
    else:
        print("That's not an option.")
        sleep(.5)
        pizza_burger2(pizza_burger)

def small_medium_large2(small_medium_large, pizza_burger):
    if small_medium_large.lower()=='small' or small_medium_large=='1':
        b='small'
        pizza_type=input('Do you want a cheese, pepperoni, buffalo chicken, bbq chicken, or meat lovers pizza?: ')
        pizza_type2(pizza_type, small_medium_large, pizza_burger)
    elif small_medium_large.lower()=='medium' or small_medium_large.lower()=='med' or small_medium_large=='2':
        b='medium'
        pizza_type=input('Do you want a cheese, pepperoni, buffalo chicken, bbq chicken, or meat lovers pizza?: ')
        pizza_type2(pizza_type, small_medium_large, pizza_burger)
    elif small_medium_large.lower()=='large' or small_medium_large=='3':
        b='large'
        pizza_type=input('Do you want a cheese, pepperoni, buffalo chicken, bbq chicken, or meat lovers pizza?: ')
        pizza_type2(pizza_type, small_medium_large, pizza_burger)
    else:
        print("That's not an option.")
        sleep(.5)
        pizza_burger2(pizza_burger)

#---------------------------------------------------------------------------------------------------------------------------------------------------------

def lettuce2(lettuce, burger_meat, pizza_burger):
    if lettuce.lower()=='yes' or lettuce.lower()=='y' or lettuce=='1':
        c='with'
        tomato=input('How about tomatoes?: ')
        tomato2(tomato, lettuce, burger_meat, pizza_burger)
    elif lettuce.lower()=='no' or lettuce.lower()=='n' or lettuce=='2':
        c='without'
        tomato=input('How about tomatoes?: ')
        tomato2(tomato, lettuce, burger_meat, pizza_burger)
    else:
        print("That's not an option.")
        sleep(.5)
        burger_meat2(burger_meat, pizza_burger)

def pizza_type2(pizza_type, small_medium_large, pizza_burger):
    if pizza_type.lower()=='cheese' or pizza_type.lower()=='cheese pizza' or pizza_type.lower()=='1':
        c='cheese'
        drink=input('Do you want a drink?: ')
        drink2(drink, pizza_type, small_medium_large, pizza_burger)
    elif pizza_type.lower()=='pepperoni' or pizza_type.lower()=='pepperoni pizza' or pizza_type.lower()=='2':
        c='pepperoni'
        drink=input('Do you want a drink?: ')
        drink2(drink, pizza_type, small_medium_large, pizza_burger)
    elif pizza_type.lower()=='buffalo' or pizza_type.lower()=='buffalo chicken' or pizza_type.lower()=='buffalo chicken pizza' or pizza_type.lower()=='3':
        c='buffalo chicken'
        drink=input('Do you want a drink?: ')
        drink2(drink, pizza_type, small_medium_large, pizza_burger)
    elif pizza_type.lower()=='bbq chicken' or pizza_type.lower()=='bbq' or pizza_type.lower=='bbq chicken pizza' or pizza_type.lower()=='4':
        c='bbq chicken'
        drink=input('Do you want a drink?: ')
        drink2(drink, pizza_type, small_medium_large, pizza_burger)
    elif pizza_type.lower()=='meat' or pizza_type.lower()=='meatlovers' or pizza_type.lower()=='meat lovers' or pizza_type.lower()=='meat lovers pizza' or pizza_type.lower()=='meatlovers pizza' or pizza_type.lower()=='5':
        c='meat lovers'
        drink=input('Do you want a drink?: ')
        drink2(drink, pizza_type, small_medium_large, pizza_burger)
    else:
        print("That's not an option.")
        sleep(.5)
        small_medium_large2(small_medium_large, pizza_burger)

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    
def tomato2(tomato, lettuce, burger_meat, pizza_burger):
    print("I didn't finish yet.")

def drink2(drink, pizza_type, small_medium_large, pizza_burger):
    print("I didn't finish yet.")


"""def tomato2(tomato, lettuce, burger_meat, pizza_burger):
    if tomato.lower()=='yes' or tomato.lower()=='ok':
        d='with'
    elif tomato.lower()=='no':
        d='without'
    else:
        print("That's not an option.")
        sleep(.5)
        lettuce2(lettuce, burger_meat, pizza_burger)


def drink2(drink, pizza_type, small_medium_large, pizza_burger):
    if drink.lower()=='yes':
        d='with'
        drink_type=input('Do you want a water, coke, pepsi, dr pepper, root beer, or sprite?: ')
        drink_type2(drink_type)
    elif drink.lower()=='no':
        d='without'
        no_drink_side=input('Do you want a side?: ')
        no_drink_side2(no_drink_side)
    else:
        print("That's not an option.")
        sleep(.5)
        pizza_type2(pizza_type, small_medium_large, pizza_burger)"""
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------

greeting2(greeting)





