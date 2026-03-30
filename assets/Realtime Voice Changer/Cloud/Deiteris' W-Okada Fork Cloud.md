---
icon: archive
order: 1000
---

``Last update: March 24, 2026``

***
:::content-center
## Introduction
:::
- This is a [cloud-based](https://docs.aihub.gg/extra/glossary/#cloud-based) alternative to run [Wokada Deiteris Fork](https://docs.aihub.gg/realtime-voice-changer/local/deiteris-w-okada-fork/), for users without a powerful local PC GPU, via Google Colab, Kaggle, or Lightning.AI.

{{ include "cloud-services/warnings/cloud-server-audio.md" }}

{{ include "cloud-services/setups/virtual-audio-cable.md" }}


{{ include "cloud-services/start-decision.md" }}
{{ include "cloud-services/grid-cards/google-colab-card.md" }}
{{ include "cloud-services/grid-cards/kaggle-card.md" }}
{{ include "cloud-services/grid-cards/lightning-ai-card.md" }}
{{ include "cloud-services/end-decision.md" }}


***
:::content-center
### Google Colab
:::

{{ include "cloud-services/warnings/google-colab.md" }}

!!!danger
You need the Google Colab Paid Tier to run this, as it uses a Web UI; otherwise, you could risk getting disconnected or banned.
!!!

- **1. Access:** Open the [Deiteris Colab](https://colab.research.google.com/github/deiteris/voice-changer/blob/master-custom/Colab_RealtimeVoiceChanger.ipynb).

- **2. Install:** Start from the top and run the first cell.
<img src="../wokada-colab-img/colab1.png" alt="Colab Install" width="900">

- **3. Second Cell:** When it finishes (it will output `Done! Proceed with the next steps`), run the second cell.
<img src="../wokada-colab-img/colab2.png" alt="Colab Second Cell" width="600">

- **4. Ngrok:** Scroll to the last cell, place your [Ngrok token](https://dashboard.ngrok.com/get-started/your-authtoken) into the `TOKEN_HERE` field.
<img src="../wokada-colab-img/colab3.png" alt="Ngrok Token" width="600">

- **5. Launch:** Run the cell. (Optional) Under the token field, you can change the region selection for lower latency. Once it finishes downloading, click the generated Ngrok link to start the Web UI.


***
:::content-center
### Kaggle
:::

{{ include "cloud-services/warnings/kaggle.md" }}

{{ include "cloud-services/setups/kaggle-account.md" }}

#### <u>Notebook Creation & Setup</u>

- **Clone:** Go to the [realtime voice changer notebook](https://www.kaggle.com/code/suneku/voice-changer-public) and click "Copy and Edit".
<img src="../wokada-kaggle-img/wokada-deiteris-fork-kaggle-notebook.png" alt="Wokada Deiteris Fork Kaggle Notebook" width="1000">

- **Persistence:** In the sidebar on the right, turn on **Internet**. Make sure persistence is set to **Files and variables**.
<img src="/img/cloud-services/kaggle-img/kaggle-internet.png" alt="Internet" width="450">

- **GPU:** Turn on T4 x2 GPUs in the Accelerator settings.
<img src="/img/cloud-services/kaggle-img/kaggle-gpu.png" alt="GPU" width="250">

- **Save:** (Optional) Turn on "Save version" to save your progress.
<img src="/img/cloud-services/kaggle-img/kaggle-pers.png" alt="Persistence" width="250">

#### <u>Installation & Ngrok Setup</u>

- **Install:** Starting from the top, run the first installation cell. When it outputs `Done! Proceed with the next steps`, run the third cell.

<img src="../wokada-kaggle-img/install-1.png" alt="Install 1" width="900">

<img src="../wokada-kaggle-img/install-2.png" alt="Install 2" width="600">

- **Ngrok:** Scroll to the last cell, paste your token in the field, and run it to get your public URL.
<img src="../wokada-kaggle-img/token.png" alt="Token" width="600">


***
:::content-center
### Lightning.AI
:::

{{ include "cloud-services/warnings/lightning-ai.md" }}

{{ include "cloud-services/setups/lightning-ai-account.md" }}

- **Studio:** Clone the [Wokada-Deiteris-Fork Studio](https://lightning.ai/nick088/studios/wokada-deiteris-fork).
<img src="/img/cloud-services/lightning-ai-img/lightning-ai-clone-studio.png" alt="Clone" width="300">

- **GPU:** Switch to a GPU environment (Studio Environment -> Switch To GPU).
<img src="/img/cloud-services/lightning-ai-img/gpu-setting.png" alt="GPU Settings" width="500">

- **Install:** Run the first cell to install dependencies, and the second cell to configure the server.

- **Tunnels:** In the third cell, choose your tunnel (Port Viewer recommended) and run it. 

- **File Management:** Use the **Teamspace Drive** button on the right sidebar to upload files.
<img src="/img/cloud-services/lightning-ai-img/teamspace-drive.png" alt="Drive" width="500">

- **Notebook:** If you want to return to the code, click the **Jupyter** icon on the right.
<img src="/img/cloud-services/lightning-ai-img/jupyter.png" alt="Jupyter" width="500">


***
:::content-center
## Usage
:::
Now that you have the Web UI running, the rest of the process is **identical to using a local installation.**

[!button text="Continue with the Local Guide" icon="arrow-right" target="blank"](https://docs.aihub.gg/realtime-voice-changer/local/deiteris-w-okada-fork/#voice-models)


***
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::