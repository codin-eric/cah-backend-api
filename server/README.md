Back end del proyecto.
Aquí encontraras toda la lógica para levantar tu propio servidor de Codin Contra el Mundo

 Reglas
====
1. Se requiere un minimo de 4 jugadores para arrancar el juego.
2. Cada jugador agarra 10 cartas blancas.
3. Un jugador al azar es elegido como "Card Czar" para agarrara una carta negra y liderar la ronda. 
4. El resto de los jugadores eligen la mejor respuesta para la carta negra
5. El "Card Czar" lee las respuestas sin saber quien dio cada una y decide cual es la mas graciosa
6. El ganador es el que gana mas cartas negras!

 Guia
====
- Para levantar el servidor debes crear la imagen definida en el Dockerfile con el comando `docker build -t cah_backend .`
- Para consumir la API de momento se debe correr el container con `docker run --rm -v $(pwd):/data --network host cah_backend python /data/server.py` 
En un futuro estaria bueno tener definido un entry point para no tener que hacer todo eso.
- Los comandos que se deben pasar a la API todavia no están definidos (No llegué tan lejos jah)

 Test
====
- WIP

#### ToDo
- [ x ] Crear sala
- [ x ] Escribir las reglas del juego
- [ ] Unir usuario a la sala
- [ ] Dar el ok de todos los usuarios en la sala para iniciar
- [ ] Repartir cartas blancas
- [ ] Repartir carta negra
- [ ] Votar por la mejor respuesta
- [ ] Sumar puntos
- [ ] Crear un entry point en la imagen para no tener que hacer el docker run con todos los parametros innecesarios