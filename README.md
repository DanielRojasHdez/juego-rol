# juego-rol
# 🐍 Proyecto Colaborativo Python

Bienvenido al repositorio del equipo. Aquí gestionaremos el código de nuestro proyecto.

## 📥 Cómo unirse al proyecto (Solo la primera vez)
** Abre el visual studio code y asegurate de cerrar los proyectos que tengas abiertos.
Para descargar el proyecto en tu ordenador, abre la terminal y ejecuta:
1. cd documents (para ubicarnos en el directorio de documentos)
2. git clone https://github.com/DanielRojasHdez/juego-rol
3. cd juego-rol
4. code .
Al ejecutar estos comandos se te abrirá un nuevo visual studio code con el proyecto descargado (o por lo menos eso es lo que me ha salido a mi xD)
## Como trabajar con ramas(Branches)
** El comando checkout se utiliza para crear si no existe una rama o movernos a una rama concreta si ya existe la misma, en este caso nos movemos a la rama main que es la principal del proyecto para descargar las ultimas actualizaciones que hemos aprobado.
1. Actualiza tu repositorio local para descargar las ultimas actualizaciones que se han hecho.
- git checkout main
- git pull origin main

2. Crea tu propia rama(cambiale el nombre por algo como rama-bernat o rama-ruben)
** Una vez creada la correspondiente al usuario el comando checkout servirá para movernos a la rama que hemos indicado(siempre trabajaremos cada uno en nuestra rama)
- git checkout -b nombre-de-tu-rama
- git merge main (sirve para traernos el contenido actualizado que hay en la rama main a nuestra rama)

3. Como subir tus aportaciones
cuando hayas terminado de programar tus cambios, guardalos localmente.
- git add . (IMPORTANTE: añadir un espacio despues de add y el .)
- git commit -m "explicacion breve de lo que has hecho"

4. sube la tama a github
- git push origin nombre-de-tu-rama

RESUMEN DE LOS COMANDOS EXPLICADOS PARA EL EQUIPO:
## 💡 Comandos clave explicados para el equipo

Para que tus compañeros no se pierdan, aquí tienes lo que hace cada comando que les estás pidiendo:

* **`git pull origin main`**: Es como "descargar la actualización". Trae todo lo que otros compañeros hayan subido y aprobado.
* **`git checkout -b`**: Crea un espacio de trabajo seguro (la rama) para que, si rompen algo, no afecte al código que ya funciona en `main`.
* **`git add .`**: Selecciona todos los archivos nuevos o modificados para la "foto" que vas a guardar.
* **`git commit -m`**: Es el título de esa "foto". Ayuda a saber qué se hizo en ese momento.
