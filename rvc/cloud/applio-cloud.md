``Last update: June 27, 2026``

***
:::content-center
<img src="/img/applio-banner.png" alt="Applio Banner" width="600">

## Introduction
:::
- This is a [cloud-based](https://docs.aihub.gg/extra/glossary/#cloud-based) alternative to run [Applio](https://docs.aihub.gg/rvc/local/applio/), an RVC Fork, for users who do not have a powerful local PC GPU. 
- Most of these options provide the exact same Web UI as the local version. 

!!!warning "Official Applio Discord Moved"
The original **IA Hispano (Applio)** Discord server has migrated.
- **What happened:** To leave behind thousands of inactive accounts and scam bots, the development team consolidated their resources and moved official Applio support over to their former Dione (another IA Hispano Archived Project about automated AI Installations, kind of like Pinokio) server.
- **The old server:** The old, bloated server was transferred/sold to prominent Argentinean streamer and ex-VTuber [Nimu Spacecat VTuber](https://www.youtube.com/@NimuVT), who has rebranded it to **AI Maxxing**, an AI News Hub. It has **no affiliation** with Applio development.
- **Where to go:** For official Applio support, updates, and open-source RVC community channels, please use their new permanent Discord server:
- 👉 **[Join the New Official Applio Discord](https://discord.gg/wY7gmqTyEV)**
!!!

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
    
    <a href="#google-colab-web-ui" class="cloud-card">
        <img src="/img/google-colaboratory-logo.svg" alt="Colab">
        <h3>Google Colab Web UI</h3>
        <p>Decent performance and easiest setup for standard use.</p>
    </a>
    
    <a href="#kaggle" class="cloud-card">
        <img src="/img/kaggle-icon.svg" alt="Kaggle">
        <h3>Kaggle</h3>
        <p>Generous free GPU quotas. Great alternative if Google Colab is limited.</p>
    </a>
    
    <a href="#lightningai" class="cloud-card">
        <img src="/img/lightning-ai-logo.svg" alt="Lightning">
        <h3>Lightning.AI</h3>
        <p>Persistent storage and powerful GPUs.</p>
    </a>
    
    <a href="#huggingface-space-appliox" class="cloud-card">
        <img src="/img/huggingface-icon.svg" alt="HuggingFace Space">
        <h3>HuggingFace Space</h3>
        <p>Best for quick inference. Limited free hardware.</p>
    </a>
    
    <a href="#google-colab-no-ui-usage" class="cloud-card">
        <img src="/img/google-colaboratory-logo.svg" alt="Google Colab No UI">
        <h3>Google Colab No UI</h3>
        <p>No UI workflow for no ban risk on free tier and maximum resource efficiency.</p>
    </a>
</div>

<br><br>

***
:::content-center
### Google Colab Web UI
:::

!!!danger Google Colab Service
**Check the [Google Colab Glossary](https://docs.aihub.gg/extra/glossary/#google-colab) for more info on Free Tier, Limits, Verification, Pricing and other things.**

**Disallowed Activities:** **Running Web UIs on the Google Colab Free Tier is a violation of Google's Terms of Service**. Please be aware that Google’s detection systems operate mid-run, not just at startup; even if you bypass the initial "Disallowed Code" check through encryption, your session remains at risk. Persistent violations can lead to a progressive penalty: starting with reduced GPU availability and potentially escalating to a permanent restriction of your Google account's ability to execute Colab notebooks. See [Google's official policy](https://research.google.com/colaboratory/faq.html#disallowed-activities) for more information.
!!!

#### <u>Setting Up</u> :icon-download:

- Access the Colab space [here](https://colab.research.google.com/github/iahispano/applio/blob/master/assets/Applio.ipynb). Then log in to your Google account.

- Execute the **Install Applio** cells section. This will take around 2 minutes and will require you to grant permission to use Google Drive to save your models.

<img src="../applio-cloud-img/google-colab-web-ui-img/install-applio-cell-section.png" alt="Install Applio Cell Section" width="400">

- It'll finish when you see a tick symbol on the left.

<img src="../applio-cloud-img/google-colab-web-ui-img/finished-installation.png" alt="Finished Installation" width="400">

***
###### ‎
- Sync with Google Drive to automatically save or load models.

<img src="../applio-cloud-img/google-colab-web-ui-img/sync-google-drive-cell.png" alt="Sync with Google Drive" width="500">

***
###### ‎
- Select a Sharing method and Run the Server, using a tunnel that securely exposes the application running in your private cloud environment to the public internet. The notebook gives you 3 different services to do this. Choose one from the `method` dropdown menu in the code cell.

- **Gradio (Fast, Popular, Reliable & Default)**
    - **How it works:** This is a built-in [Gradio](https://docs.aihub.gg/extra/glossary/#gradio) feature. It's one of the most straightforward methods as it doesn't require any external accounts or tokens.
    - **Steps:**
        1. Select "Gradio" from the `method` dropdown menu.
        2. Run the cell. The public Gradio URL (ending in `gradio.live`) will be printed in the output once the server is ready. Click on it to access the Web UI.

- **Ngrok (Fast, Popular & Reliable)**
    - **How it works:** Ngrok is a popular service that creates secure tunnels. It requires a free account and an authentication token. It has a 1GB Bandwidth Free Monthly Limit.
    - **Steps:**
        1. Go to the [Ngrok Dashboard](https://dashboard.ngrok.com/get-started/your-authtoken) to get your free authtoken.
        2. In the notebook cell, paste your token into the `ngrok_token` field.
        3. (Optional) To potentially reduce latency, select a geographical `Region` from the list of parameter options next to it, that is closest to you.
        4. Run the cell. The public Ngrok URL (ending in `ngrok.io`) will be printed in the output once the server is ready. Click on it to access the Web UI.

- **LocalTunnel (No Account, Password Protected)**
    - **How it works:** LocalTunnel is another free service that doesn't require an account. For security, it generates a unique URL that is protected by a password.
    - **Steps:**
        1. Select "LocalTunnel" from the `method` dropdown menu.
        2. Run the cell.
        3. The output will display two key pieces of information: the public URL (ending in `loca.lt`) and a `Local Tunnel Password` below it.
        4. Click the URL. A new page will ask for a password.
        5. Copy the password from the notebook output and paste it into the password prompt in your browser to access the Web UI.

<img src="../applio-cloud-img/google-colab-web-ui-img/start-server-cell.png" alt="Start Server Cell" width="550">

***
:::content-center
### Kaggle
:::

!!!danger Kaggle Service
**Check the [Kaggle Glossary](https://docs.aihub.gg/extra/glossary/#kaggle) for more info on Free Tier, Limits, Verification, Pricing and other things.**
!!!

#### <u>Account Setup</u>

- Start by making an account [here](https://www.kaggle.com/account/login?phase=startRegisterTab&returnUrl=%2F).

<img src="/img/cloud-services/kaggle-img/kaggle-sign-in.png" alt="Kaggle Sign In" width="575">

- Verify your account with a phone number. This is required to enable the "Internet" option in your notebooks, which is necessary for downloading models and dependencies.

<img src="/img/cloud-services/kaggle-img/kaggle-phone.png" alt="Kaggle Phone Verification" width="575">

***
#### <u>Notebook Creation & Setup</u>

- Go to [Kaggle](https://www.kaggle.com) and click **Create** then **New Notebook** at the top left. 

<img src="/img/cloud-services/kaggle-img/new.png" alt="New Notebook" width="400">

- Under your session's name click **File** then **Import Notebook**.

<img src="/img/cloud-services/kaggle-img/import.png" alt="Import Notebook" width="450">

- In the new window, click the **Link** tab and paste the following URL into the box: `https://github.com/IAHispano/Applio/blob/main/assets/Applio_Kaggle.ipynb`. Click **Import** on the bottom right once you've done this.

<img src="/img/cloud-services/kaggle-img/link.png" alt="Link Tab" width="700">

- In the sidebar on the right, under "Session options", turn on the **Internet** switch. Make sure persistence is set to **Files and variables**.

<img src="/img/cloud-services/kaggle-img/kaggle-internet.png" alt="Kaggle Internet Toggle" width="250"> 

- Under "Accelerator", select the **T4 x2** GPU.

<img src="/img/cloud-services/kaggle-img/kaggle-gpu.png" alt="Kaggle GPU Toggle" width="250">

- *(Optional)* To ensure your session doesn't time out during long training processes, you can enable "Save version". Go to the top right, click **Save version**, and choose **Save & Run All (Commit)** from the dropdown. In the advanced settings, select **Always save output** for the notebook.

<img src="/img/cloud-services/kaggle-img/kaggle-pers.png" alt="Kaggle Persistence" width="250">

***
#### <u>Installation & Tunnels Setup</u>

- Start by running the first few cells of the notebook to install the necessary dependencies.

- Configure and Run Tunnels: The next cell is for setting up the tunneling service, which exposes the Applio interface to the internet. Choose one from the `Tunnel` dropdown menu.

- **Ngrok (Recommended & Default method):** Requires a free account and an authentication token. Paste your token into the `ngrok_authtoken` field, select "Ngrok", and run the cell.
- **Gradio + LocalTunnel (No Account & Password Protected):** Uses Gradio's built-in tunnel for the main Applio interface and LocalTunnel for Tensorboard. Select this, run the cell, and use the provided password for LocalTunnel links.
- **LocalTunnel (No Account, Password Protected):** Generates a unique URL protected by a password. Select this, run the cell, and copy the `LocalTunnels Password` from the output.
- **Horizon (Fast, Requires Account & ID):** Requires a free account and a personal ID. Go to the [Horizon Dashboard](https://hrzn.run/dashboard/), copy your ID, paste it into `horizon_id`, and run the cell.

- Once configured, run the cell. The output will print public URLs for Applio, Tensorboard, and the Filebrowser. Click the Applio link to open the Web UI.

***
:::content-center
### Lightning.AI
:::

!!!danger Lightning.AI Service
**Check the [Lightning.AI Glossary](https://docs.aihub.gg/extra/glossary/#lightningai) for more info on Free Tier, Limits, Verification, Pricing and other things.**
!!!

#### <u>Create an Account</u>

- First, make an account with [Lightning Ai](https://lightning.ai).

<img src="/img/cloud-services/lightning-ai-img/signup.png" alt="LightningAI Signup" width="300">

- Make sure you verify yourself with a phone number. Once you've done that you will get an email that looks like this:

<img src="/img/cloud-services/lightning-ai-img/verification.png" alt="LightningAI Verification" width="400">

!!!danger Verification Time
You will need to wait 2-3 business days to become fully verified.
!!!

***
#### <u>Studio Setup & Installation</u>

- After creating your Lightning.AI account, open the [Applio Notebook Studio](https://lightning.ai/nick088/studios/applio-ui?view=public&section=featured) and Clone it.

<img src="/img/cloud-services/lightning-ai-img/lightning-ai-clone-studio.png" alt="LightningAI Clone Studio" width="300">

- Activate/Switch GPU: If you aren't on a GPU environment by default, you must switch to a GPU environment. On the right-hand lateral menu, click on **Studio Environment** (the processor icon).

<img src="/img/cloud-services/lightning-ai-img/gpu-setting.png" alt="LightningAI GPU Setting" width="500">

- Click **Switch To GPU**, select an available GPU, and wait for the environment to restart.

<img src="/img/cloud-services/lightning-ai-img/gpus-list.png" alt="LightningAI GPUs List" width="500">

!!!info Free GPU Credits List:
- 75 hours monthly of T4 16gb
- 31 hours monthly of L4 24gb
- 15 hours monthly of L40 48gb
!!!

- Run the first code cell to download the latest version of Applio and install necessary dependencies. It will print "Installed!" when finished.

***

#### <u>Tunnels & Server Setup</u>

- Launch the Server via Tunnels: Navigate to the third code cell, titled "Start Server **using Tunnels**". Choose one from the `Tunnel` code menu in the code cell.

- **Port Viewer (Recommended & Default method):** A built-in Lightning.AI feature. Select "Port Viewer". Click the `+` at the bottom of the right tab, click on Web Apps and install Port Viewer. Run the cell. In the right-hand sidebar, click the **Web Apps** tab, click Port Viewer -> Add a new port. Enter `18888` and click your Port to open it.
- **Gradio (Fast, Popular & Reliable):** Select "Gradio" and run the cell. Click the `.gradio.live` link in the output.
- **Ngrok (Fast, Popular & Reliable):** Get your [Ngrok authtoken](https://dashboard.ngrok.com/get-started/your-authtoken), paste it into the `Token` field, and run the cell.
- **Cloudflare (Easy, No Account Needed):** Select "Cloudflare" and run the cell. A `.trycloudflare.com` link will appear.
- **LocalTunnel (No Account, Password Protected):** Select "LocalTunnel" and run the cell. Copy the `Local Tunnel Password` and use it on the generated link.
- **Horizon (Fast, Requires Account & ID):** Go to the [Horizon Dashboard](https://hrzn.run/dashboard/), copy your ID, paste it into the `Token` field, and run the cell.

- Accessing Files manually: Find the **Teamspace Drive** button on the right sidebar and click it. The path to Applio is `Studio > this_studio > Applio > Applio`. You can drag, drop, and download files directly from here.

<img src="/img/cloud-services/lightning-ai-img/teamspace-drive.png" alt="LightningAI Teamspace Drive" width="500">

- Opening the TensorBoard: Find the TensorBoard icon on the right sidebar, click it, and start it to monitor your training visually.

<img src="/img/cloud-services/lightning-ai-img/tensorboard.png" alt="LightningAI TensorBoard" width="500">

- Opening the notebook: If you want to go back to the code view, simply click on the `Jupyter` icon on the right sidebar.

<img src="/img/cloud-services/lightning-ai-img/jupyter.png" alt="LightningAI Jupyter" width="500">

- **Maintenance:** If you need to update the Program or start fresh, you can run the final cell in the notebook, "Delete everything". This will remove all downloaded files and configurations from your persistent storage, allowing for a clean installation by re-following the notebook with perhaps a changed branch variable.

***
:::content-center
### HuggingFace Space
:::

!!!danger HuggingFace Space Service
**Check the [HuggingFace Space Glossary](https://docs.aihub.gg/extra/glossary/#huggingface-space) for more info on Free Tier, Limits, Quotas and other things.**
!!!

!!!danger HuggingFace Space Limits
- The ApplioX HuggingFace Space doesn't have Training, Realtime, or Plugin tabs. It is for Inference only.
- RVC HuggingFace Spaces frequently get paused without warning.
!!!

!!!danger RVC HuggingFace Spaces Pausing Issue
**Please be aware that HuggingFace has recently been pausing RVC-related Spaces without providing any reason.**
!!!

- Open the [ApplioX HuggingFace Space](https://huggingface.co/spaces/IAHispano/ApplioX).

- The Web UI will load directly in your browser without any installation required.

***
:::content-center
## Web UI Usage
:::

Once you have the Web UI running via your chosen Cloud Provider (Colab, Kaggle, Lightning.AI, or ApplioX), the rest of the process is **identical to using a local installation.** 

Use the Local Guide below for detailed instructions on Inference, Training, TTS, and Plugins.

[!button text="Continue with the Local Guide" icon="arrow-right" target="blank"](https://docs.aihub.gg/rvc/local/applio/#inference)

***
:::content-center
## Google Colab No UI Usage
:::
This is a strictly code-based workflow for users who want to maximize Colab resource efficiency and avoid potential bans on the free tier by not loading a Web UI.

!!!warning Note on Updates
Because this workflow relies directly on executing notebook cells rather than a stable Web UI, the notebook's structure and variable names might change frequently between updates. 
!!!

- Open the [Applio No UI Colab](https://colab.research.google.com/github/IAHispano/Applio/blob/main/assets/Applio_NoUI.ipynb) and run the `Installation` cell.

<img src="../applio-cloud-img/google-colab-no-ui-img/installation-cell.png" alt="Installation Cell" width="600">

**2. Preprocess Dataset:** Name your model, upload your dataset to Google Drive, paste the path in `dataset_path`, select your sample rate, and run the cell.

<img src="../applio-cloud-img/google-colab-no-ui-img/preprocess-cell.png" alt="Preprocess Cell" width="800">

**3. Extract Features:** Choose your `f0_method` (RMVPE recommended) and run the cell.

**4. Training:** Set the `total_epoch`, choose your `batch_size` (8 recommended), enable `cleanup` (if this is a fresh run), and tick `save_only_latest`. Run the cell to start training!

<img src="../applio-cloud-img/google-colab-no-ui-img/training-cell.png" alt="Training Cell" width="700">

**5. Resuming:** If you get disconnected, enter the exact model name from before, run the first two cells, select your sample rate/f0, and run the final training cell again.

***
:::content-center
## Troubleshooting
:::

==- There's no Gradio Public URL.
- In case the public URL doesn't show up, Gradio might be down. Check [here](https://status.gradio.app/).
- To bypass this, use other tunnels depending on the cloud service you're using (such as Ngrok, LocalTunnel, or Cloudflare).
===

==- I can't use the Cloud GPU after some time.
- You have exhausted the Free Cloud GPU. You will need to wait for it to reset, pay or switch to a different account.
===

==- There's no option for my sample rate.
- If it's lower than 32k: select `32k`.       
- If it's 44.1k: select `40k`.   
- If it's higher than 48k: select `48k`.
===

==- :question: I couldn't find my answer.
- Report your issue [here](https://docs.aihub.gg/contributions).
===

***
:::content-center
## Communities :icon-people:
:::

<style>
  .social-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
    margin: 1.5rem 0;
  }
  .social-card {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 0.8rem 1.2rem;
    min-width: 240px;
    border: 1px solid rgba(150, 150, 150, 0.2);
    border-radius: 10px;
    text-decoration: none !important;
    color: inherit !important;
    background: rgba(128, 128, 128, 0.05);
    transition: all 0.2s ease;
  }
  .social-card:hover {
    transform: translateY(-2px);
    background: rgba(128, 128, 128, 0.12);
    border-color: rgba(150, 150, 150, 0.5);
  }
  .social-card img {
    width: 24px;
    height: 24px;
  }
  .social-card span {
    font-weight: 600;
    font-size: 0.95rem;
  }
</style>
<div class="social-grid">
    <a href="https://discord.gg/mmRR2TUJF5" class="social-card">
    <img src="/img/discord-logo.svg" alt="Discord">
    <span>AI HUB's Discord</span>
</a>
    <a href="https://discord.gg/wY7gmqTyEV" class="social-card">
    <img src="/img/discord-logo.svg" alt="Discord">
    <span>IA Hispano (Applio)' Discord</span>
</a>
</div>

###### ‎   ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
