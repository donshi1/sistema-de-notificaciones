from abc import ABC, abstractmethod
#esta es la clase observadora, encargada de actualizar as notificaciones de los mensajes
class obser(ABC):
    @abstractmethod
    def actu(self,mensaje: str):
        pass
#ambas clases tanto el obser como noti dependen de la abstraccion y de un metodo especifico
#esta clase esta encargada de enviar las actualizaciones/mensajes a los usuarios.
class noti(ABC):
    @abstractmethod
    def enviar(self, usuario, mensaje: str):
        pass
#aqui estan implementadas 3 clases, todas utilizando los SOLID. cada una se encarga unicamente de un solo proposito.
class notiema(noti):#notiema=notificacion de email.
    def enviar(self, usuario, mensaje: str):
        print(f"enviando email a {usuario.email}: '{mensaje}'")
class smsnoti(noti):#smsnoti=notificacion de sms
    def enviar(self,usuario, mensaje:str):
        print(f"enviando sms a {usuario.telefono}: '{mensaje}'")
class notipush(noti):#notificacion tipo push
    def enviar(self, usuario, mensaje:str):
        print(f"enviando noti a {usuario.nombre}: '{mensaje}'")
#aqui utilizo los patrones de diseño: el metodo factory. aqui el mensaje que quieras enviar se hara en base a la necesidad/suscreipcion del usuario.
#dentro de esta factory se puede extender la funcionalidad sin modificar el codigo existente
class factonoti:
    def creanoti(self, tipo:str) -> noti:
        if tipo.lower() == 'email':
            return notiema()
        elif tipo.lower() =='sms':
            return smsnoti()
        elif tipo.lower() =='push':
            return notipush()
        else:
            print("error.")
#esta es la clase de usuario. aqui se crean los usuarios (actualmente solo modificable desde el codigo fuente)
# SOLID: Single Responsibility - Representa a un usuario del sistema
class usu(obser):
    def __init__(self, nombre: str, email: str, telefono: str, notiprefe: str):
        self.nombre=nombre
        self.email=email
        self.telefono=telefono
        self.notiprefe=notiprefe
        self._fabrica = factonoti()
    def actu(self, mensaje:str):#utilizo el metodo factory para decirle que cree la notificacion basado en su notificacion preferida (sms,email,push)
        noti_conc=self._fabrica.creanoti(self.notiprefe)
        noti_conc.enviar(self, mensaje)
class notifi: #dentro de esta clase ingreso a los observadores que estaran atentos a las actualizaciones, ademas de que puedo eliminar, notificar o agregar a alguno.
    def __init__(self):
        self._observadores=[]
    def agreobs(self, observador: obser):
        print(f"se ha suscrito a: {observador.nombre}")
        self._observadores.append(observador)
    def elimiobs(self, observador: obser):
        print(f"se ha quitado la suscripcion a: {observador.nombre}")
        self._observadores.remove(observador)
    def notiobs(self, mensaje:str):
        print("se notificara a todos.")
        for observador in self._observadores:
            observador.actu(mensaje)
        print("se ha notificado.")
if __name__=="__main__":
    princnoti=notifi()
    usuario_ana= usu(nombre="ana", email="umpalimpa@gmail.com", telefono="123-123", notiprefe="email")
    usuario_gogo= usu(nombre="gogo", email="umpalumpa@gmail.com", telefono="234-453", notiprefe="sms")   
    usuario_gugu= usu(nombre="gugu", email="umpalampa@gmail.com", telefono="234-123", notiprefe="push")

    princnoti.agreobs(usuario_ana)
    princnoti.agreobs(usuario_gogo)
    princnoti.agreobs(usuario_gugu)

    mens1="tienes una actualizacion disponible"
    princnoti.notiobs(mens1)
    princnoti.elimiobs(usuario_gogo)
    mens2="se actualizara automaticamente este noche"
    princnoti.notiobs(mens2)