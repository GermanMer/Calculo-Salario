#Este programa solicita al usuario que ingrese la cantidad de horas trabajadas y la tarifa por hora.
#Con esa información, calcula el salario correspondiente, teniendo en cuenta que las horas que excedan un total de 40 horas trabajadas se pagarán a una tarifa equivalente a una hora y media.

while True:
    horas = input('Introduzca cantidad de horas trabajadas: ')
    try:
        horas = float(horas)
        break  # Continuar si se ha ingresado un número válido
    except ValueError:
        print('Error, por favor introduzca un número válido')

while True:
    tarifa = input('Introduzca tarifa por hora: ')
    try:
        tarifa = float(tarifa)
        break  # Continuar si se ha ingresado un número válido
    except ValueError:
        print('Error, por favor introduzca un número válido')

if horas > 40.0:
    horas_extra = horas - 40.0
    tarifa_horas_extra = tarifa * 1.5
    salario = ((horas - horas_extra) * tarifa) + (horas_extra * tarifa_horas_extra)
else:
    salario = horas * tarifa

print('Salario:', salario)

#En este código, se utiliza un bucle while para solicitar el input repetidamente hasta que se introduzca un valor numérico válido.
#Si se ingresa un valor no numérico, se muestra un mensaje de error y se vuelve a solicitar el input.
#El bucle continuará hasta que se ingrese un valor válido, momento en el que se romperá el bucle y el programa continuará ejecutándose.
