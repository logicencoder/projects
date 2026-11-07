# Logic Encoder — Projects

I am an independent developer who orchestrates, architects and ships software. This page collects what I have built: applications, dashboards, tools, experiments and engineering notes. They are in very different stages. Some run publicly on logicencoder.com, some serve me every day on my own machines, some were test projects to learn a technology, and some are prototypes or unfinished. The list starts with the most substantial and most interesting work and ends with smaller pieces.

A lot of what I build exists because the tool I needed did not exist or did not fit the way I work, so I made it. I treat software as a craft and like to build something working from nothing, watch it handle real data and improve it from what I see. Much of it is data-intensive and real-time: ingesting live feeds, normalising, aggregating, caching and presenting them so that they are useful. I work across the stack: Python (FastAPI, asyncio), Node.js and TypeScript, React and Vite, Rust, C#, PHP and WordPress, plus blockchain and exchange tooling, media processing, Linux operations and security, directing AI coding agents and making the architecture decisions myself.

Each entry says why I built the project. What it does in detail, the screenshots and the technology are in the linked overview. The code itself is private.

[Website](https://logicencoder.com) · [Applications on the site](https://logicencoder.com/applications/) · [About](https://logicencoder.com/about/) · [Contact](https://logicencoder.com/contact/)

## Applications

### Universal Service Manager

![Universal Service Manager services grid with status, logs and lifecycle controls](https://raw.githubusercontent.com/logicencoder/universal-service-manager-overview/69911dc6b38ee5e5ab071ca3b6847aa15666f0e0/assets/universal-service-manager-services-grid.png)

Running a growing set of applications meant a terminal for each of them, separate tools for logs, Docker and systemd, and an SSH session for every small change. I wanted to work efficiently with everything in one place, and I found nothing that fitted my requirements, so I built my own.

One browser dashboard now controls the services, containers, native units and firewall and shows logs and resources beside them. It saves the time I used to lose switching between tools, and it is the control point for most of what I run.

**Status:** In daily use on my own servers

**Built with:** Python; HTML, CSS, JavaScript; YAML; psutil, Server-Sent Events; Docker, Docker Compose, systemd, SSH, UFW; Linux

[Overview](https://github.com/logicencoder/universal-service-manager-overview)

### Logic Encoder Crypto App Store

![Crypto App Store catalogue, basket, payment progress and completed delivery](https://raw.githubusercontent.com/logicencoder/le-crypto-app-store-overview/a273c0866b31eca342d3e34f0c1d2db2358c27f8/assets/crypto-app-store-catalogue-basket-payment-delivery.png)

I wanted to sell digital products through Telegram with crypto payments and automatic delivery, and I could not find anything like it. So I designed the whole architecture myself: the storefront, payment verification, delivery to the buyer and an operator workspace.

It was also a test bed for security. I used it to try protections and to see how well a payment and delivery flow holds up against abuse.

**Built with:** JavaScript, Node.js, Fastify; HTML, CSS, JavaScript; DuckDB; Telegram Mini Apps, Telegraf; Ethereum, USDC, ETH, ethers; WebSockets

[Overview](https://github.com/logicencoder/le-crypto-app-store-overview)

### Logic Encoder Work Brain

![Logic Encoder Work Brain 3D knowledge graph](https://raw.githubusercontent.com/logicencoder/second-brain-overview/ade90436790d039dca7ef10b3221989c35a76dea/assets/logic-encoder-work-brain-3d-knowledge-graph.png)

My work is spread over dozens of projects, notes and decisions. Based on Andrej Karpathy's idea of an LLM-maintained wiki and the 3D brain application from Nate Herk's AIS-OS, I built a personal knowledge system so that I can work more efficiently.

I can find what I have already built and decided, and an AI assistant works from a small, reviewed set of facts instead of guessing. It keeps work material only.

**Built with:** Python; Node.js; WebGL; Markdown wiki in Git; OpenRouter, OpenAI and Anthropic APIs

[Overview](https://github.com/logicencoder/second-brain-overview)

### MEXC Trading App

![MEXC Trading App dashboard with chart, order book and manual order panel](https://raw.githubusercontent.com/logicencoder/mexc_trading_app-overview/b79be717b87b75ccec6b3d8b426609f326df60b5/assets/mexc-trading-app-trading-dashboard-order-book.png)

Building my own trading interface with bots, completely from the ground up, was a dream of mine for many years. I wanted full control over how I trade and a place to test what real-time software can do.

It began as a way to test and optimise processing a large stream of market data, aggregating it, drawing it and acting on it without lag, and it grew into a complete workstation for manual trading and automation.

**Built with:** Python, FastAPI; HTML, CSS, JavaScript; MEXC; TradingView; WebSockets

[Overview](https://github.com/logicencoder/mexc_trading_app-overview)

### ETH Gas Live

![ETH Gas Live dashboard with gas price chart and fee tiers](https://raw.githubusercontent.com/logicencoder/eth-gas-live-plugin-overview/0cafbf56bb6dccdd61aa9cd2831f681cc8dfea47/assets/eth-gas-live-dashboard-gas-price-chart.png)

Other gas trackers did not have everything I wanted, so I built my own: a live view of what a transaction costs now, how fees have moved, and tools to plan the next one. It runs publicly on my site.

**Built with:** PHP, WordPress; HTML, JavaScript; Chart.js and Tailwind CSS (both loaded from a public CDN); Ethereum

[Overview](https://github.com/logicencoder/eth-gas-live-plugin-overview) · [Live](https://logicencoder.com/ethereum-gas-tracker/)

### MEXC Live Statistics

![MEXC Live Statistics dashboard with market trades and analytics](https://raw.githubusercontent.com/logicencoder/mexc-live-stats-plugin-overview/f6dcf708abb56af0f24a134d11fda7ed140583f7/assets/mexc-live-statistics-live-dashboard-market-trades.png)

A real-time statistics site for exchange markets, fed by my own data service and published on logicencoder.com. The same thing exists for the Gate exchange.

**Built with:** PHP, WordPress; HTML, CSS, JavaScript; MEXC public market data; WebSockets; optional TradingView chart (off by default)

[Overview](https://github.com/logicencoder/mexc-live-stats-plugin-overview) · [Live](https://logicencoder.com/mexc-app/) · [Same thing for the Gate exchange](https://logicencoder.com/gate-app/)

### LE Karaoke Studio

![LE Karaoke Studio workspace with transcription, editor and timeline](https://raw.githubusercontent.com/logicencoder/le-karaoke-studio-overview/2ed33c86e42aa9774c3cfee7a482f40597e4e0c6/assets/le-karaoke-studio-work-transcription-editor-timeline.png)

I was curious how the applications that add subtitles to a video are made, so I started to take the idea apart. That was reverse engineering, and step by step I kept adding more multimedia features.

The audio-effects lab came from something I had wanted for years: building effects for music myself. Today it is a studio that takes a media file all the way to a finished video.

**Built with:** Python, FastAPI; React, TypeScript; Whisper, PyTorch; FFmpeg, Remotion, HyperFrames; yt-dlp

[Overview](https://github.com/logicencoder/le-karaoke-studio-overview)

### LE HSCR — Radio Monitoring Workspace

![LE HSCR radio monitoring workspace](https://raw.githubusercontent.com/logicencoder/le-hscr-overview/fcbe22bb9830dc80983ea6d5e8b2455d5cc27e72/assets/le-hscr-radio-monitoring-workspace.png)

One workspace for looking at what radio devices are around: Bluetooth, Wi-Fi, satellite reception and USB, for authorized radio and device investigations.

**Built with:** Python, FastAPI; JavaScript; Docker

[Overview](https://github.com/logicencoder/le-hscr-overview)

### WP Visitor Stats

![WP Visitor Stats dashboard with visits, content and audience panels](https://raw.githubusercontent.com/logicencoder/wp-visitor-stats-plugin-overview/573c313132c88976cf8010599765a73789680ce2/assets/wp-visitor-stats-dashboard-dark.png)

The existing website-analytics solutions did not suit me, so I built my own the way I want to look at my site. It has functions that other plugins usually keep behind a paywall, and the things I wanted that they lack.

**Built with:** PHP, WordPress; JavaScript, HTML, CSS; MySQL

[Overview](https://github.com/logicencoder/wp-visitor-stats-plugin-overview)

### Celestial Lab

![Celestial Lab satellite map with a 3D globe of orbiting objects](https://raw.githubusercontent.com/logicencoder/celestial-lab-plugin-overview/75f0c881bf7ccb1e8403e5c7ca94fd8cdb3036f3/assets/celestial-lab-satellite-map-3d-globe-orbits.png)

Mostly a fun project: I am an astronomy fan, so I put together one place where I can look at satellites, aurora, the Sun, crews in orbit, exoplanets, asteroid encounters and launches. It runs on my site.

**Built with:** WordPress, PHP, JavaScript, HTML, CSS; Three.js, Globe.gl, WebGL; Python

[Overview](https://github.com/logicencoder/celestial-lab-plugin-overview) · [Live](https://logicencoder.com/celestial-lab/)

### System Monitor App

![System Monitor App terminal dashboard](https://raw.githubusercontent.com/logicencoder/system-monitor-app-overview/d254228adc2cccd1bde1f951493a704bdd7c1990/system-monitor-app-terminal-dashboard.png)

I did not want seven terminals open just to watch the hardware. One terminal dashboard shows CPU, memory, disk, network, GPU and sensors together, so everything is in one place and I can keep working.

**Status:** In daily use

**Built with:** Python; Textual; psutil; Linux

[Overview](https://github.com/logicencoder/system-monitor-app-overview)

### Rocinante Command Center

![Rocinante Command Center simulated navigation](https://raw.githubusercontent.com/logicencoder/roci-command-center-overview/76d1af1701427683a75136a5c288d2611a859333/assets/rocinante-command-center-solar-system-tactical-deck.png)

A fictional ship command deck that I built to show a visual style which I can deploy to other applications: dense, instrument-like panels, 3D scenes and live-moving data. All telemetry is simulated; the point is the look and feel.

**Built with:** React 18, Vite; Three.js; Recharts; Tailwind CSS

[Overview](https://github.com/logicencoder/roci-command-center-overview) · [Live](https://logicencoder.com/rocinante/)

### Le Sound Normalizer

![Le Sound Normalizer with compressor knobs and 15-band equalizer](https://raw.githubusercontent.com/logicencoder/le-sound-normalizer-overview/7344dee31d360d8ccbcd3850b46fb6ba634ed37f/assets/le-sound-normalizer-15-band-equalizer-compressor.png)

Watching films, the jump from quiet dialogue to a loud action scene meant reaching for the volume again and again, which is annoying. I built a normalizer that keeps loudness under control so dialogue stays understandable.

It was also my test of building, compiling and packaging an application for Windows, because most of what I write targets Linux.

**Status:** Test project, in use

**Built with:** C#, Windows Forms; C++ audio processing object; WASAPI, NAudio; 32-bit floating-point DSP

[Overview](https://github.com/logicencoder/le-sound-normalizer-overview)

### Ethereum Chain Swap Monitor

![Ethereum Chain Swap Monitor swap detail with pool liquidity breakdown](https://raw.githubusercontent.com/logicencoder/eth-chain-swaps-monitor-overview/8fe4193f20b100d6523d750b175e89951727ae87/assets/eth-chain-swap-monitor-pool-liquidity-breakdown-swap-detail.png)

Another data-heavy build: following swaps on Ethereum as they happen, decoding and valuing them and presenting a live feed. The challenge is processing a large amount of data reliably in real time.

It has also taught me how long-running services fail. A full disk once silently stopped its scanner for weeks, and the fix was a scanner that restarts itself and reports when it stalls.

**Built with:** Python, FastAPI; JavaScript; Web3; WebSockets

[Overview](https://github.com/logicencoder/eth-chain-swaps-monitor-overview) · [Live](https://logicencoder.com/ethereum-chain-swap-monitor/)

### CEX/DEX Arbitrage App

![CEX/DEX Arbitrage App with pool discovery, arbitrage scanner and trading rules](https://raw.githubusercontent.com/logicencoder/cex-dex-arb-overview/5a6b8c1144a49414fa3fb7ccf8cf3581b60bbd86/assets/cex-dex-arbitrage-app-pool-discovery-arb-scanner-trading-rules.png)

One of my first big applications, a monolith of roughly twenty thousand lines. I used it to test how such a project can be taken apart into microservices, how to display a lot of different real-time data at once and how to automate trades by market criteria.

**Status:** Test project

**Built with:** Python, FastAPI; HTML, CSS, JavaScript; Web3.py; MEXC, Gate, Uniswap; TradingView

[Overview](https://github.com/logicencoder/cex-dex-arb-overview)

### Red-Team Lite

A small scanner for a quick first security pass over a web application you own or may test: it crawls, probes for common weaknesses, captures evidence and writes a report.

**Built with:** Python; Playwright; FastAPI; JSON and Markdown reports

[Overview](https://github.com/logicencoder/redteam-lite-overview)

### LE Media Player

A test project: porting my browser-based audio-effects lab to Rust. I wanted to learn Rust, development, building and compiling, so I picked something I already understood. The result is a fast native Linux player with an equalizer and visualizers.

**Status:** Test project

**Built with:** Rust; cpal, ffmpeg, rustfft; egui, Slint, GTK4; custom 20-band equalizer

[Overview](https://github.com/logicencoder/le-media-player-overview)

### Dynex MEXC Balance Monitor

![Dynex MEXC Balance Monitor dashboard with balance, in and out charts and transaction feed](https://raw.githubusercontent.com/logicencoder/dynex-mexc-balance-monitor-plugin-overview/8b2c6d80a105ee7ceb0ac9247f2a88e8e4670eb4/assets/dynex-mexc-balance-monitor-live-dashboard-in-out-charts.png)

The data about how much DNX the exchange wallet holds and moves was not published anywhere; only I had it. I wanted to make those flows visible to everyone, so I built this monitor and put it on my site.

**Built with:** PHP, WordPress; JavaScript; Python worker

[Overview](https://github.com/logicencoder/dynex-mexc-balance-monitor-plugin-overview) · [Live](https://logicencoder.com/dynex-mexc-balance-monitor/)

### TS Analyzer

![TS Analyzer inspecting an actual receiver transport stream](https://raw.githubusercontent.com/logicencoder/ts-analyzer-overview/0d6b2ffbd7964526782d51f9fec36e1c8ad081d5/assets/ts-analyzer-transport-analysis.png)

I am a satellite TV enthusiast and wanted an application for analysing transport streams: not just watching a channel but looking inside the stream, at tuning, reception and what the stream contains.

**Built with:** Rust; Python; FastAPI; JavaScript; HTML; CSS

[Overview](https://github.com/logicencoder/ts-analyzer-overview)

### LE Settings

![LE Settings administration console](https://raw.githubusercontent.com/logicencoder/le-settings-plugin-overview/bb65c6d7748d5787a647417964705b8f1b6cf4f6/assets/le-settings-admin-console-overview.png)

A test bed for managing my own WordPress site from one console: protection and security features, and notifications to me when something happens.

**Built with:** PHP, WordPress; HTML, CSS, JavaScript; Telegram

[Overview](https://github.com/logicencoder/le-settings-plugin-overview)

### Logic Encoder Enhanced Theme

![Logic Encoder Enhanced WordPress theme front page](https://raw.githubusercontent.com/logicencoder/logic-encoder-theme-overview/8e5a586b41684e5d0334b9169c93d9a22c014dc2/logic-encoder-theme-wordpress-front-page.png)

The WordPress theme behind logicencoder.com, connecting application pages, technical writing and member content in one presentation.

**Built with:** PHP, WordPress; JavaScript, CSS

[Overview](https://github.com/logicencoder/logic-encoder-theme-overview) · [Live](https://logicencoder.com/)

### Russian DC Observatory

![Russian DC Observatory populated public overview](https://raw.githubusercontent.com/logicencoder/russian-dc-observatory-monitor-overview/951c2fe0ab4e9a9cbee154fcaa1294e5c0433732/assets/russian-dc-observatory-connectivity-overview.png)

A comparison of Russian Internet connectivity, service reports and infrastructure records that keeps sources and uncertainty visible.

**Built with:** Python; SQLite; JavaScript; HTML; CSS; SVG

[Overview](https://github.com/logicencoder/russian-dc-observatory-monitor-overview) · [Live](https://logicencoder.com/russian-dc-observatory/)

### Awair Monitor Dashboard

![Awair environmental metrics and measurement history](https://raw.githubusercontent.com/logicencoder/le-awair-monitor-dashboard-overview/1154807b0cd2a9dd009256f177a5bbb623567599/assets/awair-monitor-dashboard-air-quality-score-trend-history.png)

Nothing like this existed: the manufacturer only offers a complicated cloud route. I found that the device has a local API, so I built my own dashboard in the browser that talks to it directly.

**Built with:** Python; Svelte; JavaScript; SQLite

[Overview](https://github.com/logicencoder/le-awair-monitor-dashboard-overview)

### Slovak Air Quality Dashboard

![Slovak Air Quality Dashboard history of hourly readings and station changes](https://raw.githubusercontent.com/logicencoder/air-quality-bridge-overview/42e86a73e4c0228d0a01324f2fe9c00f0281804c/assets/slovak-air-quality-dashboard-history-hourly-source-index.png)

Station readings, history and geographic context for air quality in Slovakia, with the source and the age of every reading visible.

**Built with:** Python; SQLite; PHP, WordPress; JavaScript

[Overview](https://github.com/logicencoder/air-quality-bridge-overview) · [Live](https://logicencoder.com/air-quality-slovakia/)

### Dynex Large Transactions

![Dynex Large Transactions live transaction feed](https://raw.githubusercontent.com/logicencoder/dynex-large-transactions-plugin-overview/7272500cdab077e7e8f7dc234a7918703a1a9b08/assets/dynex-large-transactions-live-transactions-expanded.png)

A live view of large DNX transfers, with search by address and transaction detail.

**Built with:** PHP, WordPress; JavaScript; Python

[Overview](https://github.com/logicencoder/dynex-large-transactions-plugin-overview) · [Live](https://logicencoder.com/dynex-large-transactions-monitor/)

### React + Vite Architecture Guide

![React and Vite project architecture diagram](https://raw.githubusercontent.com/logicencoder/react-vite-architecture-for-dummies/4f156135dfad47f9517db68415e481718a8361b0/react-vite-architecture-diagram.png)

A plain-English guide to how a React and Vite project fits together. It is also a demonstration: I can produce this kind of architecture overview for any project, so that other people understand quickly what it consists of and how it works.

**Built with:** React, Vite, JavaScript; Markdown

[Overview](https://github.com/logicencoder/react-vite-architecture-for-dummies)

### SatPI — SAT>IP server for the Vu+ Duo 4K SE

I wanted the open-source SatPI SAT>IP server to work on my Vu+ Duo 4K SE, where upstream delivered no data on the second tuner bank and could not switch DiSEqC. I fixed it, tested it end to end and wrote down the investigation.

**Built with:** C++; SAT>IP (RTSP, HTTP); ARM cross-build

[Overview](https://github.com/logicencoder/satpi)

### TechniSat SkyStar USB 2 HD CI — Linux driver and SAT>IP

The Windows drivers for this card stopped at Windows 7, there were none for Windows 11, and plugging it into USB 3 crashed the machine with a blue screen. I did not want to throw the hardware away, so I tried to make it usable another way.

Then I found that the Linux drivers were wrong too and never locked DVB-S2, so I fixed that as well. The card now tunes and locks, and it is rescued and back in use.

**Built with:** Linux kernel module (stb0899); minisatip SAT>IP

[Overview](https://github.com/logicencoder/technisat-skystar-usb-2-hd-ci-satip)

### XEX Spread Monitor

Price gaps between two exchanges for the same coin, with fees and liquidity taken into account.

**Built with:** Python; SQLite; PHP, WordPress; JavaScript

[Overview](https://github.com/logicencoder/xex-spread-bridge-overview) · [Live](https://logicencoder.com/mexc-gate-price-spreads/)

### Deriv Board

Funding, open interest and volume of perpetual futures from several venues in one workspace.

**Built with:** Python; SQLite; PHP, WordPress; JavaScript

[Overview](https://github.com/logicencoder/deriv-board-bridge-overview) · [Live](https://logicencoder.com/crypto-perp-funding/)

### LE Auto Record

A plugin for an OpenPLi receiver that keeps programmes I watched long enough as normal recordings.

**Built with:** Python; Enigma2 on OpenPLi

[Overview](https://github.com/logicencoder/le-auto-record-overview)

### 0xDNX DHIP Richlist

Holder rankings, balances and transactions of wrapped Dynex with their chain context.

**Built with:** PHP, WordPress; JavaScript; Python; Ethereum

[Overview](https://github.com/logicencoder/dynex-0xdnx-dhip-richlist-plugin-overview) · [Live](https://logicencoder.com/0xdnx-dhip-v2-richlist/)

### Logic Encoder Login System

Registration, email verification, login, account recovery and access administration for the site.

**Built with:** PHP, WordPress; HTML, CSS, JavaScript

[Overview](https://github.com/logicencoder/logicencoder-login-system-plugin-overview) · [Live](https://logicencoder.com/login/)

### European Electricity Monitor

European electricity prices set against demand, generation and cross-border activity.

**Built with:** Python; PHP; WordPress; JavaScript; SQLite

[Overview](https://github.com/logicencoder/elec-prices-bridge-overview) · [Live](https://logicencoder.com/european-electricity-monitor/)

### CVE DoS

Exploited vulnerabilities from public records in a searchable digest, being developed into a professional security search application.

**Built with:** Python; PHP, WordPress; JavaScript; CISA KEV and NVD data

[Overview](https://github.com/logicencoder/cve-watch-bridge-overview) · [Live](https://logicencoder.com/cve-exploit-tracker/)

### Military Flights Monitor

Public ADS-B aircraft observations on a map, a globe and a searchable board.

**Built with:** Python; PHP; WordPress; JavaScript

[Overview](https://github.com/logicencoder/mil-flights-bridge-overview) · [Live](https://logicencoder.com/military-flight-tracker/)

### Application boilerplates

Starting skeletons I reuse for new projects: chain monitors, FastAPI real-time services, operator web apps, product pairs, Telegram mini apps, terminal dashboards, service-manager services and WordPress plugins.

**Built with:** Python, JavaScript, PHP

---

Retired components, deployment backups, shared libraries, supporting services and utilities are kept in their own repositories and are not listed here.

**[Logic Encoder](https://logicencoder.com)** · [GitHub](https://github.com/logicencoder) · [Contact](https://logicencoder.com/contact/)
