``Última actividad: Feb 10, 2024``   
 
***
###### ‎ 
:::content-center
## Introducción ‎ :icon-book:
:::   
- Mangio es un [<u>fork</u>](https://aihubdocs.github.io/es/otro/glosario/#fork) de RVC, hecho por [Mangio621](https://github.com/Mangio621), [Kalomaze](https://github.com/kalomaze), & [Alexolotl](https://github.com/alexlnkp).

- Considerado uno de los mejores <u>[forks](https://aihubdocs.github.io/es/otro/glosario/#fork)</u>, principalmente por sus características extras, inclusión de [<u>Mangio-Crepe</u>](https://aihubdocs.github.io/es/recursos-de-rvc/opciones-de-inferencia/#pitch-extraction-algorithm), & su estabilidad.

- Desafortunadamente, a día de hoy el proyecto está abandonado, así que no esperes actualizaciones de los desarrolladores pronto.     

‎           
### Pros & Contras‎ :icon-tasklist:
==- ***Abrir***
!!!
***Los pros & contras son subjetivos según tus necesidades.***
!!!

||| ✔️ **PROS** 
- Fácil de instalar.      
- Incluye Mangio-Crepe.        
- Buen UI.       
- Tiene más opciones que [<u>Mainline</u>](https://aihubdocs.github.io/es/rvc/local/mainline/).        
- Tiene *hybrid training*.        
- Más ligero en almacenamiento, si instalas la versión de solo [<u>inferencia</u>](https://aihubdocs.github.io/es/otro/glosario/#inferencia).
||| ❌ **CONTRAS**    
- Un poco más lento que Mainline.     
- Estará desactualizado por mucho tiempo.     
- Subida de modelos manual.
||| 
===
***
###### ‎      
###### ‎   
:::content-center
## Instalar & Abrir ‎:icon-download:
:::
###### ‎   

1. Para exclusivamente **[<u>inferencia</u>](https://aihubdocs.github.io/es/otro/glosario/#inferencia)**, presiona [<u>aquí</u>](https://huggingface.co/MangioRVC/Mangio-RVC-Huggingface/resolve/main/Mangio-RVC-v23.7.0_INFER.7z).      
    Para inferencia & **entrenamiento**, presiona [<u>aquí</u>](https://huggingface.co/MangioRVC/Mangio-RVC-Huggingface/resolve/main/Mangio-RVC-v23.7.0_INFER_TRAIN.7z).     

2. Mangio comenzará a descargarse. Cuando termine, descomprime el .ZIP.

3. Abra la carpeta de Mangio, encuentra el archivo "``go-web.bat``" y ejecútalo.        
    ‎       
    <img src="../mangio-img/k.png" alt="" width="600" height="auto">‎ 

    ‎       
    Se abrirá una consola, y luego de un momento tu navegador predeterminado con Mangio listo para usarse.
    ‎       
    ‎             
    <img src="../mangio-img/inferencetab.png" alt="image" width="500" height="auto">  
    ‎       
5. **(Opcional)** Para acceder a RVC más rápido, crea un acceso directo de el archivo ``go-web``.
‎       
!!!warning No cierres la consola hasta que termines de usarlo, o dejará de funcionar.
!!! 
***
###### ‎       
###### ‎      
:::content-center   
## Inferencia :icon-unmute:
###### ‎     
!!!success
Si te topas con un problema, lee el capítulo [Solución de Problemas](https://aihubdocs.github.io/es/rvc/local/mangio/#soluci%C3%B3n-de-problemas-).
!!!
:::
###### ‎    
#### 1. Sube el modelo de voz.
a. Abre la carpeta de Mangio y pon el archivo [<u>**.PTH**</u>](https://aihubdocs.github.io/es/gu%C3%ADas-populares/modelos-de-voz/#archivos-de-modelos) del modelo dentro de la carpeta `weights`.

    <img src="../mangio-img/g.png" alt="image" width="500" height="auto"> 
###### ‎       
b. Y pon su archivo [<u>**.INDEX**</u>](https://aihubdocs.github.io/es/gu%C3%ADas-populares/modelos-de-voz/#archivos-de-modelos) en la carpeta `logs`.

    <img src="../mangio-img/h.png" alt="image" width="500" height="auto"> 
***
###### ‎  
#### 2. Selecciona el modelo.
a. En RVC, toca ``Refresh voice list and index path``.

    <img src="../mangio-img/1.png" alt="image" width="400" height="auto">     
    
‎   
b. A su izquierda, toca `Inferencing voice` & selecciona el modelo.

    <img src="../mangio-img/b.png" alt="image" width="400" height="auto">    

***
###### ‎  
#### 3. Inserta vocales.      
En ``Enter the path of the audio file`` pega la [<u>ruta de archivo</u>](https://www.solvetic.com/tutoriales/article/8447-copiar-ruta-archivo-windows-10-ruta-de-acceso/) de tu audio.     

<img src="../mangio-img/2.png" alt="image" width="400" height="auto"> 

‎       

!!!
Si hay múltiples audios en dicha dirección, toca `Select audio path from the dropdown` & selecciona el que desees.
!!!
***
###### ‎  
#### 4. Ajusta opciones. (opcional)      
Si quieres, modifique las [<u>opciones de inferencia</u>](https://aihubdocs.github.io/es/recursos-de-rvc/opciones-de-inferencia/) para mejores resultados.
***
###### ‎  
#### 5. Convierte.
Presiona en botón largo de ``Convert`` abajo. El audio empezará a convertirse.    
 
El procesamiento dependerá principalmente de tus [specs](https://aihubdocs.github.io/es/otro/glosario/#specs), duración del audio & el algoritmo que elegiste.
***
###### ‎  
#### 6. Obtén el audio de salida.
Cuando termine, aparecerá un audio reproducible en la casilla de `Export audio`.   
Los audios de salida estarán disponible en la carpeta `audio-outputs` de Mangio.

<img src="../mangio-img/a.png" alt="image" width="" height="auto"> 

***
###### ‎
###### ‎       
:::content-center
## Entrenamiento :icon-dependabot:
:::
###### ‎  
!!!warning <u> NOTAS:</u>
La guía estará centrada en el uso de <u>[TensorBoard](https://aihubdocs.github.io/es/recursos-de-rvc/epochs-sobreentrenar--tensorboard/#tensorboard)</u>. Si no eres familiar con este, primero lee [<u>aquí</u>](https://aihubdocs.github.io/es/recursos-de-rvc/epochs-sobreentrenar--tensorboard/).       
 
Si te topas con un problema, lee el capítulo [Solución de Problemas](https://aihubdocs.github.io/es/rvc/local/mangio/#soluci%C3%B3n-de-problemas-).        
!!!
:::
###### ‎      
###### ‎       
:::content-center
### <u> Paso 1 </u>
:::
###### ‎   
#### 1. Ve al sector de entrenamiento.
Abre Mangio y ve a la pestaña `Train`.            

<img src="../mangio-img/4.png" alt="image" width="" height="auto"> 

***
###### ‎  
#### 2. Nombra el modelo.
En `Enter the experiment name` nombra tu modelo. No insertes caracteres especiales/espacios.        

<img src="../mangio-img/5.png" alt="image" width="340" height="auto"> ‎     

***
###### ‎  
#### 3. Selecciona tasa de muestreo.
En `Target sample rate` selecciona la [<u>tasa de muestreo</u>](https://aihubdocs.github.io/es/recursos-de-rvc/formato-de-audio--sample-rate/#sample-rate) de tu <u>[dataset](https://aihubdocs.github.io/es/aislamiento-vocal--datasets/datasets/)</u>.        
Ingresar un valor incorrecto podría arruinar la calidad del modelo.

<img src="../mangio-img/6.png" alt="image" width="" height="auto"> 

***
###### ‎       
:::content-center
### <u>Paso 2a</u>
:::
###### ‎     
#### 4. Selecciona dataset.
Abre la carpeta de Mangio, ve a la carpeta `datasets` & mueve tu dataset ahí.      

<img src="../mangio-img/c.png" alt="image" width="550" height="auto"> 

‎       
!!!warning *Cuando termines de entrenar, asegúrate de quitar el dataset de la carpeta.*
!!!
***
###### ‎  
#### 5. Process Data.
Toca el botón de `Process Data` en el centro.      

RVC procesará los factores previos para el entrenamiento, que podría tomar un momento dependiendo de qué tan grande sea el <u>[dataset](https://aihubdocs.github.io/es/aislamiento-vocal--datasets/datasets/)</u>.

<img src="../mangio-img/8.png" alt="image" width="370" height="auto"> 

‎       

Finalizará cuando la casilla de `output information` diga ``end preprocess``.

<img src="../mangio-img/17.png" alt="image" width="380" height="auto"> 


***
‎   
:::content-center
### <u>Step 2b</u>
:::
###### ‎  
#### 6. Selecciona GPUs.
En `Enter the GPU index(es)` determina qué [GPUs](https://aihubdocs.github.io/es/otro/glosario/#gpu) usarás para el entrenamiento, poniendo su índice seguido de un guión (ej: `0`).

<img src="../mangio-img/9.png" alt="image" width="300" height="auto"> 

***
###### ‎  
#### 7. <u>Selecciona el algoritmo.</u>
a. A la derecha selecciona el <u>[algoritmo de extracción](https://aihubdocs.github.io/es/recursos-de-rvc/opciones-de-inferencia/#pitch-extraction-algorithm)</u>.       
Elige únicamente ``RMVPE``, ``Crepe`` o `Mangio-Crepe`, ya que el resto están obsoletos.               

    <img src="../mangio-img/10.png" alt="image" width="270" height="auto"> ‎    

###### ‎   
b. Ahora presiona el botón de `Feature extraction` a la derecha.     

    <img src="../mangio-img/11.png" alt="image" width="320" height="auto">‎        
    ‎      
    ‎   
    Finalizará cuando la casilla ponga ``all-feature-done``.

    <img src="../mangio-img/18.png" alt="image" width="320" height="auto">  

***
###### ‎  
#### 8. Crea el .INDEX.
Presiona el botón de `Train feature index` del centro.       
Esto generará el archivo [<u>.INDEX</u>](https://aihubdocs.github.io/es/gu%C3%ADas-populares/modelos-de-voz/#archivos-de-modelos) del modelo.

<img src="../mangio-img/11.png" alt="image" width="280" height="auto"> ‎       
‎       
Terminará cuando el output ponga `Successful index Construction`.

<img src="../mangio-img/i.png" alt="image" width="280" height="auto"> 

***
###### ‎     
:::content-center
### <u> Paso 3 </u>
:::
###### ‎         
#### 9. Determina save frequency.
Define cada cuantos <u>[epochs](https://aihubdocs.github.io/es/recursos-de-rvc/epochs-sobreentrenar--tensorboard/)</u> se guardará el modelo. Los modelos guardados se le conocen como "checkpoints" (puntos de guardado).

Si eres novato, dejalo en `15`.    

Ej: con un valor de ``10``, se guardará tras el epoch 10, 20, 30, 40, etc.

<img src="../mangio-img/12.png" alt="image" width="250" height="auto"> 

***
###### ‎  
#### 10. Inserta epochs totales.
En `Total training epochs` determina la cantidad de [epochs](https://aihubdocs.github.io/es/recursos-de-rvc/epochs-sobreentrenar--tensorboard/) para el modelo.     

Pero ya que usaremos [TensorBoard](https://aihubdocs.github.io/es/recursos-de-rvc/epochs-sobreentrenar--tensorboard/), usa un valor arbitrariamente alto como ``2000``.

<img src="../mangio-img/13.png" alt="image" width="250" height="auto">

***
###### ‎  
#### 11. Selecciona batch size.
Si no sabes lo que hace, déjalo `Batch size per GPU` en `8`
    
Pero si tu <u>[dataset](https://aihubdocs.github.io/es/aislamiento-vocal--datasets/datasets/)</u> es pequeño (alrededor de 2 minutos o menos), usa ``4``.

<img src="../mangio-img/14.png" alt="image" width="250" height="auto"> 

***
###### ‎  
#### 12. Abre TensorBoard.
Antes de empezar a entrenar, abre TB.     

Si aún no lo haz hecho, empieza a leer [<u>aquí</u>](https://aihubdocs.github.io/es/recursos-de-rvc/epochs-sobreentrenar--tensorboard/).
***
###### ‎  
#### 13. Empieza a entrenar.
Toca ``Train model`` para empezar a entrenar.

<img src="../mangio-img/16.png" alt="image" width="290" height="auto"> 

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

<img src="../mangio-img/d.png" alt="image" width="290" height="auto"> 

***
###### ‎      
#### 15. Busca el modelo.
a. Crea una nueva carpeta en dónde sea, nombrada tras tu modelo.

a. Abre la carpeta de RVC, ve a la carpeta ``logs``, y verás una carpeta nombrada tras tu modelo.       
Selecciona el `.INDEX` llamado ``added_`` & muévelo a la carpeta que recién creaste.

    <img src="../mangio-img/e.png" alt="image" width="470" height="auto"> 

    ‎      

c. Luego ve a la carpeta ``weights``, y ahí encontrarás los puntos de guardado del modelo.

    Selecciona el más **cercano** a ***antes*** del punto de sobreentrenamiento, y muévelo a la nueva carpeta.      

    Los modelos estarán organizados en este formato: **Nombre_Epoch_Step.pth**   

    Ejemplo: ``arianagrande_e60_s120.pth``

    <img src="../mangio-img/f.png" alt="image" width="500" height="auto">‎      
    ‎       
    Y eso es todo. Diviértete con tu modelo.    
    Para testearlo, haz una [<u>inferencia</u>](https://aihubdocs.github.io/es/gu%C3%ADas-populares/c%C3%B3mo-hacer-un-cover-de-ia/) como de costumbre.   
***
###### ‎   
:::content-center
### <u>Reentrenar</u>   
:::
###### ‎ 
Si el entrenamiento finalizó pero aún le faltaba entrenamiento al modelo, no tienes que empezar desde cero.       
**Sigue este procedimiento:**

- Simplemente inserta exactamente los **mismos datos & criterios** que insertaste previamente.
Nombre del modelo, tasa de muestreo, <u>[dataset](https://aihubdocs.github.io/es/aislamiento-vocal--datasets/datasets/)</u>, etc.
No tienes que presionar ``Process Data`` o crear el [<u>.INDEX</u>](https://aihubdocs.github.io/es/gu%C3%ADas-populares/modelos-de-voz/#archivos-de-modelos) devuelta si ya se hizo.

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
- **Si es <u>44.1k**</u>: selecciona ``40k``.   
‎   
- **Si es mayor a <u>48k</u>**: selecciona ``48k``.

===

==- *La voz tiene fallos.*
###### ‎   
- Este es un fenómeno llamado artifacting. Para solucionarlo, lee [aquí](https://aihubdocs.github.io/es/recursos-de-rvc/artifacting/).

===

==- *RVC va lento en mi equipo con AMD/Intel.*  
###### ‎   
- Esto es porque RVC no es compatible con estas [GPUs](https://aihubdocs.github.io/es/otro/glosario/#gpu), solo con NVIDIA.
- Por esto, es más propenso a errores & y usa tu CPU para trabajar, lo que ralentiza mucho el proceso.
- Para [inferencia](https://aihubdocs.github.io/es/otro/glosario/#inferencia), te conviene usar [Ilaria RVC](https://aihubdocs.github.io/es/rvc/en-la-nube/inferencia/ilaria-rvc/). Y para entrenar modelos, [RVC Disconnected](https://aihubdocs.github.io/es/rvc/en-la-nube/entrenar/rvc-disconnected/) o [Paperspace](https://aihubdocs.github.io/es/rvc/en-la-nube/entrenar/paperspace/).

===

***
‎
:::content-center
``Escrito por: Julia``    
:::
:::content-center
``Agradecimientos a: Poopmaster, Eddy, Raid, SimplCup.``    
:::
:::content-center
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Envíanos Ideas"](https://forms.gle/Q1WX8AxWkH2vuMRd9)
:::
***