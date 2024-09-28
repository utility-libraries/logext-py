# -*- coding=utf-8 -*-
r"""

"""
import logging


__all__ = ['is_configured']


def is_configured() -> bool:
    return len(logging.root.handlers) > 0
