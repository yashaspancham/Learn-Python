# Master Project List

## Beginner Tier (25 Projects)

### Cloud (AWS/Azure/GCP)
1. **S3 File Uploader:** Script to upload a local file to an S3 bucket using Boto3. [Done]
2. **EC2 Instance Lister:** Program to list all running cloud instances and their IDs. [Done]
3. **IAM User Auditor:** List all IAM users and their last login dates.
4. **Cloud Storage Space Checker:** Script to report the total size of a cloud bucket.
5. **Static Site Deployer:** Automate uploading a `dist/` folder to a static website host.

### Linux & Systems
6. **System Info Reporter:** CLI tool that prints OS version, CPU usage, and RAM.
7. **Automated Backup:** Script to zip a folder and move it to a backup directory with a timestamp.
8. **Process Watchdog:** Monitor if a specific process (e.g., `nginx`) is running; alert if not.
9. **Log Pattern Finder:** Search system logs for "ERROR" or "CRITICAL" and save to a report.
10. **Directory Cleaner:** Script to delete files older than 30 days in a specific folder.

### Data Engineering & Analysis
11. **CSV to JSON Converter:** Robust script to transform flat CSV data into nested JSON.
12. **Sales Revenue Calculator:** Read a CSV of transactions and calculate totals per category.
13. **Duplicates Remover:** Script to find and delete duplicate rows in a dataset using Sets.
14. **Web Scraper (Static):** Use `requests` and `BeautifulSoup` to extract prices from a single page.
15. **Currency Converter CLI:** Fetch exchange rates from a public API and convert user input.

### AI/ML (Basics)
16. **Sentiment Scorer:** Use a library like `TextBlob` to classify user input as positive/negative.
17. **Manual Linear Regression:** Calculate a line of best fit for 10 data points without ML libraries.
18. **Iris Explorer:** Use `scikit-learn` to load the Iris dataset and print its basic statistics.
19. **Keyword Chatbot:** A rule-based bot that identifies intent using string matching.
20. **Handwritten Digit Visualizer:** Use `matplotlib` to display images from the MNIST dataset.

### Finance & Quant (Basics)
21. **Stock Price Fetcher:** Fetch real-time stock prices from a public API and display gain/loss.
22. **Loan Amortization Table:** Calculate and print a full monthly payment schedule for a loan.
23. **Budget Analyzer:** Read a CSV of expenses, categorize them, and print a spending summary.
24. **Portfolio Value Tracker:** Track the current value of a stock portfolio defined in a JSON file.
25. **Compound Interest Calculator:** Compare investment growth across different compounding periods.

## Intermediate Tier (25 Projects)

### Cloud (AWS/Azure/GCP)
1. **Serverless CRUD API:** Build a Lambda-based task manager using Boto3 and DynamoDB.
2. **Bucket Event Trigger:** Automate image resizing upon upload to cloud storage.
3. **IAM Policy Generator:** A tool to create least-privilege JSON policies based on user input.
4. **Cloud Cost Auditor:** Identify under-utilized instances and generate a savings report.
5. **Multi-Region Backup:** Script to replicate critical data across global cloud regions.

### Linux & Systems
6. **SSH Automation Tool:** Execute commands on multiple remote servers simultaneously using `paramiko`.
7. **Custom Shell (OOP):** Build an interactive shell that supports history and custom command plugins.
8. **Network Port Scanner:** Multi-threaded tool to identify open ports on a local network.
9. **Log Rotation Manager:** A custom `logrotate` clone using context managers for safe file handling.
10. **System Config Synchronizer:** Tool to sync and version-control dotfiles across different machines.

### Data Engineering & Analysis
11. **Streaming Data Pipeline:** Process a 5GB dataset using generators and `yield` to maintain low RAM.
12. **Database Migration Tool:** Script to move schema and data between SQL and NoSQL databases.
13. **Data Validation Framework:** Use decorators to enforce data types and schemas on function inputs.
14. **API Wrapper with Caching:** Build a professional API client that caches results to a local SQLite DB.
15. **Custom CSV Parser:** A robust parser that handles complex delimiters and mixed encoding.

### AI/ML (Advanced Concepts)
16. **Decision Tree from Scratch:** Implement the ID3 algorithm using pure Python OOP.
17. **Custom Scikit-Learn Transformer:** Build a custom preprocessing class for a machine learning pipeline.
18. **ML Model API:** Serve a pre-trained sentiment analysis model via a FastAPI web interface.
19. **News Article Summarizer:** Build a tool to extract key sentences from text using `NLTK` or `SpaCy`.
20. **Stock Price Predictor:** Use `Pandas` and `Scikit-learn` to build a basic time-series forecast model.

### Finance & Quant (Intermediate)
16. **Algorithmic Trading Backtester:** Test a simple moving average crossover strategy on historical price data.
17. **Options Pricing Model:** Implement the Black-Scholes formula to price European call and put options.
18. **Risk Metrics Calculator:** Compute VaR, Sharpe Ratio, and Max Drawdown from a daily returns series.
19. **Financial Report Parser:** Extract key metrics (EPS, revenue) from SEC 10-K HTML filings using `BeautifulSoup`.
20. **Order Book Simulator:** Simulate a basic limit order book with a price-time priority matching engine.

## Advanced Tier (25 Projects)

### Cloud (AWS/Azure/GCP)
1. **Multi-Cloud Inventory Aggregator:** Use `asyncio` to fetch and unify resources from AWS, GCP, and Azure simultaneously.
2. **Custom IaC Tool:** Build a YAML-to-Infrastructure parser that manages cloud resources via their low-level APIs.
3. **Kubernetes Sidecar Injector:** A Python-based admission controller to automatically add logging containers to pods.
4. **Cloud-Native Honey-pot:** Deploy a fake serverless endpoint to capture and analyze malicious request patterns.
5. **Serverless Workflow Engine:** A system that coordinates complex, multi-step Lambda functions with state management.

### Linux & Systems
6. **Async SSH Orchestrator:** Manage and run commands on 1,000+ servers concurrently using `asyncio` and `libssh2`.
7. **Cloud-Backed FUSE Filesystem:** Build a Linux filesystem in userspace that transparently stores data in S3.
8. **Python System Call Tracer:** Use `ptrace` or `ebpf` wrappers to monitor and log every system call made by a process.
9. **Linux Container from Scratch:** Use `unshare` and `cgroups` to build a minimal container isolation tool in pure Python.
10. **Live Kernel Log Analyzer:** A high-performance tool that parses `/dev/kmsg` in real-time to detect hardware failures.

### Data Engineering & Analysis
11. **Distributed Task Queue:** Build a custom `Celery` clone using Redis as a broker and multi-processing workers.
12. **Vector Database Indexer:** Implement basic HNSW or IVF indexing for fast similarity searches on text embeddings.
13. **Parquet Metadata Explorer:** A tool to analyze and optimize the row-group structure of massive Parquet files.
14. **Real-Time Data Dashboard:** Stream system metrics via WebSockets to a live dashboard with zero-latency updates.
15. **AST Data Lineage Tracker:** Use Python's `ast` module to trace how data flows through a complex pipeline of scripts.

### AI/ML (Architectural Foundations)
16. **Autograd Engine from Scratch:** Implement a reverse-mode automatic differentiation engine using pure Python.
17. **NumPy-Only CNN:** Build and train a Convolutional Neural Network for image recognition without PyTorch/TensorFlow.
18. **Attention Mechanism Implementation:** Code a multi-head attention module from the "Attention is All You Need" paper.
19. **RL Agent for Gaming:** Use Reinforcement Learning (Q-Learning) to train a bot that plays a custom text-based game.
20. **Model Compression Suite:** Implement weight pruning and quantization algorithms to shrink a model's memory footprint.

### Finance & Quant (Advanced)
16. **Real-Time Market Data Pipeline:** Stream and normalize tick data from a WebSocket feed using `asyncio`.
17. **Monte Carlo Portfolio Optimizer:** Use simulation to plot the efficient frontier and find the max Sharpe portfolio.
18. **Pairs Trading Engine:** Statistical arbitrage strategy using cointegration tests and z-score entry/exit signals.
19. **Tick Data Aggregator:** Aggregate raw trade ticks into OHLCV bars at arbitrary resolutions with microsecond accuracy.
20. **Sentiment-Driven Signal Generator:** NLP pipeline on financial news headlines to produce long/short trading signals.

## Ultra Tier (25 Projects)

### Cloud (High Performance & Scale)
1.  **Custom Load Balancer:** Cython-optimized Layer 7 load balancer handling 10k req/s using `uvloop`.
2.  **Distributed Consensus Engine:** Implement Raft or Paxos from scratch for a custom cluster state store.
3.  **Serverless Cold Start Optimizer:** Tool analyzing Lambda memory snapshots to optimize init time.
4.  **Global State Store (CRDTs):** Conflict-free Replicated Data Type store for edge synchronization.
5.  **Custom VPN Protocol:** UDP-based encrypted tunnel using raw sockets for maximum throughput.

### Linux & Systems (Kernel & Low Level)
6.  **eBPF Packet Filter:** Python wrapper for eBPF to drop packets at the kernel level (DDoS protection).
7.  **Memory Profiler (C-Ext):** C-extension that hooks into `malloc` to track allocations and leaks.
8.  **Process Freezer:** Tool to checkpoint and restore running processes (similar to CRIU logic).
9.  **Custom File System Driver:** FUSE driver implementing a unique encryption scheme in C/Cython.
10. **Hardware Monitor (I2C/SPI):** Interface directly with hardware sensors via `/sys/class` or memory mapping.

### Data Engineering & Analysis (Internals)
11. **Apache Arrow Clone:** Implement a zero-copy columnar memory format from scratch.
12. **JIT-Compiled Query Engine:** Use Numba to compile SQL-like queries into machine code at runtime.
13. **Custom Serialization Protocol:** Binary format faster than Protobuf using struct packing and memory views.
14. **Shared Memory Dataframe:** Pandas-like structure living in `mmap` shared memory for IPC.
15. **Database Storage Engine:** B-Tree implementation managing raw byte pages on disk.

### AI/ML (Metal & Optimization)
16. **CUDA Kernel in Python:** Use Numba to write custom CUDA kernels for GPU acceleration.
17. **Transformer Inference Engine:** Optimized C++ binding for running LLMs (like `llama.cpp` logic) in Python.
18. **Graph Neural Network (Sparse):** Implement sparse matrix operations for GNNs using Cython.
19. **Federated Learning System:** Encrypted gradient aggregation protocol across unreliable nodes.
20. **Genetic Algorithm Hypervisor:** Evolution strategy that modifies its own code/architecture (AST manipulation).

### Finance & Quant (Ultra)
16. **Custom FIX Protocol Engine:** Implement a FIX 4.2 session and message layer for low-latency order routing.
17. **Lock-Free Order Book (LMAX):** Cache-optimized matching engine using ring buffers and zero-allocation design.
18. **Real-Time Risk Engine:** Sub-millisecond PnL and Greeks calculation across a portfolio using Cython and NumPy.
19. **Alpha Factor Research Platform:** Framework to research, rank, and combine alpha signals across thousands of instruments.
20. **Distributed Backtesting Cluster:** Multi-process engine with vectorized strategy evaluation across decades of tick data.

## God Tier (25 Projects)

### Cloud & Distributed Systems (Planetary Scale)
1.  **Global Distributed Database:** Spanner-like database with true external consistency using atomic clocks logic.
2.  **Serverless Platform from Scratch:** Build the container orchestration, routing, and isolation (Firecracker-like) layers.
3.  **P2P Content Delivery Network:** Decentralized CDN using Kademlia DHT and WebRTC.
4.  **Cloud Hypervisor Controller:** Python interface to KVM/QEMU managing VM lifecycles at the bare metal level.
5.  **Distributed Ledger/Blockchain:** A high-throughput consensus chain with smart contract execution in Python.

### Linux & Kernel (The Metal)
6.  **Custom Python Keyword (C-Level):** Modify CPython source to add a `until` loop or `switch` statement and recompile.
7.  **Python OS Shell:** A complete init system (PID 1) written in Python to manage user space boot.
8.  **Kernel-Level Rootkit Detector:** Analyze raw memory pages (`/dev/mem`) to find hidden process structures.
9.  **Device Driver Interface:** Userspace driver for a custom USB device using `libusb` and `ctypes`.
10. **ELF Binary Patcher:** Tool to inject Python bytecode payloads into running ELF binaries.

### Data Engineering & Internals (Foundational)
11. **Database Storage Engine (LSM Tree):** Implement a Log-Structured Merge-tree storage engine (like RocksDB) in pure Python/C.
12. **Custom Query Language Compiler:** Lexer, Parser, and Optimizer for a SQL-variant compiling to bytecode.
13. **Distributed File System:** Master/Chunkserver architecture (like GFS/HDFS) with replication and fault tolerance.
14. **Memory-Mapped Graph DB:** Zero-copy graph traversals on terabyte-scale datasets using `mmap`.
15. **Data Compression Algorithm:** Implement LZ77 or Huffman coding from scratch for a custom archive format.

### AI/ML (Genesis)
16. **Deep Learning Framework:** Build "PyTorch" from scratch—Tensors, Autograd, Optimizers, and CUDA backends.
17. **Transformer from Scratch (C/CUDA):** Implement the Attention mechanism in C++ with Python bindings for max speed.
18. **Probabilistic Programming Language:** A DSL for Bayesian inference (like Stan/PyMC3) with custom sampling steps.
19. **Neuromorphic Chip Simulator:** Simulate Spiking Neural Networks (SNNs) modeling biological neuron behavior.
20. **AI Code Compiler:** A model that compiles natural language directly into optimized Python bytecode (skipping source).

### Finance & Quant (God)
21. **Full Exchange Matching Engine:** Production-grade exchange with all order types, clearing, and settlement logic.
22. **ML Alpha Generator:** Deep RL agent that learns raw order book features and outputs actionable trading signals.
23. **Custom Financial Time-Series DB:** Columnar storage engine optimized for OHLCV and tick data with custom indexing.
24. **Decentralized Exchange (DEX):** On-chain AMM with Python smart contract logic, LP mechanics, and arbitrage bot.
25. **Systemic Risk Simulator:** Agent-based model simulating financial contagion across a network of interconnected institutions.
