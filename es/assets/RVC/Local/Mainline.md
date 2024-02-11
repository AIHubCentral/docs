``Última actividad: Feb 10, 2024``

***
###### ‎
:::content-center
## Introducción ‎ :icon-book:
:::

- "Mainline" es la versión base, original y sin modificar de RVC. Hecho por el equipo de [<u>RVC-Project</u>](https://github.com/RVC-Project).

- Tiene menos opciones comparado con otros [<U>forks</u>](http://localhost:5000/otro/glosario/#fork), pero conserva las herramientas necesarias para hacer un trabajo decente.

- Es especialmente querido por ser algo más rápido que otras versiones, al ser más liviano. 

- Su nombre real no es "mainline" (línea principal), el público se lo asignó para distinguirlo bien de las otros <u>[forks](http://localhost:5000/otro/glosario/#fork)</u>.     
‎       
### Pros & Contras‎ :icon-tasklist:
==- ***Abrir***
!!!
***Los pros & contras son subjetivos según tus necesidades.***
!!!

||| ✔️ **PROS**  
- Fácil de instalar.                   
- El más simple de usar.     
- Más rápido comparado con otros <u>[forks](http://localhost:5000/otro/glosario/#fork)</u>.
||| ❌ **CONTRAS** 
- Tiene menos opciones.     
- No trae el algoritmo [<u>Mangio-Crepe</u>](http://localhost:5000/recursos-de-rvc/opciones-de-inferencia/#pitch-extraction-algorithm).      
- Subida de modelo manual.
||| 
===
***
###### ‎
###### ‎      
:::content-center
## Instalar & Abrir ‎:icon-download:
:::
###### ‎
1. Ve a su página de descarga [<u>aquí</u>](https://huggingface.co/lj1995/VoiceConversionWebUI/blob/main/RVC1006Nvidia.7z).             

3. Toca <u>``download``</u>. RVC comenzará a descargarse.      
    ‎       
    <img src="../mainline-img/4.png" alt="image" width="550" height="auto">       
    ‎   
3. Cuando termine, descomprime el .ZIP.

4. ***<u>Para abrirlo</U>***, abre la carpeta, busca el archivo "``go-web.bat``" y ejecútalo.       
        ‎       
        <img src="../mainline-img/3.png" alt="image" width="550" height="auto">      
        ‎       
    Se abrirá una consola, y luego de un momento tu navegador predeterminado con RVC listo para usarse.
    ‎       
    ‎             
    <img src="../mainline-img/inferencetab.png" alt="image" width="450" height="auto">‎   
    ‎       
5. **(Opcional)** Para acceder a RVC más rápido, crea un acceso directo de el archivo ``go-web``.      
‎       
!!!warning No cierres la consola hasta que termines de usarlo, o dejará de funcionar.
!!! 
***
###### ‎      
###### ‎       
:::content-center
## Inferencia ‎:icon-unmute:
!!!success
Si te topas con un problema, lee el capítulo <u>[Solución de Problemas](http://localhost:5000/rvc/local/mainline/#soluci%C3%B3n-de-problemas-)</u>.
!!!
:::
###### ‎
#### 1. Sube el modelo de voz.
a. Abre la carpeta de RVC. Ve a la carpeta `assets`, y pon el archivo [<u>**.PTH**</u>](http://localhost:5000/gu%C3%ADas-populares/modelos-de-voz/#archivos-de-modelos) del modelo dentro de la carpeta `weights`.       
    ‎       
    <img src="../mainline-img/5.png" alt="image" width="520" height="auto">      
‎       
       
b. Regresa a la carpeta anterior y pon el [<u>**.INDEX**</u>](http://localhost:5000/gu%C3%ADas-populares/modelos-de-voz/#archivos-de-modelos) del modelo en la carpeta `logs`.

    <img src="../mainline-img/6.png" alt="image" width="520" height="auto"> 

***
###### ‎  
#### 2. Selecciona el modelo.
a. En RVC, toca ``Refresh voice list and index path``.

    <img src="../mainline-img/1.png" alt="image" width="400" height="auto"> 

    ‎       
b. A la izquierda, toca `Inferencing voice` & selecciona el modelo.

    <img src="../mainline-img/7.png" alt="image" width="400" height="auto"> 

***
###### ‎  
#### 3. Selecciona vocales.      
En ``Enter the path of the audio file`` pega la [<u>ruta de archivo</u>](https://www.solvetic.com/tutoriales/article/8447-copiar-ruta-archivo-windows-10-ruta-de-acceso/) de tu audio.
Asegúrate que la ruta no incluya caracteres especiales/espacios.

<img src="../mainline-img/8.png" alt="image" width="650" height="auto"> 

***
###### ‎  
#### 4. Ajusta opciones. (opcional)      
Si quieres, modifica las [<u>opciones de inferencia</u>](http://localhost:5000/recursos-de-rvc/opciones-de-inferencia/) para mejores resultados.
***
###### ‎  
#### 5. Procesa.
Presiona en botón largo de ``Convert`` abajo. El audio empezará a convertirse.    
 
El procesamiento dependerá principalmente de tus <u>[specs](http://localhost:5000/otro/glosario/#specs)</u>, duración del audio & el algoritmo que elegiste.
***
###### ‎  
#### 6. Descarga el resultado.
Cuando termine, aparecerá un audio reproducible en la casilla de `Export audio`.     
Para descargarlo, toca los tres puntos a la derecha y presiona `Download`.

<img src="../mainline-img/9.png" alt="image" width="500" height="auto">‎        

***
###### ‎      
###### ‎     
:::content-center
## Entrenamiento :icon-dependabot:
###### ‎  
:::
!!!warning <u> NOTAS: </u>
La guía estará centrada en el uso de **<u>[TensorBoard](http://localhost:5000/recursos-de-rvc/epochs-sobreentrenar--tensorboard/#tensorboard)</u>**. Lee su artículo primero, si aún no lo haz hecho.

Si te topas con un problema, lee el capítulo <u>[Solución de Problemas](http://localhost:5000/rvc/local/mainline/#soluci%C3%B3n-de-problemas-)</u>.
!!!
###### ‎   
###### ‎   
:::content-center
### <u> Paso 1 </u>
:::
###### ‎      
#### 1. Ve al sector de entrenamiento.
Abre RVC y ve a la pestaña `Train`.  

<img src="../mainline-img/10.png" alt="image" width="" height="auto">   

***
###### ‎  
#### 2. Nombra el modelo.
En `Enter the experiment name` nombra tu modelo. No insertes caracteres especiales/espacios.     


<img src="../mainline-img/11.png" alt="image" width="300" height="auto">    

***
###### ‎  
#### 3. Selecciona tasa de muestreo.
En `Target sample rate` selecciona la [<u>tasa de muestreo</u>](http://localhost:5000/recursos-de-rvc/formato-de-audio--sample-rate/#sample-rate) de tu <u>[dataset](http://localhost:5000/aislamiento-vocal--datasets/datasets/)</u>.        
Ingresar un valor incorrecto podría arruinar la calidad del modelo.

<img src="../mainline-img/g.png" alt="image" width="" height="auto">         

‎       
***
###### ‎      
:::content-center
### <u> Paso 2a </u>
:::
###### ‎  
#### 4. Selecciona dataset.
En `Enter the path of the training folder` pega la [<u>ruta de archivo</u>](https://www.solvetic.com/tutoriales/article/8447-copiar-ruta-archivo-windows-10-ruta-de-acceso/5) de tu <u>[dataset](http://localhost:5000/aislamiento-vocal--datasets/datasets/)</u>.        
Asegúrate que la ruta no incluya caracteres especiales/espacios.

<img src="../mainline-img/13.png" alt="image" width="" height="auto">  

###### ‎       

!!!secondary
Si por defecto la casilla tiene texto, primero elimínalo.
!!!
***
###### ‎  
#### 5. Process data.
Toca el botón de `Process Data` en el centro.      

RVC procesará los factores previos para el entrenamiento, que podría tomar un momento dependiendo de qué tan grande sea el dataset.

<img src="../mainline-img/14.png" alt="image" width="450" height="auto">  

‎       

Finalizará cuando la casilla de `output information` diga ``end preprocess``.

<img src="../mainline-img/a.png" alt="" width="" height="auto">  

***
###### ‎     
:::content-center
### <u> Paso 2b </u>
:::
###### ‎     
#### 6. Selecciona GPUs.
En `Enter the GPU index(es)` determina qué <u>[GPU](http://localhost:5000/otro/glosario/#gpu)</u>(s) usarás para el entrenamiento, poniendo su índice seguido de un guion (ej: `0`).

<img src="../mainline-img/15.png" alt="image" width="" height="auto">  

***
###### ‎  
#### 7. Selecciona el algoritmo.
a. A la derecha, selecciona el <u>[algoritmo de extracción](http://localhost:5000/recursos-de-rvc/opciones-de-inferencia/#pitch-extraction-algorithm)</u>.       
Elige únicamente ``RMVPE_GPU`` o ``Crepe``, ya que el resto están obsoletos.            

    <img src="../mainline-img/16.png" alt="image" width="" height="auto"> ‎      

###### ‎   
b. Ahora presiona el botón de `Feature extraction` a la derecha.    

    <img src="../mainline-img/17.png" alt="image" width="370" height="auto">‎        
    ‎      
    ‎   
    Finalizará cuando la casilla ponga ``all-feature-done``.

    <img src="../mainline-img/b.png" alt="image" width="320" height="auto">  

***
###### ‎  
#### 8. Crea el .INDEX.
Presiona el botón de `Train feature index` del centro.       
Esto generará el archivo [<u>.INDEX</u>](http://localhost:5000/gu%C3%ADas-populares/modelos-de-voz/#archivos-de-modelos) del modelo.

<img src="../mainline-img/i.png" alt="image" width="250" height="auto">‎     
‎       
Terminará cuando el output diga algo así:

<img src="../mainline-img/h.png" alt="image" width="270" height="auto"> 

***
###### ‎     
:::content-center
### <u> Step 3 </u>
:::
###### ‎           
#### 9. Determina save frequency.
Define cada cuantos <u>[epochs](http://localhost:5000/recursos-de-rvc/epochs-sobreentrenar--tensorboard/)</u> se guardará el modelo. Los modelos guardados se le conocen como "checkpoints" (puntos de guardado).

Si eres novato, dejalo en `15`.    

Ej: con un valor de ``10``, se guardará tras el epoch 10, 20, 30, 40, etc.

‎   
<img src="../mainline-img/18.png" alt="image" width="" height="auto">

***
###### ‎  
#### 10. Inserta epochs totales.
En `Total training epochs` determina la cantidad de <u>[epochs](http://localhost:5000/recursos-de-rvc/epochs-sobreentrenar--tensorboard/)</u> para el modelo.     

Pero ya que usaremos <u>[TensorBoard](http://localhost:5000/recursos-de-rvc/epochs-sobreentrenar--tensorboard/)</u>, usa un valor arbitrariamente alto como ``2000``.

<img src="../mainline-img/19.png" alt="image" width="" height="auto">  

***
###### ‎  
#### 11. Selecciona batch size.
Si no sabes lo que hace, deja `Batch size per GPU` en `8`
    
Pero si tu <u>[dataset](http://localhost:5000/aislamiento-vocal--datasets/datasets/)</u> es pequeño (alrededor de 2 minutos o menos), usa ``4``.

<img src="../mainline-img/20.png" alt="image" width="" height="auto">  

***
###### ‎  
#### 12. Abre TensorBoard.
Antes de empezar a entrenar, abre TB.     

Si aún no lo haz hecho, aprende acerca de este [<u>aquí</u>](http://localhost:5000/recursos-de-rvc/epochs-sobreentrenar--tensorboard/).
***
###### ‎  
#### 13. Empieza a entrenar.
Toca ``Train model`` para empezar a entrenar.

<img src="../mainline-img/21.png" alt="image" width="250" height="auto"> 

‎   
‎   

Recuerda monitorear TB, también la consola por si acaso.        
La consola mostrará errores en caso de que sucedan, e información de los epochs & cuando se realicen los puntos guardado.       
‎   
<img src="../mainline-img/j.png" alt="image" width="550" height="auto"> 

***
###### ‎  
#### 14. Detén el entrenamiento.
Cuando estés seguro de estar sobreentrenando, deténlo presionando ``Stop Training``, ubicado en la parte inferior, donde solía estar ``Train model``.

***
###### ‎  
#### 15. Busca el modelo.
a. Crea una nueva carpeta en dónde sea, nombrada tras tu modelo.

a. Abre la carpeta de RVC, ve a la carpeta ``logs``, y verás una carpeta nombrada tras tu modelo.       
Selecciona el `.INDEX` llamado ``added_`` & muévelo a la carpeta que recién creaste.

    <img src="../mainline-img/c.png" alt="image" width="" height="auto">  

‎   

c. Luego ve a la carpeta ``weights``, y ahí encontrarás los puntos de guardado del modelo.

    Selecciona el más **cercano** a ***antes*** del punto de sobreentrenamiento, y muévelo a la nueva carpeta.      

    Los modelos estarán organizados en este formato: **Nombre_Epoch_Step.pth**   

    Ejemplo: ``arianagrande_e60_s120.pth``

    <img src="../mainline-img/d.png" alt="image" width="" height="auto"> ‎  
    ‎       
    Y eso es todo. Diviértete con tu modelo.    
    Para testearlo, haz una [<u>inferencia</u>](http://localhost:5000/gu%C3%ADas-populares/c%C3%B3mo-hacer-un-cover-de-ia/) como de costumbre.     

***
###### ‎   
:::content-center
### <u>Reentrenar</u>   
:::
###### ‎   
Si el entrenamiento finalizó pero aún le faltaba entrenamiento al modelo, no tienes que empezar desde cero.       
**Sigue este procedimiento:**

- Simplemente inserta exactamente los **mismos datos & criterios** que insertaste previamente.
Nombre del modelo, tasa de muestreo, <u>[dataset](http://localhost:5000/aislamiento-vocal--datasets/datasets/)</u>, etc.
No tienes que presionar ``Process Data`` o crear el [<u>.INDEX</u>](http://localhost:5000/gu%C3%ADas-populares/modelos-de-voz/#archivos-de-modelos) devuelta si ya se hizo.

- Puedes cambiar el **save frequency**, o aumentar los **epochs** totales en caso de no haber insertado suficientes anteriormente. 

- Comienza a entrenar, & recuerda monitorear TB & la consola como antes.

***
###### ‎ 
###### ‎  
:::content-center
## Solución de Problemas :icon-tools:
:::
###### ‎  
==- *No hay una opción para mi tasa de muestreo.*
###### ‎   

- **Si tu tasa es menor a <u>32k**</u>: selecciona ``32k``.     
‎   
- **Si es de <u> 32k**</u>: a la derecha en <u>Version</u> toca `v1` & toca `v2` devuelta. Asegúrate de dejarlo en `v2`. Ahora te aparecerá `32k`.      
‎   
- **Si es <u>44.1k**</u>: selecciona ``40k``.   
‎   
- **Si es mayor a <u>48k</u>**: selecciona ``48k``.

===

==- *La voz tiene fallos.*
###### ‎   
- Este es un fenómeno llamado artifacting. Para solucionarlo, lee <u>[aquí](http://localhost:5000/recursos-de-rvc/artifacting/)</u>.

===

==- *RVC va lento en mi equipo con AMD/Intel.*  
###### ‎   
- Esto es porque RVC no es compatible con estas <u>[GPUs](http://localhost:5000/otro/glosario/#gpu)</u>, solo con NVIDIA.
- Por esto, es más propenso a errores & y usa tu CPU para trabajar, lo que ralentiza mucho el proceso.
- Para <u>[inferencia](http://localhost:5000/otro/glosario/#inferencia)</u>, te conviene usar <u>[Ilaria RVC](http://localhost:5000/rvc/en-la-nube/inferencia/ilaria-rvc/)</u>. Y para entrenar modelos, <u>[RVC Disconnected](http://localhost:5000/rvc/en-la-nube/entrenar/rvc-disconnected/)</u> o <u>[Paperspace](http://localhost:5000/rvc/en-la-nube/entrenar/paperspace/)</u>.

===
:::content-right
`Hecho por Julia & Poopmaster`
:::
‎     
:::content-right
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Envíanos Ideas"](https://forms.gle/Q1WX8AxWkH2vuMRd9)
:::
‎     
‎     
***