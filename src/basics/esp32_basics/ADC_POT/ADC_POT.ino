#define POT 15 
//PIN GPIO 15, donde está conectado el potenciometro 

void setup() {
  Serial.begin(115200); //inicia comunicacion serial al 11520 
}

void loop() {
  int valor = analogRead(POT); //leemos el valor analog del pin 
  Serial.println(valor); //lo mandamos por serial
  delay(100); //esperamos antes de volver a hacerlo
}
