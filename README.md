# R6 Locker Account Checker

<div align="center">

```
██████╗  ██████╗     ██╗      ██████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔════╝     ██║     ██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝███████╗     ██║     ██║   ██║██║     █████╔╝ █████╗  ██████╔╝
██╔══██╗██╔═══██╗    ██║     ██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝    ███████╗╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
```

**High-Performance Rainbow Six Siege Account Checker**

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Private-red?style=flat-square)]()

</div>

---

## Features

| Feature | Description |
|---------|-------------|
| 🚀 **Parallel Processing** | Run multiple browsers simultaneously |
| 🔒 **Undetected Mode** | Bypasses bot detection using nodriver |
| 🤖 **Auto Captcha** | Handles Cloudflare Turnstile automatically |
| 📊 **Live Statistics** | Real-time progress with ETA estimation |
| 💬 **Discord Webhooks** | Instant notifications for valid accounts |
| 📁 **Auto Cleanup** | Removes invalid accounts from source file |
| ⚙️ **CLI Interface** | Easy command-line configuration |

---

## Requirements

- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Chrome Browser** (auto-managed)
- **Windows 10/11** (recommended)

---

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Add Accounts

Edit `accounts.txt` with your accounts (one per line):

```
email@example.com:password123
another@email.com:password456
```

### 3. Configure Webhook (Optional)

Edit `webhook_config.txt` with your Discord webhook URL:

```
https://discord.com/api/webhooks/YOUR_WEBHOOK_URL
```

### 4. Run

```bash
python checker.py
```

---

## CLI Options

```
usage: checker.py [-h] [-w WORKERS] [--headless] [--shuffle] [--timeout TIMEOUT] [-v] [accounts_file]

positional arguments:
  accounts_file         Path to accounts file (default: accounts.txt)

options:
  -h, --help            Show help message
  -w, --workers N       Number of parallel browsers (default: 2)
  --headless            Run in headless mode (no visible window)
  --shuffle             Shuffle accounts before checking
  --timeout SECONDS     Login timeout per account (default: 25)
  -v, --version         Show version
```

### Examples

```bash
# Use custom accounts file
python checker.py my_accounts.txt

# Run with 3 workers in headless mode
python checker.py -w 3 --headless

# Shuffle accounts and use 60 second timeout
python checker.py --shuffle --timeout 60
```

---

## Configuration

Edit `config.py` to customize default behavior:

```python
@dataclass
class BrowserConfig:
    max_workers: int = 2        # Parallel browsers (1-5 recommended)
    window_width: int = 500     # Browser window width
    window_height: int = 600    # Browser window height
    login_timeout: int = 25     # Max seconds per login attempt
```

### Performance Guide

| Workers | RAM Usage | Speed | Reliability |
|---------|-----------|-------|-------------|
| 1 | ~500MB | Slow | High |
| 2 | ~1GB | Medium | High |
| **3** | ~1.5GB | **Fast** | **Good** |
| 4 | ~2GB | Very Fast | Medium |

---

## Output

Results are saved to `results/results_YYYYMMDD_HHMMSS.txt`:

```
# R6 Locker Checker Results - 2025-01-15 10:30:00
# Format: email:password | username | level | credits | renown | items | elites | platform

email@example.com:pass123 | PlayerName | Lv150 | Credits: 500 | Renown: 10000 | 250 items | 5 elites | PC
```

---

## Discord Webhook

When configured, valid accounts send rich embeds with:

- 📧 Email & Password (spoilered)
- 📊 Level with color coding
- 💳 Credits & Renown
- 🎒 Items & Elites count
- 🎮 Platform (PC/PSN/XBL)

**Level Colors:**
- 🟣 Purple: 200+
- 🟢 Green: 100+
- 🟡 Yellow: 50+
- 🟠 Orange: <50

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Captcha stuck | Wait for auto-refresh or increase timeout |
| Rate limited | Checker auto-waits with exponential backoff |
| Browser crashes | Reduce workers with `-w 1` |
| "accounts.txt not found" | Create the file with account data |

---

## Running Tests

```bash
python tests.py
```

---

## Project Structure

```
├── checker.py          # Main application
├── config.py           # Configuration settings
├── tests.py            # Unit tests
├── accounts.txt        # Account list (user-provided)
├── webhook_config.txt  # Discord webhook URL
├── requirements.txt    # Python dependencies
├── results/            # Output directory
└── README.md           # This file
```

---

## Disclaimer

This tool is for educational purposes only. Use responsibly and in accordance with applicable terms of service.

---

<div align="center">

**Made for the R6 Community**

</div>
