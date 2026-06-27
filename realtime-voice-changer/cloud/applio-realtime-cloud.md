``Last update: June 27, 2026``

***
:::content-center
## Introduction
:::

Some of the Applio Cloud versions support the **Realtime** tab. This allows users without a powerful local GPU to perform live voice conversion using cloud-hosted hardware.

!!!warning Official Applio Discord Moved
The original **IA Hispano (Applio)** Discord server has transitioned ownership and has been rebranded to **AI Maxxing**. 
- It is **no longer affiliated** with the original Applio development team or its open-source creators.
- To receive official Applio updates, support, and community discussions, please use their new official server link:
- 👉 **[Join the Official Applio Discord Community](https://discord.gg/wY7gmqTyEV)**
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
    
    <a href="https://docs.aihub.gg/rvc/cloud/applio-cloud/#google-colab" class="cloud-card">
        <img src="/img/google-colaboratory-logo.svg" alt="Google Colab">
        <h3>Google Colab Web UI</h3>
        <p>Reliable performance and easiest setup for standard use.</p>
    </a>
    
    <a href="https://docs.aihub.gg/rvc/cloud/applio-cloud/#kaggle" class="cloud-card">
        <img src="/img/kaggle-icon.svg" alt="Kaggle">
        <h3>Kaggle</h3>
        <p>Generous free GPU quotas. Great alternative if Colab is limited.</p>
    </a>
    
    <a href="https://docs.aihub.gg/rvc/cloud/applio-cloud/#lightningai" class="cloud-card">
        <img src="/img/lightning-ai-logo.svg" alt="Lightning AI">
        <h3>Lightning.AI</h3>
        <p>Persistent cloud storage and powerful compute environments.</p>
    </a>
</div>

<br><br>

***

### Realtime Setup on Cloud
Once you have the Applio WebUI running and accessible via your tunnel link from your chosen cloud provider, the usage steps are exactly the same as the local version.

Click below to learn how to configure your inputs and outputs for live voice changing.[!button text="Continue with the Local Realtime Guide" icon="arrow-right" target="blank"](https://docs.aihub.gg/realtime-voice-changer/local/applio-realtime/)

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

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
