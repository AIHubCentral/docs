---
icon: ":musical_note:"
order: 3000
---

``Last update: March 24, 2026``
***
:::content-center
## Introduction
:::
- This is a [cloud-based](https://docs.aihub.gg/extra/glossary/#cloud-based) alternative to run [AICoverMaker](https://docs.aihub.gg/rvc/local/aicovermaker/), Applio RVC Fork, only for people who don't have a good PC GPU, with a Web User Interface.


{{ include "cloud-services/start-decision.md" }}
{{ include "cloud-services/grid-cards/google-colab-card.md" }}
{{ include "cloud-services/grid-cards/kaggle-card.md" }}
{{ include "cloud-services/end-decision.md" }}


***
:::content-center
### Google Colab
:::

{{ include "cloud-services/warnings/google-colab.md" }}

#### <u>Installation & Setup</u> :icon-book:

- Go to the [AICoverMaker Colab](https://colab.research.google.com/github/Eddycrack864/RVC-AI-Cover-Maker-UI/blob/main/assets/RVCAICoverMakerUI.ipynb) and run the first cell. 

   <img src="../aicovermaker-cloud-img/1.png" alt="image" width="200" height="">

‎ 

!!!
Installation may take a couple of minutes, be patient.
!!! 

- Next go to the second cell and put your ngrok token in the text box and run it. If you dont have a ngrok acount sign up [here](https://ngrok.com/) and you can authenticate your ngrok tunnel agent [here](https://dashboard.ngrok.com/get-started/your-authtoken). 

   <img src="../aicovermaker-cloud-img/2.png" alt="image" width="400" height="">

‎

- (Optional) You can choose not to use Ngrok if you desire to by running the third cell.

   <img src="../aicovermaker-cloud-img/3.png" alt="image" width="400" height="">

‎

- Once you've run either the cell with or without ngrok a link under the cell will apear, click it and it will take you the WebUI.


***
:::content-center
### Kaggle
:::

{{ include "cloud-services/warnings/kaggle.md" }}

{{ include "cloud-services/setups/kaggle-account.md" }}

***

#### <u>Installation & Setup</u> :icon-book:

- Go to the [AICoverMaker Kaggle notebook](https://www.kaggle.com/code/eddycrack864/rvc-ai-cover-maker-ui) and click `Copy & Edit` on the top right. 

   <img src="../aicovermaker-cloud-img/8.png" alt="image" width="900" height="">

‎ 

- Once you're in the notebook run the first installation cell. Once it's done it will output `Requirements installed`.

   <img src="../aicovermaker-cloud-img/9.png" alt="image" width="800" height="">

‎

!!!
Installation may take a couple of minutes, be patient.
!!!

- Next go to the second cell and put your Ngrok token in the `TOKEN HERE` spot and run it. If you dont have a Ngrok acount sign up [here](https://ngrok.com/) and you can authenticate your ngrok tunnel agent [here](https://dashboard.ngrok.com/get-started/your-authtoken). 

   <img src="../aicovermaker-cloud-img/10.png" alt="image" width="900" height="">

- Once you've run the final cell a ngrok link will appear under the cell, click it and it will take you the WebUI.

***
## <u>Downloading Music & Models</u>
***

#### Music Download

- When in the UI look at the top left and look for the tab named `Download Music` and click it.

   <img src="../aicovermaker-cloud-img/5.png" alt="image" width="600" height="">

‎ 

- Then put the song you want to download in the text box and click download.


   <img src="../aicovermaker-cloud-img/6.png" alt="image" width="1000" height="">

***

#### Model Download

- In the UI look at the top left and look for the tab named `Download Model` and click it.

   <img src="../aicovermaker-cloud-img/4.png" alt="image" width="600" height="">

‎ 

- Then put the model you want to download in the text box and click download.


   <img src="../aicovermaker-cloud-img/7.png" alt="image" width="1000" height="">

‎

- You can also drag and drop your model in the `Drop files` box to upload them directly.

***

## Inference

Please use our [Inference Settings guide](https://docs.aihub.gg/rvc/resources/inference-settings/) to find out the inference settings do what.

**TTA** - results in longer separation time, it gives a little better SDR score but hard to tell if it's really audible in most cases". it “means "test time augmentation", it will do 3 passes on the audio file instead of 1. 1 pass with be with original audio. 1 will be with inverted stereo (L becomes R, R become L). 1 will be with phase inverted and then results are averaged for final output. 


{{ include "end-badge.md" }}