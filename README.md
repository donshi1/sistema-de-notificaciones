# 🔔 Sistema de Notificaciones

## 📖 Descripción
Sistema de notificaciones que permite enviar mensajes a usuarios a través de diferentes medios (email, SMS, push) implementando los patrones de diseño **Observer** y **Factory Method**, siguiendo los **principios SOLID**.

## 🏗️ Arquitectura del Sistema

### 📐 Patrones de Diseño Implementados

#### 1. **Patrón Observer** 👀
**Propósito:** Establecer relación uno-a-muchos entre objetos para notificaciones automáticas.

**Implementación:**
- `Obser` (Interfaz) - Define el contrato para recibir actualizaciones
- `Usu` (Observador Concreto) - Implementa la actualización de notificaciones
- `Notifi` (Sujeto) - Gestiona observadores y notifica cambios

**Flujo:**
Notificador → notiobser() → actuobser() → Notificación.enviar()

#### 2. **Patrón Factory Method** 🏭
**Propósito:** Crear objetos sin especificar la clase exacta, encapsulando la lógica de creación.

**Implementación:**
- `Notifi` (Interfaz Producto)
- `Notificacion de Email`, `Notificacion de SMS`, `Notificacion de Push` (Productos Concretos)
- `Factonoti` (Factory) - Decide qué notificación crear

## 🔧 Principios SOLID Aplicados

### ✅ **S - Single Responsibility Principle**
Cada clase tiene una única responsabilidad bien definida:

- `Usu`: Representar a un usuario del sistema
- `NotificacionEmail/SMS/Push`: Enviar un tipo específico de notificación
- `Notificador`: Gestionar observadores y notificaciones
- `Factonoti`: Crear instancias de notificaciones

### ✅ **O - Open/Closed Principle**
El sistema está **cerrado para modificación** pero **abierto para extensión**:


# Para agregar nueva notificación (Ej: WhatsApp):
class NotificacionWhatsApp(Notificacion):
    def enviar(self, usuario, mensaje: str):
        print(f"Enviando WhatsApp a {usuario.telefono}: '{mensaje}'")

# Solo agregar en la fábrica:
elif tipo.lower() == 'whatsapp':
    return NotificacionWhatsAp()
✅ L - Liskov Substitution Principle
Todas las subclases pueden sustituir a sus clases base sin alterar el comportamiento
✅ I - Interface Segregation Principle
Interfaces específicas y no sobrecargadas
✅ D - Dependency Inversion Principle
Dependencias basadas en abstracciones, no implementaciones
🔄 Flujo del Sistema
Configuración: Crear notificador y usuarios

Suscripción: Usuarios se registran como observadores

Notificación: Notificador envía mensaje a todos los observadores

Procesamiento: Cada usuario recibe la notificación según su preferencia

Entrega: Se ejecuta el método de notificación específico
