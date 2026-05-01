"""Custom type aliases for the Paper2Video project."""

from typing import Literal

# Type alias for degradation types
Degradation = Literal[
    "low resolution",
    "noise",
    "motion blur",
    "defocus blur",
    "haze",
    "rain",
    "dark",
    "jpeg compression artifact",
    "blur",  # Used as alternative for "low resolution"
]

# Type alias for degradation levels
Level = Literal["very low", "low", "medium", "high", "very high"]

# Type alias for subtask types
Subtask = Literal[
    "super-resolution",
    "denoising",
    "motion deblurring",
    "defocus deblurring",
    "dehazing",
    "deraining",
    "brightening",
    "jpeg compression artifact removal",
]
