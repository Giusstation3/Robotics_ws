Giuseppe Valencia Carrillo
Prueba de velocity turtle  publisher y subscriber turtle topicos 
EL nodo publisher envía datos usando el topico /velocity usando mensajes de tipo float y el subscriptor escucha o se suscribe al topico para recibir los datos y mostrarlos. Solo hizo falta modificar los valores del if dentro del codigo para que se detuviera
Comandos utilizados: ros2 topic list, rqt_graph, ros2 topic info /velocity, ros2 node info /velocity_publisher python3 velocity publisher.py y python3 velocity_subscriber.py
ningun problema encontrado durante el desarrollo
https://itam2-my.sharepoint.com/:v:/g/personal/giuseppe_valencia_itam_mx/IQAT0q8MGYklRaglpJRT3KoCASzNYzvzNVlWHa5iyBtAKCw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=Tgv9v0

Actividad 3 Publicador y publicador serial 

Se implementan los nodos de publicacion y subscripcion para controlar un led y lectura de un potenciometro ambos conectados a un ESP32 que se comunican con ROS2 usando el puerto serial.
led blink.py es un nodo de ros2 que publica los numeros 1 y 0 en alternancia en el topico led command cada segundo. Esto representa si el led estara prendido o apagado.
Serial bridge es un nodo de ros2 que subscribe a led command y traduce cada valor enviado por el puerto serial hacia el esp32 
finalmente led serial ino es el codigo que se ejecuta en el esp32 y lo que hace es leer los caracteres que llegan por serial y enciende o apagar el LED conectado. 

Entonces: led blink publica en el topico led command, serial bridge lo recibe y lo traduce al puerto serial y led serial ino enciende o apaga el led. 

Para el potenciometro ADC pot ino es el codigo que corre en el esp32m lee el valor analogico del potenciometro y lo envia al puerto serial. analog_serial_pub.py es un nodo de ROS2 que lee el puertoserial, valida el dato recibido sea numerico y lo publica en el topico analog. Finalmente analog_subs.py es un nodo de ROS2 que se subscribe a analog e imprime el valor en la consola. 

Entonces: ADC pot lee el potenciometro, lo envia por serial, analog serial lo lee y lo publia en el topico analog y analog subs se subscribe y muestra el valor. 
