---
icon: chevron-right
order: 8000
---
 
``Last update: August 7, 2025``

***
:::content-center
<img src="..\appliocolab-img\banner.png" alt="image" width="600">

:::
###### ‎
:::content-center
## Introduction ‎
:::
- This is a <u>[cloud-based](http://docs.aihub.gg/extra/glossary/#cloud-based)</u> alternative to run [Applio](https://docs.aihub.gg/rvc/local/applio/), RVC Fork, only for people who don't have a good PC GPU, via the <u>[Kaggle Service](http://docs.aihub.gg/extra/glossary/#kaggle)</u>. With a Web User Interface.

!!!danger Kaggle Service
**Check the <u>[Kaggle Glossary](http://docs.aihub.gg/extra/glossary/#kaggle)</u> for more info on Free Tier, Limits, Verification, Pricing and other things.**
!!!


#### Pros & Cons :icon-tasklist:

==- ***Learn more***
!!! *The pros & cons are subjective to your necessities.*        
!!!
||| **✔️ PROS:**  
- Has good GPU's  
- Has 30 GPU hours
- Fast  
- TensorBoard included
- You can leave training unsupervised.  
||| ❌ **CONS**       
- Takes some time to set up.      
 
|||
===


***
###### ‎   
## Create an Account   
###### ‎   
#### 1. <u>Set up account.</u>
a. Start by making an account <u>[here](https://www.kaggle.com/account/login?phase=startRegisterTab&returnUrl=%2F)</u>.
‎  

   <img src="../kaggle-img/kaggle-sign-in.png" alt="image" width="575" height="auto">

‎  

b. Verify your acount with a phone number so you can turn on the "internet" option.  

 <img src="../kaggle-img/kaggle-phone.png" alt="image" width="575" height="auto">    
 

***  

###### ‎  
## Notebook Creation & Setup
###### ‎  
#### 2. <u>Clone Notebook</u>
a. Go to <u>[Kaggle](https://www.kaggle.com)</u> and click "Create" then "New Notebook" at the top left. 

   <img src="../applio-kaggle-img/new.png" alt="image" width="400" height="auto"> 

‎ 
b. Under your session's name click "File" then "Import Notebook".

   <img src="../applio-kaggle-img/import.png" alt="image" width="450" height="auto">     

‎   

c. On the new window that appeared on the right click "Link" then type in the box this link `https://github.com/IAHispano/Applio/blob/main/assets/Applio_Kaggle.ipynb`.

   <img src="../applio-kaggle-img/link.png" alt="image" width="700" height="auto"> 

Click "Import" on the bottom right once you've done this.

d. When it's done importing it will display this text window.

   <img src="../applio-kaggle-img/settings-updated.png" alt="image" width="600" height="auto">

‎  
e. Under "Session options" in the sidebar turn on "internet". Make sure persistance is on for both files and varibles.

   <img src="../kaggle-img/kaggle-internet.png" alt="image" width="" height=""> 

f. Turn on T4 X2 GPUs in accelerator.           

   <img src="../kaggle-img/kaggle-gpu.png" alt="image" width="" height=""> 

‎ 
g: (Optional) Turn on headless mode so you can run so you can run the GPU on all sessions and save your progress. Go to the top right and click "Save version" then open the advanced dropdown.

<img src="../kaggle-img/kaggle-pers.png" alt="image" width="" height=""> 

‎
!!!warning Warning
Your runtime will continue draining when you're not running any cells with this option on. 
!!!
***

###### ‎   
## Ngrok Setup
###### ‎  
#### 3. <u>Ngrok Setup</u>
a. Scroll down to the fifth cell and you should see a section where you put your ngrok token. If you dont have a ngrok acount sign up <u>[here](https://ngrok.com/)</u>.             
     a2. Once you have an acount you can authenticate your ngrok tunnel agent here: https://dashboard.ngrok.com/get-started/your-authtoken   
‎       
b. put the Ngrok token in the second cell like so:

   <img src="../kaggle-img/ngrok-applio.png" alt="image" width="600" height="">  

c. Once the Ngrok token is there run the cell.

!!!warning Warning               
There is a monthly limit rate with Ngrok so dont be supprised if training is suddenly interrupted.
!!!

***

###### ‎   
## Installation
###### ‎  
#### 4. <u>Installation Cells</u>
a. Starting from the top run all the cells, with the first being:

   <img src="../kaggle-img/install-cell.png" alt="image" width="900" height=""> 

a2. When it's done it will output `Finished`.

b. Now run the last cell which is:

   <img src="../kaggle-img/start-cell.png" alt="image" width="600" height=""> 

***

###### ‎   
## Using Applio
###### ‎  
#### 5. <u>Ngrok Links</u>

a. Click on the Applio URL link to open Applio's UI, click the Tensorboard Url link to open the Tensorboard and click File Url to open the file manager.

   <img src="../applio-kaggle-img/urls.png" alt="image" width="800" height=""> 

‎

b. Once you've click the Applio Url it will take you to Applio's UI where it operates the same as normal Applio. If you happen to not know how to use Applio you can read about it in the <u>[Local Applio Docs](https://docs.aihub.gg/rvc/local/applio/)</u>, it operates similarly.

***

###### ‎   ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::