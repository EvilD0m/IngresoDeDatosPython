def sistemaAlumnos():
    opciones = 0
while True:
    print('''
!Ingreso de datos en Python¡

iniciar: (1)
Salir: (99)
     ''')
    opciones = int(input('Opciones: '))
    if opciones == 1:
         # Variables
            alumno = input('Ingrese el nombre(s) del estudiante: ')
            alumnoApellido1 = input('Ingrese apellido Paterno: ')
            alumnoApellido2 = input('Ingrese apellido Materno: ')
            edad = int(input('Ingresa edad del estudiante: '))
            matricula = input('Ingrese Matricula: ')
            resultadoAlumno = (f'''
Nombre: {alumno} {alumnoApellido1} {alumnoApellido2}
Edad: {edad}
Matricula: {matricula}
    ''')
            lista = [resultadoAlumno]
            print(resultadoAlumno)
    elif opciones == 99:
        break         
    else:
        print('\n !Ingrese una opción validad¡')     
sistemaAlumnos()