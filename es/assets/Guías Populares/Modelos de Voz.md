# :icon-dependabot: Modelos de Voz

``Última Actividad: Feb 10, 2024``       
  
‎
:   ‎
:::       
:::content-center
## ¿Qué es un Modelo de Voz?
:::
###### ‎
- ***En el campo de la IA***, es un programa que fue entrenado para reconocer ciertos patrones o tomar ciertas decisiones.

- ***En este caso***, los modelos de voz son modelos de IA entrenados para **replicar** una voz, y con IA las aplica al audio de entrada.

- Existen una gran cantidad de estos subidos a internet, hechos por el público. Y la mejor manera de hacerlos es con el software **RVC**.       
Aprende cómo [<u>aquí</u>](http://localhost:5000/gu%C3%ADas-populares/c%C3%B3mo-hacer-un-modelo-de-voz/).      
###### ‎   
### Archivos de Modelos 
==- *Están compuestos por 2 archivos:*        
###### ‎    
##### :icon-triangle-down: <u>INDEX:</u>     
- Contiene datos acerca del acento & forma de hablar.       
- Este es adicional, pero usualmente **crucial** para la **calidad** del modelo.        
- Al entrenar, RVC genera dos archivos .INDEX, pero el que debes usar se llamará ``added_`` por defecto.         
###### ‎       
##### :icon-triangle-down: <u>PTH:</u>
- Este archivo es el modelo en sí.
- Contiene datos acerca del tono.     
- Al entrenar, RVC generará otros .PTH nombrados `D_` y `G_`, pero estos son los "puntos de guardado", no modelos utilizables.
***
!!!warning *Cuando subas un modelo, asegúrate de usar los archivos correctos mencionados.*
La gente aveces lo suben de manera incorrecta.
!!!
===      

***
###### ‎
:::content-center
## Cómo Buscar Modelos de Voz
##### *``Cuatro métodos para encontrar uno en internet.``*
:::
###### ‎  
!!!
**Recordatorio:** Los modelos de <u>kits.ai</u> no se pueden descargar.
!!!     
+++ weights.gg   
:::content-center  
<img src="../searchrvcmodels-img/1.png" alt="image" width="300" height="auto">           
:::  
***
:::content-center
### <u> Descripción</u>    
:::
- Este es un sitio web donde los usuarios pueden subir modelos de voz.
- Modelos subidos a **AI Hub** & **AI Hub France** se almacenan automáticamente aquí también.         
- El público pueden leer/compartir opiniones acerca de los modelos mediante comentarios & likes.     
***
###### ‎
:::content-center
### <u>Cómo Buscar</u>
:::
###### ‎
#### 1. Inicia sesión.  
Ingresa al sitio [<u>aquí</u>](https://weights.gg), e inicia sesión tocando el icono superior derecho.
***
###### ‎
#### 2. Busca el modelo. 
Escribe el nombre del modelo en la barra ``Buscar`` & selecciona un resultado.     
      
<img src="../searchrvcmodels-img/2.png" alt="image" width="260" height="auto"> ‎    
‎   

!!!
Si te aparecen modelos de la misma persona en diferentes años, recuerda que su voz cambia a lo largo del tiempo.
!!!
***
###### ‎
#### 3. Analiza el modelo. (opcional)      
- Revisa la descripción, likes, comentarios & audio de muestra. Pueden ayudarte a saber que tan bueno es el modelo.        
- El audio del género y estilo vocal de acuerdo al modelo da la representación más certera.     
- Este paso es útil cuando hay múltiples resultados del mismo modelo.   

    <img src="../searchrvcmodels-img/3.png" alt="image" width="400" height="auto">

***
###### ‎
#### 4. Descarga el modelo.       
Toca los tres puntos y ``Descargar modelo``. Se descargará un archivo .ZIP de este.        
‎   
<img src="../searchrvcmodels-img/4.png" alt="image" width="600" height="auto">‎               
‎                     
Si necesitas un link de este, usa los otros métodos.        
Si solo existe en weights.gg, descarga el .ZIP y súbelo a HF. Aprende más <u>[aquí](http://localhost:5000/gu%C3%ADas-populares/subir-modelos-a-hugging-face/)</u>.   
###### ‎      
!!! *Acerca de los 'epochs'.*
Epoch es una unidad de medida de los ciclos de entrenamiento del modelo.        
Más epochs no equivale a un mejor modelo. Aprende más <U>[aquí](http://localhost:5000/recursos-de-rvc/epochs-sobreentrenar--tensorboard/)</u>.
!!!

+++ Canal Voice Models     
:::content-center
<img src="../searchrvcmodels-img/aihub.png" alt="image" width="200" height="auto">        
:::
***
:::content-center
### <u>Descripción</U>
:::
- Este es un canal de foros en **AI Hub** en donde los usuarios suben sus propios modelos de voz.       
- Buscar uno aquí es especialmente útil si necesitas un link del modelo, ya que los posts incluyen uno.</u>.       
***
###### ‎  
:::content-center
### <u>Cómo Buscar</u>
:::
###### ‎   
#### 1. Entra al canal.     
Si aún no lo has hecho, únete a AI Hub [<u>aquí</u>](https://discord.gg/aihub).         
Luego ve al canal ``#voice-models``.       
       
<img src="../searchrvcmodels-img/5.png" alt="image" width="480" height="auto"> 

***
###### ‎
#### 2. Busca el modelo.        
En la barra superior, busca un modelo y selecciona un post.
***
###### ‎
#### 3. Descarga modelo.      
Toca el link de Hugging Face para descargarlo, o cópialo si lo necesitas.      
Puedes escuchar el audio de muestra para tener una vista previa de como suena.

<img src="../searchrvcmodels-img/6.png" alt="image" width="480" height="auto"> 

+++ Bot ModelAI 
:::content-center
### <u>Descripción</U>
:::
- Este es un bot de Discord que busca modelos publicados en varios servidores de AI Hub.
- También la base de datos de modelos de AI Hub & el canal #voice-models.
- Fue desarrollado por el usuario **Iroak**.
***
###### ‎
:::content-center
### <u>Cómo Buscar</u>
:::
###### ‎
#### 1. Ingresa al canal.      
Si aún no lo has hecho, únete al server [<u>aquí</u>](https://discord.gg/aihub).        
Ve al canal de ``#search-models``.
***
###### ‎
#### 2. Escribe el comando.        
##### <u>En el chat:</u>
- Escribe ``/search``
- Selecciona el comando de **ModelAI**
- Escribe el nombre del modelo
- Envía el mensaje

<img src="../searchrvcmodels-img/8.png" alt="image" width="420" height="auto"> 

***     
###### ‎
#### 3. Descarga el modelo.
   <img src="../searchrvcmodels-img/7.png" alt="image" width="400" height="auto"> ‎    
‎   
- ⬇️‎ Toca ``Download Model`` para **descargarlo**.        

- 🔗‎ Para obtener el **link**, haz click-derecho en ``Download Model`` & toca ``Copy link``.   

- 🔎‎ Si hay **múltiples** resultados, toca la barra ``List of found models`` y ve más resultados.     

- 💾‎ Con ``Save``  el bot te enviará un MD con el resultado, si lo quieres guardar.      

+++ Búsqueda en Hugging Face
:::content-center
<img src="../searchrvcmodels-img/11.png" alt="image" width="510" height="auto">       
:::
***
###### ‎
:::content-center
### <u>Descripción</U>
:::
- Esta una plataforma en línea gratuita & de código abierto para alojar aplicaciones interactivas de IA, modelos de IA, y <u>[datasets](http://localhost:5000/aislamiento-vocal--datasets/datasets/)</u>.
- Aquí los usuarios de RVC suelen almacenar sus modelos de voz.
***
###### ‎
:::content-center
### <u>Cómo Buscar</u>
:::
###### ‎
1. Ve a la página de búsqueda de modelos [<u>aquí</u>](https://huggingface.co/models). Busca el modelo en la barra ``Filter by name``.

    <img src="../searchrvcmodels-img/9.png" alt="image" width="" height="auto">‎                   
‎       
2. Selecciona un modelo y ve a la pestaña ``Files and versions``.   
Para descargarlo, toca el símbolo de descarga ( :icon-download: ) del archivo .ZIP a su derecha.        
Si necesitas su link, hazle click derecho y copia el enlace.

    <img src="../searchrvcmodels-img/10.png" alt="image" width="500" height="auto">        
###### ‎       
!!! *En caso de que no haya un .ZIP.*
Descarga los <u>[archivos correctos](http://localhost:5000/gu%C3%ADas-populares/modelos-de-voz/#archivos-de-modelos)</u> del modelo.     
Si necesitas su **link** súbelo tu mismo. Aprende [<u>aquí</u>](http://localhost:5000/gu%C3%ADas-populares/subir-modelos-a-hugging-face/).
!!!
+++
##### ‎ 
#### Si no encontraste tu modelo, tienes 3 opciones:    
- Haz el modelo tu mismo
- Escoge otro
- Paga a un model maker y que lo haga por ti         

##### Si te interesa la primera, aprende [<u>aquí</u>](http://localhost:5000/gu%C3%ADas-populares/c%C3%B3mo-hacer-modelos-de-voz/).

***
:::content-right
`Hecho por Julia`      
:::
‎  
:::content-right
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Envíanos Ideas"](https://forms.gle/Q1WX8AxWkH2vuMRd9)
::: 
‎  
‎  
***