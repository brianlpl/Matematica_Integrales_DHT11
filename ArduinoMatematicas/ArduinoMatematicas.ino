#include "DHT.h"

// Definimos el pin de conexión y el tipo de sensor
#define DHTPIN 2     // Pin digital donde está conectado el pin de DATOS del DHT11
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

// Temperatura base de confort para tu cálculo de integrales
const int tempBase = 24; 

void setup() {
  Serial.begin(9600);
  dht.begin();
  
  // Imprimir el encabezado de la tabla una sola vez al iniciar
  Serial.println("Iniciando registro de temperatura...");
  Serial.println("Temp Exterior(C) (DHT11)\tTemp Base(C)");
  Serial.println("-------------------------------------------------");
}

void loop() {
  // Leer la temperatura real en grados Celsius
  float tReal = dht.readTemperature();

  // Comprobar si hubo un error en la lectura (cable desconectado o falla del sensor)
  if (isnan(tReal)) {
    Serial.println("¡Error al leer del sensor DHT11!");
  } else {
    // Imprimir los datos en el Monitor Serie
    Serial.print(tReal, 1); // Imprime con 1 decimal
    Serial.print("\t\t\t\t");
    Serial.println(tempBase);
  }
  
  // Esperar 30 minutos (30 min * 60 seg * 1000 ms = 1800000 ms)
  delay(1800000); 
}