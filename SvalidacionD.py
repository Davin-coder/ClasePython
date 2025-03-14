#sistema de validacion de datos

nombrep = str (input('ingrese el nombre del producto: '))

#comando if para validar si el nombre ingresado es de tipo str
if (type(str(nombrep)).__name__=='str'):
    print('nombre de producto valido')

# bucle tipo while true para regresar al input si este no cumple las condiciones
while True:
    
    try:
        preciop = float (input('ingrese el precio del producto: '))
        
        if (type(float(preciop)).__name__!='float'):
            continue #continue para volver al input
        
        if ( preciop <= 0):
            print('el valor no puede ser negativo')
            continue
        
        #valida si el valor es tipo float y mayor a 0 para terminar el bucle
        if (type(float(preciop)).__name__=='float' and preciop >= 0):
            print('precio de producto valido ')
        break #break para romper el bucle si se cumple la condicion
    
    except ValueError: #except valuerror para cuando se ingrese algun valor erroneo, repetir desde el input
        print('ingrese un valor valido') 
# bucle tipo while true para regresar al usuario al input si este ingresa una cantidad no valida
while True:
    
    try:
        cantp = int (input('ingrese la cantidad de productos a comprar: '))
        
        if (type(int(cantp)).__name__!='int'):
            print('el valor debe ser un numero entero')
            continue
        
        if (cantp < 0):
            print('la cantidad debe ser positiva')
            continue #continue para regresar al input si se cumple la condicion
        
        #valida si al cumplir la condicion rompe el bucle
        if (type(int(cantp)).__name__=='int'):
            print('cantidad ingresada valida')
            break
    
    except ValueError:
        print('porfavor ingrese una cantidad valida')
#verificar si se le va a aplicar descuento o no al producto
while True:
    
        desc = input('desea ingresar un descuento?(si/no): ').lower() #terminacion en .lower para que no importe si la respuesta se usan mayusculas
        
        if desc == 'si' or desc == 'no':
            
            break
        
        else:
            print('la respuesta ingresada no es valida')
#operador logico if para ingresar el descuento si el usuario quiere asignar uno          
if desc == 'si':
    
    while True:
        
        try:
            
            descp = int(input('ingrese la cantidad de descuento: '))
        
            if descp < 0:
                
                print('porfavor ingrese un valor positivo')
                continue
        
            if (type(int(descp)).__name__=='int' and descp <= 0 >= 100):
                 print('valor de descuento valido')
            break
           
        except ValueError:
            print('ingrese un valor valido')
#operador logico if por si el usuario no quiere agregar un descuento, este no lo calcule       
if desc == 'no':
    
    descp = 0
                
subtotal = (preciop * cantp)   
monto_descontado = (subtotal * (descp / 100))
total = subtotal * (1 - descp / 100)

print ('---FACTURA DE LA COMPRA---')

print (f'Nombre de producto: {nombrep}')

print (f'Precio unitario del producto: ${preciop}')

print (f'Cantidad ha comprar: {cantp}')

print (f'Subtotal: ${round(subtotal, 2)}') #uso round para redondear y despues de la variable asigno el numero de decimales que quiero que tome en cuenta

print (f'Monto descontado: -${monto_descontado}')

print (f'TOTAL: ${round(total, 2)}') #uso round para redondear y despues de la variable asigno el numero de decimales que quiero que tome en cuenta
