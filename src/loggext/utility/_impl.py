# -*- coding=utf-8 -*-
r"""

"""
import os
import sys
import logging


__all__ = ['logging_is_configured']


def logging_is_configured() -> bool:
    r"""
    :returns: if :func:`logging.basicConfig` was already called. (if the root-logger has handlers)
    """
    return len(logging.root.handlers) > 0


def is_running_as_service() -> bool:
    r"""
    :returns: if the current script is running as a service (or not)
    """
    return os.getenv('TERM') is None and os.isatty(sys.stdin.fileno())


def is_running_in_shell() -> bool:
    r"""
    :returns: if the current script is running in a shell (or not)
    """
    return os.isatty(sys.stdin.fileno())
