# Logic Encoder — Projects

I am a hobbyist coder and software architect, curious how things work under the surface. This page collects what I have built: applications, WordPress plugins and a theme, dashboards, tools, experiments and engineering notes. They are in very different stages. The public ones are listed at https://logicencoder.com/applications/; others are tools I use myself, test projects to learn a technology, prototypes or unfinished work. The order is rough: bigger, more complete projects first, smaller pieces and unfinished work at the end.

A lot of what I build exists because the tool I needed did not exist or did not fit the way I work, so I made it. I like to build something working from nothing, watch it handle real data and improve it from what I see. Much of it is data-intensive and real-time: ingesting live feeds, normalising, aggregating, caching and presenting them so that they are useful.

The technology listed with each project is not a limit; I use whatever a project requires. So far that has been Python (FastAPI, asyncio), Node.js and TypeScript (Fastify), JavaScript with React, Vite and Svelte, PHP and WordPress (plugins and a theme), and Rust, C# and C++ for native software. For data I have used SQLite, PostgreSQL, DuckDB and MySQL plus in-memory caches, WebSockets and Server-Sent Events for live updates, Three.js, Globe.gl and Chart.js for graphics, Docker and systemd for running things, Web3 tooling for blockchain, and Playwright, Whisper, PyTorch, FFmpeg and Remotion for testing and media. Most entries say why I built the project; what each one does in detail, the screenshots and the technology are in the linked overview. The code itself is private.

[Website](https://logicencoder.com) · [Applications on the site](https://logicencoder.com/applications/) · [About](https://logicencoder.com/about/) · [Contact](https://logicencoder.com/contact/)

## Applications

### Universal Service Manager

![Universal Service Manager services grid with status, logs and lifecycle controls](https://raw.githubusercontent.com/logicencoder/universal-service-manager-overview/69911dc6b38ee5e5ab071ca3b6847aa15666f0e0/assets/universal-service-manager-services-grid.png)

Running a growing set of applications meant a terminal for each of them, separate tools for logs, Docker and systemd, and an SSH session for every small change. I wanted to work efficiently with everything in one place and found nothing that fitted my requirements, so I built my own.

Python apps, Node.js tools, shell jobs, containers and native services appear together as one fleet, as cards or in a dense table, with their running state, resource use and controls. Beside them sit host resources, a view of every process (including ones outside the managed fleet) and logs that can be narrowed to warnings and errors, so I can tell whether one application is struggling or the whole machine is under pressure and act on it right there.

| Layer | Technologies |
|---|---|
| Application | Python |
| Dashboard | HTML, CSS, JavaScript |
| Configuration | YAML |
| Monitoring | psutil, Server-Sent Events |
| Integrations | Docker, Docker Compose, systemd, SSH, UFW |
| Platform | Linux |

[Overview](https://github.com/logicencoder/universal-service-manager-overview)

### Logic Encoder Crypto App Store

![Crypto App Store catalogue, basket, payment progress and completed delivery](https://raw.githubusercontent.com/logicencoder/le-crypto-app-store-overview/a273c0866b31eca342d3e34f0c1d2db2358c27f8/assets/crypto-app-store-catalogue-basket-payment-delivery.png)

I did not set out to sell things; I wanted to try what it takes to sell digital products at all. Accepting crypto payments means solving a lot of different problems, from the security around payments to reliable delivery, and it was demanding and instructive. I could not find anything like it, so I designed the whole architecture myself. It was also a test bed for security: I used it to try protections and to see how well a payment and delivery flow holds up against abuse.

Everything happens inside Telegram: the buyer browses applications with images, prices and versions, gets a payment screen with an order reference, the exact amount, the address and the remaining time, and after verified payment the files arrive directly in the chat. A browser storefront offers the same catalogue. Behind it an operator workspace follows every order live, with filters for waiting, confirming, completed and problem orders, and a warehouse where products, prices, versions and deliverable files are maintained.

| Layer | Technologies |
|---|---|
| Application | JavaScript, Node.js, Fastify |
| Interfaces | HTML, CSS, JavaScript |
| Data | DuckDB |
| Telegram | Telegram Mini Apps, Telegraf |
| Payments | Ethereum, USDC, ETH, ethers |
| Live updates | WebSockets |
| Catalogue integration | WordPress |

[Overview](https://github.com/logicencoder/le-crypto-app-store-overview)

### Logic Encoder Work Brain

![Logic Encoder Work Brain 3D knowledge graph](https://raw.githubusercontent.com/logicencoder/second-brain-overview/ade90436790d039dca7ef10b3221989c35a76dea/assets/logic-encoder-work-brain-3d-knowledge-graph.png)

My work is spread over dozens of projects, notes and decisions. Based on Andrej Karpathy's idea of an LLM-maintained wiki and the 3D brain application from Nate Herk's AIS-OS, I built a personal knowledge system so that I can work more efficiently. It really does improve my work; I have checked that myself.

Notes become points of an explorable 3D graph, coloured by kind (work knowledge, projects, skills, source documents, drafts) with the links between them as lines. Source documents stay unchanged, and the assistant writes synthesis pages that cite them, record contradictions and keep a dated history. When I ask something, the workspace gathers the matching passages into a packet that I review before anything leaves my machine, so the AI answers from checked facts. Reusable working methods are kept as skills, and a control panel shows the health of the wiki and of the services behind it.

| Layer | Technologies |
|---|---|
| Knowledge store | Markdown wiki and immutable source files tracked in Git |
| Tooling | Python command-line tools for validation, search, ingestion and audits |
| 3D graph | Node.js server with a prebuilt WebGL renderer |
| Workspace | A Python web workspace for search, review and model questions |
| Model access | OpenRouter, OpenAI and Anthropic APIs with keys held only in the running session |

[Overview](https://github.com/logicencoder/second-brain-overview)

### MEXC Trading App

![MEXC Trading App dashboard with chart, order book and manual order panel](https://raw.githubusercontent.com/logicencoder/mexc_trading_app-overview/b79be717b87b75ccec6b3d8b426609f326df60b5/assets/mexc-trading-app-trading-dashboard-order-book.png)

Building my own trading interface with bots, completely from the ground up, was a dream of mine for many years. I wanted full control over how I trade, with manual trading and automation in one workstation that I understand to the last detail.

It is a configurable trading desk: panels can be moved, resized and collapsed, and the layout saved and reset, around a chart, the order book with depth, a live trades tape, balances and a trading panel with size shortcuts. The bot panel offers five modes: Mode 1 Instant Execution takes orders from other traders inside a price range with market orders (styles TAKE, PING, 50/50 or RANDOM); Mode 2 Grid Limit Orders places layered limit orders and replenishes them when filled; Mode 3 Step Re-entry Ladder places one order and moves the price by a percentage after each full fill until a stop rule or the budget is reached; Mode 4 Front of Book keeps one order at the best bid or ask and re-quotes one tick ahead when displaced; Mode 5 Scheduled Exact places one exact limit order at a set time. A multi-bot workspace, performance information, system statistics and debug logs help me follow and investigate what the bots do.

| Layer | Technologies |
|---|---|
| Application | Python, FastAPI |
| Supporting technologies | HTML, CSS, JavaScript; MEXC; TradingView; WebSockets |

[Overview](https://github.com/logicencoder/mexc_trading_app-overview)

### ETH Gas Live

![ETH Gas Live dashboard with gas price chart and fee tiers](https://raw.githubusercontent.com/logicencoder/eth-gas-live-plugin-overview/0cafbf56bb6dccdd61aa9cd2831f681cc8dfea47/assets/eth-gas-live-dashboard-gas-price-chart.png)

Other gas trackers did not have everything I wanted, so I built my own. It runs publicly on my site and was also a test bed for server-side rendering and search-engine optimisation.

Every new block becomes three send tiers (economical, standard and faster inclusion) with fee estimates that follow the EIP-1559 base and priority fee, plus a congestion index and a spike score. History charts and a weekly heatmap show when fees are usually low or high. A fee calculator multiplies a gas limit, chosen from presets for common actions or typed by hand, by a live tier or a custom price and shows the cost in ether and dollars, and alerts warn when a chosen level is reached. Eleven dedicated pages explain the numbers.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Application | PHP, WordPress |
| Supporting technologies | HTML, JavaScript; Chart.js and Tailwind CSS (both loaded from a public CDN); Ethereum |

[Overview](https://github.com/logicencoder/eth-gas-live-plugin-overview) · [Live](https://logicencoder.com/ethereum-gas-tracker/)

### MEXC Live Statistics

![MEXC Live Statistics dashboard with market trades and analytics](https://raw.githubusercontent.com/logicencoder/mexc-live-stats-plugin-overview/f6dcf708abb56af0f24a134d11fda7ed140583f7/assets/mexc-live-statistics-live-dashboard-market-trades.png)

A test of optimisation: processing a lot of real-time data, aggregating it and drawing it for many visitors at once without wasting resources. The same thing exists for the Gate exchange.

A visitor picks a coin and sees its price, 24-hour statistics, volume, how trading splits between buyers and sellers, detected bot activity and a live tape of trades, all updated over a WebSocket. For the operator there is a Coin Manager (tracked, dead and missing pairs, add and reload, an activity log) and a monitoring area for connection throughput and server health. Each coin is also published as a server-rendered page with structured data, so search engines can read it without running JavaScript.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Application | PHP, WordPress |
| Supporting technologies | HTML, CSS, JavaScript; MEXC public market data; WebSockets; optional TradingView chart (off by default) |

[Overview](https://github.com/logicencoder/mexc-live-stats-plugin-overview) · [Live](https://logicencoder.com/mexc-app/) · [Same thing for the Gate exchange](https://logicencoder.com/gate-app/)

### LE Karaoke Studio

![LE Karaoke Studio workspace with transcription, editor and timeline](https://raw.githubusercontent.com/logicencoder/le-karaoke-studio-overview/2ed33c86e42aa9774c3cfee7a482f40597e4e0c6/assets/le-karaoke-studio-work-transcription-editor-timeline.png)

I was curious how the applications that add subtitles to a video are made, so I started to take the idea apart. That was reverse engineering, and step by step I kept adding more multimedia features. The audio-effects lab came from something I had wanted for years: building effects for music myself.

It is one web application with ten workspaces: Studio (transcribe, edit lines, style and render), audio and video effects labs, context prompts, a video editor, a downloader, vocal and stem separation, a GPU watch panel, an automation workflow and settings. Clips can be processed one by one or in batches, with subtitle styling and visualiser options for a consistent look, job progress and downloadable results, from source file to finished video. It runs on a GPU machine under my own control.

| Layer | Technologies |
|---|---|
| Application | Python, FastAPI |
| Supporting technologies | React, TypeScript; Whisper, PyTorch; FFmpeg, Remotion, HyperFrames; yt-dlp |

[Overview](https://github.com/logicencoder/le-karaoke-studio-overview)

### LE HSCR — Radio Monitoring Workspace

![LE HSCR radio monitoring workspace](https://raw.githubusercontent.com/logicencoder/le-hscr-overview/fcbe22bb9830dc80983ea6d5e8b2455d5cc27e72/assets/le-hscr-radio-monitoring-workspace.png)

A single browser console for Bluetooth, Wi-Fi, satellite reception and USB, meant for authorised radio research on equipment and networks I own or may test.

It shows what the connected adapters and the tuner can see, keeps the history of what was seen and merges the logs of all radios into one stream. Bluetooth LE scans actively or passively and parses iBeacon and Eddystone advertisements; Wi-Fi scans in managed or monitor mode with a spectrum trace and waterfall; the satellite tuner is detected, powered and tuned by transponder or manually; the USB view lists attached devices and can reset one when an adapter disappears. It runs in a Docker container with the adapters passed through, stays on the local network by default and sends no telemetry.

| Layer | Technologies |
|---|---|
| Backend | Python with FastAPI |
| Interface | One HTML page with JavaScript, draggable panels and charts |
| Radios | Bluetooth LE adapter, Wi-Fi adapter in managed or monitor mode, DVB satellite tuner or SAT>IP |
| Packaging | Docker image based on Kali Linux, or a direct install on Ubuntu |

[Overview](https://github.com/logicencoder/le-hscr-overview)

### WP Visitor Stats

![WP Visitor Stats dashboard with visits, content and audience panels](https://raw.githubusercontent.com/logicencoder/wp-visitor-stats-plugin-overview/573c313132c88976cf8010599765a73789680ce2/assets/wp-visitor-stats-dashboard-dark.png)

The existing website-analytics solutions did not suit me, so I built my own the way I want to look at my site. It has functions that other plugins usually keep behind a paywall, and the things I wanted that they lack.

Inside WordPress it shows how visitors reach the site and what they use: an overview of traffic, content reports, geographic and technology reports, campaigns, custom events, interaction heatmaps, bot activity and ban management. Retention (180 days by default), excluded addresses and tracking options are configurable.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Application | PHP, WordPress |
| Supporting technologies | JavaScript, HTML, CSS; MySQL |

[Overview](https://github.com/logicencoder/wp-visitor-stats-plugin-overview)

### Celestial Lab

![Celestial Lab satellite map with a 3D globe of orbiting objects](https://raw.githubusercontent.com/logicencoder/celestial-lab-plugin-overview/75f0c881bf7ccb1e8403e5c7ca94fd8cdb3036f3/assets/celestial-lab-satellite-map-3d-globe-orbits.png)

Mostly a fun project: I am an astronomy fan, and I wanted one place where I can look at space instead of many separate archives.

Seven experiences share one workspace, starting with a source-aware summary. Satellite Map explores published orbital catalogues, filters orbital bands and follows the ISS or Tiangong, with a separately loaded Starlink layer; aurora, space environment, solar wind and alerts relate geomagnetic activity to the measurements behind it; Sun Live combines an observed solar disk, wavelengths, active regions and flares; People in Space separates the provider-reported roster from mission context; and there are views for exoplanets, asteroid encounters and launches.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Application | WordPress, PHP, JavaScript, HTML, CSS |
| Interactive visualization | Three.js, Globe.gl, WebGL |
| Data collection | Python |

[Overview](https://github.com/logicencoder/celestial-lab-plugin-overview) · [Live](https://logicencoder.com/celestial-lab/)

### System Monitor App

![System Monitor App terminal dashboard](https://raw.githubusercontent.com/logicencoder/system-monitor-app-overview/d254228adc2cccd1bde1f951493a704bdd7c1990/system-monitor-app-terminal-dashboard.png)

I did not want seven terminals open just to watch the hardware, so I put everything in one place and can keep working.

A single terminal program (Textual and psutil, one self-contained Linux executable) with panels for CPU with per-core load, memory and swap, network, disk, GPU and temperature sensors. Processes can be sorted by CPU or memory with one key, important systemd services and blocked firewall connections are listed, and an alerts panel keeps the last 100 alerts. It works in a plain SSH session, with no desktop on the monitored machine.

| Layer | Technologies |
|---|---|
| Application | Python |
| Supporting technologies | Textual; psutil; Linux |

[Overview](https://github.com/logicencoder/system-monitor-app-overview)

### Rocinante Command Center

![Rocinante Command Center simulated navigation](https://raw.githubusercontent.com/logicencoder/roci-command-center-overview/76d1af1701427683a75136a5c288d2611a859333/assets/rocinante-command-center-solar-system-tactical-deck.png)

A fictional ship command deck that I built to show a visual style I can deploy to other applications: dense, instrument-like panels, 3D scenes and live-moving data.

You can operate it: a command deck for a light frigate with three sections and four scenarios (Cruise, High-G Burn, Emergency, Comms Interference). One section shows a moving contact picture, another the vessel with drive, power distribution and six shield sectors, the third five radio channels. The solar system and hull schematic are 3D, and panels are resizable with remembered sizes. Every reading is simulated in the browser; nothing is real telemetry.

| Layer | Technologies |
|---|---|
| Interface | React 18, JavaScript, HTML and CSS with Tailwind utility classes |
| 3D and charts | Three.js for the solar system, hull, antenna and signal-field scenes; Recharts for the history plots |
| Simulation | A local step simulation that advances velocity, fuel, drive temperature, shield strength and signal interference over time |
| Build | Vite |

[Overview](https://github.com/logicencoder/roci-command-center-overview) · [Live](https://logicencoder.com/rocinante/)

### Le Sound Normalizer

![Le Sound Normalizer with compressor knobs and 15-band equalizer](https://raw.githubusercontent.com/logicencoder/le-sound-normalizer-overview/ca883ee28549150d457c51dd0e0c5d7fe200c17f/assets/le-sound-normalizer-15-band-equalizer-compressor.png)

Watching films, the jump from quiet dialogue to a loud action scene meant reaching for the volume again and again, which is annoying. I built a normalizer for that. It was also my test of building, compiling and packaging an application for Windows, because most of what I write targets Linux.

You choose a loudness ceiling and how firmly loud material is pulled toward quiet material (Soft, Balanced and other characters), and films, series and games stay at one comfortable level. A controller window sits beside a native audio component in the Windows audio path, so it works with whatever player you use. It offers LED meters, a live spectrum and oscilloscope, a simple bass, middle and treble control, a 15-band graphic equalizer, presets for film, evening or music, and green and cyan palettes.

| Layer | Technologies |
|---|---|
| Controller | C#, Windows Forms, .NET Framework 4.8, x64 |
| Audio component | C++ Windows audio processing object (APO) loaded by the Windows shared-mode audio engine |
| Compatibility engine | WASAPI capture and playback with NAudio (MIT licence) and an existing VB-CABLE installation |
| DSP | 32-bit floating-point processing for 1, 2, 6 and 8 channels, sample-peak limiter, compression, tone and graphic equalizer |
| Controller to component link | Shared settings block with revision and sequence ownership, bounded telemetry ring |
| Packaging | Single setup executable with controller, audio component and runtime files |
| Verification | Native processing scenario suite, controller and UI checks, installer checks |

[Overview](https://github.com/logicencoder/le-sound-normalizer-overview)

### Ethereum Chain Swap Monitor

![Ethereum Chain Swap Monitor swap detail with pool liquidity breakdown](https://raw.githubusercontent.com/logicencoder/eth-chain-swaps-monitor-overview/8fe4193f20b100d6523d750b175e89951727ae87/assets/eth-chain-swap-monitor-pool-liquidity-breakdown-swap-detail.png)

Another data-heavy build: following swaps on Ethereum as they happen means processing a large amount of data reliably in real time.

A Python process reads new Ethereum blocks and logs from a node, recognises swaps in known liquidity pools and values them in dollars. The dashboard shows a live feed of the latest 250 swaps with expandable detail, the 20 most active addresses with address search, saved quote tables per pool and a live terminal. Four monitoring modes choose what is read, and three themes and collapsible panels suit a long session.

| Layer | Technologies |
|---|---|
| Application | Python |
| Supporting technologies | HTML, CSS, JavaScript; Ethereum; WebSockets |

[Overview](https://github.com/logicencoder/eth-chain-swaps-monitor-overview) · [Live](https://logicencoder.com/ethereum-chain-swap-monitor/)

### CEX/DEX Arbitrage App

![CEX/DEX Arbitrage App with pool discovery, arbitrage scanner and trading rules](https://raw.githubusercontent.com/logicencoder/cex-dex-arb-overview/5a6b8c1144a49414fa3fb7ccf8cf3581b60bbd86/assets/cex-dex-arbitrage-app-pool-discovery-arb-scanner-trading-rules.png)

One of my first big applications, a monolith of roughly twenty thousand lines. I used it to test how such a project can be taken apart into microservices, how to display a lot of different real-time data at once and how to automate trades by market criteria.

Comparing an exchange price with a decentralised market is only the start of judging an opportunity, so screening, trade-size comparison and execution controls share one workspace. Arbitrage tables show buying on the exchange and selling on the DEX and the reverse for several trade sizes, a scanner discovers candidate pairs and tests their pools, and live order books for MEXC and Gate.io, own and all trades and a TradingView chart sit beside the comparison. A manual swap panel trades through an MEV-protected route, with a readout of whether swapping is currently allowed.

| Layer | Technologies |
|---|---|
| Application | Python, FastAPI |
| Supporting technologies | HTML, CSS, JavaScript; Web3.py; MEXC, Gate, Uniswap; TradingView |

[Overview](https://github.com/logicencoder/cex-dex-arb-overview)

### Red-Team Lite

A small scanner for a quick first security pass over a web application you own or may test.

It crawls the target to a chosen depth, collecting routes, forms and parameters, and probes them for exposed files, reflected cross-site scripting, SQL injection errors, local file inclusion, server-side request forgery, template injection, open redirects, insecure direct object references, exposed admin panels and default credentials you supply. Findings are rated by severity, serious ones get a browser screenshot as evidence, and each scan ends in JSON and Markdown reports. It runs from the command line, an API or a simple web form, and a bundled vulnerable sample application allows a safe trial run.

| Layer | Technologies |
|---|---|
| Scanner | Python with a crawler and HTTP probes |
| Evidence | Playwright with Chromium for screenshots |
| Interface | Command line, a FastAPI endpoint and a single-page web form |
| Reports | JSON and Markdown files |

[Overview](https://github.com/logicencoder/redteam-lite-overview)

### LE Media Player

A test project: porting my browser-based audio-effects lab to Rust. I wanted to learn Rust, development, building and compiling, so I picked something I already understood.

A fast native Linux player for local audio and video and for URLs such as YouTube, with a Winamp-style playlist where files and whole folders can be dropped in. The effects rack has a 20-band equalizer with presets (Flat, Rock, Metal, Techno, Bass boost, Pop, Vocal, Classical), a pre-amp and loudness control, and the visualizers react to the live spectrum and a beat detector: bars, waveforms, particles, circular spectrum, a bass-driven orb, frequency rings and a cymatics plate.

| Layer | Technologies |
|---|---|
| Language | Rust (2021 edition) |
| Audio | cpal output, ffmpeg decoding, rustfft analyser, lock-free ring buffers |
| DSP | Custom 20-band biquad equalizer, loudness normalizer, soft limiter, WSOLA time stretch |
| UI | egui / eframe (OpenGL), Slint, GTK4 — three frontends on one engine library |
| Integration | MPRIS over D-Bus (zbus), X11 and Wayland, .desktop entry, portable bundle |
| Online sources | yt-dlp |

[Overview](https://github.com/logicencoder/le-media-player-overview)

### Dynex MEXC Balance Monitor

![Dynex MEXC Balance Monitor dashboard with balance, in and out charts and transaction feed](https://raw.githubusercontent.com/logicencoder/dynex-mexc-balance-monitor-plugin-overview/8b2c6d80a105ee7ceb0ac9247f2a88e8e4670eb4/assets/dynex-mexc-balance-monitor-live-dashboard-in-out-charts.png)

The data about how much DNX the exchange wallet holds and moves was not published anywhere; only I had it. I wanted to make those flows visible to everyone, so I built this monitor and put it on my site.

A Python worker scans the chain and posts summaries to a WordPress plugin. The dashboard shows the DNX balance of the monitored wallet, total incoming and outgoing amounts and the progress of the scan, a live feed of deposits and withdrawals that can be filtered, searched and exported as CSV, and four charts (net flow, incoming against outgoing volume, transaction count and balance over time) with hourly, daily or weekly steps.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Plugin | PHP and WordPress with a shortcode, a REST API and an admin settings page |
| Front end | JavaScript, CSS, WebSocket and AJAX updates, interactive charts |
| Data worker | A Python worker that scans the Dynex chain and posts summaries to the site |
| Storage | WordPress database tables trimmed by scheduled jobs |

[Overview](https://github.com/logicencoder/dynex-mexc-balance-monitor-plugin-overview) · [Live](https://logicencoder.com/dynex-mexc-balance-monitor/)

### TS Analyzer

![TS Analyzer inspecting an actual receiver transport stream](https://raw.githubusercontent.com/logicencoder/ts-analyzer-overview/0d6b2ffbd7964526782d51f9fec36e1c8ad081d5/assets/ts-analyzer-transport-analysis.png)

I am interested in satellite feeds and in analysing streams, not in watching television. I wanted an application for looking inside transport streams.

A stream can look unstable because of reception, tuning, transport errors or the content itself, so the browser workspace walks from choosing a satellite source (discovering a SAT>IP receiver or entering one) to inspecting the arriving stream. Findings on transponders, television and radio services are collected for later review; on an Enigma2 receiver the programme already being watched can be analysed without changing channel; signal strength, SNR and error readings appear when the receiver supplies them, and a constellation view accepts external I/Q samples from compatible equipment.

| Layer | Technologies |
|---|---|
| Core stack | Rust; Python; FastAPI; JavaScript; HTML; CSS |

[Overview](https://github.com/logicencoder/ts-analyzer-overview)

### LE Settings

![LE Settings administration console](https://raw.githubusercontent.com/logicencoder/le-settings-plugin-overview/bb65c6d7748d5787a647417964705b8f1b6cf4f6/assets/le-settings-admin-console-overview.png)

A test bed for managing my own WordPress site from one console: protection and security features, and notifications to me when something happens.

The console has nine tabs. Status shows which protections and trackers are on; Telegram handles notifications with throttling and a test message; Protection covers brute-force lockouts that grow with repeated failures, IP whitelist and blacklist, security headers, maintenance mode and update control; SEO and Redirects manage descriptions, robots rules and path redirects (or 410 Gone); and the bot, visitor and security logs and a debug tab show what happened.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Application | PHP, WordPress |
| Supporting technologies | HTML, CSS, JavaScript; Telegram |

[Overview](https://github.com/logicencoder/le-settings-plugin-overview)

### Logic Encoder Enhanced Theme

![Logic Encoder Enhanced WordPress theme front page](https://raw.githubusercontent.com/logicencoder/logic-encoder-theme-overview/8e5a586b41684e5d0334b9169c93d9a22c014dc2/logic-encoder-theme-wordpress-front-page.png)

The WordPress theme behind logicencoder.com.

A dark technical design with a homepage built from sections whose text, colours and fonts can all be changed in the WordPress Customizer instead of in template files: hero, approach, capabilities, applications, blog teaser, stack, about and call to action. An App Manager page maintains the application catalogue in place, templates cover sign-in, password reset, email verification and account pages, and shortcodes show content only to logged-in users, a role or a membership level.

| Layer | Technologies |
|---|---|
| Type | WordPress theme |
| Theme | PHP and WordPress template hierarchy with Customizer API settings |
| Front end | HTML, CSS and JavaScript, with effects that can be switched off |
| Administration | A custom application manager and custom list screens for pages and posts |
| Verification | Playwright end-to-end tests |

[Overview](https://github.com/logicencoder/logic-encoder-theme-overview) · [Live](https://logicencoder.com/)

### Russian DC Observatory

![Russian DC Observatory populated public overview](https://raw.githubusercontent.com/logicencoder/russian-dc-observatory-monitor-overview/951c2fe0ab4e9a9cbee154fcaa1294e5c0433732/assets/russian-dc-observatory-connectivity-overview.png)

A research workspace for comparing evidence about Russian Internet connectivity, where sources and uncertainty stay visible and a missing observation is never treated as proof of an outage.

The overview brings service observations, network incidents, traffic context and source freshness together; Services groups provider components, incident references and maintenance; Access shows website-access measurement samples and their coverage; facility and map views explore the infrastructure geographically; and watchlists with an in-app change feed follow the sites and components you care about.

| Layer | Technologies |
|---|---|
| Application | Python; SQLite |
| Dashboard | JavaScript; HTML; CSS; SVG |
| Administration | WordPress; PHP |

[Overview](https://github.com/logicencoder/russian-dc-observatory-monitor-overview) · [Live](https://logicencoder.com/russian-dc-observatory/)

### Awair Monitor Dashboard

![Awair environmental metrics and measurement history](https://raw.githubusercontent.com/logicencoder/le-awair-monitor-dashboard-overview/1154807b0cd2a9dd009256f177a5bbb623567599/assets/awair-monitor-dashboard-air-quality-score-trend-history.png)

Nothing like this existed: the manufacturer only offers a complicated cloud route. I found that the device has a local API, so I built my own dashboard in the browser.

A score gauge and cards for temperature, humidity and the other air-quality values the device reports are read live, with trend charts and score history, daily, trends and correlations views and the device uptime. History lives in a local SQLite database and can be exported as CSV or JSON. There are two visual styles (Aurora and Nexus), English and Slovak interfaces and notifications through a webhook or ntfy.

| Layer | Technologies |
|---|---|
| Core stack | Python; Svelte; JavaScript; SQLite |

[Overview](https://github.com/logicencoder/le-awair-monitor-dashboard-overview)

### Slovak Air Quality Dashboard

![Slovak Air Quality Dashboard history of hourly readings and station changes](https://raw.githubusercontent.com/logicencoder/air-quality-bridge-overview/42e86a73e4c0228d0a01324f2fe9c00f0281804c/assets/slovak-air-quality-dashboard-history-hourly-source-index.png)

Air quality in Slovakia from the national monitoring network, with the source and the age of each number visible.

One board and one map show where the air is clean, where it is not and how that changed over recent hours and days. The overview summarises the latest snapshot, the map colours every station by quality class, a searchable directory lists stations with observation times, pollutants (PM10, PM2.5, nitrogen dioxide, ozone, sulphur dioxide) are separated, and history charts and day comparisons look beyond the last reading. Data refreshes every hour.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Data collection | Python worker that polls the public API of the Slovak national monitoring network (SHMU) once an hour |
| History | SQLite with one reading per station and hour, source revisions merged into the existing record |
| Delivery | REST ingest with an API key into a WordPress plugin written in PHP |
| Interface | Server-rendered table with delegated JavaScript for sorting, filtering and paging; AJAX refresh |
| Map | Leaflet with station markers and fullscreen mode |
| Charts | Lightweight in-house chart script (distribution, history and comparison charts) |
| Quality bands | Official SHMU air-quality classes from very good to very poor |

[Overview](https://github.com/logicencoder/air-quality-bridge-overview) · [Live](https://logicencoder.com/air-quality-slovakia/)

### Dynex Large Transactions

![Dynex Large Transactions live transaction feed](https://raw.githubusercontent.com/logicencoder/dynex-large-transactions-plugin-overview/7272500cdab077e7e8f7dc234a7918703a1a9b08/assets/dynex-large-transactions-live-transactions-expanded.png)

Large transfers disappear in a busy chain feed, so this view keeps them apart.

The feed lists large Dynex transfers with time, block, transaction hash, direction and amount; a statistics panel gives totals, the sent and received split, counts for today, 24 hours, 7 and 30 days, velocity and volume; and a search box returns the transactions of any wallet address. It is embedded with a shortcode whose settings control size, refresh interval and which panels appear.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Application | PHP, WordPress |
| Supporting technologies | HTML, CSS, JavaScript; Dynex |

[Overview](https://github.com/logicencoder/dynex-large-transactions-plugin-overview) · [Live](https://logicencoder.com/dynex-large-transactions-monitor/)

### React + Vite Architecture Guide

![React and Vite project architecture diagram](https://raw.githubusercontent.com/logicencoder/react-vite-architecture-for-dummies/4f156135dfad47f9517db68415e481718a8361b0/react-vite-architecture-diagram.png)

A plain-English guide to how a React and Vite project fits together. It is also a demonstration: I can produce this kind of architecture overview for any project, so that other people understand quickly what it consists of and how it works.

It walks through every file and folder, including what is safe to ignore, then follows how index.html, main.jsx and App.jsx lead to rendered components, and ends with a diagram of the whole structure and the five things worth remembering.

| Layer | Technologies |
|---|---|
| Subject | React, Vite, JavaScript, npm project structure |
| Format | Long-form Markdown guide with an architecture diagram |

[Overview](https://github.com/logicencoder/react-vite-architecture-for-dummies)

### SatPI — SAT>IP server for the Vu+ Duo 4K SE

I wanted the open-source SatPI SAT>IP server to work on my Vu+ Duo 4K SE, a receiver with dual FBC tuners where the upstream version delivered nothing on the second tuner bank. I fixed it and wrote down the investigation.

The fork fixes the NEXUS demultiplexer handling (source selection, mid-stream PID changes, the all-PIDs request), routes DiSEqC on the FBC child tuners in the correct tone, voltage, command and mini-burst order, stops the daemon crashing on closed connections or empty keepalives, and tolerates the case differences and stale values that clients such as DVBViewer send. It was verified on OpenPLi 9.2 with three orbital positions while the receiver software keeps running, and the measurements and packet captures are published on logicencoder.com.

| Layer | Technologies |
|---|---|
| Language | C++ (upstream SatPI codebase) |
| Protocols | SAT>IP over RTSP/HTTP — DVB-S/S2, DVB-T/T2, DVB-C |
| Target hardware | Vu+ Duo 4K SE — Broadcom bcm7335 / NEXUS, dual FBC DVB-S2 |
| Build | ARM cross-toolchain, statically linked (-static -static-libstdc++ -static-libgcc) |
| Verified on | OpenPLi 9.2, DVBViewer clients, Enigma2 running alongside |

[Overview](https://github.com/logicencoder/satpi)

### TechniSat SkyStar USB 2 HD CI — Linux driver and SAT>IP

The Windows drivers for this card stopped at Windows 7, there were none for Windows 11, and plugging it into USB 3 crashed the machine with a blue screen. I did not want to throw the hardware away, so I tried to make it usable another way. Then I found that the Linux drivers were wrong too and never locked DVB-S2, so I fixed that as well, and the card is rescued and back in use.

The repository ships one out-of-tree kernel module, the stb0899 driver patched for DVB-S2 lock, signal scale and SNR calibration, together with a minisatip SAT>IP server for free-to-air channels. Calibrated signal and SNR appear in DVBViewer, TransEdit and the minisatip web page, complete transponder scans work, DiSEqC ports switch, and it is tested on Ubuntu 24.04.

| Layer | Technologies |
|---|---|
| Driver | Out-of-tree stb0899.ko kernel module — DVB-S2 lock, signal scale, SNR calibration patches |
| Sat>IP server | minisatip — RTSP port 8554, web UI 8080 |
| Host | Ubuntu 24.04 LTS, kernel 6.8 (tested); Windows clients consume via Sat>IP |
| Clients | DVBViewer, TransEdit, VLC, ffprobe |

[Overview](https://github.com/logicencoder/technisat-skystar-usb-2-hd-ci-satip)

## Prototypes, skeletons and unfinished work

These are skeletons, prototypes and work in progress. They are listed so it is clear what is unfinished; some of them run publicly, none is a finished product.

### XEX Spread Monitor

Price gaps between two exchanges for the same coin, with fees and liquidity taken into account.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Collection | Python worker fetching the all-pairs public tickers of MEXC and Gate every 30 seconds |
| Computation | Shared USDT pairs only, combined 24-hour volume floor, gap as MEXC last price over Gate last price, plausibility cut-off for broken or mismatched… |
| History | SQLite log of every snapshot (prices, bids and asks on both sides, gap, direction, both volumes) |

[Overview](https://github.com/logicencoder/xex-spread-bridge-overview) · [Live](https://logicencoder.com/mexc-gate-price-spreads/)

### Deriv Board

Funding, open interest and volume of perpetual futures from several venues in one workspace.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Collection | Python worker polling the public APIs of Binance USD-M, Bybit linear, Hyperliquid, Aster and Lighter every two minutes, with no API keys |
| History | SQLite snapshots per venue, symbol and time |
| Delivery | Authenticated REST ingest into a WordPress plugin written in PHP, with page caching switched off for the live view |

[Overview](https://github.com/logicencoder/deriv-board-bridge-overview) · [Live](https://logicencoder.com/crypto-perp-funding/)

### LE Auto Record

A plugin for an OpenPLi receiver that keeps programmes I watched long enough as normal recordings.

| Layer | Technologies |
|---|---|
| Receiver platform | Enigma2 on OpenPLi, with its configuration and on-screen list screens |
| Plugin | Python, using the receiver's timeshift buffer, EPG and timers |
| Recording and storage | MPEG transport stream files, local disk or CIFS network share |

[Overview](https://github.com/logicencoder/le-auto-record-overview)

### 0xDNX DHIP Richlist

Holder rankings, balances and transactions of wrapped Dynex with their chain context.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Application | PHP, WordPress |
| Supporting technologies | HTML, CSS, JavaScript; Dynex |

[Overview](https://github.com/logicencoder/dynex-0xdnx-dhip-richlist-plugin-overview) · [Live](https://logicencoder.com/0xdnx-dhip-v2-richlist/)

### Logic Encoder Login System

Registration, email verification, login, account recovery and access administration for the site.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Application | PHP, WordPress |
| Supporting technologies | HTML, CSS, JavaScript |

[Overview](https://github.com/logicencoder/logicencoder-login-system-plugin-overview) · [Live](https://logicencoder.com/login/)

### European Electricity Monitor

European electricity prices set against demand, generation and cross-border activity.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Core stack | Python; PHP; WordPress; JavaScript; SQLite |

[Overview](https://github.com/logicencoder/elec-prices-bridge-overview) · [Live](https://logicencoder.com/european-electricity-monitor/)

### CVE DoS

Exploited vulnerabilities from public records in a searchable digest, being developed into a professional security search application.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Collection | Python worker that downloads the CISA KEV catalogue and recent NVD publications every six hours |
| Relevance filter | Keyword list for common server and developer stacks (operating systems, web servers, PHP and WordPress, Python, Node, Java, containers, databases,… |
| History and de-duplication | SQLite log of what was already published |

[Overview](https://github.com/logicencoder/cve-watch-bridge-overview) · [Live](https://logicencoder.com/cve-exploit-tracker/)

### Military Flights Monitor

Public ADS-B aircraft observations on a map, a globe and a searchable board.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Core stack | Python; PHP; WordPress; JavaScript |

[Overview](https://github.com/logicencoder/mil-flights-bridge-overview) · [Live](https://logicencoder.com/military-flight-tracker/)

### Application boilerplates

Starting skeletons I reuse for new projects: chain monitors, FastAPI real-time services, operator web apps, product pairs, Telegram mini apps, terminal dashboards, service-manager services and WordPress plugins.

| Layer | Technologies |
|---|---|
| Languages | Python, JavaScript, PHP |
| Patterns | Chain monitors, FastAPI real-time services, operator web apps, product pairs, Telegram mini apps, terminal dashboards, service-manager services, WordPress plugins |

## In short

In short: real-time data and exchange tooling, blockchain monitoring, media processing, native desktop software, WordPress plugins and web applications, hardware and driver work, and the tools that keep it all running. Each project is a place where I learned how something works.

---

Retired components, deployment backups, shared libraries, supporting services and utilities are kept in their own repositories and are not listed here.

**[Logic Encoder](https://logicencoder.com)** · [GitHub](https://github.com/logicencoder) · [Contact](https://logicencoder.com/contact/)
