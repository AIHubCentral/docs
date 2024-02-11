``Última actividad: Feb 10, 2024``
***
###### ‎
:::content-center
## Introducción
:::
###### ‎              
- RVC Disconnected (o *RVC-D*) es un port de <u>[Mangio](https://aihubdocs.github.io/es/recursos-de-rvc/opciones-de-inferencia/#pitch-extraction-algorithm)</u> a [<u>Google Colab</u>](https://aihubdocs.github.io/es/otro/glosario/#google-colab), para exclusivamente entrenar. Notebook hecha por [<u>Kit Lemonfoot</u>](https://huggingface.co/Kit-Lemonfoot).

- Es gratis, incluye herramientas necesarias para un modelo de calidad, [<U>TensorBoard</u>](https://aihubdocs.github.io/es/recursos-de-rvc/epochs-sobreentrenar--tensorboard/#tensorboard), y es el espacio de Colab más rápido para entrenar.    

- Esto lo vuelve el mejor método (gratis) para entrenar modelos de RVC en la nube. El único gran inconveniente es el límite de uso (aunque puedes cambiar a otra cuenta y continuar).      
‎       
### Pros & Contras :icon-tasklist:

==- ***Abrir***
!!!
***Los pros & contras son subjetivos según tus necesidades.***
!!!
||| ✔️ **PROS**     
- Incluye TensorBoard    
- Incluye Mangio-Crepe.     
- Opción para guardar modelo a HF.  
- Incluye los nuevos *pretrains*.
||| ❌ **CONTRAS**        
- No tiene buena interfaz.   
- Toma un tiempo para cargar.    
- No puedes dejar entrenar sin supervisión por mucho tiempo.
- <u>Para usuarios gratis:</u>
    - Es más lento comparando con RVC local. 
    - No puedes entrenar largos <u>[datasets](https://aihubdocs.github.io/es/aislamiento-vocal--datasets/datasets/)</u> sin tener que pausar el proceso.
|||
===
***
###### ‎ 
###### ‎ 
:::content-center
## Cómo Entrenar
###### ‎ 
!!!warning <u>IMPORTANTE:</u>
1.‎ La guía estará centrada en el **<u>[TensorBoard](https://aihubdocs.github.io/es/recursos-de-rvc/epochs-sobreentrenar--tensorboard/#tensorboard)</u>**. Si no lo conoces, primero lee [<u>aquí</u>](https://aihubdocs.github.io/es/recursos-de-rvc/epochs-sobreentrenar--tensorboard/).   
2. Activa las cookies de terceros de tu navegador, o puede que TB no funcione.
!!!
:::
###### ‎ 

### 1. Prepara el dataset  

a. Primero, haz una carpeta nombrada tras el modelo & mueve el dataset ahí. No incluyas espacios/caracteres especiales.

    <img src="../rvcdisconnected-img/1.png" alt="image" width="210" height="auto">‎                     
‎       
b. Luego [<u>comprime</u>](https://support.microsoft.com/es-es/windows/comprimir-y-descomprimir-archivos-8d28fa72-f2f9-712f-67df-f80cf89fd4e5#:~:text=Para%20comprimir%20un%20archivo%20o%20una%20carpeta&text=Mantenga%20presionado%20o%20haga%20clic,nombre%20en%20la%20misma%20ubicaci%C3%B3n) la carpeta en un .ZIP. 7ZIP y RAR no son compatibles con RVC-D.

    <img src="../rvcdisconnected-img/2.png" alt="image" width="210" height="auto">‎           
‎       
!!!success RECORDATORIO:
Con versiones modernas de RVC, el dataset puede ser un único archivo de audio. No hace falta dividirlo.
!!!
***
###### ‎ 
### 2. Prepara el Colab      
a. Ve al [<u>espacio de Colab</u>](https://colab.research.google.com/drive/1XIPCP9ken63S7M6b5ui1b36Cs17sP-NS#scrollTo=ZodNcumpg-JM). Arriba a la derecha, inicia sesión en tu cuenta de Google.

b. Ejecuta la celda ``Dependencies`` y toca `Ejecutar de todos modos`. Esto tomará un rato.

    <img src="../rvcdisconnected-img/3.png" alt="image" width="280" height="auto">‎  
‎           

d. Cuando aparezca esto, toca `Conectar con Google Drive`, selecciona tu cuenta y `Continuar`.‎    
‎   
    <img src="../rvcdisconnected-img/5.png" alt="image" width="400" height="auto">‎   
‎   
e. Cuando la celda termine de cargarse, en Google Drive ve a la carpeta ``rvcDisconnected`` & pon el .ZIP del dataset en esa carpeta.

    <img src="../rvcdisconnected-img/19.png" alt="image" width="335" height="auto">‎    

***
###### ‎ 
### 3. Ajusta Training Variables      

- Ve a la celda `Set Training Variables`.

    <img src="../rvcdisconnected-img/18.png" alt="image" width="335" height="auto">‎    
    ‎   
- #### <u>Define estos valores:</u>
`experiment_name`
:   Nombra tu modelo. No incluyas espacios/caracteres especiales.

`pretrain_type`
:   Si no eres familiar con pretrains, selecciona `original`.

`target_sample_rate`
:   Inserta la <u>[tasa de muestreo](https://aihubdocs.github.io/es/recursos-de-rvc/formato-de-audio--sample-rate/#sample-rate)</u> de tu dataset. 

``pitch_extraction_algorithm``
:   Selecciona el <u>[algoritmo de extracción](https://aihubdocs.github.io/es/recursos-de-rvc/opciones-de-inferencia/#pitch-extraction-algorithm)</u>. No uses Harvest, está obsoleto.    

`crepe_hop_length`
:   Funciona si usas `Mangio-Crepe`. Modifica el Hop Length.

***
###### ‎ 
### 4. Prepara el entorno    
‎ ‎ ‎ ‎ ‎ ‎ ‎ <img src="../rvcdisconnected-img/8.png" alt="image" width="500" height="auto">‎   
     
a. En la celda `Load Dataset`, escribe en la barra `dataset` el nombre del .ZIP del dataset, seguido de ".zip". Ejemplo: `kalomaze.zip`.    
Luego ejecuta la celda.    
‎   
b. Debajo, ejecuta `Preprocessing`, ``Feature Extraction``, & ``Save preprocessed dataset files to Google Drive``.

    <img src="../rvcdisconnected-img/9.png" alt="image" width="335" height="auto">‎   
***
###### ‎ 
### 5. Entrena el .INDEX 
a. Ejecuta ``Index Training`` para crear el [<u>.INDEX</u>](https://aihubdocs.github.io/es/gu%C3%ADas-populares/modelos-de-voz/#archivos-de-modelos) del modelo.      

    <img src="../rvcdisconnected-img/17.png" alt="image" width="450" height="auto">‎        
‎       
b. Para descargarlo, ve a `rvcDisconnected` en Google Drive. Abre la carpeta nombrada tras tu modelo y descarga el .INDEX llamado `added`.
 
    <img src="../rvcdisconnected-img/13.png" alt="image" width="450" height="auto">‎  
***
###### ‎ 
### 6. Prepara el entrenamiento      
- Ve a la celda `Training`.  

    <img src="../rvcdisconnected-img/10.png" alt="image" width="350" height="auto">‎    
‎   
- #### <u>Define estos valores:</u>

`save_frequency`
:   Cada cuantos <u>[epochs](https://aihubdocs.github.io/es/recursos-de-rvc/epochs-sobreentrenar--tensorboard/)</u> se guardará el modelo. Estos son los puntos de guardado (o "checkpoints"). Si eres novato, déjalo en `15`.      
    <u>Ej:</u> con un valor de ``10``, se guardará tras el epoch 10, 20, 30, 40, etc.    

`total_epochs`
:   Cantidad de <u>[epochs](https://aihubdocs.github.io/es/recursos-de-rvc/epochs-sobreentrenar--tensorboard/)</u> para el modelo. Pero ya que usaremos <u>[TensorBoard](https://aihubdocs.github.io/es/recursos-de-rvc/epochs-sobreentrenar--tensorboard/)</u>, usa un valor arbitrariamente alto como ``2000``.

`batch_size`
:   Usa ``8`` si eres principiante. Pero si tu dataset es pequeño (cerca de 2 minutos o menos), usa ``4``.

***
###### ‎ 
### 7. Empieza a entrenar   
- Ejecuta la celda `Training` para empezar el entrenamiento. Ten paciencia, puede que tarde horas.

- El [TensorBoard](https://aihubdocs.github.io/es/recursos-de-rvc/epochs-sobreentrenar--tensorboard/#tensorboard) se abrirá automáticamente tras unos segundos, recuerda monitorearlo.             

- La celda te irá mostrando información de los epochs & cuando se realicen los puntos de guardado.      
‎
!!!warning <u>Al entrenar, puede que te desconectes si: </u>
• Te quedaste sin tiempo de uso.        
• No interactuaste con el espacio por mucho tiempo (estar AFK).      
• Tu internet se desconectó.        
• No resolviste los captchas que (tal vez) aparecen a veces.        
!!!
***
###### ‎ 
### 8. Descarga el modelo   
- Cuando estás seguro de estar sobreentrenando, detenlo con el botón de pausa de la celda ``Training``.    

- Toca el símbolo de la carpeta a la derecha, abre la carpeta ``Mangio-RVC-Fork``, y luego `weights`. Ahí encontrarás los puntos de guardado del modelo.

    <img src="../rvcdisconnected-img/20.png" alt="image" width="210" height="auto">‎        
‎   
- Haz click derecho al modelo más **cercano** a ***antes*** del punto de sobreentrenamiento, y toca ``Descargar``.  

- Los modelos estarán organizados en este formato: **Nombre_Epoch_Step.pth**.       
Ejemplo: ``arianagrande_e60_s120.pth``    

‎   
Y eso es todo. Diviértete con tu modelo. Recuerda mover sus archivos a una carpeta nueva para mantenerlo organizado. 

Para testearlo, haz una [<u>inferencia</u>](https://aihubdocs.github.io/es/recursos-de-rvc/opciones-de-inferencia/) como de costumbre.   


***
###### ‎ 
### Reentrenar
Si el entrenamiento finalizó pero aún le faltaba entrenamiento al modelo, no tienes que empezar desde cero.    

##### <u>Instrucciones:</u>

1. Ve al espacio de Colab e inserta los mismos datos que introdujiste anteriormente, & ejecuta las celdas como de costumbre, pero <u>no</u> ``Preprocessing`` & ``Feature Extraction``.    
     
2. Ejecuta la celda `Load preprocessed dataset files`.   

    <img src="../rvcdisconnected-img/14.png" alt="image" width="450" height="auto">‎  
‎       
3. Ve a `Import Model from Drive to Notebook`. En `STEPCOUNT` introduce ``2333333`` & ejecuta la celda.    

    <img src="../rvcdisconnected-img/16.png" alt="image" width="450" height="auto">‎  
    ‎       
4. Puedes cambiar ``save_frequency``, o aumentar ``total_epochs`` en caso de no haber insertado suficientes anteriormente. 

5. Ejecuta `Training` para reentrenar nuevamente. Recuerda monitorear <u>[TB](https://aihubdocs.github.io/es/recursos-de-rvc/epochs-sobreentrenar--tensorboard/#tensorboard)</u> como antes.
***
###### ‎
:::content-center
``Guía original: Angetyde``        
:::
:::content-center
``Rehecho por: Julia, Eddy, Poopmaster & Light``       
:::   
:::content-center
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Envíanos Ideas"](https://forms.gle/Q1WX8AxWkH2vuMRd9)
:::
***