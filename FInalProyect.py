agenda = {}

def mostrar_menu():
    #Muestra el menú de opciones en la terminal.
    print("=" * 40)
    print("📞 CONTACTOS 📞".center(40))
    print("1️⃣ Agregar contacto")
    print("2️⃣ Buscar contacto")
    print("3️⃣ Eliminar contacto")
    print("4️⃣ Mostrar todos los contactos")
    print("5️⃣ Salir 🚪")
    print("=" * 40)

#Escribirá el nombre del contacto,luego su numero e imprimirá "guardado", pero si este ya ha sido guardado; imprimirá "ya existe"
def agregar_contacto():
    nombre = input("📝 Ingresa el nombre del contacto: ").strip().capitalize()
    if nombre in agenda:
         print(f"⚠️ El contacto '{nombre}' ya existe.")
    else:
        telefono = input("📞 Ingresa el número de teléfono: ").strip()
        agenda[nombre] = telefono
        print(f"✅ Contacto '{nombre}' agregado exitosamente.")

#1-Buscará el nombre del contacto, pero si este contacto NO existe, "imprimirá  no existe".
def buscar_contacto():
    nombre = input("🔍 Ingresa el nombre a buscar: ").strip().capitalize()
    if nombre in agenda:
        print(f"📱 {nombre}: {agenda[nombre]}")
    else:
        print(f"❌ El contacto '{nombre}' no existe.")

#2-Escribirá el nombre del contacto y SI existe, imprimirá "eliminado". Si NO existe imprimirá "no existe"
def eliminar_contacto():
    nombre = input("❌ Ingresa el nombre a eliminar: ").strip().capitalize()
    if nombre in agenda:
        del agenda[nombre]
        print(f"✅ Contacto '{nombre}' eliminado.")
    else:
        print(f"⚠️ El contacto '{nombre}' no existe.")

#3-Si no hay contactos GUARDADOS, imprimirá "La agenda está vacía". Si hay contactos GUARDADOS, imprimirá "Lista de contactos" y serán mostrados los contactos guardados anteriormente)
def mostrar_contactos():
    if not agenda:
        print("📂 La agenda está vacía.")
    else:
        print("-" * 40)
        print("\n📋 LISTA DE CONTACTOS 📋")
        print("-" * 40)
        for nombre, telefono in agenda.items():
            print(f"📌 {nombre}: {telefono}")
        print("-" * 40)

# Interacción con el usuario, pasos a seguir: 

while True:
    mostrar_menu()
    opcion = input("📌 Elige una opción: ").strip()

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        eliminar_contacto()
    elif opcion == "4":
        mostrar_contactos()
    elif opcion == "5":
        print("\n👋 Saliendo del menú... ¡Hasta luego!, ten un buen día\n")
        break
    else:
        print("\n⚠️ Esta opción no es válida, intenta de nuevo.\n") 
        