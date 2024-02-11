``Última actividad: Feb 10, 2024``   
***
###### ‎
:::content-center
## Introducción
:::
- ***En el campo de la IA***, es la colección de datos usados para entrenar un modelo de IA. Contiene ejemplos de las entradas que debe de manejar, junto con las respuestas correctas.

- ***En el contexto de RVC***, es un archivo de audio que se le da a RVC, que contiene la voz que el modelo replicará. Puede ser una voz hablando o cantando.

- La **calidad** & **duración** del dataset son los factores que mayormente determinan la calidad final del modelo. Expliquemos.
***
###### ‎
:::content-center
## Duración
:::
- Para los nuevos, recomendamos usar **10 minutos**, o **20** si lo quieres de muy alta calidad.        

- Si quieres ir a por más, ten en cuenta que más de 40 minutos no es necesario.      

- Con versiones modernas de RVC, el dataset puede ser un único archivo de audio. No hace falta dividirlo en varios audios.
***
###### ‎
:::content-center
## Calidad
#### ``Recomendaciones & requisitos para un buen dataset:``
:::
##### ‎   
#### :icon-chevron-down: Rango.
- La voz tiene que ser clara, alcanzar notas altas/bajas, y pronunciar cada vocal correctamente.

#### :icon-chevron-down: Limpieza.
- Que no contenga ruido de fondo, reverb, voces hablando al mismo tiempo, música, distorsión, o pequeños silencios. Aprenderás cómo removerlos en la sección **Limpieza de Datasets**.

#### :icon-chevron-down: Calidad de audio.
- Es mejor que tenga buena calidad y con un formato <u>[sin pérdida](https://aihubdocs.github.io/es/recursos-de-rvc/formato-de-audio--sample-rate/)</u>, como **WAV** o **FLAC**. No con pérdida como MP3 u OGG. 

#### :icon-chevron-down: Sin silbidos/popping.
- Adicionalmente, que no incluya silbidos fuertes (pronunciación "S" & "SH" ruidosa), o sonidos "popping" (pronunciación fuerte de la "P").
***
###### ‎
:::content-center
## Limpieza de Datasets
:::  
1. Primero, elimina los ruidos indeseados anteriormente mencionados con un programa de <u>[aislamiento vocal](https://aihubdocs.github.io/es/aislamiento-vocal--datasets/aislamiento-vocal/)</u>.      
***     
2. Tras esto, para remover silencios, distorsión & minimizar (aún más) ruido de fondo, usaremos <u>[**Audacity**](https://www.audacityteam.org/download/)</u>. Un [<u>EAD</u>](https://aihubdocs.github.io/es/otro/glosario/#ead) gratis, simple, y muy liviano.           
    ‎     
    {.list-icon}  
    #### Paso 1: Puerta de Ruido.   
    - Primero, arrastra el archivo de audio hacia la aplicación.  

    - Luego presiona las teclas ``CTRL + A`` para seleccionarlo. 
         
    - Arriba, ve al menú ``Efectos``. Ve a `Reducción de ruido y reparación` y selecciona ``Puerta de ruido``.      
    - Usa estos valores, y toca `Aplicar`:       
    ‎       
 <img src="../datasets-img/1.png" alt="image" width="420" height="auto">   
    ***
    ###### ‎
    #### Paso 2: Truncar silencio.    

    - Ve a Efectos > Especial > Truncar silencio.    
    - Usa los siguientes valores:         
    ‎        
    <img src="../datasets-img/2.png" alt="image" width="420" height="auto">    

    ***
    ###### ‎
    #### Paso 3: Normalizar.    
    - Y finalmente ve a Efectos > Volume y compresión > Normalizar
    - Usa estos valores:      
‎       
<img src="../datasets-img/3.png" alt="image" width="420" height="auto">  

    ***
    ###### ‎
    #### Paso 4: Exporta.
    - Arriba a la derecha ve a `Archivo` y presiona ``Exportar audio``.       
    ‎   
    <img src="../datasets-img/4.png" alt="image" width="250" height="auto"> 
    ‎    
    ‎      
    ‎       
    - Finalmente, introduce estos valores:
        - **Formato**: ``FLAC``    
        - **Canales:** `Mono` (opcional)
        - **Profundidad de bit**: ``24 bit``   
        - **Nivel**: ``8``       
        
    ‎       
    <img src="../datasets-img/5.png" alt="image" width="450" height="auto">

***
###### ‎
:::content-center
## Tips Para Grabar Datasets

#### ``Si harás un modelo de ti mismo, aquí hay unos tips``
:::
###### ‎       
- Grábate leyendo algo, como un libro.
- Antes de grabar, prepara tu voz. Aclara tu garganta & lee en voz alta.
- Que suene como tu voz natural, no lo hagas robótico. 
- Pronuncia las vocales de manera clara.
- Incluye notas altas y agudas. No exageres el tono si no es necesario.
- Acércate al micrófono, pero no mucho.
- Evita el ruido de fondo. Cierra las ventanas, puerta, apaga la computadora, desconecta el refrigerador, etc.
- No grabes en una habitación con reverb. Es mejor en una de tamaño pequeño-mediano con muchos objetos, especialmente suaves (camas, sofás, almohadas, sábanas, etc.)
- Mantén una buena postura, para un buen control de la respiración.
- Ten una bebida a mano para no deshidratarte.
***
:::content-right
`Hecho por Julia, Faze Masta & Litsa`  
:::
‎     
:::content-right
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Envíanos Ideas"](https://forms.gle/Q1WX8AxWkH2vuMRd9)
:::
‎     
‎     
***