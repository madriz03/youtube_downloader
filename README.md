# *Youtube Downloader*
Hemos creado un scripts para descargar videos de youtube con pocas lineas de codigo, solo debes ejecutar el scripts e ingresarle una URL del video que prefieras.

Para esto usamos la[ librería pytube](http://https://pytube.io/en/latest/ " librería pytube") de la cual hicimos uso de la clase YouTube.

Como ya te comente solo debes hacer uso de la libreria pytube si no la tienes instalada esto lo puedes hacer desde la consola con el comando:

#### ***pip install pytube***
Como buena practica es recomendable hacerlo en un entorno virtual.

Comenzamos nuestra linea de codigo indicando que usaremos de pytube la clase YouTube:

### ***from pytube import Youtube***

Para luego comenzar con la definicion de nuestra funcion la cual debe recibir un parametro el cual almacenara el link del video a descargar.

Seguimos con el cuerpo de la funcion donde se crea un objeto el cual sera una instancia de la clase Youtube importada en la primera linea de codigo.

Luego procedimos a aplicar un metodo de la clase Youtube que consigue que el video sea descargado en la mayor resolucion disponible.

Finalmente usamos el metodo de descarga para asi dar por terminada la definicion de la funcion.

Podrias agregar manejo de excepciones a este funcion tomando en cuenta que  en algun momento el usuario pueda pasarle una URL no valida o rota, sientete libre de agregar las funcionalidades que creas pertinentes, aqui estamos aprendiendo.

Con intencion de hacerlo mas interactivo creamos un input para que cada vez que se ejecute el scripts se le pida la URL al usuario una vez el usuario la ingrese y ejecute el scripts se ejecutara la funcion que tomara como parametro la URL que ingreso el usuario como input.

Espero te haya gustado esta funcionalidad, te invito a profundizar en la documentacion y descubirir todas las funcionalidades y metodos.
<br>
<br>
<br>
Creditos a este video de youtube donde vi la implementacion de esta funcionalidad por primera vez y quise ensayarla y compartirla.


[Tutorial de Youtube](http://https://www.youtube.com/watch?v=EMlM6QTzJo0&t=409s "Tutorial de Youtube")