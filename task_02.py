#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using custom exception class"""


class CustomError(Exception):
    """A class called CustomError, with an argument of Exception."""

    def __init__(self, msg, cause):
        """A constructor for CustomError.

        Args:
            Has 2 arguments; msg and cause.

        Attribute:
            cause(mixed): can take any value.
        """
        Exception.__init__(self)
        self.cause = cause
        self.msg = msg