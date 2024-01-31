*`Written by Julia`*        
``Last update: Jan 31, 2024``         
***
###### ‎           
:::content-center
## What is a Voice Model? 💾
:::
###### ‎
- In the field of AI, an AI model is a program that was trained to recognize certain patterns or make certain decisions.

- In this case, voice models are AI models trained to **replicate** a voice, and with AI it **apply** it to a given audio.

- The best way to make voice models is with the software **RVC**. Learn more [<u>here</u>](https://aihubdocs.github.io/en/essentials/how-to-make-an-rvc-voice-model/).      
###### ‎   
### Voice Model Files 
They are made up of two files, of ``.index`` and ``.pth`` extension:         
‎    
#### :icon-triangle-right: <u>INDEX:</u>     
- Contains data regarding the voice's accent and speech manner.       
- File is dditional, but usually **crucial** for the **quality** of the model.        
- While training, RVC generates other .INDEX file, but the right one will be named ``added_`` by default.         
‎       
#### :icon-triangle-right: <u>PTH:</u>
- This file is the model itself.
- Contains data regarding pitch.     
- While training, RVC generates other .PTHs named `D_` or `G_`, but these are training checkpoints, not usable models. The right one will be simply named as the model.        
           
!!!warning *Be sure to upload the correct files mentioned before.*
Otherwise you can't make a proper use of models with incorrect ones.
!!!

***
###### ‎
:::content-center
## How to Search Voice Models 🔍
:::
###### ‎
You have a few methods to search a voice model on the Internet:      
1. weights.gg
2. AI Hub's Voice Models channel
3. ModelAI Discord bot
4. Hugging Face search

Let's explain.

!!! <u>Reminder:</u>
Models from **kits.ai** can't be downloaded.
!!!
######               
+++ weights.gg   
:::content-center  
<img src="../searchrvcmodels-img/1.png" alt="image" width="300" height="auto">           
:::  
***
:::content-center
### Description 📜     
:::
- This a website where people can upload voice models.
- Models uploaded in **AI Hub** & **AI Hub France** get automatically stored here too.  
- Both have a partnership with weights.gg.       
- Users can read/share feedback about the models through comments & likes.     
***
###### ‎
:::content-center
### How to Search 🔍
:::
###### ‎
#### 1. <u>Log in.</u>      
Head over to the website [<u>here</u>](https://www.weights.gg/es), and login by clicking the icon on the upper right corner.
***
###### ‎
#### 2. <u>Search the model.</u>  
Type the name of the model in the ``Search`` bar & click a result.     
      
<img src="../searchrvcmodels-img/2.png" alt="image" width="260" height="auto"> ‎    
‎   

!!!
If you get models from different years, remember, the person's voice changes overtime.
!!!
***
###### ‎
#### 3. <u>Evaluate the model.</u> (optional)      
- Check the description, likes, comments, & audio sample. Feedback can help you know how great the model is.        
- The sample of the gender & vocal style according to the model gives the most accurate representation.     
- This step is specially useful if you get multiple results of the same model.   

    <img src="../searchrvcmodels-img/3.png" alt="image" width="400" height="auto">

***
###### ‎
#### 4. <u>Download model.</u>       
Tap the three dots and ``Download model``. This will download a .ZIP file of it.        

<img src="../searchrvcmodels-img/4.png" alt="image" width="600" height="auto">‎                          
       
!!! NOTES:      
If you need the model as a link instead, use the other methods.     
But if it only exists in weights.gg, download the .ZIP & upload it to HF. Learn more <u>[here](https://aihubdocs.github.io/en/essentials/how-to-upload-models-to-hugging-face/)</u>.      
       
**Regarding epochs**, 'epoch' is a unit of measuring the training cycles of a model. More epochs don't necessarily equal better model.   
Learn more [<u>here</u>](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/).
!!!

+++ Voice Models channel     
:::content-center
<img src="../searchrvcmodels-img/aihub.png" alt="image" width="200" height="auto">        
:::
***
:::content-center
### Description 📜
:::
- This is a forum channel in **AI Hub** where people upload their own voice models.       
- Searching here is specially useful if you need the model as a link, as the posts include HF links.       
***
:::content-center
### How to Search 🔍
:::
###### ‎   
#### 1. <u>Enter the channel</u>.     
If you haven't already, join AI Hub [<u>here</u>](https://discord.gg/aihub).         
Then go to the ``#voice-models`` channel.       
       
<img src="../searchrvcmodels-img/5.png" alt="image" width="480" height="auto"> 

***
###### ‎
#### 2. <u>Search the model</u>.        
In the upper search bar, search your model & click the post.
***
###### ‎
#### 3. <u>Download model</u>.      
Click the [<u>Hugging Face</u>](https://aihubdocs.github.io/en/other/glossary/#hugging-face) link to download the model, or copy it if that's what you need.      
You can listen to the audio sample to get a preview of the it.

<img src="../searchrvcmodels-img/6.png" alt="image" width="480" height="auto"> 

+++ ModelAI bot
:::content-center
### Description 📜
:::
- This is a Discord bot that searches models uploaded on various AI Hub servers.
- As well as the model database of the AI Hub server & voice-models channel
- Developed by user **Iroak**.
***
###### ‎
:::content-center
### How to Search 🔍
:::
###### ‎
#### 1. <u>Enter the channel</u>.      
If you haven't already, join AI Hub [<u>here</u>](https://discord.gg/aihub).        
Head over to the ``#search-models`` channel.
***
###### ‎
#### 2. <u>Type command</u>.        
In the chatbox, type ``/search``, click the **ModelAI** command, type your model, & send the message.

<img src="../searchrvcmodels-img/8.png" alt="image" width="420" height="auto"> 

***     
###### ‎
#### 3. <u>Download model</u>.
   <img src="../searchrvcmodels-img/7.png" alt="image" width="400" height="auto"> ‎    
‎   
- ⬇️‎ Click ``Download Model`` to **download it** it.        

- 🔗‎ To get its **link**, right-click ``Download Model`` and tap ``Copy link``.        
(for mobile users, open it & copy the URL)

- 🔎‎ If there are **multiple** results, click the ``List of found models`` bar to see other results.     

- 💾‎ With the ``Save`` button the bot will DM you said result, in case you want it for later.      

+++ Hugging Face search
:::content-center
<img src="../searchrvcmodels-img/11.png" alt="image" width="510" height="auto">       
:::
***
###### ‎
### Description 📜
:::
- This is a platform where you can upload & share AI models, AI apps, & datasets, and where people usually store their RVC models.
- Learn more about it [<u>here</u>](https://aihubdocs.github.io/en/other/glossary/#hugging-face).
***
###### ‎
:::content-center
### How to Search 🔍
:::
###### ‎
1. Go to the model search page [<u>here</u>](https://huggingface.co/models), and search the model in the ``Filter by name`` bar.

    <img src="../searchrvcmodels-img/9.png" alt="image" width="" height="auto">‎                   
‎       
2. Click the model and go to ``Files and versions``.       
3. Download the model's .ZIP file by clicking the download button on the right.       
If you need its link, right-click it and copy the address.

    <img src="../searchrvcmodels-img/10.png" alt="image" width="500" height="auto">        
       
!!! <u>*In case there isn't a .ZIP.*</u>
Download the **.INDEX** file named `added_`, and the **.PTH** that doesn't start with ``D_`` or ``G_``.       

If you need it as a **link**, download the two files mentioned & upload it yourself. Learn more [<u>here</u>](https://aihubdocs.github.io/en/essentials/how-to-upload-models-to-hugging-face/).
!!!
+++
       
If you couldn't find your model anywhere, you have three options:       
Make the model yourself, use a different one, or pay a model maker to make it for you.          

If you are interested in the first option, click [<u>here</u>](https://aihubdocs.github.io/en/essentials/how-to-make-an-rvc-voice-model/).
***
:::content-right
||| *Did I miss anything?*        
Send any feedback [<u>here</u>](https://forms.gle/5i6hTJRVkXRohvVF9) 👈
|||
:::
