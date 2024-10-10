---
icon: chevron-right
order: 1000
---
 
``Last update: Feb 10, 2024``

***
:::content-center
<img src="../paperspace-img/logo1.jpg" alt="image" width="710" height="auto">        
:::

## ‎ 
## Introduction  
- Paperspace is a cloud-based platform for using AI apps, powered by virtual machines with powerful GPU's.     

- It's a great alternative for training RVC voice models through the cloud, since it's even faster than Google Colab.

- Making this platform one of the most competent counterparts to Colab, if you don't mind paying a monthly subscription.      
***
###### ‎   
## Important Notes
1. Although Paperspace has a free plan, you can't do much with it, it's more convenient to buy its **Pro** or **Growth** plan.

3. There have been people who had to try a couple of times before Paperspace accepted their card. Be patient if that happens to you.

3. Aditionally, you can pay hourly for **faster** GPU's instead of using the free ones by default.    
This is optional, the paid plans are fast enough.
***
###### ‎   
## How to Use   
###### ‎   
#### 1. <u>Set up account.</u>
a. Start by making an account <u>[here</u>](https://console.paperspace.com/signup).

b. Buy a plan in the `Platform Plans` section on the right <u>[here</u>](https://www.paperspace.com/pricing).

   <img src="../paperspace-img/3.png" alt="image" width="575" height="auto">      

***
###### ‎   
#### 2. <u>Create notebook.</u>
a. Make sure you are in the ``Gradient`` tab, and click the `CREATE` button.

   <img src="../paperspace-img/5.png" alt="image" width="200" height="auto"> 
        ‎       
   <img src="../paperspace-img/4.png" alt="image" width="150" height="auto">           
###### ‎     
b. Make sure there are free GPU's available, and below select the number of hours you want the notebook to remain active.

   <img src="../paperspace-img/6.png" alt="image" width="450" height="auto">     
###### ‎  
c. Then click ``START NOTEBOOK``.           
You'll find yourself in a screen like this:

   <img src="../paperspace-img/7.png" alt="image" width="" height=""> 
***
###### ‎   
#### 3. <u>Install Mangio.</u>
a. Copy this, paste it in the Terminal and hit enter:      

        wget https://huggingface.co/lollenape/LollenApeRVC/resolve/main/install.py 
‎       
b. Once it's done installing, open the `paper.ipynb` file.

   <img src="../paperspace-img/8.png" alt="image" width="650" height=""> ‎      
‎       
c. Execute the `INSTALL EVERYTHING` cell.

   <img src="../paperspace-img/9.png" alt="image" width="430" height=""> ‎   
‎               
d. Once that one is done, execute the ``START GUI`` one.    
Then you can start using Mangio.

   <img src="../paperspace-img/10.png" alt="image" width="430" height=""> ‎ 
‎               
‎       
!!! <u>Notes about training:</u>
**1.** To create the dataset folder, open the notebook, right click the ``Mangio-RVC-Fork`` folder, click `New folder`, name it `dataset`, and put your dataset there.    
‎       
**2.** If you get an error when you click ``Process data``, don't worry, it's a visual glitch. Keep working as usual.   
!!!
‎           
### Opening TensorBoard
To run TensorBoard while using RVC you'll have to do it on a separate terminal.         

a. Go to your notebook and open a new terminal by clicking the Terminal symbol ( :icon-terminal: ) on the right.

b. Then introduce this:

        cd/notebooks/Mangio-RVC-Fork
        make TensorBoard
        
***
###### ‎   
:::content-center
## Comparison With Colab
:::
###### ‎
>###### ‎
>:::content-center
><img src="../paperspace-img/11.png" alt="image" width="600" height=""> ‎   
>:::
>‎         
>‎       
>*"The main difference lies in the model training process, as the GPUs available on Paperspace are more powerful.         
‎       
You can achieve training speeds that are approximately 3 times faster compared to Colab, which translates to saving a significant amount of time.               
‎       
So, if you were to train a model with a dataset that takes around an hour and a half (1:30) on Paperspace, it would take approximately three and a half hours (3:30).       
‎       
On the other hand, on Colab, it might take around 7 hours (without considering the account switching)."*         
>***
>:::content-right
>``- Picture & quote by LollenApe``    
>:::     
>‎        
>‎    

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/rvc/#contributions)
:::