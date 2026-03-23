---
icon: cloud
order: 4000
---

``Last update: March 24, 2026``


***
:::content-center
## Introduction
:::

Some of the Applio's Cloud versions support the **Realtime** tab. This allows users without a powerful local GPU to perform live voice conversion using cloud-hosted hardware.


***
## Choose Your Cloud Service
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
    <a href="https://docs.aihub.gg/rvc/cloud/applio-colab" class="cloud-card">
        <img src="/img/google-colaboratory-logo.svg" alt="Colab">
        <h3>Google Colab</h3>
        <p>Reliable performance and full control for power users.</p>
    </a>
    <!-- Kaggle -->
    <a href="https://docs.aihub.gg/rvc/cloud/applio-kaggle" class="cloud-card">
        <img src="/img/kaggle-icon.svg" alt="Kaggle">
        <h3>Kaggle</h3>
        <p>Generous free GPU quotas. Great alternative if Colab is limited.</p>
    </a>
    <!-- Lightning.AI -->
    <a href="https://docs.aihub.gg/rvc/cloud/applio-lightning-ai" class="cloud-card">
        <img src="/img/lightning-ai-logo.svg" alt="Lightning AI">
        <h3>Lightning.AI</h3>
        <p>Persistent cloud storage and powerful compute environments.</p>
    </a>
</div>

***

### Realtime Setup on Cloud
Once you have the Applio WebUI open from your cloud provider:

[!button text="Continue with the Local Guide" icon="arrow-right" target="blank"](https://docs.aihub.gg/realtime-voice-changer/local/applio-realtime/)

***

:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::