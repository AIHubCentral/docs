---
icon: chevron-right
order: 3000
visibility: private
---
``Last update: July 30, 2025`` 
***

## </u>Introduction</u>
***

- This is a fork of mainline RVC running on Hugging Face Spaces, it’s called this way because it runs on Hugging Face’s ZeroGPU, which currently is an A100 GPU.

- Here is the link to the space <u>[Ilaria RVC Zero](https://huggingface.co/spaces/TheStinger/Ilaria_RVC)</u>.

!!!danger Currently broken for uknown issues
For unknwon related ZeroGPU issues, the space is broken. We suggest alternatives till it's fixed or we have updates on the situation.
!!!

!!!danger
This space is only for inference which means you can not train a model here.
!!!
***

## </u>Model Downloader</u>
***

a. Go to any RVC Hugging Face Models and get the Download link by going to the “Files and versions” tab, then right click the Download icon next to the .zip file, and click copy address link, like in the image

   <img src="../zero-img/1.png" alt="image" width="1000" height="auto">

‎
b. Then go to the “Model Loader” tab in the space and click on “Model Downloader”, paste the link into the Model URL give the model a name and click “download model”.

   <img src="../zero-img/2.png" alt="image" width="1000" height="auto">

***

## </u>Inference </u>

a. After you finally uploaded the model, go to the “Inference” tab, and upload the audio which vocals you want to convert to the model’s voice. Click “Refresh Models” and in the “Model” dropdown menu choose yours then click “Convert”.

   <img src="../zero-img/3.png" alt="image" width="800" height="auto">

Then after you get your output, just click on the Download Icon at the top right of the audio file.

==- Inference Settings
Settings (Inference)
While converting, you might have issues of the output pitch may not be the same as the model one, but that’s a thing you can easily fix with the settings!

- Go to the “Inference” tab, click on “Settings”, i will explain you the important settings that you may wanna change:
- Pitch level: if the output pitch seems different than the model’s pitch, you need to play around with this: 
     - Lower value = male, deeper.
     - Higher value = female, higher voice tone.
- Index influence: How much accent (the one from the .index file) is applied:
     - Lower value = Less accent of the model’s voice, but helps to reduce artifacting (noises).
     - Higher value = More accent of the model’s voice, but could have artifacting (depends on the model’s dataset, as the index file depends on it).

For the rest of the settings, you don’t need to change them, leave them as they are.


===


***

## </u>Ilaria TTS</u>
***

a. Go to the “Inference” tab, click on “Ilaria TTS” write all the text you want in “Text”, choose an Edge TTS Model in “Language and Model”, it’s suggested to use one that has the same language and gender of the RVC mode.

b Click on “Speak”, it will generate a TTS audio with the original Edge TTS Model, and then automatically using it as an input

   <img src="../zero-img/4.png" alt="image" width="1000" height="auto">

***

==- Errors
#### GPU task aborted:
ZeroGPU HuggingFace Spaces have a max inference time duration, it’s the time it takes to do an Inference (use the model, not the time of your audio file itself), on default it’s around 1 minute which is what Ilaria RVC uses. You need to retry with a shorter audio, you could also split your audio.
***
#### You have exceeded your GPU quota ( NUMBER s left vs. 60s requested). Sign-up on Hugging Face to get more quotas or retry in Hour:Minutes:Seconds
ZeroGPU HuggingFace Spaces have a quota per account, if you aren’t signed in you will get less quota so it’s better to login for more quota. You could get the ‘Sign-up’ part even if you are logged in. The ZeroGPU Quota can’t be seen but it isn’t unlimited. You can either:
- Login so you get more quota
- Wait
- Pay to be an HuggingFace PRO Member to get X5 times more quota

You can find your ZeroGPU quota <u>[here](https://huggingface.co/settings/billing)</u>
***
#### No GPU is currently available for you after 60 seconds:
As all ZeroGPU Spaces share this hardware, there might be times where ZeroGPU is busy, if you ever go through this error, you just need to wait a bit and retry.
***
#### The file is too large. You can only download files up to 500 MB in size:
Ilaria RVC Zero got a limit for the Model Upload Size, if you run into this either use another model.

===

***

###### ‎   ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
