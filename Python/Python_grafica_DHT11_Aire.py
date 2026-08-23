import matplotlib.pyplot as plt

# Datos extraídos de la tabla
horas = ["17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", 
         "21:00", "21:30", "22:00", "22:30", "23:00", "23:30", "24:00"]
temp_exterior = [12, 11.8, 11.5, 11.3, 11, 10.6, 10.5, 10.3, 10, 9.3, 9.5, 9.6, 9.8, 9.9, 10]
temp_base = [24] * len(horas)

# Configuración del gráfico
plt.figure(figsize=(12, 6))

# Graficar la temperatura base (línea punteada roja)
plt.plot(horas, temp_base, label="Temperatura Base (Confort 24°C)", color='red', linestyle='--', linewidth=2)

# Graficar la temperatura exterior medida (línea azul con marcadores)
plt.plot(horas, temp_exterior, label="Temperatura Exterior (DHT11)", color='blue', marker='o', linewidth=2)

# Rellenar el área entre las dos curvas (Representación visual de la Integral)
plt.fill_between(horas, temp_exterior, temp_base, color='lightblue', alpha=0.5, label="Área de Integración (HDD)")

# Títulos y etiquetas
plt.title("Tiempo en Fray Bentos, 23 de agosto\n(Análisis de Demanda Energética)", fontsize=14, fontweight='bold', color='#1a365d')
plt.xlabel("Hora", fontsize=12)
plt.ylabel("Temperatura (°C)", fontsize=12)
plt.xticks(rotation=45) # Rotar las horas para que se lean bien
plt.grid(True, linestyle=':', alpha=0.7)

# Mostrar leyenda
plt.legend(loc='center right')

# Ajustar el diseño para que no se corten las etiquetas
plt.tight_layout()

# Guardar y mostrar
plt.savefig("grafica.png")
print("Gráfica guardada exitosamente.")