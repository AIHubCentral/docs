``Last update: Jan 9, 2024``   
***
###### ‎
:::content-center
## Introduction
:::
- ***In the field of AI***, it's the collection of data used to train an AI model. It contains examples of the inputs the model is expected to handle, along with the correct outputs.

- **In the context of RVC**, it's an audio file that's given to RVC, containing the voice the model is going to replicate. It can be either a speaking or singing voice.

- The **quality** & **length** of the dataset are the biggest determining factors of the final quality of the model. Let's explain.
***
###### ‎
:::content-center
## Length
:::
- For beginners we recommend sticking with **10 minutes**, or **20** if you want it very high quality.        

- If you wish to go for more, keep in mind, usually anything further than 40 minutes isn't necessary.      

- With modern versions of RVC, the dataset can be just a single audio file, no need to split it in multiple files.  
***
###### ‎
:::content-center
## Quality
#### ``Recommendations & requirements for a quality dataset:``  
:::
###### ‎
#### :icon-chevron-down: Range.
- Vocals must be clear, hit low/high notes, & pronounce every vowel correctly.

#### :icon-chevron-down: Clean vocals.
- Ensure there isn't background noise, reverb, overlapping voices, music, distortion, or small silences. You'll learn more in the **Cleaning Datasets** section below.

#### :icon-chevron-down: Audio quality.
- The higher the audio quality, the better. If possible have it in a <u>[lossless](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/)</u> format like **WAV** or **FLAC**, not a lossy one like MP3.

#### :icon-chevron-down: No sibilance/popping.
- Additionally, don't include harsh sibilance (loud "S" & "SH" pronunciation) or popping sounds (loud "P" sound).
***
###### ‎
:::content-center
## Cleaning Datasets
:::
1. First, clean the undesired noises explained before using a <u>[vocal isolation](https://aihubdocs.github.io/en/vocal-isolation--datasets/vocal-isolation/)</u> software.     
***   
2. Then, to remove silences, distortion & minimize (even more) noise, we'll use tools from <u>[Audacity</u>](https://www.audacityteam.org/download/). A free, simple & very light-weighted <u>[DAW](https://aihubdocs.github.io/en/other/glossary/#daw)</u>.            
    ‎     

    {.list-icon}  
    #### Paso 1: Noise Gate.   
    - First input your dataset by dragging the audio file into the app.     

    - Press CTRL + A to select the whole audio.       

    - Navigate to the ``Effect`` menu at the top, go to `Noise removal and Repair` and select ``Noise Gate``.

    - Use these values & apply the changes:      
    ‎       
 <img src="../datasets-img/1.png" alt="image" width="420" height="auto">   
    ***
    ###### ‎
    #### Step 2: Truncating Silence.    

    - Go to Effects -> Special -> Truncate Silence     
    - Use the following values:         
    ‎  
    <img src="../datasets-img/6.png" alt="image" width="420" height="auto">    
    ***
    ‎
    #### Step 3: Audio Normalization.    
    - Go go to Effects -> Volume and Compression -> Normalization
    - Use these values:     
‎       
<img src="../datasets-img/3.png" alt="image" width="420" height="auto">  

    ‎
    #### Step 4: Export.
    - On the upper right corner go to File and click ``Export Audio``.       
    ‎   
    <img src="../datasets-img/4.png" alt="image" width="370" height="auto"> 
    ‎       
    ‎       
    ‎       
- And finally, introduce these values:  
    - **Format**: ``FLAC``    
    - **Bit depth**: ``24 bit`
    - **Level**: ``8``         
    ‎       
<img src="../datasets-img/5.png" alt="image" width="650" height="auto">

***
###### ‎
:::content-center
## Tips for Recording Datasets
#### `Advice for making a model of yourself`
:::
###### ‎    
- Record while reading anything, like a book.
- Warm up your voice. Clear your throat & read out loud before starting.
- Make it natural, not robotic. 
- Pronounce every vowel correctly.
- Hit low & high notes. Don't have to exaggerate it if you don't need to.
- Get close to the mic, not too much to avoid sibilance/popping
- Avoid background noise. Close windows, door, turn off the computer, unplug fridge, etc.
- Don't be in a room with reverb. It's best if it's in a small-to-medium sized room with lots of stuff in it, specially soft like beds, couches, pillows, etc.
- Have a good posture, it's good for breath support.
- Have a drink at your side to not dehydrate.
***
:::content-right
*``Written by Julia, Faze Masta & Litsa``* 
:::
‎     
:::content-right
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Send Suggestions"](https://forms.gle/3GVR7opzpQrhgRCj9)
:::
‎     
‎      
***