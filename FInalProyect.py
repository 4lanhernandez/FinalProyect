agenda = {}

def mostrar_menu():
    """Muestra el menú de opciones en la terminal."""
    print("=" * 40)
    print("📞 CONTACTOS 📞".center(40))
    print("1️⃣ Agregar contacto")
    print("2️⃣ Buscar contacto")
    print("3️⃣ Eliminar contacto")
    print("4️⃣ Mostrar todos los contactos")
    print("5️⃣ Salir 🚪")
    print("=" * 40)

    def agregar_contacto():
    nombre = input("📝 Ingresa el nombre del contacto: ").strip().capitalize()
    if nombre in agenda:
        print(f"⚠️ El contacto '{nombre}' ya existe.")
    else:
        telefono = input("📞 Ingresa el número de teléfono: ").strip()
        agenda[nombre] = telefono
        print(f"✅ Contacto '{nombre}' agregado exitosamente.")