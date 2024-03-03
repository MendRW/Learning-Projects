# def = store
# invoke or use excluded
# to call the function, just say the defined name of the function
# arguments adjust how the function is invoked
# given function named x
# def x(lang)
def x(lang)
    if lang == 'es':
        print('Hola')
    elif lang == 'fr' :
        print('Bonjour')
    else:
        print('hello')
# checks if lang is es, fr else choose eng
x('en')
x('es')
x('fr')
# def rememmbers what x means 
