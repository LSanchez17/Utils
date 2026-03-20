"""Convert time strings to milliseconds.

Supported formats:
- "SS" (seconds)
- "M:SS" (minutes:seconds)
- "H:MM:SS" (hours:minutes:seconds)

Assumes valid inputs and bounds (seconds/minutes < 60, hours < 24).
"""
from __future__ import annotations

from typing import List


def convert_time_to_milliseconds(time_str: str) -> int:
    """Convert a time string to milliseconds.

    Examples:
    - "01:33" -> 93000
    - "33" -> 33000
    - "2:01" -> 121000
    - "2" -> 2000
    - "1:23:33" -> 5013000
    """
    parts: List[str] = [p.strip() for p in time_str.split(":")]
    if len(parts) == 1:
        hours = 0
        minutes = 0
        seconds = int(parts[0])
    elif len(parts) == 2:
        hours = 0
        minutes = int(parts[0])
        seconds = int(parts[1])
    elif len(parts) == 3:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
    else:
        raise ValueError(f"Unsupported time format: {time_str}")

    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds * 1000


__all__ = ["convert_time_to_milliseconds"]
