"""
╔═══════════════════════════════════════════════════════════════════╗
║                    R6 LOCKER CHECKER - CONFIG                     ║
╚═══════════════════════════════════════════════════════════════════╝
Configuration settings for the R6 Skins Account Checker
"""

from dataclasses import dataclass, field
from typing import Optional
import os


@dataclass
class BrowserConfig:
    """Browser and automation settings."""
    max_workers: int = 2                    # Parallel browser instances (increased)
    window_width: int = 500                 # Browser window width (compact)
    window_height: int = 600                # Browser window height (compact)
    page_timeout: int = 5                   # Page load timeout (reduced)
    login_timeout: int = 18                 # Max time per login attempt (reduced)
    captcha_click_interval: float = 0.3     # Seconds between captcha clicks (reduced)
    worker_stagger_delay: float = 0.8       # Delay between starting workers (reduced)
    headed: bool = True                     # Run with visible browser (False for headless)


@dataclass
class TimingConfig:
    """Timing constants - optimized for speed."""
    post_navigate_wait: float = 0.2         # Wait after page navigation (reduced)
    post_submit_wait: float = 0.5           # Wait after form submission (reduced)
    post_login_stats_wait: float = 0.2      # Wait before extracting stats (reduced)
    post_refresh_wait: float = 0.3          # Wait after page refresh (reduced)
    poll_interval_fast: float = 0.15        # Fast polling interval (reduced)
    poll_interval_slow: float = 0.25        # Slow polling after 5s (reduced)
    poll_slowdown_threshold: float = 6.0    # Seconds before switching to slow poll
    stuck_threshold: float = 12.0           # Seconds before considering stuck (reduced)
    inter_account_delay: float = 0.2        # Base delay between accounts (reduced)
    queue_timeout: float = 1.0              # Worker queue get timeout (reduced)


@dataclass
class RetryConfig:
    """Retry and rate limiting settings."""
    max_retries: int = 1                    # Max retries per account (reduced)
    rate_limit_wait: int = 15               # Base wait time when rate limited (reduced)
    rate_limit_backoff_mult: float = 1.3    # Multiplier for consecutive rate limits
    rate_limit_max_wait: int = 60           # Max wait time for rate limits (reduced)
    retry_delay: float = 0.5                # Base delay between retries (reduced)
    stuck_threshold: int = 8                # Attempts before refresh (reduced)


@dataclass
class AccountConfig:
    """Account loading and processing settings."""
    shuffle: bool = False                   # Shuffle accounts to prevent burst patterns
    shuffle_seed: Optional[int] = None      # Seed for reproducible shuffling (None = random)


@dataclass
class WebhookConfig:
    """Discord webhook settings."""
    enabled: bool = True
    config_file: str = "webhook_config.txt"
    timeout: int = 3                        # Request timeout (reduced)
    queue_workers: int = 2                  # Async webhook workers


@dataclass
class OutputConfig:
    """Output and logging settings."""
    results_dir: str = "results"
    accounts_file: str = "accounts.txt"
    flush_interval: int = 5                 # Flush results every N accounts
    remove_failed: bool = True              # Remove failed accounts from file


@dataclass
class UIConfig:
    """UI and display settings."""
    show_progress_bar: bool = True
    compact_mode: bool = False              # Less verbose output
    color_theme: str = "cyber"              # cyber, neon, classic


@dataclass 
class Config:
    """Master configuration container."""
    browser: BrowserConfig = field(default_factory=BrowserConfig)
    retry: RetryConfig = field(default_factory=RetryConfig)
    webhook: WebhookConfig = field(default_factory=WebhookConfig)
    output: OutputConfig = field(default_factory=OutputConfig)
    ui: UIConfig = field(default_factory=UIConfig)
    timing: TimingConfig = field(default_factory=TimingConfig)
    accounts: AccountConfig = field(default_factory=AccountConfig)
    
    # Target URL
    target_url: str = "https://r6skins.locker/home"
    
    # Debug settings
    debug_html_on_failure: bool = False     # Log raw HTML on unexpected failures
    debug_dir: str = "debug_logs"           # Directory for debug output
    
    def __post_init__(self):
        """Ensure directories exist."""
        os.makedirs(self.output.results_dir, exist_ok=True)
        if self.debug_html_on_failure:
            os.makedirs(self.debug_dir, exist_ok=True)


# Global config instance
config = Config()
