   
``Last update: Feb 10, 2024``   

*** 
:::content-center
## Lossy Formats
:::

- Common lossy formats are **MP3**, OGG, OPUS, M4A, etc.

- These compress (lose) the original quality. They're built to be faster for transmission & be space-efficient. 

- By getting rid of some data (in this case, quality), they achieve a smaller file size.       
      
***
###### ‎ 
:::content-center
## Lossless Formats
#### *``(ideal for RVC)``*   
:::
- The main ones are **WAV** & **FLAC**. These don't compress the original quality.

- **FLAC** uses an algorithm that compresses the data without losing quality. We recommend it over WAV since it's space-efficient.        
- **WAV** doesn't do any kind of compression. It's purely the full original data. Therefore it has a much bigger file size.

- They're recommended for RVC, as the more quality an audio has, the more accurate results they'll give.

!!! <u>NOTES:</u>
Both formats give the same results & don't have an audible difference.      
Converting a lossy audio to a lossless one won't restore the lost quality.
!!!
***
###### ‎  
:::content-center
## Sample Rate
:::
- Sample rate is a unit that determines the total amount of samples (data) that can fit within one second of an audio.     

- This higher the sample rate, the more information it stores, therefore the higher the quality.

- They are measured in kilohertz.    

- The most common sample rates are **32, 40, 44.1, & 48**.      

###### ‎ 
### Determining Sample Rate
- While training in RVC, you'll have to input the **target sample rate** of your dataset.

- Inputting an incorrect one will affect the final quality.  
   
- To determine the amount, we'll use **Ilaria Audio Analyzer**    

    ***

    #### <u>Instructions:</u>  

    - ##### STEP 1:   
        Enter the HF space <u>[here</u>](https://huggingface.co/spaces/TheStinger/Ilaria_Audio_Analyzer).        
    ***
    - ##### STEP 2:   
        Press the box on the right to input your audio. Or just simply drag the file to it.       
        Then click `Create Spectrogram and Get Info`.  

        <img src="../audioformats-img/1.png" alt="image" width="500" height="auto">‎   
    ***
    - ##### STEP 3:     
        At the right in ``Samples per second`` you'll see the audio's full sample rate.        

        <img src="../audioformats-img/2.png" alt="image" width="400" height="auto">   

    ***

    !!!warning <u>Important Note:</u>   
    If the frequencies don't reach the top of the spectrogram, see at which number peaks & multiply it by <U>**2**</u>.
    !!!

    ###### ‎
    {.list-icon}
    - #### <u>Example:</u>
        <img src="../audioformats-img/3.png" alt="image" width="480" height="auto">‎    
    ‎
    >Here it reached 20 kHz. **Doubling** it gives 40kHz. Therefore the ideal target sample rate would be ``40k`` 

***
###### ‎
:::content-center
## Bitrate & Bit Depth
#### *`Extra info`*
:::

#### :icon-chevron-down: BITRATE:
- The amount of data processed per unit of time. Usually measured in kilobits per second (KBPS).
- Higher bitrate equals a higher quality.
- You can think of it as video resolution (240, 480p, 1080p, etc.).     
###### ‎   
#### :icon-chevron-down: BIT DEPTH:
- Defines the dynamic range of each sample.
- This determines the difference between the quietest & loudest sound of an audio.        
- Basically, higher bit depths represent more accurately the loudness of an audio.        

***
:::content-right
*`Written by Julia & Alex`*    
:::
‎  
:::content-right
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Send Suggestions"](https://forms.gle/3GVR7opzpQrhgRCj9)          
:::
‎  
‎  
***
