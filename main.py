import datetime
from db import motor

def agregar_gastos():
    descripcion= input("Ingrese la descripcion del gasto: ")
    monto= float(input("Ingrese el monto del gasto: "))
    categoria= input("Ingrese la categoria del gasto: ")
    fecha_hoy= datetime.datetime.today().strftime("%d/%m/%Y")

    gasto= {"descripcion": descripcion,
            "monto": monto,
            "categoria": categoria,
            "fecha": fecha_hoy}
    return gasto
print(motor)
def eliminar_gastos():
    pass

def mostrar_gastos():
    pass

def editar_gastos():
    pass

def ver_gasto_total():
    pass

def interfaz():
    diccionario_funciones= {"1": agregar_gastos,
                            "2": eliminar_gastos,
                            "3": mostrar_gastos,
                            "4": editar_gastos,
                            "5": ver_gasto_total}

    while True:
        print("CONTADOR DE GASTOS")
        print("1. Agregar gasto")
        print("2. Eliminar gasto")
        print("3. Mostrar gastos")
        print("4. Editar gastos")
        print("5. Ver gasto total")
        print("6.Salir")

        opcion= input("Ingrese una opcion: ")

        if opcion == "6":
            break
        else:
            resultado=diccionario_funciones[opcion]()

    print(resultado)  