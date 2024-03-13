---
icon: chevron-right
order: 3000
---

``Last update: Mar 8, 2024``
***
:::content-center

#### *List of smaller keywords.* 
:::
‎
:   ‎
:::
### :icon-chevron-down:Backing vocals
- Vocal lines that contribute to the sound of the lead vocals in a song.      

***
###### ‎   
### :icon-chevron-down:Bit depth
- In the field of digital audio, it defines the dynamic range of each sample.

- This determines the difference between the quietest & loudest sound. 

- Basically, higher bit depths represent more accurately the loudness of an audio.     

***
###### ‎   
### :icon-chevron-down:Bitrate
- The amount of data processed per certain unit of time, usually in kilobits per second (KBPS).

- Higher bitrate equals a higher quality.

- You can think of it as video resolution (240, 480, 1080, etc.).     
   
***
###### ‎
### :icon-chevron-down:Checkpoints

- In RVC, these are files of a model that generate over the course of training, that can be very useful.        
‎  
- The rate at which they're saved is determined by the **save frequency** value (or save rate or similar names). **For newbies, it's recommended use a value of `15`.**      
‎    
- **They are divided by two types:**  
‎  
    - <u>**Weights:**</u>    
        - These are actual models.
        - They're organized with this format: **modelname_epoch_step.pth**
        - Example: `Tyler_e60_s120.pth`    
‎  
    - <u>**G and D:**</u>
        - Named **G_** and **D_**, followed by the step number & **.pth**.
        - Example: `G_70.pth` and `D_70.pth` 
        - These allow you to resume training, if G and D's numbers match.

***
###### ‎
### :icon-chevron-down:Cloud-based
- Any software or application that's stored, managed, and available through the provider's virtual servers, and is accessed through a web browser.        

- The opposite of <u>[local running</u>](https://docs.aihub.wtf/extra/glossary/#local-running).       

***

###### ‎       
### :icon-chevron-down:CUDA
- A technology developed by NVIDIA, that uses the power of graphics cards to perform calculations that require great processing power.    
- It's especially useful for AI tools, such as RVC and UVR, which greatly optimizes the process.       

- CUDA is downloaded automatically as a part of the NVIDIA driver.            
***
###### ‎       
### :icon-chevron-down:DAW
- It stands for **Digital Audio Workstation**, and it's any software used for making and mixing music.    

- For **basic** audio editing, we recommend <u>[Audacity</u>](https://www.audacityteam.org/).     

- For **professional** mixing, <u>[FL Studio</u>](https://www.image-line.com/fl-studio-download/).        
***
###### ‎       
### :icon-chevron-down:Fine-tuning
- Further improving an AI model, training it with a another dataset.

***
###### ‎       
### :icon-chevron-down:Fork
- It's a copy of a main GitHub project. It aims to make a different version of the project with improvements, changes & new features.       
***
###### ‎
### :icon-chevron-down:Google Colab
- Google Colaboratory is a product of Google that allows anybody to write & execute arbitrary python code through websites.       

- It's free version is slower & with a usage time of their GPUs of around **3 hours a day**. Once you exhaust it, you'll have to wait 12 - 24 hours.

- Learn how to bypass their limitations <u>[here](https://rentry.org/colab_workarounds)</u>.
***
###### ‎       
### :icon-chevron-down:GPU
- It stands for Graphics Processing Unit. It's designed to rapidly manipulate and alter memory to accelerate creation of images.    

- In AI training, is used for quick parallel independent computations, which increases the speed substantially.     

- Basically the speed at which RVC/UVR will work will depend on how good your GPU is.       
               
***
###### ‎       
### :icon-chevron-down:Inference
- In the context of AI, it's using an AI model to complete any task. 

- For this, using the GPU is more convenient as it's faster. Though normally you can still use CPU, which takes longer.

- For example, in RVC is when a voice model is used to transform an audio, to make it sound like the model.       
***

###### ‎       
### :icon-chevron-down:Local running
- Running locally is a process that involves running apps in your own machine, using its resources.       

- The opposite of <u>[cloud-based](https://docs.aihub.wtf/extra/glossary/#cloud-based)</u>.    

***

###### ‎ 
### :icon-chevron-down:Lossless Formats
- Audio formats that **don't compress** (lose) the original quality.        
‎       
- They're recommended for RVC, as the more quality an audio has, the more accurate results they'll offer.       
‎         
- The main ones are **WAV & FLAC**:     
    ‎   
    - **FLAC:**   
        - Its algorithm compresses the data without losing quality. 
        - It's recommended over WAV since it's space-efficient.          
‎   
    - **WAV:**
        - Doesn't do any kind of compression. It's purely the original data.
        - Therefore it has a much bigger file size.
        - It's more accurate to describe it as an *uncompressed* format
        
!!!
Both formats give the same results & don't have an audible difference.      
Converting a lossy audio to a lossless one won't restore the lost quality.
!!!
***
###### ‎ 
### :icon-chevron-down:Lossy Formats

- Audio formats that **compress** (lose) the original quality. They're built to be space-efficient.

- So by getting rid of some data (in this case, quality), they achieve a smaller file size.       

- Common lossy formats are **MP3**, OGG, OPUS, M4A, etc.

***
###### ‎       
### :icon-chevron-down:Model training
- In the field of AI, is the process where an AI model is fed with its dataset & learns from it.
***
###### ‎       
### :icon-chevron-down:Specs
- It refers to a computer's specifications. Hardware like <u>[GPU</u>](https://docs.aihub.wtf/extra/glossary/#gpu), CPU, RAM, etc.     

- The performance of the hardware of a computer directly correlates to the performance of all its software.

***
###### ‎       
### :icon-chevron-down:0 Shot Training
- Doing <u>[inference](https://docs.aihub.wtf/rvc/extra/glossary/#inference)</u> on an AI model without explicitly training on it. 

- It's faster but with less quality, and you won't be able to save the model.

- For example, in TTS you do inference by cloning a voice with an audio, a data it hasn't seen before.

- Different from making a dataset & doing the long training process, based on lots of criteria such as <u>[epochs](https://docs.aihub.wtf/rvc/resources/epochs--tensorboard/)</u>. 

- In some cases you can do it on GPU, some in CPU.

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.wtf/rvc/#contributions)
:::