``Última actividad: Feb 10, 2024``
‎             
***
###### ‎ 
### Introducción        
En RVC, artifacting es una anomalía en la que la voz del audio de salida suena 
con fallos o de manera "robótica".     
Esto ocurre tras el proceso de [<u>inferencia</u>](http://localhost:5000/otro/glosario/#inferencia) o de entrenamiento del modelo.     
***
###### ‎ 
### Motivos    
Ocurre cuando el [dataset](http://localhost:5000/aislamiento-vocal--datasets/datasets/)/muestra de audio contiene alguna de estas características: 

‎ ‎ ‎ • ‎ Audio es de baja calidad      
‎ ‎ ‎ • ‎ El modelo de voz fue mal entrenado            
‎ ‎ ‎ • ‎ Hay voces hablando al mismo tiempo     
‎ ‎ ‎ • ‎ Tiene reverberación       
‎ ‎ ‎ • ‎ Contiene ruido
             
Como notaste, la mayoría de las causas se reducen a tener un audio no lo suficientemente **limpio**. RVC está hecho para trabajar puramente con voces, no otros sonidos.

Recuerda que cuanto más limpio sea tu audio de entrada, mejores resultados tendrás.
***
###### ‎ 
### Soluciones    
#### 1. Usa un formato sin pérdida:      
- Si es posible, es mejor si tu audio están en un [<u>formato sin pérdida</u>](http://localhost:5000/recursos-de-rvc/formato-de-audio--sample-rate/), como `WAV` o `FLAC`, preservando su calidad original.

- Evita los audios con pérdida, como `MP3` o `OGG`.     
‎   
#### 2. En caso de hacer <u>[inferencia](http://localhost:5000/otro/glosario/#inferencia)</u>:
- Remueve los ruidos indeseados con un programa de [<u>aislamiento vocal</u>](http://localhost:5000/aislamiento-vocal--datasets/aislamiento-vocal/).

- Bajar el [<u>search feature ratio</u>](http://localhost:5000/recursos-de-rvc/opciones-de-inferencia/#search-feature-ratio) puede minimizar artifacting.

- Si los sonidos de respiración lo producen, suprímelos bajando el valor de <u>[Protection](http://localhost:5000/recursos-de-rvc/opciones-de-inferencia/#protect-voiceless-consonants)</u>.     
‎   
#### 3. En caso de hacer modelos:
- Asegúrate de <u>[limpiar el dataset](http://localhost:5000/aislamiento-vocal--datasets/datasets/)</u> correctamente, esto incluye remover distorsiones y silencios.

***
:::content-right
`Escrito por Julia`  
:::
‎   
:::content-right
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Envíanos Ideas"](https://forms.gle/Q1WX8AxWkH2vuMRd9)
:::
‎   
‎  
***