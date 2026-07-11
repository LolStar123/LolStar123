<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img src="assets/banner-light.svg" alt="Atul Kanodia- Economics @ UCL, London. I build autonomous systems- markets, content, daily ops." width="100%">
</picture>

Economics student who ships end-to-end systems: ingestion, models, governance,
and the surface on top. The common thread is **autonomy with proof**- pipelines
that verify their own output before anyone trusts it.

## Featured builds

<table>
<tr>
<td width="50%" valign="top">

### [Baxter](https://github.com/LolStar123/baxter)

An autonomous chief-of-staff running 24/7 on my PC. Reads 4 inboxes (Gmail x3,
Discord, WhatsApp, voice), triages into an Obsidian vault, and **builds its own
features**- gated by a two-model PRD process, a usage governor, and a verify
layer that treats "done" as a claim, not a fact.

`~48k lines core` `112 test files` `0 unsupervised sends`

</td>
<td width="50%" valign="top">

### [Reels Factory](https://github.com/LolStar123/reels-factory)

A research pipeline that happens to publish to Instagram: reads quant papers,
backtests them walk-forward on real data, renders the result as a voiced,
captioned 9:16 reel. Two independent honesty gates; nothing posts without a
human `APPROVE`.

`34 modules` `4-engine TTS chain` `red-teamed QC`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Markets Backtesting](https://github.com/LolStar123/markets-backtesting)

Walk-forward harness implementing **50 trading signals, each cited to an
academic paper**, ranked honestly across full history *and* an out-of-sample
crisis window. Built under a hackathon deadline.

`pandas` `walk-forward` `50 cited signals`

</td>
<td width="50%" valign="top">

### [TfL Reliability](https://github.com/LolStar123/tfl-reliability)

Live pipeline polling Transport for London's API, storing every status
snapshot, and rating each Tube line with an **Elo-style reliability score**.
ETL → event detection → rating model → dashboard.

`TfL API` `SQLite` `Elo ratings`

</td>
</tr>
</table>

## Toolbox

`Python` · `pandas` / `numpy` · `PowerShell` · `SQLite` · `matplotlib` · `Streamlit` ·
REST APIs · ffmpeg · a growing fleet of supervised AI agents

📫 **atulswaggalicious@gmail.com**
