#En esta clae definimos el tipo de clase Alumno para despues hacerlo objetos
class Alumnos():
	def __init__(self,Nombre,Calificacion,Grupo):
		self.nombre= Nombre
		self.grupo= Grupo
		self.calificacion=Calificacion

class Grupo():
    def __init__(self,AñoSalon):
        self.c_AñoSalon = AñoSalon
        self.c_NiñosMecos = []


 #Esta funcion sirve para abrir el archico con la lista de alumos  ordenada por grupo
def LeerArchivoYOrdenar():
    Directorio= "Alumnos.txt"
    Directorio2="GrupoOrdenado.txt"
    ListaPendeja=[]
    ListadeGrupos = []
    Leido=open(Directorio,"r").read().splitlines()
    Leido2=open(Directorio2,"r").read().splitlines()
    for PasadoAString in Leido:
        PasadoAString = PasadoAString.split()
        Test=Alumnos(PasadoAString[0],PasadoAString[1],PasadoAString[2])
        ListaPendeja.append(Test)
    NoEncontrado = 0
    for estudiante in ListaPendeja:
        if len(ListadeGrupos) > 0:
            for grupo in ListadeGrupos:
                if estudiante.grupo == grupo.c_AñoSalon:
                    grupo.c_NiñosMecos.append(estudiante)
                    NoEncontrado = 0
                    break
                else:
                    NoEncontrado = NoEncontrado + 1
            if NoEncontrado > 0:
                NoEncontrado = 0
                CreacionDelSeñor=Grupo(estudiante.grupo)
                CreacionDelSeñor.c_NiñosMecos.append(estudiante)
                ListadeGrupos.append(CreacionDelSeñor)
        else:
            CreacionDelSeñor=Grupo(estudiante.grupo)
            CreacionDelSeñor.c_NiñosMecos.append(estudiante)
            ListadeGrupos.append(CreacionDelSeñor)
       

    ContadorOP=5
    for grupo in ListadeGrupos:
        PasadoAString2=str(ContadorOP)
        ArchivoNuevo=open("Grupo"+PasadoAString2+".txt","w")
        ArchivoNuevo.write(grupo.c_AñoSalon)
        PasadoAString2==str(ContadorOP)
        for estudiante in grupo.c_NiñosMecos:
            TuGfa=str("\n" + estudiante.nombre + ", " + estudiante.calificacion + ', ' + estudiante.grupo  + "\n")
            ArchivoNuevo.write(TuGfa)
            print(TuGfa)
        ContadorOP= ContadorOP-1
     
    Usuario= str(input("Si desea ordenar su archivo por Calificacion escriba 1, si desea ordenar por Nombre del alumno escriba 2: "))

    if Usuario=="2":
        Lista=[]
        for alv in Leido:
            Lista.append(alv)
        OrdenamientoBurbuja(Lista)
        print(Lista)
    elif Usuario=="1":
        NuevaLista=[]
        for alv2 in Leido2:
            NuevaLista.append(alv2)
        OrdenamientoBurbuja(NuevaLista)
        NuevaLista.reverse()
        print(NuevaLista)
    else:
        print("Esa opcion no esta disponible")
      
    Usuario2=str(input("Desea agregar alumno?"))
    if Usuario2=="Si" or Usuario=="si":
        NombreUsuario=str(input("Que nombre desea para el alumno?: "))
        print("Listo")
        CalificacionUsuario=str(input("Que calificacion tiene el alumno?: "))
        print("Listo")
        print("Advertencia: de no ser un grupo existente el alumno sera autoasignado a un grupo")
        GrupoUsuario=str(input("Eliga el grupo del usuario(ejemplo=2016B): "))
        Test=Alumnos(NombreUsuario,CalificacionUsuario,GrupoUsuario)
        ListaPendeja.append(Test)
    elif Usuario=="No" or "no":
        print("Terminando programa")
    else:
        print("Terminando programa...")
        

def OrdenamientoBurbuja(Lista):
    for Iterador in range(len(Lista)-1,0,-1):
        for i in range(Iterador):
            if Lista[i]>Lista[i+1]:
                simon = Lista[i]
                Lista[i] = Lista[i+1]
                Lista[i+1] = simon
LeerArchivoYOrdenar()