# custom-planner

## Ingreas fechas

Formas de hacer inputs de eventos,

Fecha completa, 

```start``` 2025-06-12 12:20

```end``` 2025-06-12 13:00

Evento que dura todo el día,

```start``` 2025-06-12

```end``` (dejar vacío) 

Se hace un autocomplete del día de termino.

Ingresar eventos del mes rápido,

e.g. el próximos lunes hay prueba de Termo,

```Name``` I2 Termo

```start``` 19 17:30

```end``` 19 20:00

```info``` (opcional)

Se hace autocomplete de la fecha para el mes actual.
Si no se ingresa una hora se hace autocomplete para evento que dura todo el día.

## Path 

Si quieres que te mueste las cosas que tienes que hacer en el día cuando abras una ventana nueva
de la terminal tienes que ejecutar el código al final del ```.bashrc``` o la shell que uses (creo). 
Así que ahí tienes que usar un path adecuado para que la función ```create_table``` no te cree una ```db``` en el
root o home folder (L diseño). 

Si solo lo vas a correr en la carpeta donde lo guardes solo pon en los path ```my_database.db```.
