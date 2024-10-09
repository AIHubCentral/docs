---
icon: chevron-right
order: 1000
---

# GPT-SoVITS

`Last update: Mar 8, 2024`

***
###### ‎
:::content-center
## Introduction :icon-book:

[`See original guide`](https://www.yuque.com/baicaigongchang1145haoyuangong/ib3g1e)

:::

- GPT-SoVITS is an open-source repository focused on TTS & cross-language inference, with a Colab port coming soon. Credits to <u>[RVC-Boss](https://space.bilibili.com/5760446)</u>.		
		
- Currently it only supports Chinese, English & Japanese. More languages are coming soon.		
	
- You'll require great specs & a NVIDIA GPU with >=6G VRAM to run it smoothly. Otherwise, use the Colab.

- This guide is a translation of the original one with a few tweaks, made by Delik. [ Discord: @delik - Wechat: Dellikk ]
‎
***
###### ‎
:::content-center
## Installation :icon-download:

:::

###### ‎
#### 1. Download prezip
- Download the prezip of the **latest version** <u>[here](https://huggingface.co/datasets/Delik/gptsovits_i18nfix/tree/main)</u>.

***
###### ‎
#### 2. Extract

- Unzip the folder. It's advisable to use <u>[7-ZIP](https://www.7-zip.org)</u> to do so.
***
###### ‎
#### 3. Launch
- Open the folder & run ``go-web.bat`` to open WebUI.

***
###### ‎
:::content-center
## Training :icon-rocket:
:::
###### ‎
#### 1. Prepare dataset

- The dataset should be between 1 - 30 minutes. But you must prioritize **quality** over quantity.

- For the best results, ensure the audio is properly **cleaned**, free of undesired noises & distortions.

- GPT-So-VITS is made for **TTS only**, so it's also best to remove any singing/muffly voice parts.

- #### <u>[Learn how to clean datasets](https://docs.ai-hub.wtf/rvc/resources/datasets/)</u>.
***
###### ‎
#### 2. Audio Slicer
![](https://i.postimg.cc/7Lnnt3gN/screenshot-2.png)

a. Copy the path file of your dataset & paste it in the **Audio slicer input** bar.

b. Create a new folder somewhere. Copy its path folder & paste in **Audio slicer output**. This is where the outputs are getting stored.

c. Adjust the parameters **if needed**.

d. Finally, click **Start Audio Slicer** to complete this step.
***
###### ‎
#### 3. ASR
![](https://i.postimg.cc/8cfrYztT/screenshot-2.png)
a. The **Input folder path** should be the same as **Audio slicer output**. Jst copy the path & paste it inside the bar.

b. If the dataset is in English/Japanese, use ``Faster-Whisper large v3``.

	If it's in Chinese, use ``达摩ASR``.	

c. Then click ``Start batch ASR``.

	If you run GPT-SoVITS for the first time, you might need to wait for a few minutes for it to download the ASR model you select.		

d. Finally, locate the ``.list`` file & copy the path. It will be in **output/asr_opt**, if you didn't change the folder for **Output folder path**.

***
###### ‎
#### 4. Text Labelling (optional)
![](https://i.postimg.cc/DZ1WGDWf/screenshot-2.png)
a. Paste the ``.list`` file path into **.list annotation file path**.

b. Tick **Open labelling WebUI** to open Text Labelling WebUI. A new tab will open.

![](https://i.postimg.cc/mrG9PGjD/screenshot-2.png)

- Listen to each clip & edit the text if it's not transcribed properly.

- The functions are self-explanatory. Use **next index** & **previous index** to check the next/previous page.

- If you make changes, remember to **save file** & **submit text**.

***

###### ‎
#### 5. Formatting

a. Click **1-GPT-SOVITS-TTS** & **1A-Dataset formatting** to enter the training page.
![](https://i.postimg.cc/YqGYtLsN/screenshot-2.png)

b. Input the name of your model in **Experiment/model name**, & the ``.list`` file path to **Text labelling file**.

c. Scroll down to the end & start **One-click formatting** to begin formatting.	
***

###### ‎
#### 6. SoVITS Training
a. Scroll up then click **1B-Fine-tuned training**.   
‎   
![](https://i.postimg.cc/0Q1SrsVy/screenshot-2.png)‎		
###### ‎      

- ##### Recommended settings for SoVITS training:


Batch size
:   ``2`` | Use ``1`` if the GPU has 6GB VRAM.

Total epochs
:   ``8``

Text model learning rate weighting
:   <=``0.4``

Save frequency
:   ``4``    

‎
:   ‎

b. After that, click **Start SoVITS training**

***
###### ‎  
#### 7. GPT Training
- ##### Recommended settings for GPT training:

Batch size
:   2 (1 if your  gpu has 6G vram)

Total epochs
:   10

Save frequency
:   5

DPO training
:   disabled (explained later)

‎
:   ‎

After that, click **Start GPT training**

!!!warning You can't train both simultaneously unless you have 2 or more GPUs.
!!!

***
###### ‎     
#### :icon-chevron-down: DPO training (optional)
- DPO training greatly improves the performance (not audio quality) & stability of the model.

- It can infer more text at once without slicing & it's less prone to errors (like repeating/skipping words) when inferring.

- ##### For this, you'll requiere:
	- A GPU with 12G VRAM or more.
	- A **very high quality** dataset (you need to do text labelling) to enable this.
	- Using a batch size of 1. Keep the other settings same as above.
	- Otherwise, this will worsen the model.     
***
###### ‎     
:::content-center
## Inference :icon-unmute:
:::

![](https://i.postimg.cc/6qdPzLkw/screenshot-2.png)
a. Go to the **1C-inference** tab.

b. Press **refreshing model paths** & select your models from the dropdowns respectively.

c. Tick **Open TTS inference WEBUI**.
![](https://i.postimg.cc/Xvr27Gfw/screenshot-2.png)

d. Upload a clip for reference audio (**must be 3-10 seconds**). Then fill-in the **Text for reference audio**, which is what does the character say in the audio. Choose the language on the right.

	- The reference audio is very important as it determines the speed & emotion of the output. Try different ones to polish your output.

	- You can reopen the text proofreading tool to download the reference audio, and copy & paste the text for reference audio.

	- Hover above the "duration" to adjust the length of the reference audio, & hover above "it" to delete the current reference audio.

	- No reference text mode exists, but it's not advisable to use it. It affects the quality a lot.   
‎   
e. Fill the **Inference text** & set the **Inference language**, then click ``Start inference``.

	- If the text is too long choose the options in **How to slice the sentence**.

	- If you did not get your desired output, you can infer it **again** or **change reference audio** and/or **adjust GPT parameters**.


***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/rvc/#contributions)
:::