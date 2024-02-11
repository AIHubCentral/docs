``Última actividad: Feb 10, 2024``

***
:::content-center
<img src="../paperspace-img/logo1.jpg" alt="image" width="710" height="auto">        
:::

## ‎ 
## Introducción  
- Paperspace es una plataforma basada en la nube para usar programas de IA, ejecutadas por máquinas virtuales con potentes GPU.

- Es una buena alternativa para entrenar modelos de voz RVC por la nube, ya que es más rápido que <u>[Google Colab](http://localhost:5000/otro/glosario/#google-colab)</u>.

- Esto hace Paperspace una contraparte muy competente a Colab, si es que no te importa pagar una suscripción mensual.
***
###### ‎   
## Notas Importantes
1. Aunque Paperspace tiene un plan gratuito, no puedes hacer mucho con este, te conviene comprar el plan **Pro** o **Growth**.

3. Algunas personas tuvieron que intentar un par de veces hasta que Paperspace aceptara su tarjeta. Ten paciencia si esto te pasa.

3. Adicionalmente, puedes pagar por **GPU's más rápidas** en lugar de usar las gratuitas que vienen por defecto.
Esto es opcional, el plan de paga es lo suficientemente rápido.
***
###### ‎   
## Cómo Usar
###### ‎   
#### 1. <u>Prepara tu cuenta.</u>
a. Empieza haciendo una cuenta [<u>aquí</u>](https://console.paperspace.com/signup).

b. Compra un plan de la sección `Platform Plans` a la derecha, [<u>aquí</u>](https://www.paperspace.com/pricing).

   <img src="../paperspace-img/3.png" alt="image" width="575" height="auto">      

***
###### ‎   
#### 2. <u>Crea la notebook.</u>
a. Asegúrate de estar en la pestaña ``Gradient``, y toca el botón de `CREATE`.

   <img src="../paperspace-img/5.png" alt="image" width="200" height="auto"> 
        ‎       
   <img src="../paperspace-img/4.png" alt="image" width="150" height="auto">           
###### ‎     
b. Asegúrate de que haya una GPU gratuita disponible, y selecciona la cantidad de horas que quieres que la notebook permanezca activa.

   <img src="../paperspace-img/6.png" alt="image" width="450" height="auto">     
###### ‎  
c. Luego presiona ``START NOTEBOOK``.           
Aparecerá una pantalla como esta:

   <img src="../paperspace-img/7.png" alt="image" width="" height=""> 
***
###### ‎   
#### 3. <u>Instala Mangio.</u>
a. Copia esto, pégalo en el terminal y presiona Enter:

       wget https://huggingface.co/lollenape/LollenApeRVC/resolve/main/install.py 
###### ‎      
b. Cuando termine de instalarse, abre el archivo `paper.ipynb`.

   <img src="../paperspace-img/8.png" alt="image" width="650" height=""> ‎      
‎       
c. Ejecuta la celda `INSTALL EVERYTHING`.

   <img src="../paperspace-img/9.png" alt="image" width="430" height=""> ‎   
‎               
d. Cuando termine de instalarse, ejecuta la de ``START GUI``.
Y luego ya podrás empezar a usar <u>[Mangio](http://localhost:5000/rvc/local/mangio/)</u>.

   <img src="../paperspace-img/10.png" alt="image" width="430" height=""> ‎ 
‎               
‎       
!!! <u>NOTAS:</u>
**1.** Para crear la carpeta del dataset, abre la notebook, haz click derecho en la carpeta ``Mangio-RVC-Fork``, toca `New folder`, nómbralo `dataset`, y pon tu dataset ahí.    
‎       
**2.** Si te sale un error al tocar ``Process data``, no te preocupes, es una falla visual. Sigue trabajando como de costumbre.   
!!!
***
‎           
### Abrir TensorBoard
Para abrir Tensorboard mientras usas RVC, tendrás que hacerlo en otra terminal por separado.         

a. Ve a tu notebook y toca el símbolo de la terminal ( :icon-terminal: ) en la derecha, para abrir una nueva.

b. Luego introduce esto:

        cd/notebooks/Mangio-RVC-Fork
        make tensorboard
        
***
:::content-center
###### ‎   
## Comparación con Colab
:::
###### ‎
>###### ‎
>:::content-center
><img src="../paperspace-img/11.png" alt="image" width="600" height=""> ‎   
>:::
>‎         
>‎       
>*"La principal diferencia radica en el proceso de entrenar modelos, ya que las GPU disponibles en Paperspace son más poderosas.    
‎     
Llegan a una velocidad aproximadamente 3 veces más rápida en comparación con Colab, lo que equivale en ahorrar una gran cantidad de tiempo.     
‎     
Por lo que si tuvieras que entrenar un modelo con un dataset de alrededor de hora y media (1:30), en Paperspace tomaría más o menos tres horas y media (3:30).    
‎     
Por otro lado, en Colab puede tomar alrededor de 7 horas (sin considerar el cambiar de cuenta)."*             
>***
>:::content-right
>##### ``- Foto & frase de LollenApe``    
>:::     
>‎        
>‎    
***
:::content-center
`Guía original: LollenApe`    
`Rehecho por: Julia & Leo`
:::
:::content-center
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Envíanos Ideas"](https://forms.gle/Q1WX8AxWkH2vuMRd9)
:::
***