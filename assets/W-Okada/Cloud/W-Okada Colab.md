---
icon: chevron-right
order: 4000
---

``Last update: Feb 19, 2025``

***
:::
###### ‎
:::content-center
## Introduction ‎
:::
- This cloud version is hosted in <u>[Google Colab](https://docs.ai-hub.wtf/extra/glossary/#google-colab)</u>, remember that you have a runtime of 4 hours.    

***

###### ‎   
## Installation
###### ‎  
#### 1. <u>Installation Cells</u>
a. Click <u>[here](https://colab.research.google.com/github/deiteris/voice-changer/blob/master-custom/Colab_RealtimeVoiceChanger.ipynb)</u> to access the colab. Then starting from the top run the first cell:

   <img src="../colab-img/colab1.png" alt="image" width="900" height=""> 

a2. When it's done, which may take a couple of minutes, it will output `Done! Proceed with the next steps`.

b. Run the second cell:

   <img src="../colab-img/colab2.png" alt="image" width="600" height=""> 

***

###### ‎   
## Ngrok & Sever Setup
###### ‎  
#### 2. <u>Ngrok Setup</u>
a. Scroll down to the last cell and you should see a section where you put your ngrok token. If you dont have a ngrok acount sign up <u>[here](https://ngrok.com/)</u>.             
     a2. Once you have an acount you can authenticate your ngrok tunnel agent here: https://dashboard.ngrok.com/get-started/your-authtoken   
‎       
b. When you have your ngrok token place it in the text box that says `TOKEN_HERE`

   <img src="../colab-img/colab3.png" alt="image" width="600" height="">  

c. Once the Ngrok token is there run the cell and let it download what it needs then you can click on the ngork link and start using W-Okada.

!!!warning Warning               
There is a monthly limit rate with Ngrok so dont be supprised if training is suddenly interrupted.
!!!

d. (Optional) Directly under where you put your ngrok token there is region selection. You can change it to any of these servers to get less latency:
- us -> United States (Ohio)
- ap -> Asia/Pacific (Singapore)
- au -> Australia (Sydney)
- eu -> Europe (Frankfurt)
- in -> India (Mumbai)
- jp -> Japan (Tokyo)
- sa -> South America (Sao Paulo)

c. From here it's pretty much the same as using local W-Okada.

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/rvc/contributions/)
:::