``Última actividad: Feb 10, 2024``
‎ 
***  
###### ‎ 
:::content-center
## Introducción
:::
- Ilaria RVC es un port de EasyGUI ([<u>Mangio</u>](https://aihubdocs.github.io/es/rvc/local/mangio/)) a [<u>Google Colab</u>](https://aihubdocs.github.io/es/otro/glosario/#google-colab). Hecho por <u>[Ilaria](https://ko-fi.com/ilariaowo)</u>.     

- Funciona solo para <u>[inferencia](https://aihubdocs.github.io/es/otro/glosario/#inferencia)</u>, tiene una buena interfaz, enorme velocidad, y las buenas herramientas que Mangio ofrece (como el algoritmo [<u>Mangio-Crepe</u>](https://aihubdocs.github.io/es/recursos-de-rvc/opciones-de-inferencia/#pitch-extraction-algorithm)).

- Y por esto es considerado una de las mejores alternativas para hacer inferencia por la nube.      
‎               
### Pros & Contras :icon-tasklist:
==- ***Abrir***
!!!
***Los pros & contras son subjetivos según tus necesidades.***
!!!
||| **✔️ PROS** 
- Subida de modelos mediante links.    
- Dos opciones de TTS.     
- Buena interfaz.        
- Inclusión de Mangio-Crepe.      
- No toma mucho tiempo en cargarse.  
- Es muy rápido.  
|||  **❌ CONTRAS**   
- Límite de uso para usuarios gratis.  
- Toma 3 minutos en cargarse.
|||
===

***
###### ‎ 
:::content-center
## Inferencia

!!!success
Si tienes un problema, lee el capítulo de [<u>Solución de Problemas</u>](https://aihubdocs.github.io/es/rvc/en-la-nube/inferencia/ilaria-rvc/#soluci%C3%B3n-de-problemas-).
!!!
:::

###### ‎ 
#### 1. <u>Ingresa al espacio.</u>
a. Primero inicia sesión en Google [<U>aquí</u>](https://accounts.google.com/). 

b. Luego accede al espacio de Colab [<u>aquí</u>](https://colab.research.google.com/drive/16LkwvFZeudTpUOsE_6bMjOq2qkxFo8Hr?usp=sharing)
***
###### ‎ 
#### 2. <u>Prepara el espacio.</u>

- Ejecuta la celda `Install Ilaria-RVC`, y luego presiona `Ejecutar de todas formas`.       
- RVC empezará a cargarse.    

    <img src="../ilarvc-img/a.png" alt="image" width="250" height="auto">‎ ‎ ‎<img src="../ilarvc-img/b.png" alt="image" width="320" height="auto">‎               
‎   
- Terminará cuando la celda ponga `Done Cloning Repo`.

    <img src="../ilarvc-img/d.png" alt="image" width="300" height="auto">‎      
‎   
!!!success
Es normal que aparezca texto en rojo mostrando error.
!!!
***
###### ‎ 
#### 3. <u>Abre el Gradio.</u> 
a. Debajo de este, ejecuta la celda `Start`.        

b. Tras unos segundos te mostrará dos links. Abre el de **gradio.live** en una pestaña aparte.        

    <img src="../ilarvc-img/e.png" alt="image" width="540" height="auto">‎              
‎        
!!!warning No cierres la pestaña de <u>Colab</u> hasta que termines de usar Ilaria RVC.      
Sino, tendrás que iniciar el procedimiento desde cero.
!!!
***
###### ‎ 
#### 4. <u>Descarga el modelo de voz.</u>
{.list-icon}
- <img src="../ilarvc-img/3.png" alt="image" width="450" height="auto">‎  
    ‎   
a. En el Gradio, ve a la pestaña ``Download Voice Models``.     

b. Pega el link del modelo en la barra `Hugging Face Link`. Debe ser un link público de **Hugging Face**/**Google Drive**.

c. En `Name of the model`, nombra tu modelo. No le insertes espacios/caracteres especiales.

d. Luego toca `Download`.        

***
###### ‎ 
#### 5. <u>Selecciona modelo.</u>  
a. Regresa a la ventana `Inference`, & toca el botón superior `Refresh`.
b. Despliega la casilla `Choose the model` & selecciona tu modelo.

    <img src="../ilarvc-img/4.png" alt="image" width="450" height="auto">
***
###### ‎ 
#### 6. <u>Selecciona audio.</u>  
- Debajo de este, arrastra el audio hacia la casilla `Coloque el archivo aquí`, o presionalo para subirlo manualmente.      

    <img src="../ilarvc-img/5.png" alt="image" width="450" height="auto"> 

***
###### ‎ 
#### 7. <u>Ajusta opciones.</u> (opcional)    
- Si quieres, despliega `Index Settings` & `Advanced Options` para modificar las <u>[Opciones de Inferencia](https://aihubdocs.github.io/es/recursos-de-rvc/opciones-de-inferencia/)</u>, para mejores resultados.   

    <img src="../ilarvc-img/6.png" alt="image" width="500" height="auto"> ‎                  
      
***

###### ‎ 
#### 8. <u>Convierte el audio.</u>     
- Toca el botón superior de `Convert`, y espera un momento a que se haga la inferencia.

    <img src="../ilarvc-img/7.png" alt="image" width="250" height="auto">   

***
###### ‎ 
#### 9. <u>Descarga el resultado.</u>        
- Cuando termine de procesarse, aparecerá un audio reproducible en la ``Final Result!``.      
- A la derecha de este, toca los tres puntos & `Descargar`.         

    <img src="../ilarvc-img/8.png" alt="image" width="" height="auto">‎     
    
***
:::content-center
[!button variant="danger" corners="pill" icon="heart-fill" iconAlign="right" text="Apoyar a Ilaria"](https://ko-fi.com/ilariaowo)
:::
‎
:   ‎


:::content-center
## TTS
#### *`y con un modelo de RVC`*
###### ‎
:::
1. Primero accede al Gradio. Si no sabes como, sigue los 3 primeros pasos del <u>[capítulo anterior](https://aihubdocs.github.io/es/rvc/en-la-nube/inferencia/ilaria-rvc/#inferencia)</u>.
***
2. Ve a la sección de `IlariaTTS`. 

    <img src="../ilatts-img/1.png" alt="image" width="450" height="auto">‎     

    Si quieres, puedes usar el otro TTS `ElevenLabs / Google TTS`.
***
3. En `Voice` escoge una voz del género, lenguaje & acento que desees. Y debajo de este, inserta el texto.      

    Si usarás un modelo de RVC, escoge el tipo de voz que más se aproxime a este.
***
4. Toca `Speak`, y el TTS empezará a procesarse.
***
5. Cuando termine de procesarse, aparecerá un audio reproducible en la ``Final Result!``.      
A la derecha de este, toca los tres puntos & `Descargar`.         

    <img src="../ilarvc-img/8.png" alt="image" width="" height="auto">‎     
     
***
6. Para usar un modelo de voz de RVC, simplemente sube el resultado a Ilaria RVC y conviértelo usando tu modelo. (Opcional)        
    Si no sabes cómo, lee <u>[aquí](https://aihubdocs.github.io/es/rvc/en-la-nube/inferencia/ilaria-rvc/#inferencia)</u>.

***
###### ‎
###### ‎
:::content-center
## Solución de Problemas :icon-tools:
:::
###### ‎
==- *Me aparece un mensaje de `Error` en rojo.*  
###### ‎   
- Esto es normal. Intenta repetir tu acción.        
‎   
- Si el error persiste, recarga la página de Gradio.     
‎   
- Asegúrate que tu audio esté seleccionado en `Choose the audio file`. Si no está en la lista, toca `Refresh` a su derecha y selecciónalo.      
‎     
- Si persiste, reinicia el espacio de Colab:        
    - Ve al Colab y arriba toca la flecha :icon-triangle-down:
    - Presiona `Desconectarse y eliminar entorno de ejecución`. 
    - Recarga la página y carga RVC desde cero.
===

==- *Mi modelo no tiene un link de HF/GD.*
###### ‎
- Tendrás que crear el link tú mismo. Aprende [<u>aquí</u>](https://aihubdocs.github.io/es/gu%C3%ADas-populares/subir-modelos-a-hugging-face/).

===

==- *No puedo descargar el modelo.*     
###### ‎
- Esto puede ser debido a uno de estos motivos:     

    1. **Link es privado:** 
        - Si es de GD, su `Acceso general` tiene que ser `Cualquiera con el link`.
        - Si es de HF, el repo debe ser `Público`. Aprende más [<u>aquí</u>](https://aihubdocs.github.io/es/gu%C3%ADas-populares/subir-modelos-a-hugging-face/).            
        ‎   
    2. **Link de HF inválido:**
        - Deber ser el link del archivo .ZIP.
        - Si contiene la palabra `blob`, reemplázala por `resolve` y pégalo.     
    ‎       
    3. **Archivos incorrectos:**
        - El modelo tiene que estar comprimido en un archivo **.ZIP**. No .RAR o .7ZIP.
        - Debe de contener su archivo .PTH e .INDEX correcto. Aprende más [<u>aquí</u>](https://aihubdocs.github.io/es/gu%C3%ADas-populares/subir-modelos-a-hugging-face/).
===

==- *La voz tiene fallos.*
###### ‎
- Este es un fenómeno llamado "**artifacting**". Aprende cómo solucionarlo [<u>aquí</u>](https://aihubdocs.github.io/es/recursos-de-rvc/artifacting/).

===

==- *No encontré mi respuesta.*
###### ‎
- Pide ayuda en nuestro servidor [<u>AI Hub</u>](https://discord.com/invite/aihub).
- Puedes pedir en `#help-rvc`, `#español`, o hacer un post en `help-forum`.

===

***

:::content-right
`Escrito por Julia` 
::: 
‎    
:::content-right
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Envíanos Ideas"](https://forms.gle/Q1WX8AxWkH2vuMRd9)
:::
###### ‎    
###### ‎ 
***