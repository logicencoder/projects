# Logic Encoder — Projects

A catalogue of the applications, dashboards, tools and engineering projects built by Logic Encoder. Each entry shows what the product does, what it offers, how it is built and where to read more. The list starts with the most substantial and most interesting work and ends with smaller tools, prototypes and unfinished work.

Across these projects: Python (FastAPI, asyncio) and Node.js backends, real-time WebSocket dashboards, blockchain and exchange tooling, WordPress themes and plugins, native desktop software in Rust and C#, Linux service operations, security checks, and AI-assisted development.

[Website](https://logicencoder.com) · [Web applications](https://logicencoder.com/applications/) · [Contact](https://logicencoder.com/contact/)

## Applications

### Universal Service Manager

![Universal Service Manager services grid with status, logs and lifecycle controls](https://raw.githubusercontent.com/logicencoder/universal-service-manager-overview/69911dc6b38ee5e5ab071ca3b6847aa15666f0e0/assets/universal-service-manager-services-grid.png)

Managing a growing collection of applications can turn a simple check into a round of terminal sessions, log searches and separate administration tools. Universal Service Manager grew out of that daily frustration: the available tools did not fit the way its creator wanted to work, so a single workspace was built around those needs.

**What it offers**

- **A single place to run the fleet** — The Services workspace makes a mixed collection of applications manageable as one fleet. Python applications, Node.js tools, shell jobs and native services appear together, with clear running or stopped states and the controls needed for everyday administration.
- **A compact overview for busy hosts** — The Overview table presents the same fleet in a denser layout. It is useful when the priority is comparing services rather than working with individual cards: scan running states, sort by resource usage and find the application that deserves attention.
- **Understand where resources are going** — The Resources workspace helps answer a practical question: is one application struggling, or is the whole machine under pressure?
- **Inspect processes and bring them into view** — The Processes workspace shows what is actually running on the host, including processes outside the managed fleet.
- **Follow logs while taking action** — The Logs workspace keeps investigation beside service control. Select an application, read its output and narrow the view to warnings or errors.

**Built with**

- **Application:** Python
- **Dashboard:** HTML, CSS, JavaScript
- **Configuration:** YAML
- **Monitoring:** psutil, Server-Sent Events
- **Integrations:** Docker, Docker Compose, systemd, SSH, UFW
- **Platform:** Linux

[Overview](https://github.com/logicencoder/universal-service-manager-overview)

### Logic Encoder Crypto App Store

![Crypto App Store catalogue, basket, payment progress and completed delivery](https://raw.githubusercontent.com/logicencoder/le-crypto-app-store-overview/a273c0866b31eca342d3e34f0c1d2db2358c27f8/assets/crypto-app-store-catalogue-basket-payment-delivery.png)

Selling digital products involves more than collecting a payment. Someone has to connect the purchase to the right files, keep the buyer informed and know whether delivery completed. Logic Encoder Crypto App Store brings that work into one purchase flow inside Telegram, with a browser storefront and a shared operator workspace.

**What it offers**

- **Browse and buy inside Telegram** — The storefront presents applications with images, descriptions, prices, versions and optional badges.
- **Clear instructions from checkout to confirmation** — The payment screen gives buyers the information needed to complete the purchase: an order reference, selected items, exact amount, destination address and remaining payment time.
- **Files delivered into the conversation** — After successful payment verification, the bot sends the purchased files directly to the buyer's Telegram chat.
- **Follow every order from one workspace** — The Orders area gives operators a live view of the sales queue. Summary figures and status filters make it easier to distinguish purchases waiting for payment, transactions being confirmed, completed deliveries and orders needing attention.
- **Keep products ready for sale** — The Warehouse brings catalogue information and deliverable availability together. Add and edit products, maintain prices and versions, manage availability and review the files associated with each application.

**Built with**

- **Application:** JavaScript, Node.js, Fastify
- **Interfaces:** HTML, CSS, JavaScript
- **Data:** DuckDB
- **Telegram:** Telegram Mini Apps, Telegraf
- **Payments:** Ethereum, USDC, ETH, ethers
- **Live updates:** WebSockets

[Overview](https://github.com/logicencoder/le-crypto-app-store-overview)

### Rocinante Command Center

![Rocinante Command Center simulated navigation](https://raw.githubusercontent.com/logicencoder/roci-command-center-overview/76d1af1701427683a75136a5c288d2611a859333/assets/rocinante-command-center-solar-system-tactical-deck.png)

Rocinante Command Center is a fictional ship interface you can operate: a command deck for a corvette-class light frigate with three sections, four switchable scenarios, a live-moving contact picture, a 3D solar system and hull schematic, and panels you can resize. Every reading, crew member, contact and radio channel is generated in the browser by a small simulation; nothing on it is a real observation of a real spacecraft. It is built for people who enjoy science-fiction interfaces and want one that behaves like a working one.

**What it offers**

- **Scenarios** — A scenario selector in the header switches the whole ship between four situations: Cruise, High-G Burn, Emergency and Comms Interference.
- **Nav and Tactical** — The first section is the navigation picture. A sensor grid shows generated contacts that move over time, and selecting one makes it the active contact across the deck.
- **Ship and Crew** — The second section covers the vessel itself. Propulsion Systems and the Epstein Drive Core show drive state, Power Distribution shows how demand is split, and Shield Grid Status with the Shield Integrity Map tracks the six shield sectors.
- **Comms and Sensors** — The third section holds five radio channels from fleet comms and emergency to deep-space and distress beacon, each with a frequency and a status.
- **Arrange the deck** — Panels are resizable and the sizes are remembered between visits in the browser. A reset control in the header restores the default layout.

**Built with**

- **Interface:** React 18, JavaScript, HTML and CSS with Tailwind utility classes
- **3D and charts:** Three.js for the solar system, hull, antenna and signal-field scenes; Recharts for the history plots
- **Simulation:** A local step simulation that advances velocity, fuel, drive temperature, shield strength and signal interference over time
- **Build:** Vite

[Overview](https://github.com/logicencoder/roci-command-center-overview)

### Logic Encoder Work Brain

![Logic Encoder Work Brain 3D knowledge graph](https://raw.githubusercontent.com/logicencoder/second-brain-overview/ade90436790d039dca7ef10b3221989c35a76dea/assets/logic-encoder-work-brain-3d-knowledge-graph.png)

Years of project notes, source documents, skills and decisions are useless when nobody can find them or relate one to another. Logic Encoder Work Brain is a personal knowledge system that turns a body of work into a searchable wiki and an explorable 3D graph, and lets an AI assistant answer questions from a small, reviewed packet of that knowledge instead of guessing. It serves one operator who builds and maintains many applications and wants every method, project fact and decision kept in one place that both a person and an assistant can read.

**What it offers**

- **The 3D graph** — Every note becomes a point and every link between notes a line. Colours separate work knowledge, project pages, skills and workflows, source documents and drafts, and the counters show how many notes, sources and connections the graph holds.
- **A wiki with sources** — Original documents stay unchanged as sources, and the assistant writes synthesis pages that cite them, record contradictions and keep a dated history of every accepted change.
- **Asking with a reviewed packet** — The workspace searches the knowledge, assembles the matching passages into a packet and shows it for review before anything leaves the machine.
- **Skills and libraries** — Reusable working methods are kept as skills: short instructions with checklists for building software, writing articles, reviewing code, securing changes, documenting products and working with the operator's servers.
- **Control panel and upkeep** — A control panel shows the health of the wiki, freshness of pages, retrieval quality, evaluation results of the skills and the state of the services the brain runs as.

**Built with**

- **Knowledge store:** Markdown wiki and immutable source files tracked in Git
- **Tooling:** Python command-line tools for validation, search, ingestion and audits
- **3D graph:** Node.js server with a prebuilt WebGL renderer
- **Workspace:** A Python web workspace for search, review and model questions
- **Model access:** OpenRouter, OpenAI and Anthropic APIs with keys held only in the running session

[Overview](https://github.com/logicencoder/second-brain-overview)

### MEXC Trading App

![MEXC Trading App dashboard with chart, order book and manual order panel](https://raw.githubusercontent.com/logicencoder/mexc_trading_app-overview/b79be717b87b75ccec6b3d8b426609f326df60b5/assets/mexc-trading-app-trading-dashboard-order-book.png)

Active trading can require repeatedly moving between a chart, order book, balances, order controls and automation settings. MEXC Trading Dashboard brings those views into a configurable trading desk so the operator can inspect the market and manage activity in one place.

**What it offers**

- **Arrange the trading desk** — Panels can be moved, resized and collapsed, and the arrangement is stored with Save Layout and restored with Reset Layout; Snapshot UI captures the current screen.
- **Inspect the market** — The market view combines a chart (a TradingView chart that can be switched on and off), the order book with its depth and the live trades tape.
- **Place and follow manual orders** — The Trading Panel places buy and sell orders beside the account balances. Size shortcuts set 25, 50, 75 or 100 percent of the available funds, or a fixed 25, 50, 100 or 250 dollars, or a custom amount.
- **Configure automation deliberately** — The Bot Panel offers five modes: Mode 1 Instant Execution takes orders from other traders inside a price range with market orders (with an execution style of TAKE, PING, 50/50 or RANDOM); Mode 2 Grid Limit Orders places layered limit orders and replenishes them when filled; Mode 3 Step Re-entry…
- **Manage several activities** — The Multi Bots workspace supports reviewing more than one configured bot context. Performance information helps examine trade and bot activity, while system statistics and debug logs assist with investigation.

**Built with**

- **Application:** Python, FastAPI
- **Supporting technologies:** HTML, CSS, JavaScript; MEXC; TradingView; WebSockets

[Overview](https://github.com/logicencoder/mexc_trading_app-overview)

### LE Karaoke Studio

![LE Karaoke Studio workspace with transcription, editor and timeline](https://raw.githubusercontent.com/logicencoder/le-karaoke-studio-overview/2ed33c86e42aa9774c3cfee7a482f40597e4e0c6/assets/le-karaoke-studio-work-transcription-editor-timeline.png)

Turning source audio or video into a finished karaoke or captioned clip usually means moving between download, stem separation, transcription, editing and export tools. LE Karaoke Studio puts those stages into one web application with ten workspaces: Studio (transcribe, edit lines, style and render), Audio Effects Lab and Video Effects Lab, Context Prompts, a Video editor, DLV (the downloader), UVR (vocal and stem separation), HW (a GPU watch panel), Automate (a managed publishing workflow) and Settings. It runs on a GPU machine under the operator's own control.

**What it offers**

- **Prepare and transcribe media** — Upload a clip or work through a batch, review its format and choose the part that should be processed.
- **Shape subtitles and visualisers** — Choose subtitle styling, line presentation and visualiser options to build a consistent look across clips.
- **Audio and visual effects workspaces** — The audio-effects and visual-effects areas let the operator experiment with the presentation around the clip.
- **Download and separate stems** — DLV downloads a source with progress and history, using yt-dlp, and UVR separates vocals from accompaniment as queued jobs with a choice of models.
- **Review, render and export** — Follow job progress, inspect results and download the finished video. Editing, trim and output options support different source material and export needs.

**Built with**

- **Application:** Python, FastAPI
- **Supporting technologies:** React, TypeScript; Whisper, PyTorch; FFmpeg, Remotion, HyperFrames; yt-dlp

[Overview](https://github.com/logicencoder/le-karaoke-studio-overview)

### LE HSCR — Radio Monitoring Workspace

![LE HSCR radio monitoring workspace](https://raw.githubusercontent.com/logicencoder/le-hscr-overview/fcbe22bb9830dc80983ea6d5e8b2455d5cc27e72/assets/le-hscr-radio-monitoring-workspace.png)

LE HSCR is a single-page radio monitoring console for Bluetooth LE, Wi-Fi and satellite reception. One browser window shows what the connected adapters and tuner can see, keeps the history of what was seen and puts the logs of all radios in one stream. It runs in a Docker container with the USB adapters passed through, or directly on a prepared host, and by default it stays on the local network with no telemetry. It is meant for authorised radio research on equipment and networks the operator owns or is allowed to test.

**What it offers**

- **Overview** — The Overview tab summarises all radios on one screen: Bluetooth, Wi-Fi and monitor key figures, the state of each adapter and the statistics of the current session.
- **Bluetooth LE** — The Bluetooth tab scans actively or passively and parses iBeacon and Eddystone advertisements into readable fields.
- **Wi-Fi** — The Wi-Fi tab scans for networks in managed or monitor mode and shows a spectrum trace with a waterfall.
- **Satellite reception** — The satellite area detects and identifies the tuner, powers it, and tunes by transponder or manually.
- **USB devices and logs** — The USB area lists attached devices with their status and can refresh or reset a device, which is the first check when an adapter disappears.

**Built with**

- **Backend:** Python with FastAPI
- **Interface:** One HTML page with JavaScript, draggable panels and charts
- **Radios:** Bluetooth LE adapter, Wi-Fi adapter in managed or monitor mode, DVB satellite tuner or SAT>IP
- **Packaging:** Docker image based on Kali Linux, or a direct install on Ubuntu

[Overview](https://github.com/logicencoder/le-hscr-overview)

### WP Visitor Stats

![WP Visitor Stats dashboard with visits, content and audience panels](https://raw.githubusercontent.com/logicencoder/wp-visitor-stats-plugin-overview/573c313132c88976cf8010599765a73789680ce2/assets/wp-visitor-stats-dashboard-dark.png)

Understanding a website's audience can become fragmented across traffic reports, campaign tools and access logs. WP Visitor Stats brings those views into WordPress, helping the owner inspect how people reach the site, what they use and where a closer look is needed.

**What it offers**

- **Understand visits and content** — The overview brings key traffic information together, while content reports help examine which pages receive attention.
- **Explore audience context** — Geographic and technology reports add context about where visits come from and how the site is being used.
- **Connect campaigns and interactions** — Campaign reports, custom events and interaction heatmaps help examine how visitors engage beyond the initial page view.
- **Separate automation and unwanted traffic** — Bot activity and ban-management views help the owner inspect traffic that needs a different response.
- **Maintain the analytics workspace** — Settings cover the data-retention period (180 days by default), the excluded addresses and the tracking options.

**Built with**

- **Application:** PHP, WordPress
- **Supporting technologies:** JavaScript, HTML, CSS; MySQL

[Overview](https://github.com/logicencoder/wp-visitor-stats-plugin-overview)

### System Monitor App

![System Monitor App terminal dashboard](https://raw.githubusercontent.com/logicencoder/system-monitor-app-overview/d254228adc2cccd1bde1f951493a704bdd7c1990/system-monitor-app-terminal-dashboard.png)

A quick host check should not require opening several monitoring utilities. System Monitor App brings resource use, processes and service information into a terminal workspace, making it useful for both local administration and remote command-line sessions.

**What it offers**

- **Read the machine at a glance** — The screen is built from panels: CPU (with per-core load), Memory and swap, Network, Disk, GPU, Sensors (temperatures where the hardware reports them) and the monitor's own usage.
- **Find the process behind the load** — The Process panel lists running processes and sorts them by CPU or by memory with one key, so the biggest consumer is at the top.
- **Check surrounding services** — The Services panel shows the state of a list of important systemd services, and the Firewall panel shows the number of connections blocked by iptables or nftables.
- **Keep attention on changes** — The Alerts panel keeps a history of the last 100 alerts raised by conditions you choose to watch.
- **Use a consistent remote workspace** — It is a single program built with Textual and psutil, distributed as one self-contained Linux executable, so it runs in an ordinary SSH session without a graphical desktop on the monitored machine.

**Built with**

- **Application:** Python
- **Supporting technologies:** Textual; psutil; Linux

[Overview](https://github.com/logicencoder/system-monitor-app-overview)

### Celestial Lab

![Celestial Lab satellite map with a 3D globe of orbiting objects](https://raw.githubusercontent.com/logicencoder/celestial-lab-plugin-overview/75f0c881bf7ccb1e8403e5c7ca94fd8cdb3036f3/assets/celestial-lab-satellite-map-3d-globe-orbits.png)

Space information is spread across orbital catalogues, solar observations, mission schedules and astronomy archives. Celestial Lab brings seven related experiences into one workspace: start with a source-aware summary, then inspect the objects, observations or events behind it without switching applications.

**What it offers**

- **A source-aware space overview** — The opening board brings satellites, space weather, solar activity, provider-reported crew, exoplanets, asteroid encounters and launches together.
- **Satellites: from orbital context to an object** — Satellite Map lets users explore published orbital catalogues, filter orbital bands, follow ISS or Tiangong and add the separately loaded Starlink layer.
- **Space weather and aurora exploration** — Aurora outlook, Space environment, Solar wind and Alerts help relate geomagnetic activity to the underlying measurements and messages.
- **Observe the Sun without confusing images and models** — Sun Live combines an observed solar disk, selectable wavelengths, reported active regions, flares and statistics.
- **People in space and station context** — People in Space separates the provider-reported roster, mission duration, station context and list history.

**Built with**

- **Application:** WordPress, PHP, JavaScript, HTML, CSS
- **Interactive visualization:** Three.js, Globe.gl, WebGL
- **Data collection:** Python

[Overview](https://github.com/logicencoder/celestial-lab-plugin-overview) · [Open application](https://logicencoder.com/celestial-lab/)

### ETH Gas Live

![ETH Gas Live dashboard with gas price chart and fee tiers](https://raw.githubusercontent.com/logicencoder/eth-gas-live-plugin-overview/0cafbf56bb6dccdd61aa9cd2831f681cc8dfea47/assets/eth-gas-live-dashboard-gas-price-chart.png)

A gas quote is only useful when it answers a practical question: what will this transaction cost, and is now a good time? ETH Gas Live is a real-time Ethereum fee dashboard on logicencoder.com that turns every new block into three send tiers, a congestion read-out, history, a fee calculator and alerts, and explains the numbers on eleven dedicated pages. It is for anyone who sends, swaps or builds on Ethereum and wants to pay a fair fee instead of guessing.

**What it offers**

- **Read current transaction conditions** — The main dashboard shows three send tiers per block: Base Route (economical), Standard Way and Faster Inclusion, each with a fee estimate that follows the EIP-1559 base fee and priority fee.
- **Compare recent patterns** — History charts show how fees moved over recent hours and days, and a heatmap lays the hours of the week out in a grid so the usually cheap and the usually expensive periods are easy to spot.
- **Estimate a specific task** — The Fee Calculator multiplies a gas limit by a gas price.
- **Explore deeper statistics** — Network Statistics has three tabs: an overview, detailed measures and a time analysis, and the backend adds a congestion index (Inclusion Pressure Index) and a spike score.
- **Publish and operate the experience** — WordPress embedding and site-operator tools support making the dashboard part of a wider site.

**Built with**

- **Application:** PHP, WordPress
- **Supporting technologies:** HTML, JavaScript; Chart.js and Tailwind CSS (both loaded from a public CDN); Ethereum

[Overview](https://github.com/logicencoder/eth-gas-live-plugin-overview) · [Open application](https://logicencoder.com/ethereum-gas-tracker/)

### MEXC Live Statistics

![MEXC Live Statistics dashboard with market trades and analytics](https://raw.githubusercontent.com/logicencoder/mexc-live-stats-plugin-overview/f6dcf708abb56af0f24a134d11fda7ed140583f7/assets/mexc-live-statistics-live-dashboard-market-trades.png)

MEXC Live Statistics is a real-time dashboard for MEXC spot markets, published on logicencoder.com. A visitor picks a coin and sees its price, 24-hour statistics, volume and buy/sell balance, a stream of recent trades and detected bot activity, all updated live over a WebSocket connection. The site operator gets a Coin Manager, connection monitoring and the search-engine tooling to publish each coin as its own page.

**What it offers**

- **Choose the market to explore** — Visitors pick a pair from the coin catalogue; the market header keeps the selected pair and its context visible.
- **Connect price with trading context** — One coin page combines several panels that all follow the selected pair live: Current Market Overview (price and 24-hour figures), Volume Analysis, Buy/Sell Analysis (how trading splits between buyers and sellers), Trade Analytics, Bot Activity and a live tape of recent trades.
- **Keep the market catalogue useful** — The Coin Manager is the operator's catalogue workspace.
- **Monitor the publishing experience** — The monitoring area shows the live health of the data connection: WebSocket throughput, download speed and messages per second over the last three hours, the number of subscribed pairs, server metrics and system logs.
- **Support discovery and presentation** — Every coin can be published as a server-rendered HTML page with Schema.org structured data, so search engines see the content without running JavaScript.

**Built with**

- **Application:** PHP, WordPress
- **Supporting technologies:** HTML, CSS, JavaScript; MEXC public market data; WebSockets; optional TradingView chart (off by default)

[Overview](https://github.com/logicencoder/mexc-live-stats-plugin-overview) · [Same thing for the Gate exchange: Gate Live Statistics](https://github.com/logicencoder/gate-live-stats-plugin-overview)

### Le Sound Normalizer

![Le Sound Normalizer with compressor knobs and 15-band equalizer](https://raw.githubusercontent.com/logicencoder/le-sound-normalizer-overview/7344dee31d360d8ccbcd3850b46fb6ba634ed37f/assets/le-sound-normalizer-15-band-equalizer-compressor.png)

Le Sound Normalizer is a Windows audio tool that keeps loud scenes from overpowering quiet dialogue. Turn the volume up so speech is understandable and the next explosion would normally blast out; the normalizer holds the output under a ceiling you choose and evens out the gap between quiet and loud passages, so a film, a series or a game stays comfortable at one listening level. It runs as a small controller window next to a native audio component that sits in the Windows audio path, so it works with the player you already use. Built and maintained by Logic Encoder at logicencoder.com.

**What it offers**

- **Ceiling and compression** — Choose a loudness ceiling and how firmly loud material is pulled toward quiet material, with Soft, Balanced and other compressor characters.
- **Meters and spectrum** — LED meters per output, a live spectrum, an oscilloscope waveform and connection status.
- **Equalizers** — A simple bass, middle and treble tone control and a 15-band graphic equalizer with their own values.
- **Presets and themes** — Save sound presets for film, evening or music, and switch between green and cyan palettes.

**Built with**

- **Controller:** C#, Windows Forms, .NET Framework 4.8, x64
- **Audio component:** C++ Windows audio processing object (APO) loaded by the Windows shared-mode audio engine
- **Compatibility engine:** WASAPI capture and playback with NAudio (MIT licence) and an existing VB-CABLE installation
- **DSP:** 32-bit floating-point processing for 1, 2, 6 and 8 channels, sample-peak limiter, compression, tone and graphic equalizer
- **Controller to component link:** Shared settings block with revision and sequence ownership, bounded telemetry ring
- **Packaging:** Single setup executable with controller, audio component and runtime files

[Overview](https://github.com/logicencoder/le-sound-normalizer-overview)

### Ethereum Chain Swap Monitor

![Ethereum Chain Swap Monitor swap detail with pool liquidity breakdown](https://raw.githubusercontent.com/logicencoder/eth-chain-swaps-monitor-overview/8fe4193f20b100d6523d750b175e89951727ae87/assets/eth-chain-swap-monitor-pool-liquidity-breakdown-swap-detail.png)

Ethereum Chain Swap Monitor follows swaps on Ethereum in real time. A Python process reads new blocks and logs from an Ethereum node, recognises swaps in known liquidity pools, values them in dollars and shows them in a live dashboard with alerts, the most active addresses, saved quote tables and a live terminal. It is a self-hosted operator tool for people who want to watch large or unusual swap activity as it happens.

**What it offers**

- **Follow the live swap feed** — The Live Alerts Feed keeps the latest 250 swaps in a list that can be scanned and expanded for detail; auto-expand opens new entries as they arrive and a freeze switch stops the list moving while you read.
- **Investigate recurring addresses** — The Top 20 Most Active Addresses ranking shows the participants that recur in the observed swaps, and the search box looks up any address.
- **Keep comparisons nearby** — Saved Quote Tables keep a quote per pool for comparison next to the feed; Refresh quotes updates them and they can be ordered latest or oldest first, by coin name (A to Z or Z to A) or by liquidity (highest or smallest).
- **Watch the operating context** — The Live Terminal shows what the monitor is doing and can be disabled or cleared.
- **Choose a comfortable presentation** — Three themes (dark, medium and light) change the colours, and every panel can be collapsed, which helps when the monitor stays open for a long session.

**Built with**

- **Application:** Python
- **Supporting technologies:** HTML, CSS, JavaScript; Ethereum; WebSockets

[Overview](https://github.com/logicencoder/eth-chain-swaps-monitor-overview)

### CEX/DEX Arbitrage App

![CEX/DEX Arbitrage App with pool discovery, arbitrage scanner and trading rules](https://raw.githubusercontent.com/logicencoder/cex-dex-arb-overview/5a6b8c1144a49414fa3fb7ccf8cf3581b60bbd86/assets/cex-dex-arbitrage-app-pool-discovery-arb-scanner-trading-rules.png)

Comparing an exchange price with a decentralised market is only the beginning of evaluating an opportunity. This dashboard brings market screening, trade-size comparisons and execution controls into one workspace, helping the operator inspect the opportunity in context before acting.

**What it offers**

- **Build a useful watchlist** — Load pools reads the stored pools, Active Coins keeps the markets under review as tabs, and Live stats and Pool Info show the selected pair and its pool.
- **Compare both directions** — The Arbitrage tables show buying on the exchange and selling on the DEX, and the reverse, for several trade sizes.
- **Screen and refine opportunities** — The ARB SCANNER has tabs for Discover (new candidate pairs, each of which can be sent to the queue or ignored), the Pool tester queue, the Ignore list and the stored coins with their pool details (pair, DEX type, fee, token), which come from the pool lab or are saved by hand.
- **Inspect market context** — Live Orderbooks for MEXC and Gate.io, the account's own trades and all trades on each exchange, and a TradingView chart sit beside the comparison, so depth and recent movement can be checked before an action.
- **Keep execution deliberate** — A Manual Swap panel buys or sells through the MEV-protected route, and the Swap gate readout shows whether swapping is currently allowed.

**Built with**

- **Application:** Python, FastAPI
- **Supporting technologies:** HTML, CSS, JavaScript; Web3.py; MEXC, Gate, Uniswap; TradingView

[Overview](https://github.com/logicencoder/cex-dex-arb-overview)

### Red-Team Lite

A quick security check of a web application should not need a heavy toolchain. Red-Team Lite crawls a target site, probes the discovered routes and parameters for common weaknesses, captures browser screenshots of serious findings and writes a report in JSON and Markdown. It serves developers and security testers who want a fast first pass over an application they own or have written permission to test.

**What it offers**

- **Discovery** — The scanner starts at the target address, follows links up to a chosen crawl depth and collects routes, forms and input parameters.
- **Probes** — Each discovered route is tested for exposed files such as configuration and repository metadata, reflected cross-site scripting, SQL injection through error disclosure, local file inclusion, server-side request forgery, template injection and open redirects.
- **Evidence and reports** — Findings are rated by severity, and critical and high findings get a Playwright screenshot as visual evidence.
- **Web form** — The web page asks for the target address, optional test credentials and the crawl depth, starts the scan and lists the findings with their severity when it finishes.

**Built with**

- **Scanner:** Python with a crawler and HTTP probes
- **Evidence:** Playwright with Chromium for screenshots
- **Interface:** Command line, a FastAPI endpoint and a single-page web form
- **Reports:** JSON and Markdown files

[Overview](https://github.com/logicencoder/redteam-lite-overview)

### LE Media Player

A fast, native desktop media player for Linux with a real-time equalizer, loudness control and a large set of music visualizers — built in Rust with no browser engine inside. It plays local audio and video, YouTube and other URLs, and keeps a Winamp-style playlist under keyboard and drag-and-drop control, for people who want one lightweight player for listening, tuning sound and watching video.

**What it offers**

- **Origin: a Rust rewrite of the AFX lab** — LE Media Player is the Rust rewrite of the AFX lab from the Logic Encoder karaoke studio — the browser-based audio-effects and visualizer workspace — as a standalone desktop application with no browser engine.
- **Beyond the browser lab** — Moving the engine into a native process opened up features that a web page cannot offer, and the player adds them on top of the original lab:
- **Sound and effects** — The effects rack is built for tuning sound while it plays. A 20-band equalizer ships with presets such as Flat, Rock, Metal, Techno, Bass boost, Pop, Vocal and Classical, plus manual gain per band and a pre-amp.
- **Visualizers** — Visualizers react to the live spectrum and to an adaptive beat detector. The collection covers bars, waveforms, particle effects and circular spectrum modes with a mirrored variant, a bass-driven orb, frequency rings and a cymatics plate.
- **Playlist** — The playlist follows Winamp conventions. Files and whole folders can be dropped in; folders are scanned recursively and the drop position decides where items land, with an insertion line and auto-scroll while dragging.

**Built with**

- **Language:** Rust (2021 edition)
- **Audio:** cpal output, ffmpeg decoding, rustfft analyser, lock-free ring buffers
- **DSP:** Custom 20-band biquad equalizer, loudness normalizer, soft limiter, WSOLA time stretch
- **UI:** egui / eframe (OpenGL), Slint, GTK4 — three frontends on one engine library
- **Integration:** MPRIS over D-Bus (zbus), X11 and Wayland, .desktop entry, portable bundle
- **Online sources:** yt-dlp

[Overview](https://github.com/logicencoder/le-media-player-overview)

### Dynex MEXC Balance Monitor

![Dynex MEXC Balance Monitor dashboard with balance, in and out charts and transaction feed](https://raw.githubusercontent.com/logicencoder/dynex-mexc-balance-monitor-plugin-overview/8b2c6d80a105ee7ceb0ac9247f2a88e8e4670eb4/assets/dynex-mexc-balance-monitor-live-dashboard-in-out-charts.png)

Exchange balances move the Dynex market, and the movements are easy to miss in a chain explorer. Dynex MEXC Balance Monitor is a WordPress dashboard on logicencoder.com that shows the DNX balance held by the monitored MEXC wallet, every deposit and withdrawal as a live feed, and charts of net flow, volume and balance over time. It serves holders and analysts who follow exchange flows of Dynex.

**What it offers**

- **Balance and totals** — The top of the dashboard shows the current balance, total incoming and outgoing DNX, transaction counts and the progress of the chain scan.
- **Live IN/OUT feed** — The feed lists transactions as they arrive, with direction, amount, address and time. A direction filter, a search box and a minimum amount keep it readable, and the list can be exported as CSV.
- **Charts and analytics** — Four interactive charts show net flow, incoming against outgoing volume, transaction count and balance over time, each with its own period of hourly, daily or weekly steps and a timespan from 24 hours to 30 days.
- **Administration** — The settings page holds the API key used by the data worker, the poll mode, thresholds, storage caps, diagnostics and row purging.

**Built with**

- **Plugin:** PHP and WordPress with a shortcode, a REST API and an admin settings page
- **Front end:** JavaScript, CSS, WebSocket and AJAX updates, interactive charts
- **Data worker:** A Python worker that scans the Dynex chain and posts summaries to the site
- **Storage:** WordPress database tables trimmed by scheduled jobs

[Overview](https://github.com/logicencoder/dynex-mexc-balance-monitor-plugin-overview) · [Open application](https://logicencoder.com/dynex-mexc-balance-monitor/)

### TS Analyzer

![TS Analyzer inspecting an actual receiver transport stream](https://raw.githubusercontent.com/logicencoder/ts-analyzer-overview/0d6b2ffbd7964526782d51f9fec36e1c8ad081d5/assets/ts-analyzer-transport-analysis.png)

A television stream can look unstable for several different reasons: reception, tuning, transport errors or the content being carried. TS Analyzer brings those checks into one browser workspace, helping an operator move from choosing a satellite source to inspecting the arriving stream and retaining useful findings.

**What it offers**

- **Find a source and prepare a scan** — Discover a SAT>IP receiver or choose one manually, then prepare the satellite positions and switch sources to investigate.
- **Inspect the scan results** — The results workspace collects transponder observations, television services and radio services for later review.
- **Examine the transport stream** — On an Enigma2 receiver, Analyze current TV inspects the programme already being watched without changing the TV channel.
- **Keep reception and transport separate** — When a supported receiver supplies RF measurements, inspect strength, SNR and available error readings alongside the transport observations.
- **Inspect a real constellation source** — The constellation view accepts current external I/Q samples from compatible measurement equipment.

**Built with**

- **Core stack:** Rust; Python; FastAPI; JavaScript; HTML; CSS

[Overview](https://github.com/logicencoder/ts-analyzer-overview)

### LE Settings

![LE Settings administration console](https://raw.githubusercontent.com/logicencoder/le-settings-plugin-overview/bb65c6d7748d5787a647417964705b8f1b6cf4f6/assets/le-settings-admin-console-overview.png)

Site operations often become a collection of unrelated settings pages, alerts and logs. LE Settings brings the site's supported operational controls into one WordPress console, helping the owner review protection, notifications and publishing-related preferences with less switching.

**What it offers**

- **See the current site setup** — The Status tab is the starting point: it lists which protections and trackers are switched on and how notifications are configured, so the intended behaviour of the site is visible before an issue is investigated.
- **Keep important events visible** — The Telegram tab holds the bot token and chat ID, a master switch, alert throttling with a limit on alerts per hour so a burst of events cannot flood the chat, an optional country in each message and a test message button.
- **Maintain protection and access preferences** — The Protection tab switches on brute-force protection with a maximum number of failed attempts and a base lockout time that grows with repeated failures (progressive lockout), an IP whitelist that is never blocked or tracked and an IP blacklist that is always blocked, blocking of locked-out…
- **Manage publishing and traffic context** — The SEO tab covers descriptions, noindex for paginated pages, hiding excerpts from crawlers and allow rules written into robots.txt, and the Redirects tab manages path redirects with a type, or a 410 Gone when no target is given.
- **Investigate and adapt** — The Debug tab shows the plugin's own log with refresh and clear buttons, and log tables can be filtered.

**Built with**

- **Application:** PHP, WordPress
- **Supporting technologies:** HTML, CSS, JavaScript; Telegram

[Overview](https://github.com/logicencoder/le-settings-plugin-overview)

### Logic Encoder Enhanced Theme

![Logic Encoder Enhanced WordPress theme front page](https://raw.githubusercontent.com/logicencoder/logic-encoder-theme-overview/8e5a586b41684e5d0334b9169c93d9a22c014dc2/logic-encoder-theme-wordpress-front-page.png)

A WordPress site that presents software products, technical writing and member pages needs one visual system and one place to change it. Logic Encoder Enhanced is a custom theme for exactly that: a dark, technical design with a homepage built from editable sections, a manager for the application catalogue, page templates for the sign-in and account journey, and a long list of Customizer controls. It is built for a site owner who wants to change text, colours, fonts and layout from the WordPress Customizer instead of editing template files.

**What it offers**

- **Homepage** — The front page is assembled from sections whose wording the owner edits in the Customizer: a hero with an eyebrow line, a description, an optional animated terminal that types out a list of lines, and a row of pills; then an approach block, a capabilities block, an applications teaser, a blog…
- **Application catalogue** — The App Manager adds an administration page for the application catalogue, with adding, editing, deleting and reordering done in place without page reloads.
- **Pages and templates** — Dedicated templates cover the pages a product site needs: homepage, blog, about, contact, sign-in, forgot password, reset password, email verification, account, dashboard, single post, search results and a 404.
- **Customizer controls** — Appearance is controlled in one place: heading, body, navigation and logo fonts, a base font size, a colour preset, two border-radius sizes, content margins and the width of the homepage wrapper.
- **Member shortcodes** — The theme registers shortcodes for content that depends on who is reading. Wrapping text in them shows it only to logged-in users, to administrators, to a chosen role or to a membership level of basic, premium or VIP, and visitors who do not qualify see a short message with a link to sign in.

**Built with**

- **Theme:** PHP and WordPress template hierarchy with Customizer API settings
- **Front end:** HTML, CSS and JavaScript, with effects that can be switched off
- **Administration:** A custom application manager and custom list screens for pages and posts
- **Verification:** Playwright end-to-end tests

[Overview](https://github.com/logicencoder/logic-encoder-theme-overview)

### Russian DC Observatory

![Russian DC Observatory populated public overview](assets/russian-dc-observatory-connectivity-overview.png)

Internet incidents, provider announcements and website-access measurements answer different questions. Russian DC Observatory brings them into one research workspace while keeping their sources and uncertainty visible. It helps users compare evidence about Russian Internet connectivity, named services and infrastructure without treating every complaint or missing observation as proof of an outage.

**What it offers**

- **Start with the evidence available** — The overview brings service observations, network incidents, traffic context and source freshness together.
- **Follow providers, services and maintenance** — The Services view groups provider-reported components, incident references and scheduled maintenance.
- **Investigate website access and remote observations** — The Access view presents website-access measurement samples and their coverage. Category counts, domain subsets and network context help users interpret the available observations.
- **Compare infrastructure and network context** — Facility and map views make the infrastructure catalogue easier to explore geographically.
- **Watch relevant changes** — Watchlists let users focus on the sites and provider components they care about. The in-app change feed helps revisit meaningful accepted changes to watched evidence.

**Built with**

- **Application:** Python; SQLite
- **Dashboard:** JavaScript; HTML; CSS; SVG
- **Administration:** WordPress; PHP

[Overview](https://github.com/logicencoder/russian-dc-observatory-monitor-overview) · [Open application](https://logicencoder.com/russian-dc-observatory/)

### Awair Monitor Dashboard

![Awair environmental metrics and measurement history](https://raw.githubusercontent.com/logicencoder/le-awair-monitor-dashboard-overview/1154807b0cd2a9dd009256f177a5bbb623567599/assets/awair-monitor-dashboard-air-quality-score-trend-history.png)

Indoor conditions are easier to understand when the latest readings can be compared with what happened earlier. Awair Monitor Dashboard brings Awair Element measurements, trends and history into one workspace, helping users notice changes in a room without repeatedly switching between device readings and separate reports.

**What it offers**

- **See the room at a glance** — The front page shows a score gauge and one card per measurement (temperature, humidity and the air-quality values the device reports), read live from the Awair Element's local interface.
- **Compare changes over time** — Trend charts and the score history show whether a change was brief or part of a longer pattern.
- **Explore daily patterns** — The Daily, Trends and Correlations views summarise each day, show how measurements moved and rank which ones move together, and Uptime shows how reliably the device reported.
- **Keep and share useful results** — A period of readings can be exported as CSV or JSON for separate analysis. The history is kept in a local SQLite database, so an earlier period can always be revisited.
- **Make the dashboard comfortable** — Two visual styles, Aurora and Nexus, and an English and Slovak interface are available. In Settings the operator can configure notifications through a webhook or an ntfy address, send a test message and snooze alerts for a while; a Logs page shows what the collector has been doing.

**Built with**

- **Core stack:** Python; Svelte; JavaScript; SQLite

[Overview](https://github.com/logicencoder/le-awair-monitor-dashboard-overview)

### Slovak Air Quality Dashboard

![Slovak Air Quality Dashboard history of hourly readings and station changes](https://raw.githubusercontent.com/logicencoder/air-quality-bridge-overview/42e86a73e4c0228d0a01324f2fe9c00f0281804c/assets/slovak-air-quality-dashboard-history-hourly-source-index.png)

A single pollution reading means little without the station, the time and the surrounding history. The Slovak Air Quality Dashboard brings the hourly readings of every station in Slovakia's national monitoring network into one board and one map, so residents, parents, runners and anyone curious about the air can see where the air is clean, where it is not and how that changed over the last hours and days. It runs on logicencoder.com and updates every hour, matching the cadence of the published data.

**What it offers**

- **Overview: the current picture** — The Overview view opens with a live summary: how many stations reported in the latest snapshot and how many of them report a numeric quality index.
- **Map: air quality in its place** — The Map view places every station on a Leaflet map and colours each marker by its quality class.
- **Stations** — The Stations view is the searchable directory. Filter by name or quality class, and read each station's readings together with their observation times, in the same quality colours as everywhere else in the dashboard.
- **Pollutants** — The Pollutants view separates the measurements the network publishes: particulate matter PM10 and PM2.5, nitrogen dioxide, ozone and sulphur dioxide, all in micrograms per cubic metre.
- **History and day comparison** — History looks beyond the latest hour. Choose a period and a station or pollutant and the chart shows the hourly readings over that window; the Compare tools line up days against each other.

**Built with**

- **Data collection:** Python worker that polls the public API of the Slovak national monitoring network (SHMU) once an hour
- **History:** SQLite with one reading per station and hour, source revisions merged into the existing record
- **Delivery:** REST ingest with an API key into a WordPress plugin written in PHP
- **Interface:** Server-rendered table with delegated JavaScript for sorting, filtering and paging; AJAX refresh
- **Map:** Leaflet with station markers and fullscreen mode
- **Charts:** Lightweight in-house chart script (distribution, history and comparison charts)

[Overview](https://github.com/logicencoder/air-quality-bridge-overview)

### Dynex Large Transactions

![Dynex Large Transactions live transaction feed](https://raw.githubusercontent.com/logicencoder/dynex-large-transactions-plugin-overview/7272500cdab077e7e8f7dc234a7918703a1a9b08/assets/dynex-large-transactions-live-transactions-expanded.png)

Large transfers can disappear into a busy chain feed. Dynex Large Transactions gives visitors a focused view of those movements, with summary figures, address search and transaction details in a WordPress dashboard.

**What it offers**

- **Follow the relevant transfers** — The feed lists large Dynex transfers in a table with date and time, block, transaction hash, direction (sent or received) and amount.
- **Read the broader context** — A statistics panel puts the feed in perspective: total transactions with the split into sent and received, counts for today, the last 24 hours, 7 days and 30 days, hourly and daily velocity, the average transaction, the total volume and the date of the oldest data.
- **Search by address** — The search box takes a wallet address and returns the transactions in which it takes part, in the same table, so a known participant can be followed without scanning the whole feed.
- **Publish and maintain the dashboard** — The dashboard is embedded with a shortcode whose attributes set the initial number of transactions, the refresh interval, the heading, and whether the statistics panel and the search box are shown.

**Built with**

- **Application:** PHP, WordPress
- **Supporting technologies:** HTML, CSS, JavaScript; Dynex

[Overview](https://github.com/logicencoder/dynex-large-transactions-plugin-overview)

### React + Vite Architecture Guide

![React and Vite project architecture diagram](https://raw.githubusercontent.com/logicencoder/react-vite-architecture-for-dummies/4f156135dfad47f9517db68415e481718a8361b0/react-vite-architecture-diagram.png)

A plain-English walk through every file and folder of a React and Vite project: what each one is, why it exists and how they connect. It ends with the "injection chain" that explains how the browser gets from index.html to a running component tree, and a one-page diagram of the whole structure. The same kind of architecture diagram can be produced for any project so that other people understand how it is built.

**What it offers**

- **Files and folders explained** — Config files, the source folder and the build output are described one by one, including what is safe to ignore.
- **The injection chain** — Shows how index.html, main.jsx and App.jsx lead to rendered components.
- **Quick reference** — A one-page summary of the five things worth remembering about a Vite project.

**Built with**

- **Subject:** React, Vite, JavaScript, npm project structure
- **Format:** long-form Markdown guide with an architecture diagram

[Overview](https://github.com/logicencoder/react-vite-architecture-for-dummies)

### SatPI — SAT>IP server for the Vu+ Duo 4K SE

A fork of the open-source SatPI SAT>IP server that makes it work on the Vu+ Duo 4K SE, a Broadcom NEXUS receiver with dual FBC DVB-S2 tuners where the upstream version delivered no data on the second tuner bank and could not switch DiSEqC. The fork was verified end to end on OpenPLi 9.2 with DVBViewer switching three orbital positions while the receiver software keeps running. A first-hand write-up with measurements and packet captures is published on logicencoder.com.

**What it offers**

- **Crash fixes** — A client closing a connection mid-write no longer kills the daemon, and empty keepalive requests no longer crash it.
- **NEXUS demultiplexer model** — Same-descriptor source selection, mid-stream PID changes and safe emulation of the all-PIDs request.
- **DiSEqC on FBC tuners** — Child tuners route DiSEqC through the already-open root frontend in the correct tone, voltage, command and mini-burst order.
- **Client compatibility** — Case-insensitive SAT>IP parameters and a relaxed retune when a client sends stale channel-list values.

**Built with**

- **Language:** C++ (upstream SatPI codebase)
- **Protocols:** SAT>IP over RTSP and HTTP, DVB-S/S2, DVB-T/T2, DVB-C
- **Target:** Vu+ Duo 4K SE, Broadcom bcm7335 NEXUS, dual FBC DVB-S2
- **Build:** ARM cross-toolchain, statically linked

[Overview](https://github.com/logicencoder/satpi)

### TechniSat SkyStar USB 2 HD CI — Linux driver and SAT>IP

The stock Linux driver cannot lock DVB-S2 on the TechniSat SkyStar USB 2 HD CI card, which is why many owners discard it. This project ships one out-of-tree kernel module with three fixes on top of the community DVB-S2 patch (DVB-S2 lock, signal scale and SNR calibration), plus a minisatip SAT>IP server for free-to-air channels. After the patch the card tunes and plays DVB-S2, reports signal and SNR in DVBViewer, TransEdit and the minisatip web page, and switches DiSEqC ports.

**What it offers**

- **DVB-S2 lock** — The patched stb0899 locks and tunes DVB-S2 transponders that the stock driver cannot.
- **Signal and SNR** — Calibrated readings appear in DVBViewer, TransEdit and the minisatip web page.
- **Full scan and DiSEqC** — Complete transponder scans with NIT and multi-dish port switching work from the SAT>IP clients.

**Built with**

- **Driver:** out-of-tree Linux kernel module (stb0899 patch)
- **Server:** minisatip SAT>IP on RTSP port 8554
- **Tested on:** Ubuntu 24.04 LTS, kernel 6.8
- **Clients:** DVBViewer, TransEdit, VLC, ffprobe

[Overview](https://github.com/logicencoder/technisat-skystar-usb-2-hd-ci-satip)

### XEX Spread Monitor

The same coin often trades at slightly different prices on different exchanges, and most of the difference disappears once fees are paid. The XEX Spread Monitor compares every pair that is listed on both MEXC and Gate in USDT, refreshes the comparison every thirty seconds and keeps a log of every snapshot, so a reader can tell a lasting price gap from a one-off glitch and see which gaps are still positive after round-trip fees. It runs on logicencoder.com from public price data.

**What it offers**

- **Overview** — The Overview gives the key numbers of the latest snapshot: how many pairs are listed on both exchanges, the median absolute gap across them, the best net edge after fees, how many pairs still beat round-trip taker fees, the time of the last snapshot in UTC and the number of snapshots in the log.
- **Spreads** — Spreads is the full table of shared pairs. Each row shows the route (buy on one exchange, sell on the other), the gross gap, the fees and the net executable edge after round-trip taker fees, the volume of the thinner side and a suspect flag.
- **Opportunities** — Opportunities lists the pairs where the gap survives taker fees on both legs, ranked by net edge.
- **Volume** — The Volume view is the liquidity check: the volume leaders and the gap plotted against liquidity.
- **History** — History is derived from the monitor's own spread log, which stores every poll cycle since deployment.

**Built with**

- **Collection:** Python worker fetching the all-pairs public tickers of MEXC and Gate every 30 seconds
- **Computation:** Shared USDT pairs only, combined 24-hour volume floor, gap as MEXC last price over Gate last price, plausibility cut-off for broken or mismatched tickers
- **History:** SQLite log of every snapshot (prices, bids and asks on both sides, gap, direction, both volumes)
- **Delivery:** Authenticated REST ingest into a WordPress plugin written in PHP
- **Interface:** JavaScript workspace with sortable tables, charts and adjustable fees and liquidity filter

[Overview](https://github.com/logicencoder/xex-spread-bridge-overview)

### Deriv Board

Funding rates, open interest and trading volume each describe a different part of a derivatives market, and every venue publishes them in its own format. Deriv Board collects the public data of perpetual futures on five venues (Binance, Bybit, Hyperliquid, Aster and Lighter) into one workspace, so traders and researchers can compare the cost of holding a position, see where open interest sits and spot crowded markets without opening five sites. It runs on logicencoder.com from public endpoints and needs no exchange account.

**What it offers**

- **Overview** — The Overview shows a snapshot of the whole board: the number of perpetual markets tracked across the five venues, combined 24-hour volume and combined open interest, the markets with the highest and lowest funding right now, how many markets have positive funding (longs pay shorts) and how many…
- **Markets** — The Markets view is the full table: one row per venue and symbol with mark price, funding rate, time to the next funding, open interest, its change against 24 hours ago, 24-hour volume and a small funding trend drawn from stored history.
- **Funding** — The Funding view studies the rate itself: a histogram of funding across markets, the extremes at both ends and a cross-venue funding difference for the same symbol, which shows where one venue charges noticeably more or less than another.
- **Open Interest and Volume** — Open Interest is a leaderboard of where the money sits, ranked by the value of open positions and showing the change over 24 hours.
- **Carry** — Carry is the board's own derived metric: the funding that a basis position (long spot against a short perpetual) would have collected or paid over the last seven days, together with the number of hours the history covers.

**Built with**

- **Collection:** Python worker polling the public APIs of Binance USD-M, Bybit linear, Hyperliquid, Aster and Lighter every two minutes, with no API keys
- **History:** SQLite snapshots per venue, symbol and time
- **Delivery:** Authenticated REST ingest into a WordPress plugin written in PHP, with page caching switched off for the live view
- **Interface:** JavaScript workspace with sortable, filterable, paged tables, histograms and leaderboards

[Overview](https://github.com/logicencoder/deriv-board-bridge-overview)

### LE Auto Record

Watching a programme and deciding later to keep it should not mean losing it when the live buffer disappears. LE Auto Record turns programmes watched long enough on OpenPLi into normal recordings, so they can be found again in the movie folder on a disk or NAS. It makes everyday viewing easier to retain without scheduling a separate recording for every show.

**What it offers**

- **Keep what you watch** — The plugin builds on the receiver's timeshift buffer.
- **Split by programme** — With the EPG splitting option on (the default), a new file starts when the programme changes, so an evening of viewing becomes one recording per programme instead of a single long file.
- **Choose the destination** — A folder selector sets where saved movies go, covering local disks and network folders.
- **Keep the disk under control** — Cleanup is configured in the same screen: a cleanup check that runs every 15 minutes to 8 hours (off by default), deletion of leftover buffer files after a number of hours (0 keeps them), and a free-space limit in megabytes below which saving stops (0 turns the check off).
- **Set up on the receiver** — The setup screen follows the receiver's normal remote control: green or OK saves, red or Exit cancels, and yellow opens the About view.

**Built with**

- **Receiver platform:** Enigma2 on OpenPLi, with its configuration and on-screen list screens
- **Plugin:** Python, using the receiver's timeshift buffer, EPG and timers
- **Recording and storage:** MPEG transport stream files, local disk or CIFS network share

[Overview](https://github.com/logicencoder/le-auto-record-overview)

### 0xDNX DHIP Richlist

Holder rankings become more useful when they can be read alongside recent activity and summary information. The 0xDNX DHIP Richlist brings those views into a WordPress dashboard, helping visitors explore the supported asset's distribution without piecing together several pages.

**What it offers**

- **Understand the distribution** — The statistics panel shows the total number of holders, the total amount of 0xDNX locked in the programme, when the data was last updated, the last block processed and the number of transactions, and the share held by the top 10 and top 50 holders.
- **Explore ranked holders** — The Top Holders table lists rank, address, balance and percentage of the programme, ordered by balance, with load-more and a live refresh that updates the figures while the page is open.
- **Connect holders with activity** — Recent transactions list time, transaction ID, type (deposit or withdrawal), amount and block beside the holder ranking, so a movement can be read in the context of the distribution.
- **Publish the dashboard on WordPress** — A shortcode places the richlist on any page; settings decide how many holders are shown, whether the full list is shown, and whether the statistics, the title and the transactions appear.
- **Operate and maintain the view** — The administrator area has Overview, Recent Transactions, Top Holders and Transaction History screens, API & Display Settings, Snapshot Settings, and database tools: table sizes and row counts, transaction statistics (total, deposits, withdrawals, oldest and newest) and a duplicate-address check…

**Built with**

- **Application:** PHP, WordPress
- **Supporting technologies:** HTML, CSS, JavaScript; Dynex

[Overview](https://github.com/logicencoder/dynex-0xdnx-dhip-richlist-plugin-overview)

### Logic Encoder Login System

Member access involves more than a login form: people need to register, verify their address, recover access and reach the content meant for them. Logic Encoder Login System brings these journeys and their administration together in WordPress.

**What it offers**

- **A coherent member journey** — The Login & Access settings decide where members land after signing in and whether marketing consent is required at registration, and set the password rules (minimum length and minimum numbers of letters, digits and special characters).
- **Recover access without a manual exchange** — Forgot-password and reset flows let members recover access themselves.
- **Control access to content** — Each post or page can be set to block non-members completely or to show a preview: a real, server-side-truncated share of the content (between 5 and 90 percent, 30 by default) followed by a login prompt, like a newspaper paywall.
- **Manage users and communication** — User administration lists members with ID, name, email, role, registration date, IP address, country, verified and consent columns.
- **Support and maintenance** — The dashboard summarises the member base, quick actions run common maintenance, recent debug logs show what the plugin did, and a test-email tool confirms that messages leave the site.

**Built with**

- **Application:** PHP, WordPress
- **Supporting technologies:** HTML, CSS, JavaScript

[Overview](https://github.com/logicencoder/logicencoder-login-system-plugin-overview)

### European Electricity Monitor

Electricity-market information is more useful when prices can be read alongside demand, generation and cross-border activity. Power Center brings these views into one European dashboard, helping users compare markets and understand the context around a price change.

**What it offers**

- **Compare European markets** — The Overview shows all tracked bidding zones at a glance: average day-ahead prices, changes against the previous day and the cheapest windows, with chips for how many zones currently return prices and how many of the eight tracked datasets returned data in the last cycle.
- **Explore prices and history** — Prices shows hourly day-ahead prices as a zone-by-hour heatmap, and History shows a day-by-hour price heatmap over 14 to 60 days.
- **Connect demand with production** — Load compares actual and forecast system load per zone, and Generation shows the mix per fuel type with each fuel's share of total output.
- **Review flows and capacity** — Flows shows physical cross-border flows and net positions between markets, and Capacity shows installed generation capacity per fuel.
- **Return to the information that matters** — The Guide explains each dataset, unit and term, and Settings adjusts colours, font size, density and page size.

**Built with**

- **Core stack:** Python; PHP; WordPress; JavaScript; SQLite

[Overview](https://github.com/logicencoder/elec-prices-bridge-overview) · [Open application](https://logicencoder.com/european-electricity-monitor/)

### CVE DoS

Keeping up with vulnerability publications means checking several feeds again and again. CVE Watch puts the two sources that matter most for day-to-day patching on one board: the CISA Known Exploited Vulnerabilities catalogue, which lists flaws that are confirmed to be used in real attacks, and newly published CVEs from the National Vulnerability Database. Administrators, developers and anyone who runs servers can see at a glance what is being exploited, what is critical and what deserves a closer look first. It runs on logicencoder.com and refreshes every few hours.

**What it offers**

- **Overview** — The Overview view is the snapshot: how many CVEs are tracked in the current window, how many of them are critical (CVSS 9.0 and above), how many are known to be exploited (KEV in window) and how many are new in the NVD feed.
- **KEV exploited** — This view lists the entries that CISA confirms are exploited in the wild, as cards sorted by remediation due date.
- **Priority** — Priority is the site's own patch-urgency index from 0 to 100. It combines four things: whether the flaw is known to be exploited, its CVSS score, how close the CISA due date is and whether ransomware use is recorded.
- **Feed** — The Feed lists every tracked CVE in one table with columns for CVE identifier, source (KEV or NVD), CVSS, severity, date or due date, affected vendor and summary.
- **Watchlist** — The Watchlist is a fixed rule, not a personal list: every item in the window with a CVSS score of 9.0 or higher, described on the page as the drop-everything list.

**Built with**

- **Collection:** Python worker that downloads the CISA KEV catalogue and recent NVD publications every six hours
- **Relevance filter:** Keyword list for common server and developer stacks (operating systems, web servers, PHP and WordPress, Python, Node, Java, containers, databases, network equipment, browsers)
- **History and de-duplication:** SQLite log of what was already published
- **Delivery:** Authenticated REST ingest into a WordPress plugin written in PHP
- **Interface:** JavaScript workspace with sortable tables, charts and an adjustable layout

[Overview](https://github.com/logicencoder/cve-watch-bridge-overview)

### Military Flights Monitor

Publicly visible aircraft activity can be difficult to explore in a long list of positions and aircraft identifiers. Military Flights Monitor brings the available military-aircraft observations into a map, globe and searchable board, making it easier to explore the activity that is actually being broadcast.

**What it offers**

- **Explore the map and globe** — The Map is the primary radar view: click an aircraft for details, switch on measuring to read distances between points, and see an activity-density layer built from the sighting history.
- **Find a relevant observation** — The Board lists every tracked military aircraft and sorts it, with callsign, airframe description and an interest score.
- **Compare patterns** — Categories shows the mix of transports, tankers, airborne early warning and surveillance aircraft; Types ranks airframe types by interest score; Tempo counts aircraft detected per hour over the last 48 hours, including the high-interest ones, from the site's own history; Intel lists aircraft…
- **Keep useful work** — The Guide explains category, score, squawk and the fields. Settings adjust the accent colour, font, density and rows per page, and the choices are remembered in the browser.
- **Understand the coverage** — The product uses publicly available ADS-B observations from adsb.fi. Only aircraft present in that source can appear; many aircraft and operations are not represented.

**Built with**

- **Core stack:** Python; PHP; WordPress; JavaScript

[Overview](https://github.com/logicencoder/mil-flights-bridge-overview)

### Application boilerplates

Starting skeletons for chain monitors, real-time FastAPI services, operator web apps, product pairs, Telegram mini apps, terminal dashboards, service-manager services and WordPress plugins.

**Built with**

- **Languages:** Python, JavaScript, PHP
- **Patterns:** chain monitors, FastAPI real-time services, operator web apps, product pairs, Telegram mini apps, terminal dashboards, service-manager services, WordPress plugins

---

Retired components, deployment backups, shared libraries, supporting services, policy archives and utilities are kept in their own repositories and are not listed here.

**[Logic Encoder](https://logicencoder.com)** · [GitHub](https://github.com/logicencoder) · [Contact](https://logicencoder.com/contact/)
