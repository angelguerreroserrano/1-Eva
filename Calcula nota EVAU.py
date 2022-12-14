# Este programa calcula la nota de la EVAU
# 1. Introduces tres carreras que quieras cursar
# 2. Calcula la nota de la FASE OBLIGATORIA. Nota mínima de 4 para ponderar con la NMB
# 3. Calcula la nota de acceso. 0.4*EVAU + 0.6*NMB. Mínimo 5, sino SUSPENSO
# 4. Asignaturas de FASE VOLUNTARIA
# 5. Calcula nota de admisión

def main():
    global acabar
    acabar = False
    while acabar == False:
        op_carreras()
        # Primero muestra las carreras
        # Luego deja elegir 3
        op_nota_acceso()
        # Pregunta nota media de bachillerato
        # Pregunta el idioma del que te has examinado
        # Pregunta la nota de los examenes de la fase obligatoria (Mínimo media de 4. En el caso contrario no habrá superado la prueba de acceso)
        # Calcula la nota de acceso (0.4*EVAU + 0.6*NMB)
        op_efv()
        # Muestra los exámenes posibles
        # Deja elegir dos exámenes (No puedes coger un examen que hayas hecho en la fase obligatoria)
        # Pregunta la nota que has sacado en cada uno
        op_nota_admision()
        acabar = True
        # Calcula las ponderaciones
        # Elige la mejor nota posible para cada carrera
        # Muestra las notas

def op_carreras():
    def main_carreras():
        muestra_carreras()
        elige_carreras()

    def muestra_carreras():
        global lista_carreras
        print("__CARRERAS__")
        print("A continuación se mostrarán las posibles carreras. Elige 3 opciones. Pulsa enter para continuar.",
              end="")
        enter = input("")
        lista_carreras = ['Biotecnología', 'Ciencia y Tecnología de los Alimentos', 'Ciencias Ambientales', 'Física',
                          'Geología', 'Matemáticas', 'Física y Matemáticas', 'Óptica y Optometría', 'Química',
                          'Enfermería',
                          'Fisioterapia', 'Medicina', 'Nutrición Humana y Dietética', 'Odontología', 'Psicología',
                          'Terapia Ocupacional', 'Veterinaria',
                          'Nutrición Humana y Dietética y Ciencias de la Actividad Física y del Deporte',
                          'Estudios en Arquitectura', 'Ingeniería Agroalimentaria y del Medio Rural',
                          'Arquitectura Técnica', 'Ingeniería Civil', 'Ingeniería de Organización Industrial',
                          'Ingeniería de Tecnologías Industriales',
                          'Ingeniería de Tecnologías y Servicios en Telecomunicacion', 'Ingeniería Eléctrica',
                          'Ingeniería Electrónica y Automática',
                          'Ingeniería en Diseño Industrial y Desarrollo de Producto',
                          'Ingeniería Informática', 'Ingeniería Mecatrónica', 'Ingeniería Mecánica',
                          'Ingenieria Química',
                          'Matemáticas e Ingeniería Informática', 'Ingeniería Mecatrónica e Ingeniería Informática',
                          'Ingeniería Mecatrónica e Ingeniería de Organización Industrial',
                          'Ingeniería de Datos en Procesos Industriales',
                          'Ingeniería Informática y Administración y Dirección de Empresas', 'Bellas Artes',
                          'Estudios Ingleses', 'Estudios Clásicos', 'Filología Hispánica', 'Filosofía', 'Historia',
                          'Historia del Arte', 'Lenguas Modernas', 'ADE',
                          'Ciencias de la Actividad Física y del Deporte',
                          'Derecho', 'Economía', 'Finanzas y Contabilidad', 'Gestión y Administración Pública',
                          'Geografía y Ordenación del Territorio', 'Información y Documentacion',
                          'Magisterio en Educación Infantil', 'Magisterio en Educación Primaria',
                          'Marketing e Investigación de Mercados', 'Periodismo', 'ADE y Derecho',
                          'Relaciones Laborales y Recursos Humanos', 'Trabajo Social', 'Turismo']

        def main_muestra_carreras():
            print("")
            carreras_ciencias()
            carreras_ciencias_sociales()
            carreras_ingenieria_arquitectura()
            carreras_arte_humanidades()
            carreras_sociales_juridicas()

        def carreras_ciencias():
            print("CIENCIAS")
            x = 0
            for j in lista_carreras[0:9]:
                print(j, end="")
                x = x + 1
                if x == 3:
                    print("")
                    x = 0
                else:
                    print(" || ", end="")
            print("")

        def carreras_ciencias_sociales():
            print("CIENCIAS SOCIALES")
            x = 0
            for j in lista_carreras[9:18]:
                print(j, end="")
                x = x + 1
                if x == 3:
                    print("")
                    x = 0
                else:
                    print(" || ", end="")
            print("")

        def carreras_ingenieria_arquitectura():
            print("INGENIERÍA Y ARQUITECTURA")
            x = 0
            for j in lista_carreras[18:37]:
                print(j, end="")
                x = x + 1
                if x == 3:
                    print("")
                    x = 0
                elif j == lista_carreras[36]:
                    print("")
                else:
                    print(" || ", end="")
            print("")

        def carreras_arte_humanidades():
            print("ARTE Y HUMANIDADES")
            x = 0
            for j in lista_carreras[37:45]:
                print(j, end="")
                x = x + 1
                if x == 4:
                    print("")
                    x = 0
                else:
                    print(" || ", end="")
            print("")

        def carreras_sociales_juridicas():
            print("CIENCIAS SOCIALES Y JURÍDICAS")
            x = 0
            for j in lista_carreras[45:61]:
                print(j, end="")
                x = x + 1
                if x == 4:
                    print("")
                    x = 0
                else:
                    print(" || ", end="")
            print("")

        main_muestra_carreras()

    def elige_carreras():
        global lista_carreras, carrera, carrera1, carrera2, carrera3, n_carrera, n_carrera1, n_carrera2, n_carrera3
        print("Elige 3 de las las opciones dadas.")
        for j in range(1, 4):
            seguir = False
            while seguir == False:
                carrera = input(f"Introduce la opción {j}: ")
                try:
                    n_carrera = lista_carreras.index(carrera)
                    seguir = True
                except:
                    print("")
                    print("__ERROR__")
                    print("Esta carrera no existe en la lista.")
                    print("Introdúcelo de forma correcta.")
                    print("")
                    seguir = False
            if j == 1:
                carrera1 = carrera
                n_carrera1 = n_carrera
            elif j == 2:
                carrera2 = carrera
                n_carrera2 = n_carrera
            else:
                carrera3 = carrera
                n_carrera3 = n_carrera

    main_carreras()

def op_nota_acceso():
    def main_calcula_nota_acceso():
        print("")
        pregunta_nmb()
        pregunta_nota_efo()
        resultado_nota_acceso()

    def pregunta_nmb():
        global nmb, seguir
        seguir = False
        while seguir == False:
            nmb = float(input("Introduce la Nota Media de Bachillerato: "))
            nota = nmb
            error_nota(nota)

    def pregunta_nota_efo():
        global idioma_efo, seguir, nota_efo_mates, nota_efo_historia, nota_efo_lengua, nota_efo_idioma, nota_efo
        seguir = False
        print("")
        while seguir == False:
            idioma_efo = input("Introduce la lengua extranjera (Inglés/Francés/Aleman) para la Fase Obligatoria: ")
            if idioma_efo != "Inglés" and idioma_efo != "Francés" and idioma_efo != "Alemán":
                print("")
                print("__ERROR__")
                print("Hay que elegir entre Inglés, Francés o Alemán.")
                print("")
                seguir = False
            else:
                seguir = True
        lista_examenes_fo = ["Matemáticas II", "Historia de España", "Lengua Castellana y Literatura II", idioma_efo]
        print("")
        for j in lista_examenes_fo:
            seguir = False
            while seguir == False:
                nota = float(input(f"Introduce la nota de {j}: "))
                error_nota(nota)
            if j == lista_examenes_fo[0]:
                nota_efo_mates = nota
            elif j == lista_examenes_fo[1]:
                nota_efo_historia = nota
            elif j == lista_examenes_fo[2]:
                nota_efo_lengua = nota
            else:
                nota_efo_idioma = nota
        nota_efo = (nota_efo_mates + nota_efo_historia + nota_efo_lengua + nota_efo_idioma) / 4

    def resultado_nota_acceso():
        global nota_efo, nota_acceso, suspenso
        if nota_efo < 4:
            print("")
            print("__ERROR 404__")
            print("Has SUSPENDIDO la Prueba de Acceso.")
            print(f"Tu nota en la Prueba de Acceso ha sido de {nota_efo}")
            print("Has sido incapaz de sacar más de un 4. :)")
            print("")
            acabar = True
            return acabar
        else:
            nota_acceso = (nota_efo * 0.4) + (nmb * 0.6)

    main_calcula_nota_acceso()

def op_efv():
    def main_op_efv():
        muestra_efv()
        elige_efv()
        pregunta_nota_efv()

    def muestra_efv():
        global lista_efv
        print("")
        print("__EXÁMENES FASE VOLUNTARIA__")
        print("A continuación se mostrarán las posibles exámenes. Elige 2 opciones. Pulsa enter para continuar.",
              end="")
        enter = input("")
        lista_efv = ['Lengua Castellana y Literatura II', 'Historia de España', 'Inglés', 'Francés', 'Alemán',
                     'Matemáticas II', 'Biología', 'Geología', 'Física', 'Química', 'Dibujo Técnico II',
                     'Matemáticas Aplicadas II', 'Historia de la Filosofía', 'Economía de la Empresa', 'Latín II',
                     'Griego II', 'Geografía', 'Historia del Arte', 'Fundamentos del Arte II',
                     'Cultura Audiovisual II',
                     'Artes Escénicas', 'Diseño']
        x = 0
        for j in lista_efv:
            print(j, end="")
            x = x + 1
            if x == 3:
                print("")
                x = 0
            else:
                print(" || ", end="")

    def elige_efv():
        global lista_efv, idioma_efo, efv1, efv2, n_efv1, n_efv2, efv, n_efv
        print("")
        for j in range(1,3):
            seguir1 = False
            while seguir1 == False:
                efv = input(f"Introduce la opción {j}: ")
                try:
                    n_efv = lista_efv.index(efv)
                    seguir1 = True
                except:
                    print("")
                    print("__ERROR__")
                    print("Este examen no existe en la lista.")
                    print("Introdúcelo de forma correcta.")
                    print("")
                    seguir1 = False
                if efv == lista_efv[0] or efv == lista_efv[1] or efv == lista_efv[5] or efv == idioma_efo:
                    print("")
                    print("__ERROR__")
                    print("No puedes realizar un examen que ya has hecho en la fase obligatoria.")
                    print("Introduce otro examen")
                    print("")
                    seguir1 = False
                elif j == 1:
                    efv1 = efv
                    n_efv1 = n_efv
                else:
                    efv2 = efv
                    n_efv2 = n_efv

    def pregunta_nota_efv():
        global efv1, efv2, nota_efv1, nota_efv2
        lista_eleccion_examenes = [efv1, efv2]
        for j in lista_eleccion_examenes:
            nota_efv = float(input(f"Introduce la nota de {j}: "))
            if nota_efv < 5:
                nota_efv = 0
            if j == efv1:
                nota_efv1 = nota_efv
            else:
                nota_efv2 = nota_efv

    main_op_efv()

def op_nota_admision():
    def main_op_nota_admision():
        global carrera1, carrera2, carrera3, n_carrera1, n_carrera2, n_carrera3, n_efv1, n_efv2, efv1, efv2, p_efv1,\
            p_efv2
        for j in range(1,4):
            if j == 1:
                carrera = carrera1
                n_carrera = n_carrera1
            elif j == 2:
                carrera = carrera2
                n_carrera = n_carrera2
            else:
                carrera = carrera3
                n_carrera = n_carrera3
            for x in range(1,3):
                if x == 1:
                    efv = efv1
                    n_efv = n_efv1
                else:
                    efv = efv2
                    n_efv = n_efv2
                calcula_ponderacion(n_carrera, n_efv)
                if x == 1:
                    p_efv1 = p_efv
                else:
                    p_efv2 = p_efv
            calcula_nota_admision(carrera, p_efv1, p_efv2)
            muestra_nota_admision(carrera)

    def calcula_ponderacion(n_carrera, n_efv):
        global p_efv, lista_n_carrera
        lista_pond = [[0,0,0,0,0,0.2,0.2,0.15,0.2,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.2,0.2,0.15,0.2,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.2,0.2,0.2,0.2,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.2,0.2,0.2,0.2,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.2,0.2,0.2,0.2,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.2,0.15,0.15,0.2,0.15,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.2,0.15,0.15,0.2,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.2,0.2,0.15,0.2,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.2,0.2,0.2,0.2,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.15,0.2,0.1,0.1,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.15,0.2,0.1,0.2,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.15,0.2,0.1,0.15,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.15,0.2,0.1,0.1,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.15,0.2,0.1,0.15,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.15,0.2,0.1,0.15,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.15,0.2,0.1,0.15,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.15,0.2,0.1,0.15,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.1,0.2,0.1,0.2,0.2,0,0.2,0,0.15,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.2,0.1,0.2,0.2,0.1,0.2,0,0,0.1,0,0,0.15,0,0,0,0,0.15],
                      [0,0,0,0,0,0.2,0.2,0.2,0.2,0.2,0.15,0,0,0.1,0,0,0.2,0,0,0,0,0.1],
                      [0,0,0,0,0,0.2,0.1,0.2,0.2,0.1,0.2,0,0,0.1,0,0,0.15,0,0,0,0,0.15],
                      [0,0,0,0,0,0.2,0.1,0.2,0.2,0.1,0.2,0,0,0.1,0,0,0.15,0,0,0,0,0.1],
                      [0,0,0,0,0,0.2,0.1,0.1,0.2,0.2,0.2,0,0,0.15,0,0,0,0,0,0,0,0.1],
                      [0,0,0,0,0,0.2,0.1,0.15,0.2,0.2,0.2,0,0,0.1,0,0,0,0,0,0,0,0.1],
                      [0,0,0,0,0,0.2,0.1,0.1,0.2,0.1,0.1,0,0,0.1,0,0,0,0,0,0,0,0.1],
                      [0,0,0,0,0,0.2,0.1,0.1,0.2,0.2,0.2,0,0,0.1,0,0,0,0,0,0,0,0.1],
                      [0,0,0,0,0,0.2,0.1,0.1,0.2,0.2,0.2,0,0,0.1,0,0,0,0,0,0,0,0.1],
                      [0,0,0,0,0,0.2,0.1,0.1,0.2,0.1,0.2,0,0,0.1,0,0,0,0,0,0,0,0.15],
                      [0,0,0,0,0,0.2,0.1,0.1,0.2,0.1,0.1,0,0,0.1,0,0,0,0,0,0,0,0.1],
                      [0,0,0,0,0,0.2,0.1,0.1,0.2,0.2,0.2,0,0,0.1,0,0,0,0,0,0,0,0.1],
                      [0,0,0,0,0,0.2,0.1,0.1,0.2,0.2,0.2,0,0,0.1,0,0,0,0,0,0,0,0.1],
                      [0,0,0,0,0,0.2,0.1,0.15,0.2,0.2,0.2,0,0,0.1,0,0,0,0,0,0,0,0.1],
                      [0,0,0,0,0,0.2,0,0,0.2,0.15,0.1,0,0,0.1,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0.2,0.1,0,0.2,0.2,0.2,0,0,0.15,0,0,0,0,0,0,0,0.1],
                      [0,0,0,0,0,0.2,0.1,0.1,0.2,0.1,0.2,0,0,0.1,0,0,0,0,0,0,0,0.1],
                      [0,0,0,0,0,0.2,0.1,0.1,0.2,0.1,0.1,0.2,0.1,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
                      [0,0,0,0,0,0,0,0,0,0,0.2,0.1,0.2,0.1,0.2,0.2,0.1,0.2,0.2,0.2,0.1,0.2],
                      [0,0,0.2,0,0,0,0,0,0,0,0,0.1,0.2,0.1,0.2,0.2,0.2,0.15,0.1,0.1,0.1,0.1],
                      [0.2,0,0,0,0,0,0,0,0,0,0,0.1,0.2,0.1,0.2,0.2,0.2,0.15,0.1,0.1,0.1,0.1],
                      [0.2,0,0,0,0,0,0,0,0,0,0,0.1,0.2,0.1,0.2,0.2,0.2,0.15,0.1,0.1,0.1,0.1],
                      [0,0,0,0,0,0,0,0,0,0,0,0.1,0.2,0.1,0.2,0.2,0.2,0.15,0.1,0.1,0.1,0.1],
                      [0,0.2,0,0,0,0,0,0,0,0,0,0.1,0.2,0.1,0.2,0.2,0.2,0.2,0.2,0.1,0.1,0.1],
                      [0,0.2,0,0,0,0,0,0,0,0,0,0.1,0.2,0.1,0.2,0.2,0.2,0.2,0.2,0.2,0.1,0.2],
                      [0,0,0.2,0.2,0.2,0,0,0,0,0,0,0.1,0.2,0.1,0.2,0.2,0.2,0.15,0.1,0.1,0.1,0.1],
                      [0,0,0,0,0,0.2,0.1,0.1,0.1,0.1,0.1,0.2,0.1,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
                      [0,0,0,0,0,0.1,0.2,0.1,0.2,0.1,0.1,0.2,0.1,0.15,0.1,0.1,0.2,0.1,0.1,0.1,0.15,0.1],
                      [0,0,0,0,0,0.1,0.1,0.1,0.1,0.1,0.1,0.2,0.2,0.2,0.2,0.2,0.1,0.1,0.1,0.1,0.1,0.1],
                      [0,0,0,0,0,0.2,0.1,0.1,0.1,0.1,0.1,0.2,0.1,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
                      [0,0,0,0,0,0.2,0.1,0.1,0.1,0.1,0.1,0.2,0.1,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
                      [0,0,0,0,0,0.2,0.1,0.1,0.1,0.1,0.1,0.2,0.1,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
                      [0,0,0,0,0,0.1,0.1,0.2,0.1,0.1,0.1,0.1,0.2,0.2,0.15,0.15,0.2,0.2,0.2,0.1,0.1,0.1],
                      [0.2,0,0,0,0,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.2,0.1,0.2,0.2,0.2,0.1,0.1,0.15,0.1,0.1],
                      [0.2,0,0,0,0,0.2,0.1,0.1,0.1,0.1,0.1,0.2,0.1,0.1,0.2,0.1,0.1,0.2,0.1,0.1,0.1,0.2,0.1,0.1,0.1],
                      [0.2,0,0,0,0,0.2,0.1,0.1,0.1,0.1,0.1,0.2,0.1,0.1,0.2,0.1,0.1,0.2,0.1,0.1,0.1,0.2,0.1,0.1,0.1],
                      [0,0,0,0,0,0.2,0.1,0.1,0.1,0.1,0.1,0.2,0.1,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
                      [0.2,0,0,0,0,0.1,0.1,0.1,0.1,0.1,0.1,0.2,0.2,0.2,0.2,0.2,0.2,0.1,0.1,0.2,0.1,0.1],
                      [0,0,0,0,0,0.2,0.1,0.1,0.1,0.1,0.1,0.2,0.1,0.2,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
                      [0,0,0,0,0,0.1,0.1,0.1,0.1,0.1,0.1,0.2,0.1,0.2,0.1,0.1,0.2,0.1,0.1,0.1,0.1,0.1],
                      [0,0,0,0,0,0.1,0.1,0.1,0.1,0.1,0.1,0.2,0.1,0.2,0.1,0.1,0.2,0.1,0.1,0.1,0.1,0.1],
                      [0,0,0.2,0.2,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.2,0.2,0.2,0.15,0.1,0.2,0.2,0.2,0.1,0.15,0.1]]
        lista_n_carrera = lista_pond[n_carrera]
        p_efv = lista_n_carrera[n_efv]

    def calcula_nota_admision(carrera, p_efv1, p_efv2):
        global lista_efv, lista_n_carrera, idioma_efo, nota_efo_mates, nota_efo_lengua, nota_efo_historia,\
            nota_efo_idioma, nota_efv1, nota_efv2, p_lengua, p_historia, p_idiomoa, p_mates, \
            nota_admision1, nota_admision2, ea1, ea2, p_ea1, p_ea2, nota_asig_pond, nota_admision
        p_lengua = lista_n_carrera[0]
        p_historia = lista_n_carrera[1]
        n_idioma_efo = lista_efv.index(idioma_efo)
        p_idioma = lista_n_carrera[n_idioma_efo]
        p_mates = lista_n_carrera[5]
        nota_ad_mates = nota_efo_mates * p_mates
        nota_ad_lengua = nota_efo_lengua * p_lengua
        nota_ad_historia = nota_efo_historia * p_historia
        nota_ad_idioma = nota_efo_idioma * p_idioma
        nota_ad_efv1 = nota_efv1 * p_efv1
        nota_ad_efv2 = nota_efv2 * p_efv2

        lista_admision = [[nota_ad_efv1, efv1, p_efv1],
                          [nota_ad_efv2, efv2, p_efv2],
                          [nota_ad_mates, "Matemáticas II", p_mates],
                          [nota_ad_lengua, "Lengua Castellana y Literatura II", p_lengua],
                          [nota_ad_historia, "Historia de España", p_historia],
                          [nota_ad_idioma, idioma_efo, p_idioma]]
        lista_admision = sorted(lista_admision)
        maximo1 = lista_admision[-1]
        nota_admision1 = maximo1[0]
        ea1 = maximo1[1]
        p_ea1 = maximo1[2]
        maximo2 = lista_admision[-2]
        nota_admision2 = maximo2[0]
        ea2 = maximo2[1]
        p_ea2 = maximo2[2]
        nota_asig_pond = float(nota_admision1) + float(nota_admision2)
        nota_admision = nota_acceso + nota_asig_pond

    def muestra_nota_admision(carrera):
        global ea1, ea2, nota_admision1, nota_admision2, nota_acceso, p_ea1, ea1, p_ea2, ea2, nota_admision, nota_admision
        print(f"__{carrera.upper()}__")
        print(f"Nota de Acceso: {round(nota_acceso, 3)}")
        print(f"Nota de Asignaturas Ponderables: {round(nota_asig_pond, 3)} = {ea1}({p_ea1}) + {ea2}({p_ea2})")
        print(f"Nota de Admisión: {round(nota_admision, 3)}")

    main_op_nota_admision()

def error_nota(nota):
    global seguir
    if nota < 0 or nota > 10:
        print("")
        print("__ERROR__")
        print("La nota tiene que estar entre 0 y 10.")
        print("")
        seguir = False
        return seguir
    else:
        seguir = True
        return seguir


main()
