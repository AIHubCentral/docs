# :icon-feed-tag: Rol Model Maker

``Última actividad: Feb 10, 2024``

‎
:   ‎
:::
:::content-center
## Requisitos
##### ``Antes de proceder, asegúrate de cumplir estos requisitos.``
:::
###### ‎
||| REQUISITOS
- Archivo <u>[.PTH](http://localhost:5000/gu%C3%ADas-populares/c%C3%B3mo-hacer-modelos-de-voz/)</u> del modelo.        
- Archivo <u>[.INDEX](http://localhost:5000/gu%C3%ADas-populares/c%C3%B3mo-hacer-modelos-de-voz/)</u> del modelo.       
- Información general del <u>[modelo](http://localhost:5000/gu%C3%ADas-populares/modelos-de-voz/).</u>
- Información general de su proceso de entrenamiento.      
- Una cuenta de Hugging Face.     
- Al menos 1 muestra de audio del modelo **<u>SIN MÚSICA</u>**.     
|||
:::


:::content-center
###### ‎ 
## Invalidantes :icon-x:
##### ``Cosas que descalificarán tu publicación``   
:::
‎
:   ‎
:::
#### :icon-chevron-down: Contiene archivos faltantes/incorrectos.
- El archivo .ZIP del modelo tiene que contener el archivo `.INDEX` y `.PTH` correcto. Aprende cuales son <u>[aquí](http://localhost:5000/gu%C3%ADas-populares/modelos-de-voz--c%C3%B3mo-buscarlos/#archivos-de-modelos)</u>.       
***
###### ‎ 
#### :icon-chevron-down: El modelo es de baja calidad.
- <u>**Un mal modelo sonará:**</u>      

   - Chirriante/rasposo
   - Inaudible
   - Diferente a la fuente
   - Incapaz de expresar ciertas notas
   - Mal articulado
   - Incapaz de pronunciar palabras en su language objetivo
   - Con [<u>artifacting</u>](http://localhost:5000/recursos-de-rvc/artifacting/)
***
###### ‎ 
#### :icon-chevron-down: Usaste un algoritmo de extracción obsoleto.
{.list-icon}
- :icon-check-circle: Solo se permite **Crepe, Mangio-Crepe**, o **RMVPE**. Aprende de ellos [<u>aquí</u>](http://localhost:5000/recursos-de-rvc/opciones-de-inferencia/#pitch-extraction-algorithm).

- :icon-x-circle: Harvest, Dio, Crepe-Tiny, PM, etc. están obsoletos. 

***
###### ‎ 
#### :icon-chevron-down: El audio de muestra tiene una instrumental.
- Para evitar problemas de copyright, no incluyas <u>NINGUNA</u> música en el audio, incluso si no tiene copyright.
***
###### ‎ 
#### :icon-chevron-down: El audio de muestra está alterado.
- No añadas reverb, ecualización, o lo edites de alguna manera. Sino no será una representación certera del modelo. Tiene que ser el audio de salida de RVC puro.             

- Remover silencios al principio/final es válido. :icon-check-circle:      
###### ‎  
***
:::content-center
## Pasos
‎
:   ‎
:::
#### 1. Comprime el modelo.
- Consigue el archivo **.PTH** e **.INDEX** y comprímelos en un archivo [<u>.ZIP</u>](https://support.microsoft.com/es-es/windows/comprimir-y-descomprimir-archivos-8d28fa72-f2f9-712f-67df-f80cf89fd4e5#:~:text=Para%20comprimir%20un%20archivo%20o%20una%20carpeta&text=Mantenga%20presionado%20o%20haga%20clic,nombre%20en%20la%20misma%20ubicaci%C3%B3n).   

- Tiene que ser **.ZIP**. No .7ZIP o .RAR.
***
###### ‎
#### 2. Súbelo a Hugging Face.
- El ZIP tiene que estar subido en Hugging Face como un repositorio **público** de licencia `openrail`.    

- ##### [<u>Aprende cómo aquí</u>](http://localhost:5000/gu%C3%ADas-populares/subir-modelos-a-hugging-face/).
***
###### ‎
#### 3. Prepara el post.
- Cuando tu modelo esté listo, ve hacia el canal **#get-model-maker**. 

- Escribe el comando `/submit` del bot **QCBot** y presiona el comando.       

<img src="../modelmaker-img/1.png" alt="image" width="800" height="auto">‎               
‎     
:::content-center
#### ``Rellena la siguiente información del modelo:``  
:::

**modelname**
:    Nombre del modelo.   

**rvc**
:     Versión de RVC con la que se entrenó (casi siempre será v2)

**extraction**
:     <u>[Método de extracción](http://localhost:5000/recursos-de-rvc/epochs-sobreentrenar--tensorboard/)</u> usado.

**epochs**
:     <u>[Epochs](http://localhost:5000/recursos-de-rvc/epochs-sobreentrenar--tensorboard/)</u> totales usados.

**link**
:     Link de descarga de Hugging Face del modelo.

**image**
:     Imagen de lo que representa (personaje/persona).   

**demo**
:     Una muestra de audio del modelo hablando/cantando. Puedes incluir más tras la confirmación del bot. 

**note** 
:   Opcional. Aquí puedes incluir un comentario tuyo.

***
!!!success
Puedes adjuntar más muestras cuando reenvíes el post a ``#voice-models``.
!!!
***
###### ‎
#### 4. Envía el post.
- Cuando termines de rellenar, envía el mensaje.    

- Tu publicación se agregará a la cola de espera, y el bot te enviará un mensaje de confirmación, conteniendo tu ***submission ID*** (número de publicación).     
**<u>Con esta ID, puedes:</u>**        
   - Revisar tu número en cola con el comando ``/queue``, seguido del ID. (ej. ``/queue 251``)        
   - Cancelar la subida con el comando ``/cancel`` seguido de, ID.    
   ‎       
- Ahora espera a que un **Model QC** (quality checker) verifique tu modelo, y tras esto se te notificará.      

- Si tu modelo es aprobado, el bot te notificará con un mensaje así:

   <img src="../modelmaker-img/2.png" alt="image" width="" height="auto">‎      
‎     
- Luego podrás re-subir el modelo (& modelos futuros) al foro ``#voice-models``.

***
:::content-right
`Guía original: FDG`      
`Rehecho por: Julia`  
:::
‎     
‎     
:::content-right
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Envíanos Ideas"](https://forms.gle/Q1WX8AxWkH2vuMRd9)
:::
‎     
‎     
***