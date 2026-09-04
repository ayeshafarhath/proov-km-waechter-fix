# log_util.py
# Lightweight logger for KM-Waechter.

import time

_log_lines: list[str] = []


def log(message: str) -> None:
    """Append a timestamped message to the in-memory log and print it."""
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {message}"
    _log_lines.append(line)
    print(line)


def flush_log(path: str) -> None:
    """Write all buffered log lines to the given file path, then clear the buffer."""
    with open(path, "a") as f:
        for line in _log_lines:
            f.write(line + "\n")
    _log_lines.clear()
