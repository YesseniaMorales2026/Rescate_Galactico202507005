#yessenia morales

RESCARE GALACTICO 

print("================================") 

print("       🚀 RESCATE GALÁCTICO") 

print("================================") 

 

nombre = input("Escribe tu nombre: ") 

 

print("\n¡Bienvenido, Capitán", nombre + "!") 

print("Tu misión es rescatar a los astronautas.") 

print("Debes encontrar 3 cristales de energía.") 

 

cristales = 0 

 

print("\n🌎 NIVEL 1") 

opcion = input("¿Quieres explorar el planeta? (si/no): ") 

 

if opcion.lower() == "si": 

    print("¡Encontraste un cristal!") 

    cristales += 1 

 

print("\n☄️ NIVEL 2") 

opcion = input("¿Quieres cruzar el campo de meteoritos? (si/no): ") 

 

if opcion.lower() == "si": 

    print("¡Superaste los obstáculos!") 

    cristales += 1 

 

print("\n🌌 NIVEL 3") 

opcion = input("¿Quieres continuar explorando? (si/no): ") 

 

if opcion.lower() == "si": 

    print("¡Encontraste el último cristal!") 

    cristales += 1 

 

if cristales == 3: 

    print("\n🎉 ¡MISIÓN COMPLETADA!") 

    print("Rescataste a los astronautas y reparaste la nave.") 

    print("🏆 ¡Ganaste una nueva nave y una insignia!") 

else: 

    print("\nLa misión terminó. ¡Inténtalo nuevamente!")