---
icon: chevron-right
order: 6000
---

``Last update: Mar 8, 2024``
‎ 
***  
###### ‎ 
:::content-center
## Introduction :icon-book:
:::
- Ilaria RVC is a port of EasyGUI (<u>[Mangio</u>](https://aihubdocs.github.io/en/rvc/local/mangio/)) to <u>[Google Colab</u>](https://aihubdocs.github.io/en/extra/glossary/#google-colab). Made by <u>[Ilaria](https://ko-fi.com/ilariaowo)</u>.     

- Works for <u>[inferencing](https://aihubdocs.github.io/en/extra/glossary/#inference)</u> only, has a pretty UI, huge speed, & the great tools that Mangio has (such as <u>[Mangio-Crepe](https://aihubdocs.github.io/en/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u> algorithm).

- And for this it's considered one of the best alternatives for doing inference through the cloud.       
‎               
#### Pros & Cons :icon-tasklist:
==- ***Learn more***
!!! *The pros & cons are subjective to your necessities.*        
!!!
||| **✔️ PROS:**  
- Model download through links.    
- Two extra TTS tools.     
- Great UI.        
- Has Mangio-Crepe.      
- Doesn't take too long to load.  
- Very quick.  
||| ❌ **CONS**  
- Usage limit for free users.     
- Takes 3 minutes to set up.
|||
===

***
###### ‎ 
:::content-center
## Inference :icon-unmute:
#### [`See video tutorial`](https://www.youtube.com/watch?v=wh4cLMLLkj0)
!!!info
If any issues arises, read the <u>[Troubleshooting</u>](https://aihubdocs.github.io/en/rvc/cloud/ilaria-rvc/#troubleshooting-) chapter.
!!!
:::

###### ‎ 
#### 1. <u>Enter the space.</u>
a. First log in to your Google account <u>[here</u>](https://accounts.google.com/). 

b. Then access the <u>[Colab space</u>](https://colab.research.google.com/drive/16LkwvFZeudTpUOsE_6bMjOq2qkxFo8Hr?usp=sharing).
***
###### ‎ 
#### 2. <u>Set up space.</u>
- Execute the `Install Ilaria-RVC` cell, by pressing the play button, then `Run anyway`.  

- Ilaria RVC will begin to set up.    

    <img src="../ilarvc-img/a.png" alt="image" width="250" height="auto">‎ ‎ ‎<img src="../ilarvc-img/b.png" alt="image" width="320" height="auto">‎       
‎   
- It'll finish when the cell says `Done Cloning Repo`.

    <img src="../ilarvc-img/d.png" alt="image" width="300" height="auto">‎         
‎   
!!!success
If red text appears showing errors, ignore it, it's normal.
!!!
***
###### ‎ 
#### 3. <u>Open Gradio.</u> 
a. Now execute the `Start` cell below.        

b. After a bit it's going to show you two links. Open the **gradio.live** one in a separate tab.        

<img src="../ilarvc-img/e.png" alt="image" width="540" height="auto">       

‎       
!!!warning Don't close the <u>Colab</u> tab until you're done using Ilaria RVC.      
Otherwise you'll have to start again.
!!!
***
###### ‎ 
#### 4. <u>Download voice model.</u>
{.list-icon}
- <img src="../ilarvc-img/3.png" alt="image" width="450" height="auto">
a. In the Gradio, go to the ``Download Voice Models`` tab.     

b. Paste the <u>[link of the model](https://aihubdocs.github.io/en/essentials/voice-models/#how-to-search-voice-models)</u> in the `Hugging Face Link` bar. It must be a public link from either **Hugging Face**/**Google Drive**.

c. In `Name of the model`, insert a name for it. Don't include spaces/special characters.

d. Then click `Download`.        


***
###### ‎ 
#### 5. <u>Select model.</u>  
a. Return to the `Inference` tab & click the upper pink `Refresh` button.
b. Unfold the `Choose the model` dropdown & select your model.

    <img src="../ilarvc-img/4.png" alt="image" width="450" height="auto">
***
###### ‎ 
#### 6. <u>Select your audio.</u>  
- Below it, in `Drag your audio file and click refresh`, click it to load your audio manually. Or just drag the file into it.         

    <img src="../ilarvc-img/5.png" alt="image" width="450" height="auto"> 

***
###### ‎ 
#### 7. <u>Adjust settings.</u> (optional)    
- If you wish, you can modify the <u>[inference settings</u>](https://aihubdocs.github.io/en/rvc/resources/inference-settings/#pitch-extraction-algorithm) in `Index Settings` & `Advanced Options` for better results.   
Tap them to unfold.      

    <img src="../ilarvc-img/6.png" alt="image" width="500" height="auto"> ‎                  
‎
***
###### ‎ 
#### 8. <u>Convert.</u>     
- Click the upper `Convert` button & wait for the inference to finish.

    <img src="../ilarvc-img/7.png" alt="image" width="250" height="auto">   

***
###### ‎ 
#### 9. <u>Download output.</u>        
- Once it's done processing, there will be a playable audio in the `Final Result!` box.  

- Tap the three buttons on the right of the audio and then `Download`.         

    <img src="../ilarvc-img/8.png" alt="image" width="" height="auto">‎     
‎       

***
:::content-center
[!button variant="danger" corners="pill" icon="heart-fill" iconAlign="right" text="Support Ilaria"](https://ko-fi.com/ilariaowo)
:::
‎
:   ‎

:::content-center
## TTS :icon-megaphone:
#### *`and with an RVC model`*
###### ‎
:::
1. First access the Gradio. If you don't know how, follow the first three steps of the <u>[previous chapter](https://aihubdocs.github.io/en/rvc/cloud/ilaria-rvc/#inference)</u>.
***
2. Go to the `IlariaTTS` section. 

    <img src="../ilatts-img/1.png" alt="image" width="450" height="auto">‎     

    If you want, you can use the other `ElevenLabs / Google TTS`.
***
3. In `Voice` pick a voice of the gender, language & accent that you wish. Under it, insert the text.      

    If you're going to use an RVC model, pick one that sounds similar to it.
***
4. Press `Speak`. The TTS will begin to process.
***
5. Once it's done processing, there will be a playable audio in the `Final Result!` box.        
At the right press the three dots & then `Download`.         

    <img src="../ilarvc-img/8.png" alt="image" width="" height="auto">‎     
     
***
6. To use an RVC model, simply upload the output to Ilaria RVC & convert it using your model. (Optional)        
    If you don't know, learn <u>[here](https://aihubdocs.github.io/en/rvc/cloud/ilaria-rvc/#inference)</u>.

***
###### ‎
###### ‎
:::content-center
## Troubleshooting :icon-tools:
:::
###### ‎
==- *I get a red `Error` message.* 
###### ‎ 
- It's normal. Try repeating your action.          
‎       
- If it persists, reload the Gradio page.       
‎       
- Ensure your audio is selected in the `Choose the audio file`. If it's not in the list, click `Refresh` on its right & select it.      
‎       
- If it's still persisting, restart the Colab space:        
    - Go to the Colab space and press the downward arrow ( :icon-triangle-down: ) at the top. 
    - Click `Disconnect and delete all data`.
    - Reload the page and load RVC again.
===

==- *My model doesn't have a link from HF/GD.*
###### ‎
- You'll have to create the link yourself. Learn how <u>[here</u>](https://aihubdocs.github.io/en/essentials/voice-models/#uploading-to-hugging-face).
===

==- *I can't download my model.* 
###### ‎     
- This could be due to a few reasons:     

    1. **Link is private:** 
        - If it's from GD, ensure the `General access` is set as `Anyone with the link`.
        - If it's from HF, ensure the repo is set as `Public`. Learn more <u><u>[here</u>](https://aihubdocs.github.io/en/essentials/voice-models/#uploading-to-hugging-face)</u>.            
        ‎   
    2. **Invalid HF link:**
        - The HF link must contain the word "**.zip**".
        - If it contains the word `blob`, replace it for `resolve` & paste it.     
    ‎       
    3. **Incorrect files:**
        - The model must be zipped in a **.ZIP** file. Not .RAR or .7ZIP.
        - It must contain its correct .PTH & .INDEX files. Learn more <u>[here](https://aihubdocs.github.io/en/essentials/voice-models/#voice-model-files)</u>.
===

==- *The voice glitches out.*
###### ‎
- This is an anomaly called "**artifacting**". Learn how to fix it <u><u>[here</u>](https://aihubdocs.github.io/en/rvc/resources/artifacting/)</u>.
===

==- *Cannot connect to GPU backend.*
###### ‎   
- You have exhausted the <u>[GPU runtime](http://aihubdocs.github.io/en/extra/glossary/#google-colab)</u> of Colab.
===

==- *I couldn't find my answer.*
###### ‎   
- Report your issue <u>[here](http://aihubdocs.github.io/en/#contributions)</u>.
===
***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](http://aihubdocs.github.io/en/#contributions)
:::