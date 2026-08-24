import numpy as np
import matplotlib.pyplot as plt

# 1. Datos de la tabla (Fray Bentos, 23 de agosto)
horas = ["17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", 
         "21:00", "21:30", "22:00", "22:30", "23:00", "23:30", "24:00"]

temp_exterior = np.array([12, 11.8, 11.5, 11.3, 11, 10.6, 10.5, 10.3, 
                          10, 9.3, 9.5, 9.6, 9.8, 9.9, 10])
temp_base = np.array([24] * len(horas))

# 2. Cálculo de la Integral usando la Regla del Trapecio paso a paso
delta_T = temp_base - temp_exterior
dt = 0.5  # Intervalo de 30 minutos en horas

trapecios = (delta_T[:-1] + delta_T[1:]) / 2 * dt
integral_acumulada = np.concatenate(([0], np.cumsum(trapecios)))
x_indices = np.arange(len(horas))

# 3. Creación del gráfico interactivo/explicativo en 2 paneles
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True, 
                               gridspec_kw={'height_ratios': [2, 1]})

# --- Subplot 1: Curvas de Temperatura y Trapecios de Integración ---
ax1.plot(x_indices, temp_base, color='#e53e3e', linestyle='--', linewidth=2.5, 
         label='Temp. Base ($T_{base} = 24^\circ$C)')
ax1.plot(x_indices, temp_exterior, color='#3182ce', marker='o', linewidth=2.5, 
         markersize=6, label='Temp. Exterior ($T_{ext}$)')

# Dibujar y delimitar cada trapecio
for i in range(len(horas) - 1):
    ax1.fill_between([x_indices[i], x_indices[i+1]], 
                     [temp_exterior[i], temp_exterior[i+1]], 
                     [temp_base[i], temp_base[i+1]], 
                     color='#63b3ed', alpha=0.35 if i % 2 == 0 else 0.50,
                     edgecolor='#2b6cb0', linestyle=':', linewidth=1)

ax1.set_ylabel("Temperatura (°C)", fontsize=12, fontweight='bold')
ax1.set_title("Análisis Energético - Fray Bentos (23 de Agosto)\nDemanda Térmica: Integración Numérica por Regla del Trapecio", 
              fontsize=14, fontweight='bold', pad=15, color='#1a365d')
ax1.set_ylim(8, 26)
ax1.legend(loc='upper right', frameon=True, facecolor='white', framealpha=0.9, fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.6)

# Cuadro explicativo de la fórmula
formula_text = (
    r"$\mathbf{Fórmula\ General:}\ I = \int_{t_0}^{t_f} (T_{base} - T_{ext})\,dt$" + "\n" +
    r"$\mathbf{Regla\ del\ Trapecio:}\ I \approx \sum_{i=0}^{N-1} \frac{\Delta T_i + \Delta T_{i+1}}{2} \cdot \Delta t$" + "\n" +
    f"donde $\Delta t = 0.5\ \mathrm{{horas}}$ (30 min)"
)
ax1.text(0.02, 0.08, formula_text, transform=ax1.transAxes, fontsize=10,
         verticalalignment='bottom', bbox=dict(boxstyle='round,pad=0.6', facecolor='#edf2f7', edgecolor='#cbd5e0', alpha=0.95))

# --- Subplot 2: Curva de Integral Acumulada ---
ax2.plot(x_indices, integral_acumulada, color='#2b6cb0', marker='s', linewidth=2.5, 
         markersize=5, label='Integral Acumulada (Grados-Hora)')
ax2.fill_between(x_indices, 0, integral_acumulada, color='#bee3f8', alpha=0.5)

# Resaltar el resultado final
ax2.plot(x_indices[-1], integral_acumulada[-1], marker='o', markersize=10, color='#c53030')
ax2.annotate(f'TOTAL: {integral_acumulada[-1]:.2f} °C·h', 
             xy=(x_indices[-1], integral_acumulada[-1]), 
             xytext=(x_indices[-1] - 2.5, integral_acumulada[-1] - 15),
             arrowprops=dict(facecolor='#c53030', shrink=0.08, width=2, headwidth=8),
             fontsize=11, fontweight='bold', color='#742a2a',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff5f5', edgecolor='#feb2b2'))

ax2.set_xlabel("Hora del Día", fontsize=12, fontweight='bold')
ax2.set_ylabel("Integral Acumulada\n(Grados-Hora)", fontsize=11, fontweight='bold')
ax2.set_xticks(x_indices)
ax2.set_xticklabels(horas, rotation=45, ha='right')
ax2.set_ylim(0, 110)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend(loc='upper left', frameon=True, facecolor='white', framealpha=0.9, fontsize=10)

plt.tight_layout()

# Guardar la imagen en alta resolución
output_path = "resolucion_integral_paso_a_paso.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"¡Imagen generada con éxito como '{output_path}'!")

plt.show()