import datetime

# Level Constants
DEBUG = "DEBUG"
ERROR = "ERROR"
INFO = "INFO"

class Logger:

    # ANSI Colors
    _COLORS = {
        DEBUG: "\033[94m", # Blue
        ERROR: "\033[91m", # Red
        INFO:  "\033[92m", # Green
        "RESET": "\033[0m"
    }

    def __init__(self, show_debug: bool = True):
        self.show_debug = show_debug

    def log(self, message: str, level: str = INFO):
        """
        Logs a message with a specific level.
        """
        # Skip debug messages if disabled
        if level == DEBUG and not self.show_debug:
            return

        # Get current time
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")

        # Get color based on level (default to white if unknown)
        color = self._COLORS.get(level, self._COLORS["RESET"])
        reset = self._COLORS["RESET"]

        # Print formatted log: [TIME] [LEVEL] Message
        print(f"{color}[{timestamp}] [{level}] {message}{reset}")
