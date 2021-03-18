"""
Una institución educativa se encuentra en proceso de finalizar semestre y en proceso de admisión para el próximo semestre. La institución requiere un software que le permita solucionar estas dos problemáticas con las siguientes restricciones. 
Para finalización de semestre: 
Se desean subir las notas de los alumnos al sistema de los programas de Desarrollo de software y Telecomunicaciones, para ello, se le pide al docente el número de alumnos, nombre de cada alumno, programa académico, si es hombre, mujer, no binario, además, las 5 notas obtenidas durante el curso. El software calcula el promedio de las 5 notas. Al finalizar la ejecución debe mostrar cuántos hombres, mujeres y no bonarios hay en cada programa académico, el promedio de notas por cada programa y el listado de alumnos con el respectivo promedio de cada uno.
Para el proceso de admisión 
La institución requiere que se le muestre cuántos estudiantes en total se matricularon y el promedio de edad de los matriculados, además, requiere saber cuántos hombres y mujeres se matricularon.
El proceso de admisión termina hasta que el usuario decida que ya no se van a matricular más personas.
"""

def averageStudent():
    average = 0
    for j in range(1,6):
        average = average + float(input(f"Ingrese nota {j}: "))
    average = average / 5
    return average

numAlumnos = 0
students = []
countWomenSoftware = 0
countMenSoftware = 0
countNotBinarySoftware = 0
countWomenTelecomunications = 0
countMenTelecomunications = 0
countNotBinaryTelecomunications = 0
averageTelecomunications = 0
averageSoftware = 0
countStudents = 0
averageAge = 0
countWomen = 0
countMen = 0
countNotBinary = 0
countStudentSoft=0
countStudentTele=0
subject = ["S-Software","T-Telecomunicaciones"]
newSubject= []

while True:
    menu = input("¿Qué desea hacer? - admision(admi) - matrícula(matri) - Crear propuesta de materias (Add): ")
    mMenu = menu.upper()

    if mMenu == "ADMI" or mMenu == "MATRI" or mMenu == "ADD":
        break

if mMenu == "ADMI":
    numAlumnos = int(input("Ingrese número de alumnos: "))
    for i in range(numAlumnos):
        name = input("Ingrese nombre: ")      

        while True:
            print(f"Listado de programas académicos disponibles: {subject}")
            print()
            academicProgram = input("Del listado escriba la letra inicial, antes del guión, que corresponde a su programa: ")
            mAcademicProgram = academicProgram.upper()

            if mAcademicProgram == "S" or mAcademicProgram == "T":
                break
        
        if mAcademicProgram == "S":
            while True:
                sex = input("Ingrese sexo - m(mujer), h(hombre), nb(no binario): ")
                mSex = sex.upper()

                if mSex == "M" or mSex == "H" or mSex == "NB":
                    break

            if mSex == "M":
                countWomenSoftware+=1
            elif mSex == "H":
                countMenSoftware+=1
            elif mSex =="NB":
                countNotBinarySoftware+=1
            averageS = averageStudent()
            students.append({"name": name, "average": averageS})
            countStudentSoft = countNotBinarySoftware+countMenSoftware+ countWomenSoftware
        
        else:
            while True:
                sex = input("Ingrese sexo - m(mujer), h(hombre), nb(no binario): ")
                mSex = sex.upper()

                if mSex == "M" or mSex == "H" or mSex == "NB":
                    break
            
            if mSex == "M":
                countWomenTelecomunications+=1
            elif mSex == "H":
                countMenTelecomunications+=1
            elif mSex =="NB":
                countNotBinaryTelecomunications+=1
            averageT = averageStudent()
            students.append({"name": name, "average": averageT})
            countStudentTele = countNotBinaryTelecomunications+countMenTelecomunications+ countWomenTelecomunications
    
    if countStudentSoft >0:
        averageSoftware = averageS / countStudentSoft
    else:
        averageSoftware = 0

    if countStudentTele >0:
        averageTelecomunications = averageT / countStudentTele
    else:
        averageTelecomunications =0

     # result
    print()
    print(f"Promedio Software: {averageSoftware}")
    print(f"Número de mujeres en Software: {countWomenSoftware}")
    print(f"Número de Hombre en Software: {countMenSoftware}")
    print(f"Número de no binarios en Software: {countNotBinarySoftware}")
    print()
    print(f"Promedio Telecomunicaciones: {averageTelecomunications}")
    print(f"Número de mujeres en Telecomunicaciones: {countWomenTelecomunications}")
    print(f"Número de Hombre en Telecomunicaciones: {countMenTelecomunications}")
    print(f"Número de no binarios en Telecomunicaciones: {countNotBinaryTelecomunications}")
    print()
    print("Estudiantes registrados con sus notas")
    print()

    for i in students: # for i in range(len(students))
        print(f"Nombre: {i['name']} - Nota final: {i['average']}")

elif mMenu == "ADD":
    numCourse = int(input("Cantidad de materias a agregar: "))
    for k in range(numCourse):
        course = input("Propuesta de materia: ")
        newSubject.append(course)
    print(newSubject)



else:
    while True:
        average=0
        average+=int(input("Ingrese edad: "))
        while True:
                sex = input("Ingrese sexo - m(mujer), h(hombre), nb(no binario): ")
                mSex = sex.upper()

                if mSex == "M" or mSex == "H" or mSex == "NB":
                    break
        if mSex == "M":
            countWomen+=1
        elif mSex == "H":
            countMen+=1
        elif mSex =="NB":
            countNotBinary+=1
        else:
            print("por favor escoga m - mujer h -hombre nb - no binario")
        
        countStudents+=1
        stopAdmission = int(input("Si desea parar de matricular ingrese 0, de lo contrario cualquier tecla para continuar: "))
        
        if stopAdmission == 0:
            break

    averageAge = average/countStudents
    print(f"Número de estudiantes matriculados: {countStudents}")
    print(f"Promedio de edad de matriculados: {averageAge}")
    print(f"Número de mujeres matriculadas: {countWomen}")
    print(f"Número de hombre matriculados: {countMen}")
   
    



 