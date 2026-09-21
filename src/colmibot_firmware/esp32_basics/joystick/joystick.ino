#define JX 32 
#define JY 33

void setup() {
  //inicializamos comunicacion serial 115200
  Serial.begin(115200);
  
}

void loop() {
  //Leemos ambos ejes del joystick
  int valorX = analogRead(JX);
  int valorY = analogRead(JY);
  //imprimimos los valores y los separo por comas 
  Serial.print(valorX);
  Serial.print(',');
  Serial.println(valorY);
  delay(100);
}
