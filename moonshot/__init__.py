"""Top-level module for moonshot."""
from beartype.claw import beartype_this_package

from .model import my_model

__all__ = ["my_model"]

beartype_this_package()