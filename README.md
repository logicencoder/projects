# Logic Encoder — Projects

I am a hobbyist coder and software architect, curious how things work under the surface. This page collects what I have built: applications, WordPress plugins and a theme, dashboards, tools, experiments and engineering notes. They are in very different stages. The public ones are listed at https://logicencoder.com/applications/; others are tools I use myself, test projects to learn a technology, prototypes or unfinished work. The order is rough: bigger, more complete projects first, smaller pieces and unfinished work at the end.

A lot of what I build exists because the tool I needed did not exist or did not fit the way I work, so I made it. I like to build something working from nothing, watch it handle real data and improve it from what I see. Much of it is data-intensive and real-time: ingesting live feeds, normalising, aggregating, caching and presenting them so that they are useful.

The technology listed with each project is not a limit; I use whatever a project requires. So far that has been Python (FastAPI, asyncio), Node.js and TypeScript (Fastify), JavaScript with React, Vite and Svelte, PHP and WordPress (plugins and a theme), and Rust, C# and C++ for native software. For data I have used SQLite, PostgreSQL, DuckDB and MySQL plus in-memory caches, WebSockets and Server-Sent Events for live updates, Three.js, Globe.gl and Chart.js for graphics, Docker and systemd for running things, Web3 tooling for blockchain, and Playwright, Whisper, PyTorch, FFmpeg and Remotion for testing and media. Most entries say why I built the project; what each one does in detail, the screenshots and the technology are in the linked overview. The code itself is private.

[Website](https://logicencoder.com) · [Applications on the site](https://logicencoder.com/applications/) · [About](https://logicencoder.com/about/) · [Contact](https://logicencoder.com/contact/)

## Applications

### Universal Service Manager

![Universal Service Manager services grid with status, logs and lifecycle controls](https://raw.githubusercontent.com/logicencoder/universal-service-manager-overview/69911dc6b38ee5e5ab071ca3b6847aa15666f0e0/assets/universal-service-manager-services-grid.png)

Running a growing set of applications meant a terminal for each of them, separate tools for logs, Docker and systemd, and an SSH session for every small change. I wanted to work efficiently with everything in one place, and I found nothing that fitted my requirements, so I built my own.

One browser dashboard now controls the services, containers, native units and firewall and shows logs and resources beside them. It saves the time I used to lose switching between tools, and it is the control point for most of what I run.

Managing a growing collection of applications can turn a simple check into a round of terminal sessions, log searches and separate administration tools. Universal Service Manager grew out of that daily frustration: the available tools did not fit the way its creator wanted to work, so a single workspace was built around those needs.

The Services workspace makes a mixed collection of applications manageable as one fleet. Python applications, Node.js tools, shell jobs and native services appear together, with clear running or stopped states and the controls needed for everyday administration. The Overview table presents the same fleet in a denser layout. It is useful when the priority is comparing services rather than working with individual cards: scan running states, sort by resource usage and find the application that deserves attention. The Resources workspace helps answer a practical question: is one application struggling, or is the whole machine under pressure? The Processes workspace shows what is actually running on the host, including processes outside the managed fleet. The Logs workspace keeps investigation beside service control. Select an application, read its output and narrow the view to warnings or errors.

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

I did not set out to sell things; I wanted to try what it takes to sell digital products at all. Accepting crypto payments means solving a lot of different problems, from the security around payments to reliable delivery, and it was demanding and instructive. I could not find anything like it, so I designed the whole architecture myself.

It was also a test bed for security: I used it to try protections and to see how well a payment and delivery flow holds up against abuse.

Selling digital products involves more than collecting a payment. Someone has to connect the purchase to the right files, keep the buyer informed and know whether delivery completed. Logic Encoder Crypto App Store brings that work into one purchase flow inside Telegram, with a browser storefront and a shared operator workspace.

The storefront presents applications with images, descriptions, prices, versions and optional badges. The payment screen gives buyers the information needed to complete the purchase: an order reference, selected items, exact amount, destination address and remaining payment time. After successful payment verification, the bot sends the purchased files directly to the buyer's Telegram chat. The Orders area gives operators a live view of the sales queue. Summary figures and status filters make it easier to distinguish purchases waiting for payment, transactions being confirmed, completed deliveries and orders needing attention. The Warehouse brings catalogue information and deliverable availability together. Add and edit products, maintain prices and versions, manage availability and review the files associated with each application.

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

My work is spread over dozens of projects, notes and decisions. Based on Andrej Karpathy's idea of an LLM-maintained wiki and the 3D brain application from Nate Herk's AIS-OS, I built a personal knowledge system so that I can work more efficiently.

I can find what I have already built and decided, and an AI assistant works from a small, reviewed set of facts instead of guessing. It really does improve my work; I have checked that myself.

Years of project notes, source documents, skills and decisions are useless when nobody can find them or relate one to another. Logic Encoder Work Brain is a personal knowledge system that turns a body of work into a searchable wiki and an explorable 3D graph, and lets an AI assistant answer questions from a small, reviewed packet of that knowledge instead of guessing. It serves one operator who builds and maintains many applications and wants every method, project fact and decision kept in one place that both a person and an assistant can read.

Every note becomes a point and every link between notes a line. Colours separate work knowledge, project pages, skills and workflows, source documents and drafts, and the counters show how many notes, sources and connections the graph holds. Original documents stay unchanged as sources, and the assistant writes synthesis pages that cite them, record contradictions and keep a dated history of every accepted change. The workspace searches the knowledge, assembles the matching passages into a packet and shows it for review before anything leaves the machine. Reusable working methods are kept as skills: short instructions with checklists for building software, writing articles, reviewing code, securing changes, documenting products and working with the operator's servers. A control panel shows the health of the wiki, freshness of pages, retrieval quality, evaluation results of the skills and the state of the services the brain runs as.

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

Active trading can require repeatedly moving between a chart, order book, balances, order controls and automation settings. MEXC Trading Dashboard brings those views into a configurable trading desk so the operator can inspect the market and manage activity in one place.

Panels can be moved, resized and collapsed, and the arrangement is stored with Save Layout and restored with Reset Layout; Snapshot UI captures the current screen. The market view combines a chart (a TradingView chart that can be switched on and off), the order book with its depth and the live trades tape. The Trading Panel places buy and sell orders beside the account balances. Size shortcuts set 25, 50, 75 or 100 percent of the available funds, or a fixed 25, 50, 100 or 250 dollars, or a custom amount. The Bot Panel offers five modes: Mode 1 Instant Execution takes orders from other traders inside a price range with market orders (with an execution style of TAKE, PING, 50/50 or RANDOM); Mode 2 Grid Limit Orders places layered limit orders and replenishes them when filled; Mode 3 Step Re-entry Ladder places one order and moves the price by a percentage after each full fill until a stop rule or the budget is reached; Mode 4 Front of Book keeps one order at the best bid or ask and re-quotes one tick ahead when displaced; Mode 5 Scheduled Exact places one exact limit order at a set time (HH:MM:SS), optionally with a one-tick jump. The Multi Bots workspace supports reviewing more than one configured bot context. Performance information helps examine trade and bot activity, while system statistics and debug logs assist with investigation.

| Layer | Technologies |
|---|---|
| Application | Python, FastAPI |
| Supporting technologies | HTML, CSS, JavaScript; MEXC; TradingView; WebSockets |

[Overview](https://github.com/logicencoder/mexc_trading_app-overview)

### ETH Gas Live

![ETH Gas Live dashboard with gas price chart and fee tiers](https://raw.githubusercontent.com/logicencoder/eth-gas-live-plugin-overview/0cafbf56bb6dccdd61aa9cd2831f681cc8dfea47/assets/eth-gas-live-dashboard-gas-price-chart.png)

Other gas trackers did not have everything I wanted, so I built my own: a live view of what a transaction costs now, how fees have moved, and tools to plan the next one. It runs publicly on my site.

It was also a test bed for server-side rendering and search-engine optimisation.

A gas quote is only useful when it answers a practical question: what will this transaction cost, and is now a good time? ETH Gas Live is a real-time Ethereum fee dashboard on logicencoder.com that turns every new block into three send tiers, a congestion read-out, history, a fee calculator and alerts, and explains the numbers on eleven dedicated pages. It is for anyone who sends, swaps or builds on Ethereum and wants to pay a fair fee instead of guessing.

The main dashboard shows three send tiers per block: Base Route (economical), Standard Way and Faster Inclusion, each with a fee estimate that follows the EIP-1559 base fee and priority fee. History charts show how fees moved over recent hours and days, and a heatmap lays the hours of the week out in a grid so the usually cheap and the usually expensive periods are easy to spot. The Fee Calculator multiplies a gas limit by a gas price. The gas limit is chosen from presets for common actions (ETH Transfer 21,000, Token Transfer 65,000, Swap on a DEX 180,000, Token Approve 46,000, NFT Mint 180,000 and NFT Sale 150,000) or typed in by hand; the gas price follows the live Base Route, Standard Way or Faster Inclusion tier or can be set manually as a custom value, and the result is shown in ether and in dollars at the current ether price. Network Statistics has three tabs: an overview, detailed measures and a time analysis, and the backend adds a congestion index (Inclusion Pressure Index) and a spike score. WordPress embedding and site-operator tools support making the dashboard part of a wider site.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Application | PHP, WordPress |
| Supporting technologies | HTML, JavaScript; Chart.js and Tailwind CSS (both loaded from a public CDN); Ethereum |

[Overview](https://github.com/logicencoder/eth-gas-live-plugin-overview) · [Live](https://logicencoder.com/ethereum-gas-tracker/)

### MEXC Live Statistics

![MEXC Live Statistics dashboard with market trades and analytics](https://raw.githubusercontent.com/logicencoder/mexc-live-stats-plugin-overview/f6dcf708abb56af0f24a134d11fda7ed140583f7/assets/mexc-live-statistics-live-dashboard-market-trades.png)

A test of optimisation: processing a lot of real-time data, aggregating it and drawing it for many visitors at once without wasting resources. It is a public statistics site fed by my own data service and published on logicencoder.com. The same thing exists for the Gate exchange.

MEXC Live Statistics is a real-time dashboard for MEXC spot markets, published on logicencoder.com. A visitor picks a coin and sees its price, 24-hour statistics, volume and buy/sell balance, a stream of recent trades and detected bot activity, all updated live over a WebSocket connection. The site operator gets a Coin Manager, connection monitoring and the search-engine tooling to publish each coin as its own page.

Visitors pick a pair from the coin catalogue; the market header keeps the selected pair and its context visible. One coin page combines several panels that all follow the selected pair live: Current Market Overview (price and 24-hour figures), Volume Analysis, Buy/Sell Analysis (how trading splits between buyers and sellers), Trade Analytics, Bot Activity and a live tape of recent trades. Its Overview summarises the tracked set, Dead & missing coins lists pairs that stopped trading or never returned data, Add & reload adds a pair or reloads the list from the exchange, All tracked coins shows the full collection, and the Activity log records what changed. The monitoring area shows the live health of the data connection: WebSocket throughput, download speed and messages per second over the last three hours, the number of subscribed pairs, server metrics and system logs. Every coin can be published as a server-rendered HTML page with Schema.org structured data, so search engines see the content without running JavaScript.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Application | PHP, WordPress |
| Supporting technologies | HTML, CSS, JavaScript; MEXC public market data; WebSockets; optional TradingView chart (off by default) |

[Overview](https://github.com/logicencoder/mexc-live-stats-plugin-overview) · [Live](https://logicencoder.com/mexc-app/) · [Same thing for the Gate exchange](https://logicencoder.com/gate-app/)

### LE Karaoke Studio

![LE Karaoke Studio workspace with transcription, editor and timeline](https://raw.githubusercontent.com/logicencoder/le-karaoke-studio-overview/2ed33c86e42aa9774c3cfee7a482f40597e4e0c6/assets/le-karaoke-studio-work-transcription-editor-timeline.png)

I was curious how the applications that add subtitles to a video are made, so I started to take the idea apart. That was reverse engineering, and step by step I kept adding more multimedia features.

The audio-effects lab came from something I had wanted for years: building effects for music myself. Today it is a studio that takes a media file all the way to a finished video.

Turning source audio or video into a finished karaoke or captioned clip usually means moving between download, stem separation, transcription, editing and export tools. LE Karaoke Studio puts those stages into one web application with ten workspaces: Studio (transcribe, edit lines, style and render), Audio Effects Lab and Video Effects Lab, Context Prompts, a Video editor, DLV (the downloader), UVR (vocal and stem separation), HW (a GPU watch panel), Automate (a managed publishing workflow) and Settings. It runs on a GPU machine under the operator's own control.

Upload a clip or work through a batch, review its format and choose the part that should be processed. Choose subtitle styling, line presentation and visualiser options to build a consistent look across clips. The audio-effects and visual-effects areas let the operator experiment with the presentation around the clip. DLV downloads a source with progress and history, using yt-dlp, and UVR separates vocals from accompaniment as queued jobs with a choice of models. Follow job progress, inspect results and download the finished video. Editing, trim and output options support different source material and export needs.

| Layer | Technologies |
|---|---|
| Application | Python, FastAPI |
| Supporting technologies | React, TypeScript; Whisper, PyTorch; FFmpeg, Remotion, HyperFrames; yt-dlp |

[Overview](https://github.com/logicencoder/le-karaoke-studio-overview)

### LE HSCR — Radio Monitoring Workspace

![LE HSCR radio monitoring workspace](https://raw.githubusercontent.com/logicencoder/le-hscr-overview/fcbe22bb9830dc80983ea6d5e8b2455d5cc27e72/assets/le-hscr-radio-monitoring-workspace.png)

One workspace for looking at what radio devices are around: Bluetooth, Wi-Fi, satellite reception and USB, for authorized radio and device investigations.

LE HSCR is a single-page radio monitoring console for Bluetooth LE, Wi-Fi and satellite reception. One browser window shows what the connected adapters and tuner can see, keeps the history of what was seen and puts the logs of all radios in one stream. It runs in a Docker container with the USB adapters passed through, or directly on a prepared host, and by default it stays on the local network with no telemetry. It is meant for authorised radio research on equipment and networks the operator owns or is allowed to test.

The Overview tab summarises all radios on one screen: Bluetooth, Wi-Fi and monitor key figures, the state of each adapter and the statistics of the current session. The Bluetooth tab scans actively or passively and parses iBeacon and Eddystone advertisements into readable fields. The Wi-Fi tab scans for networks in managed or monitor mode and shows a spectrum trace with a waterfall. The satellite area detects and identifies the tuner, powers it, and tunes by transponder or manually. The USB area lists attached devices with their status and can refresh or reset a device, which is the first check when an adapter disappears.

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

Understanding a website's audience can become fragmented across traffic reports, campaign tools and access logs. WP Visitor Stats brings those views into WordPress, helping the owner inspect how people reach the site, what they use and where a closer look is needed.

The overview brings key traffic information together, while content reports help examine which pages receive attention. Geographic and technology reports add context about where visits come from and how the site is being used. Campaign reports, custom events and interaction heatmaps help examine how visitors engage beyond the initial page view. Bot activity and ban-management views help the owner inspect traffic that needs a different response. Settings cover the data-retention period (180 days by default), the excluded addresses and the tracking options.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Application | PHP, WordPress |
| Supporting technologies | JavaScript, HTML, CSS; MySQL |

[Overview](https://github.com/logicencoder/wp-visitor-stats-plugin-overview)

### Celestial Lab

![Celestial Lab satellite map with a 3D globe of orbiting objects](https://raw.githubusercontent.com/logicencoder/celestial-lab-plugin-overview/75f0c881bf7ccb1e8403e5c7ca94fd8cdb3036f3/assets/celestial-lab-satellite-map-3d-globe-orbits.png)

Mostly a fun project: I am an astronomy fan, so I put together one place where I can look at satellites, aurora, the Sun, crews in orbit, exoplanets, asteroid encounters and launches. It runs on my site.

Space information is spread across orbital catalogues, solar observations, mission schedules and astronomy archives. Celestial Lab brings seven related experiences into one workspace: start with a source-aware summary, then inspect the objects, observations or events behind it without switching applications.

The opening board brings satellites, space weather, solar activity, provider-reported crew, exoplanets, asteroid encounters and launches together. Satellite Map lets users explore published orbital catalogues, filter orbital bands, follow ISS or Tiangong and add the separately loaded Starlink layer. Aurora outlook, Space environment, Solar wind and Alerts help relate geomagnetic activity to the underlying measurements and messages. Sun Live combines an observed solar disk, selectable wavelengths, reported active regions, flares and statistics. People in Space separates the provider-reported roster, mission duration, station context and list history.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Application | WordPress, PHP, JavaScript, HTML, CSS |
| Interactive visualization | Three.js, Globe.gl, WebGL |
| Data collection | Python |

[Overview](https://github.com/logicencoder/celestial-lab-plugin-overview) · [Live](https://logicencoder.com/celestial-lab/)

### System Monitor App

![System Monitor App terminal dashboard](https://raw.githubusercontent.com/logicencoder/system-monitor-app-overview/d254228adc2cccd1bde1f951493a704bdd7c1990/system-monitor-app-terminal-dashboard.png)

I did not want seven terminals open just to watch the hardware. One terminal dashboard shows CPU, memory, disk, network, GPU and sensors together, so everything is in one place and I can keep working.

A quick host check should not require opening several monitoring utilities. System Monitor App brings resource use, processes and service information into a terminal workspace, making it useful for both local administration and remote command-line sessions.

The screen is built from panels: CPU (with per-core load), Memory and swap, Network, Disk, GPU, Sensors (temperatures where the hardware reports them) and the monitor's own usage. The Process panel lists running processes and sorts them by CPU or by memory with one key, so the biggest consumer is at the top. The Services panel shows the state of a list of important systemd services, and the Firewall panel shows the number of connections blocked by iptables or nftables. The Alerts panel keeps a history of the last 100 alerts raised by conditions you choose to watch. It is a single program built with Textual and psutil, distributed as one self-contained Linux executable, so it runs in an ordinary SSH session without a graphical desktop on the monitored machine.

| Layer | Technologies |
|---|---|
| Application | Python |
| Supporting technologies | Textual; psutil; Linux |

[Overview](https://github.com/logicencoder/system-monitor-app-overview)

### Rocinante Command Center

![Rocinante Command Center simulated navigation](https://raw.githubusercontent.com/logicencoder/roci-command-center-overview/76d1af1701427683a75136a5c288d2611a859333/assets/rocinante-command-center-solar-system-tactical-deck.png)

A fictional ship command deck that I built to show a visual style which I can deploy to other applications: dense, instrument-like panels, 3D scenes and live-moving data. All telemetry is simulated; the point is the look and feel.

Rocinante Command Center is a fictional ship interface you can operate: a command deck for a corvette-class light frigate with three sections, four switchable scenarios, a live-moving contact picture, a 3D solar system and hull schematic, and panels you can resize. Every reading, crew member, contact and radio channel is generated in the browser by a small simulation; nothing on it is a real observation of a real spacecraft. It is built for people who enjoy science-fiction interfaces and want one that behaves like a working one.

A scenario selector in the header switches the whole ship between four situations: Cruise, High-G Burn, Emergency and Comms Interference. The first section is the navigation picture. A sensor grid shows generated contacts that move over time, and selecting one makes it the active contact across the deck. The second section covers the vessel itself. Propulsion Systems and the Epstein Drive Core show drive state, Power Distribution shows how demand is split, and Shield Grid Status with the Shield Integrity Map tracks the six shield sectors. The third section holds five radio channels from fleet comms and emergency to deep-space and distress beacon, each with a frequency and a status. Panels are resizable and the sizes are remembered between visits in the browser. A reset control in the header restores the default layout.

| Layer | Technologies |
|---|---|
| Interface | React 18, JavaScript, HTML and CSS with Tailwind utility classes |
| 3D and charts | Three.js for the solar system, hull, antenna and signal-field scenes; Recharts for the history plots |
| Simulation | A local step simulation that advances velocity, fuel, drive temperature, shield strength and signal interference over time |
| Build | Vite |

[Overview](https://github.com/logicencoder/roci-command-center-overview) · [Live](https://logicencoder.com/rocinante/)

### Le Sound Normalizer

![Le Sound Normalizer with compressor knobs and 15-band equalizer](https://raw.githubusercontent.com/logicencoder/le-sound-normalizer-overview/7344dee31d360d8ccbcd3850b46fb6ba634ed37f/assets/le-sound-normalizer-15-band-equalizer-compressor.png)

Watching films, the jump from quiet dialogue to a loud action scene meant reaching for the volume again and again, which is annoying. I built a normalizer that keeps loudness under control so dialogue stays understandable.

It was also my test of building, compiling and packaging an application for Windows, because most of what I write targets Linux.

Le Sound Normalizer is a Windows audio tool that keeps loud scenes from overpowering quiet dialogue. Turn the volume up so speech is understandable and the next explosion would normally blast out; the normalizer holds the output under a ceiling you choose and evens out the gap between quiet and loud passages, so a film, a series or a game stays comfortable at one listening level. It runs as a small controller window next to a native audio component that sits in the Windows audio path, so it works with the player you already use. Built and maintained by Logic Encoder at logicencoder.com.

Choose a loudness ceiling and how firmly loud material is pulled toward quiet material, with Soft, Balanced and other compressor characters. LED meters per output, a live spectrum, an oscilloscope waveform and connection status. A simple bass, middle and treble tone control and a 15-band graphic equalizer with their own values. Save sound presets for film, evening or music, and switch between green and cyan palettes.

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

Another data-heavy build: following swaps on Ethereum as they happen, decoding and valuing them and presenting a live feed. The challenge is processing a large amount of data reliably in real time.

It has also taught me how long-running services fail. A full disk once silently stopped its scanner for weeks, and the fix was a scanner that restarts itself and reports when it stalls.

Ethereum Chain Swap Monitor follows swaps on Ethereum in real time. A Python process reads new blocks and logs from an Ethereum node, recognises swaps in known liquidity pools, values them in dollars and shows them in a live dashboard with alerts, the most active addresses, saved quote tables and a live terminal. It is a self-hosted operator tool for people who want to watch large or unusual swap activity as it happens.

The Live Alerts Feed keeps the latest 250 swaps in a list that can be scanned and expanded for detail; auto-expand opens new entries as they arrive and a freeze switch stops the list moving while you read. The Top 20 Most Active Addresses ranking shows the participants that recur in the observed swaps, and the search box looks up any address. Saved Quote Tables keep a quote per pool for comparison next to the feed; Refresh quotes updates them and they can be ordered latest or oldest first, by coin name (A to Z or Z to A) or by liquidity (highest or smallest). The Live Terminal shows what the monitor is doing and can be disabled or cleared. Four monitoring modes decide what is read: pools with swap logs, a watchlist with swap receipts, pools with all logs, or a watchlist with all transactions (apply the mode with one button; modes 2 and 4 currently behave the same). Three themes (dark, medium and light) change the colours, and every panel can be collapsed, which helps when the monitor stays open for a long session.

| Layer | Technologies |
|---|---|
| Application | Python |
| Supporting technologies | HTML, CSS, JavaScript; Ethereum; WebSockets |

[Overview](https://github.com/logicencoder/eth-chain-swaps-monitor-overview) · [Live](https://logicencoder.com/ethereum-chain-swap-monitor/)

### CEX/DEX Arbitrage App

![CEX/DEX Arbitrage App with pool discovery, arbitrage scanner and trading rules](https://raw.githubusercontent.com/logicencoder/cex-dex-arb-overview/5a6b8c1144a49414fa3fb7ccf8cf3581b60bbd86/assets/cex-dex-arbitrage-app-pool-discovery-arb-scanner-trading-rules.png)

One of my first big applications, a monolith of roughly twenty thousand lines. I used it to test how such a project can be taken apart into microservices, how to display a lot of different real-time data at once and how to automate trades by market criteria.

Comparing an exchange price with a decentralised market is only the beginning of evaluating an opportunity. This dashboard brings market screening, trade-size comparisons and execution controls into one workspace, helping the operator inspect the opportunity in context before acting.

Load pools reads the stored pools, Active Coins keeps the markets under review as tabs, and Live stats and Pool Info show the selected pair and its pool. The Arbitrage tables show buying on the exchange and selling on the DEX, and the reverse, for several trade sizes. The ARB SCANNER has tabs for Discover (new candidate pairs, each of which can be sent to the queue or ignored), the Pool tester queue, the Ignore list and the stored coins with their pool details (pair, DEX type, fee, token), which come from the pool lab or are saved by hand. Live Orderbooks for MEXC and Gate.io, the account's own trades and all trades on each exchange, and a TradingView chart sit beside the comparison, so depth and recent movement can be checked before an action. A Manual Swap panel buys or sells through the MEV-protected route, and the Swap gate readout shows whether swapping is currently allowed.

| Layer | Technologies |
|---|---|
| Application | Python, FastAPI |
| Supporting technologies | HTML, CSS, JavaScript; Web3.py; MEXC, Gate, Uniswap; TradingView |

[Overview](https://github.com/logicencoder/cex-dex-arb-overview)

### Red-Team Lite

A small scanner for a quick first security pass over a web application you own or may test: it crawls, probes for common weaknesses, captures evidence and writes a report.

A quick security check of a web application should not need a heavy toolchain. Red-Team Lite crawls a target site, probes the discovered routes and parameters for common weaknesses, captures browser screenshots of serious findings and writes a report in JSON and Markdown. It serves developers and security testers who want a fast first pass over an application they own or have written permission to test.

The scanner starts at the target address, follows links up to a chosen crawl depth and collects routes, forms and input parameters. Each discovered route is tested for exposed files such as configuration and repository metadata, reflected cross-site scripting, SQL injection through error disclosure, local file inclusion, server-side request forgery, template injection and open redirects. Findings are rated by severity, and critical and high findings get a Playwright screenshot as visual evidence. The web page asks for the target address, optional test credentials and the crawl depth, starts the scan and lists the findings with their severity when it finishes.

| Layer | Technologies |
|---|---|
| Scanner | Python with a crawler and HTTP probes |
| Evidence | Playwright with Chromium for screenshots |
| Interface | Command line, a FastAPI endpoint and a single-page web form |
| Reports | JSON and Markdown files |

[Overview](https://github.com/logicencoder/redteam-lite-overview)

### LE Media Player

A test project: porting my browser-based audio-effects lab to Rust. I wanted to learn Rust, development, building and compiling, so I picked something I already understood. The result is a fast native Linux player with an equalizer and visualizers.

It plays local audio and video, YouTube and other URLs, and keeps a Winamp-style playlist under keyboard and drag-and-drop control, for people who want one lightweight player for listening, tuning sound and watching video.

Moving the engine into a native process opened up features that a web page cannot offer, and the player adds them on top of the original lab: The effects rack is built for tuning sound while it plays. A 20-band equalizer ships with presets such as Flat, Rock, Metal, Techno, Bass boost, Pop, Vocal and Classical, plus manual gain per band and a pre-amp. Visualizers react to the live spectrum and to an adaptive beat detector. The collection covers bars, waveforms, particle effects and circular spectrum modes with a mirrored variant, a bass-driven orb, frequency rings and a cymatics plate. The playlist follows Winamp conventions. Files and whole folders can be dropped in; folders are scanned recursively and the drop position decides where items land, with an insertion line and auto-scroll while dragging.

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

Exchange balances move the Dynex market, and the movements are easy to miss in a chain explorer. Dynex MEXC Balance Monitor is a WordPress dashboard on logicencoder.com that shows the DNX balance held by the monitored MEXC wallet, every deposit and withdrawal as a live feed, and charts of net flow, volume and balance over time. It serves holders and analysts who follow exchange flows of Dynex.

The top of the dashboard shows the current balance, total incoming and outgoing DNX, transaction counts and the progress of the chain scan. The feed lists transactions as they arrive, with direction, amount, address and time. A direction filter, a search box and a minimum amount keep it readable, and the list can be exported as CSV. Four interactive charts show net flow, incoming against outgoing volume, transaction count and balance over time, each with its own period of hourly, daily or weekly steps and a timespan from 24 hours to 30 days. The settings page holds the API key used by the data worker, the poll mode, thresholds, storage caps, diagnostics and row purging.

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

I am interested in satellite feeds and in analysing streams, not in watching television. I wanted an application for looking inside transport streams: tuning, reception and what a stream actually contains.

A television stream can look unstable for several different reasons: reception, tuning, transport errors or the content being carried. TS Analyzer brings those checks into one browser workspace, helping an operator move from choosing a satellite source to inspecting the arriving stream and retaining useful findings.

Discover a SAT>IP receiver or choose one manually, then prepare the satellite positions and switch sources to investigate. The results workspace collects transponder observations, television services and radio services for later review. On an Enigma2 receiver, Analyze current TV inspects the programme already being watched without changing the TV channel. When a supported receiver supplies RF measurements, inspect strength, SNR and available error readings alongside the transport observations. The constellation view accepts current external I/Q samples from compatible measurement equipment.

| Layer | Technologies |
|---|---|
| Core stack | Rust; Python; FastAPI; JavaScript; HTML; CSS |

[Overview](https://github.com/logicencoder/ts-analyzer-overview)

### LE Settings

![LE Settings administration console](https://raw.githubusercontent.com/logicencoder/le-settings-plugin-overview/bb65c6d7748d5787a647417964705b8f1b6cf4f6/assets/le-settings-admin-console-overview.png)

A test bed for managing my own WordPress site from one console: protection and security features, and notifications to me when something happens.

Site operations often become a collection of unrelated settings pages, alerts and logs. LE Settings brings the site's supported operational controls into one WordPress console, helping the owner review protection, notifications and publishing-related preferences with less switching.

The Status tab is the starting point: it lists which protections and trackers are switched on and how notifications are configured, so the intended behaviour of the site is visible before an issue is investigated. The Telegram tab holds the bot token and chat ID, a master switch, alert throttling with a limit on alerts per hour so a burst of events cannot flood the chat, an optional country in each message and a test message button. The Protection tab switches on brute-force protection with a maximum number of failed attempts and a base lockout time that grows with repeated failures (progressive lockout), an IP whitelist that is never blocked or tracked and an IP blacklist that is always blocked, blocking of locked-out addresses, a ban on user enumeration, security headers, a maintenance mode with its own message, redirects of guests away from protected pages, and control of automatic updates. The SEO tab covers descriptions, noindex for paginated pages, hiding excerpts from crawlers and allow rules written into robots.txt, and the Redirects tab manages path redirects with a type, or a 410 Gone when no target is given. The Debug tab shows the plugin's own log with refresh and clear buttons, and log tables can be filtered.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Application | PHP, WordPress |
| Supporting technologies | HTML, CSS, JavaScript; Telegram |

[Overview](https://github.com/logicencoder/le-settings-plugin-overview)

### Logic Encoder Enhanced Theme

![Logic Encoder Enhanced WordPress theme front page](https://raw.githubusercontent.com/logicencoder/logic-encoder-theme-overview/8e5a586b41684e5d0334b9169c93d9a22c014dc2/logic-encoder-theme-wordpress-front-page.png)

The WordPress theme behind logicencoder.com, connecting application pages, technical writing and member content in one presentation.

A WordPress site that presents software products, technical writing and member pages needs one visual system and one place to change it. Logic Encoder Enhanced is a custom theme for exactly that: a dark, technical design with a homepage built from editable sections, a manager for the application catalogue, page templates for the sign-in and account journey, and a long list of Customizer controls. It is built for a site owner who wants to change text, colours, fonts and layout from the WordPress Customizer instead of editing template files.

The front page is assembled from sections whose wording the owner edits in the Customizer: a hero with an eyebrow line, a description, an optional animated terminal that types out a list of lines, and a row of pills; then an approach block, a capabilities block, an applications teaser, a blog teaser with a configurable number of posts, a technology stack block, an about block and a closing call to action. The App Manager adds an administration page for the application catalogue, with adding, editing, deleting and reordering done in place without page reloads. Dedicated templates cover the pages a product site needs: homepage, blog, about, contact, sign-in, forgot password, reset password, email verification, account, dashboard, single post, search results and a 404. Appearance is controlled in one place: heading, body, navigation and logo fonts, a base font size, a colour preset, two border-radius sizes, content margins and the width of the homepage wrapper. The theme registers shortcodes for content that depends on who is reading. Wrapping text in them shows it only to logged-in users, to administrators, to a chosen role or to a membership level of basic, premium or VIP, and visitors who do not qualify see a short message with a link to sign in.

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

A comparison of Russian Internet connectivity, service reports and infrastructure records that keeps sources and uncertainty visible.

Internet incidents, provider announcements and website-access measurements answer different questions. Russian DC Observatory brings them into one research workspace while keeping their sources and uncertainty visible. It helps users compare evidence about Russian Internet connectivity, named services and infrastructure without treating every complaint or missing observation as proof of an outage.

The overview brings service observations, network incidents, traffic context and source freshness together. The Services view groups provider-reported components, incident references and scheduled maintenance. The Access view presents website-access measurement samples and their coverage. Category counts, domain subsets and network context help users interpret the available observations. Facility and map views make the infrastructure catalogue easier to explore geographically. Watchlists let users focus on the sites and provider components they care about. The in-app change feed helps revisit meaningful accepted changes to watched evidence.

| Layer | Technologies |
|---|---|
| Application | Python; SQLite |
| Dashboard | JavaScript; HTML; CSS; SVG |
| Administration | WordPress; PHP |

[Overview](https://github.com/logicencoder/russian-dc-observatory-monitor-overview) · [Live](https://logicencoder.com/russian-dc-observatory/)

### Awair Monitor Dashboard

![Awair environmental metrics and measurement history](https://raw.githubusercontent.com/logicencoder/le-awair-monitor-dashboard-overview/1154807b0cd2a9dd009256f177a5bbb623567599/assets/awair-monitor-dashboard-air-quality-score-trend-history.png)

Nothing like this existed: the manufacturer only offers a complicated cloud route. I found that the device has a local API, so I built my own dashboard in the browser that talks to it directly.

Indoor conditions are easier to understand when the latest readings can be compared with what happened earlier. Awair Monitor Dashboard brings Awair Element measurements, trends and history into one workspace, helping users notice changes in a room without repeatedly switching between device readings and separate reports.

The front page shows a score gauge and one card per measurement (temperature, humidity and the air-quality values the device reports), read live from the Awair Element's local interface. Trend charts and the score history show whether a change was brief or part of a longer pattern. The Daily, Trends and Correlations views summarise each day, show how measurements moved and rank which ones move together, and Uptime shows how reliably the device reported. A period of readings can be exported as CSV or JSON for separate analysis. The history is kept in a local SQLite database, so an earlier period can always be revisited. Two visual styles, Aurora and Nexus, and an English and Slovak interface are available. In Settings the operator can configure notifications through a webhook or an ntfy address, send a test message and snooze alerts for a while; a Logs page shows what the collector has been doing.

| Layer | Technologies |
|---|---|
| Core stack | Python; Svelte; JavaScript; SQLite |

[Overview](https://github.com/logicencoder/le-awair-monitor-dashboard-overview)

### Slovak Air Quality Dashboard

![Slovak Air Quality Dashboard history of hourly readings and station changes](https://raw.githubusercontent.com/logicencoder/air-quality-bridge-overview/42e86a73e4c0228d0a01324f2fe9c00f0281804c/assets/slovak-air-quality-dashboard-history-hourly-source-index.png)

Station readings, history and geographic context for air quality in Slovakia, with the source and the age of every reading visible.

A single pollution reading means little without the station, the time and the surrounding history. The Slovak Air Quality Dashboard brings the hourly readings of every station in Slovakia's national monitoring network into one board and one map, so residents, parents, runners and anyone curious about the air can see where the air is clean, where it is not and how that changed over the last hours and days. It runs on logicencoder.com and updates every hour, matching the cadence of the published data.

The Overview view opens with a live summary: how many stations reported in the latest snapshot and how many of them report a numeric quality index. The Map view places every station on a Leaflet map and colours each marker by its quality class. The Stations view is the searchable directory. Filter by name or quality class, and read each station's readings together with their observation times, in the same quality colours as everywhere else in the dashboard. The Pollutants view separates the measurements the network publishes: particulate matter PM10 and PM2.5, nitrogen dioxide, ozone and sulphur dioxide, all in micrograms per cubic metre. History looks beyond the latest hour. Choose a period and a station or pollutant and the chart shows the hourly readings over that window; the Compare tools line up days against each other.

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

A live view of large DNX transfers, with search by address and transaction detail.

Large transfers can disappear into a busy chain feed.

The feed lists large Dynex transfers in a table with date and time, block, transaction hash, direction (sent or received) and amount. A statistics panel puts the feed in perspective: total transactions with the split into sent and received, counts for today, the last 24 hours, 7 days and 30 days, hourly and daily velocity, the average transaction, the total volume and the date of the oldest data. The search box takes a wallet address and returns the transactions in which it takes part, in the same table, so a known participant can be followed without scanning the whole feed. The dashboard is embedded with a shortcode whose attributes set the initial number of transactions, the refresh interval, the heading, and whether the statistics panel and the search box are shown.

| Layer | Technologies |
|---|---|
| Type | WordPress plugin |
| Application | PHP, WordPress |
| Supporting technologies | HTML, CSS, JavaScript; Dynex |

[Overview](https://github.com/logicencoder/dynex-large-transactions-plugin-overview) · [Live](https://logicencoder.com/dynex-large-transactions-monitor/)

### React + Vite Architecture Guide

![React and Vite project architecture diagram](https://raw.githubusercontent.com/logicencoder/react-vite-architecture-for-dummies/4f156135dfad47f9517db68415e481718a8361b0/react-vite-architecture-diagram.png)

A plain-English guide to how a React and Vite project fits together. It is also a demonstration: I can produce this kind of architecture overview for any project, so that other people understand quickly what it consists of and how it works.

It ends with the "injection chain" that explains how the browser gets from index.html to a running component tree, and a one-page diagram of the whole structure.

Config files, the source folder and the build output are described one by one, including what is safe to ignore. Shows how index.html, main.jsx and App.jsx lead to rendered components. A one-page summary of the five things worth remembering about a Vite project.

| Layer | Technologies |
|---|---|
| Subject | React, Vite, JavaScript, npm project structure |
| Format | Long-form Markdown guide with an architecture diagram |

[Overview](https://github.com/logicencoder/react-vite-architecture-for-dummies)

### SatPI — SAT>IP server for the Vu+ Duo 4K SE

I wanted the open-source SatPI SAT>IP server to work on my Vu+ Duo 4K SE, where upstream delivered no data on the second tuner bank and could not switch DiSEqC. I fixed it, tested it end to end and wrote down the investigation.

The fork was verified end to end on OpenPLi 9.2 with DVBViewer switching three orbital positions while the receiver software keeps running. A first-hand write-up with measurements and packet captures is published on logicencoder.com.

A client closing a connection mid-write no longer kills the daemon, and empty keepalive requests no longer crash it. Same-descriptor source selection, mid-stream PID changes and safe emulation of the all-PIDs request. Child tuners route DiSEqC through the already-open root frontend in the correct tone, voltage, command and mini-burst order. Case-insensitive SAT>IP parameters and a relaxed retune when a client sends stale channel-list values.

| Layer | Technologies |
|---|---|
| Language | C++ (upstream SatPI codebase) |
| Protocols | SAT>IP over RTSP/HTTP — DVB-S/S2, DVB-T/T2, DVB-C |
| Target hardware | Vu+ Duo 4K SE — Broadcom bcm7335 / NEXUS, dual FBC DVB-S2 |
| Build | ARM cross-toolchain, statically linked (-static -static-libstdc++ -static-libgcc) |
| Verified on | OpenPLi 9.2, DVBViewer clients, Enigma2 running alongside |

[Overview](https://github.com/logicencoder/satpi)

### TechniSat SkyStar USB 2 HD CI — Linux driver and SAT>IP

The Windows drivers for this card stopped at Windows 7, there were none for Windows 11, and plugging it into USB 3 crashed the machine with a blue screen. I did not want to throw the hardware away, so I tried to make it usable another way.

Then I found that the Linux drivers were wrong too and never locked DVB-S2, so I fixed that as well. The card now tunes and locks, and it is rescued and back in use.

The stock Linux driver cannot lock DVB-S2 on the TechniSat SkyStar USB 2 HD CI card, which is why many owners discard it. This project ships one out-of-tree kernel module with three fixes on top of the community DVB-S2 patch (DVB-S2 lock, signal scale and SNR calibration), plus a minisatip SAT>IP server for free-to-air channels. After the patch the card tunes and plays DVB-S2, reports signal and SNR in DVBViewer, TransEdit and the minisatip web page, and switches DiSEqC ports.

The patched stb0899 locks and tunes DVB-S2 transponders that the stock driver cannot. Calibrated readings appear in DVBViewer, TransEdit and the minisatip web page. Complete transponder scans with NIT and multi-dish port switching work from the SAT>IP clients.

| Layer | Technologies |
|---|---|
| Driver | Out-of-tree stb0899.ko kernel module — DVB-S2 lock, signal scale, SNR calibration patches |
| Sat>IP server | minisatip — RTSP port 8554, web UI 8080 |
| Host | Ubuntu 24.04 LTS, kernel 6.8 (tested); Windows clients consume via Sat>IP |
| Clients | DVBViewer, TransEdit, VLC, ffprobe |

[Overview](https://github.com/logicencoder/technisat-skystar-usb-2-hd-ci-satip)

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

In short: these projects cover real-time data and exchange tooling, blockchain monitoring, media processing, native desktop software, WordPress and web applications, hardware and driver work, and the monitoring and management tools that keep it all running. Many started as a test of a technology or as a tool I could not find elsewhere, and each one taught me something about how things work under the surface.

---

Retired components, deployment backups, shared libraries, supporting services and utilities are kept in their own repositories and are not listed here.

**[Logic Encoder](https://logicencoder.com)** · [GitHub](https://github.com/logicencoder) · [Contact](https://logicencoder.com/contact/)
