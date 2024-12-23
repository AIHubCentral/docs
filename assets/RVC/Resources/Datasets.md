---
icon: chevron-right
order: 4000
---

``Last update: Dec 17, 2024``   
***
###### ‎
:::content-center
## Introduction
:::
- ***In the field of AI***, it's the collection of data used to train an AI model. It contains examples of the inputs the model is expected to handle, along with the correct outputs.

- **In the context of RVC**, it's an audio file that's given to RVC, containing the voice the model is going to replicate. It can be either a speaking or singing voice.

- The **quality** & **variety** of the dataset are the biggest determining factors of the final quality of the model. Let's explain.
***
###### ‎
:::content-center
## Length & Variety
:::
- For beginners we recommend sticking with **15 minutes**, or **40+** minutes of diverse audio if you want it natural sounding. Just remember quality over quantity.           

- The dataset can be just a single audio file or it can be split into multiple files to help prevent mode collapses.  

- Variety in your audio is also important because without it RVC lacks the ability to generate diverse audio. 
***
###### ‎
:::content-center
## Quality
#### ``Recommendations for a quality dataset.``  
:::
###### ‎
#### :icon-chevron-down: Range.
- Vocals must be clear, hit low/high notes, & pronounce every vowel correctly.      
‎   
#### :icon-chevron-down: Clean vocals.
- Ensure there very loud background noise ( Quiet background noise is fine ), reverb, overlapping voices, music, distortion, or small silences. You'll learn more in the **Cleaning** section below.   
‎   
#### :icon-chevron-down: Audio quality.
- The higher the audio quality, the better. If possible have it in a <u>[lossless](https://docs.ai-hub.wtf/extra/glossary/#lossless-formats)</u> format like **WAV** or **FLAC**, not a lossy one like MP3.   
‎   
#### :icon-chevron-down: No harsh sibilance/popping.
- Additionally, don't include harsh sibilance (loud "S" & "SH" pronunciation) or popping sounds (loud "P" sound) 
    - Robotic sibilances are due to your dataset being short. You can fix this by making your dataset larger
    - Harsh sibilances are due to your dataset having harsh sibilants. You can fix this by de-essing or making your dataset larger
‎  
#### :icon-chevron-down: No Audio Damage.
- The most inportant part of a clean dataset, if your audio is damaged RVC will struggle with it causing it to overall sound worse because RVC will create synthetic data and try to learn from it, so make sure your audio isn't damged.  
‎   
***
###### ‎
:::content-center
## Cleaning
:::
- First, clean the undesired noises explained before using a <u>[vocal isolation](https://docs.ai-hub.wtf/rvc/resources/vocal-isolation/)</u> software.     
*** 

#### Step 1: Truncating Silence.   

- Go to Effects -> Special -> Truncate Silence     
- Use the following values:         
    ‎  
    <img src="../datasets-img/trunc.png" alt="image" width="420" height="auto">    
    ***
    ‎
    #### Step 2: Audio Normalization.    
    - Go go to Effects -> Volume and Compression -> Loudness Normalization
    - Use these values:     
‎       
<img src="../datasets-img/norm.png" alt="image" width="420" height="auto"> 

> LUFS are used over db because hifigan needs perceptual quality and db doesnt offer that.
***
#### Step 3: Export.
- On the upper right corner go to File and click ``Export Audio``.       
    ‎   
    <img src="../datasets-img/4.png" alt="image" width="370" height="auto"> 
    ‎       
    ‎              

    - And finally, introduce these values:  

        - **Format**: ``FLAC``    
        - **Bit depth**: ``24 bit``
        - **Level**: ``8``       

        ###### ‎    

        <img src="../datasets-img/5.png" alt="image" width="650" height="auto">

***
#### Step 4: Slice Audio (Optional)
1. Download this: [!file](../datasets-img/split_audio.py)
2. Then place it in Applio's root folder. Then type `cmd` into the top bar where it shows your location.

<img src="../datasets-img/cmd.png" alt="image" width="420" height="auto">
‎  

3. Then type this into the cmd line `python split_audio.py wavfilelocationhere exportfolderhere sampleratehere 3 0.3`.
    - for example it would look something like this `python split_audio.py C:\Users\dawnm\Downloads\dataset.wav C:\Users\dawnm\Desktop\split\ 32000 3 0.3`.

> If you get an error saying something is missing simply type `pip install librosa numpy scipy tqdm`. 

4. Then once it's done go into the folder where you told it to export all of the slices to, then copy / cut all of the files there are place them into your dataset folder. 





***

###### ‎
:::content-center
## Recording Tips
#### `Advice for recording a dataset.`
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

###### ‎  
:::content-center
## Sample Rate
:::
- This is a unit in that defines the total amount of **samples** (data) that can **fit** within **1 second** of an audio. They are measured in kilohertz (kHz).

- The most common sample rates are **32, 40, 44.1, & 48**. The **higher** the sample rate, the more information it stores, therefore the higher the **quality**.  

- While training in RVC, you'll have to set the **target sample rate** as your dataset's. This value affects the final quality.  
   
- ##### A simple way to determine it is with <ins>Spek</ins>:  

    - ##### STEP 1:   
        Download and install Spek <u>[here</u>](https://www.spek.cc/p/download).        
    ***
    - ##### STEP 2:   
        Open spek and just drag & drop audio into it. 

        <img src="../audioformats-img/3.png" alt="image" width="500" height="auto">‎   

    !!!danger <u>WARNING:</u>   
    If the frequencies don't reach the top of the spectrogram, see at which number peaks & multiply it by <U>**2**</u>. Here it reached 20 kHz. **Doubling** it gives 40kHz. Therefore the ideal target sample rate would be ``40k``
    !!!

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/contributions/)
:::
