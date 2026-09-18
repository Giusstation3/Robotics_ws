#define LED 2 //definimos el pin gpio 2 del esp32 donde vamos a conectar el LED 

void setup() { //se ejecuta una vez al iniciar
  pinMode(LED, OUTPUT); //ponemos el pin del ledo como salida no como lectura

  Serial.begin(115200); //le decimos a que velocidad vamos a abrir la señal serial 
}

void loop() {
  if (Serial.available() > 0) { //si hay al menos un byte en el buffer entonces lo vamos a leer
    char dato = Serial.read();

    if (dato == '1') { 
      digitalWrite(LED, HIGH);
    }

    if (dato == '0') {
      digitalWrite(LED, LOW);
    } //aquí definimos el comportamiento del led de acuerdo al numero leido del puerto
  }
}
