---
icon: chevron-right
order: 4000
---

``Last update: March 24, 2026``
***
:::content-center
## Introduction
:::
- This is a [cloud-based](https://docs.aihub.gg/extra/glossary/#cloud-based) alternative to run [AICoverMaker](https://docs.aihub.gg/rvc/local/aicovermaker/), Applio RVC Fork, only for people who don't have a good PC GPU, with a Web User Interface.


***
:::content-center
## Choose your Cloud Service
:::
Set up the program using your preferred cloud service guide. Once configured, use the Public Tunnel URL to open the interface and continue with the next steps


<style>
  /* Local styling that only affects this page */
  .cloud-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    justify-content: center;
    margin: 2rem 0;
  }
  .cloud-card {
    flex: 1 1 220px;       /* Allows cards to shrink/grow, base width 220px */
    max-width: 280px;      /* Prevents cards from getting comically wide */
    padding: 1.5rem;
    border: 1px solid rgba(150, 150, 150, 0.2); /* Subtle border for light/dark mode */
    border-radius: 12px;
    text-align: center;
    text-decoration: none !important;
    color: inherit !important;
    background: rgba(128, 128, 128, 0.03); /* Barely visible background */
    transition: all 0.2s ease;
  }
  .cloud-card:hover {
    transform: translateY(-4px);
    border-color: rgba(150, 150, 150, 0.6);
    background: rgba(128, 128, 128, 0.08);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
  }
  .cloud-card img {
    width: 54px;
    height: 54px;
    margin-bottom: 1rem;
    object-fit: contain;
  }
  .cloud-card h3 {
    margin: 0 0 0.5rem 0 !important;
    font-size: 1.25rem;
    border-bottom: none !important; /* Overrides Retype's default header lines */
  }
  .cloud-card p {
    font-size: 0.9rem;
    opacity: 0.7; /* Makes description text slightly muted */
    margin: 0;
    line-height: 1.4;
  }
</style>

<div class="cloud-grid">
    <!-- Google Colab -->
    <a href="#google-colab" class="cloud-card">
        <img src="/img/google-colaboratory-logo.svg" alt="Colab">
        <h3>Google Colab</h3>
        <p>Reliable performance and full control for power users.</p>
    </a>
    <!-- Kaggle -->
    <a href="#kaggle" class="cloud-card">
        <img src="/img/kaggle-icon.svg" alt="Kaggle">
        <h3>Kaggle</h3>
        <p>Generous free GPU quotas. Great alternative if Colab is limited.</p>
    </a>
</div>

<br><br>


***
:::content-center
### Google Colab

!!!danger Google Colab Service
**Check the [Google Colab Glossary](https://docs.aihub.gg/extra/glossary/#google-colab) for more info on Free Tier, Limits, Verification, Pricing and other things.**
!!!

:::
#### <u>Installation & Setup</u> :icon-book:

**1.** Go to the [AICoverMaker Colab](https://colab.research.google.com/github/Eddycrack864/RVC-AI-Cover-Maker-UI/blob/main/assets/RVCAICoverMakerUI.ipynb) and run the first cell. 

   <img src="../aicovermaker-img/1.png" alt="image" width="200" height="">

‎ 

!!!
Installation may take a couple of minutes, be patient.
!!! 

**2.** Next go to the second cell and put your ngrok token in the text box and run it. If you dont have a ngrok acount sign up [here](https://ngrok.com/) and you can authenticate your ngrok tunnel agent [here](https://dashboard.ngrok.com/get-started/your-authtoken). 

   <img src="../aicovermaker-img/2.png" alt="image" width="400" height="">

‎
!!!warning Warning               
There is a monthly limit rate with Ngrok so dont be supprised if training is suddenly interrupted.
!!!

**2a.** You can choose not to use Ngrok if you desire to by running the third cell.

   <img src="../aicovermaker-img/3.png" alt="image" width="400" height="">

‎

**3.** Once you've run either the cell with or without ngrok a link under the cell will apear, click it and it will take you the WebUI.


***
:::content-center
### Kaggle
:::

!!!danger Kaggle Service
**Check the [Kaggle Glossary](https://docs.aihub.gg/extra/glossary/#kaggle) for more info on Free Tier, Limits, Verification, Pricing and other things.**
!!!

#### <u>Installation & Setup</u> :icon-book:

**1.** Go to the [AICoverMaker Kaggle notebook](https://www.kaggle.com/code/eddycrack864/rvc-ai-cover-maker-ui) and click `Copy & Edit` on the top right. 

   <img src="../aicovermaker-img/8.png" alt="image" width="900" height="">

‎ 

**2.** Once you're in the notebook run the first installation cell. Once it's done it will output `Requirements installed`.

   <img src="../aicovermaker-img/9.png" alt="image" width="800" height="">

‎

!!!
Installation may take a couple of minutes, be patient.
!!!

**3.** Next go to the second cell and put your Ngrok token in the `TOKEN HERE` spot and run it. If you dont have a Ngrok acount sign up [here](https://ngrok.com/) and you can authenticate your ngrok tunnel agent [here](https://dashboard.ngrok.com/get-started/your-authtoken). 

   <img src="../aicovermaker-img/10.png" alt="image" width="900" height="">

‎
 

!!!warning Warning               
There is a monthly limit rate with Ngrok so dont be supprised if training is suddenly interrupted.
!!!

‎

**3.** Once you've run the final cell a ngrok link will apear under the cell, click it and it will take you the WebUI.

***
## <u>Downloading Music & Models</u>
***

#### Music Download

**1.** When in the UI look at the top left and look for the tab named `Download Music` and click it.

   <img src="../aicovermaker-img/5.png" alt="image" width="600" height="">

‎ 

**2.** Then put the song you want to download in the text box and click download.


   <img src="../aicovermaker-img/6.png" alt="image" width="1000" height="">

***

#### Model Download

**1.** In the UI look at the top left and look for the tab named `Download Model` and click it.

   <img src="../aicovermaker-img/4.png" alt="image" width="600" height="">

‎ 

**2.** Then put the model you want to download in the text box and click download.


   <img src="../aicovermaker-img/7.png" alt="image" width="1000" height="">

‎

**3.** You can also drag and drop your model in the `Drop files` box to upload them directly.

***

## Inference

Please use our [Inference Settings guide](https://docs.aihub.gg/rvc/resources/inference-settings/) to find out the inference settings do what.

**TTA** - results in longer separation time, it gives a little better SDR score but hard to tell if it's really audible in most cases". it “means "test time augmentation", it will do 3 passes on the audio file instead of 1. 1 pass with be with original audio. 1 will be with inverted stereo (L becomes R, R become L). 1 will be with phase inverted and then results are averaged for final output. 

***
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::