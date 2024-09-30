# [loggext.extradata][]

The attribute from the normal `logging.LogRecord` are quite good but can be extended.
For that case there are some providers in [loggext.extradata][] which inject additional fields.

This allows you to add (e.g.) the hostname of the current device to your log-message.

!!! example
    ```python
    import logging
    from loggext.extradata import ProgramNameField
    
    logging.basicConfig(
       format='%(programName)s | %(message)',
    )
    ProgramNameField().install()  # (1)
    
    logging.info("Hello World")  # "script.py | Hello World" (2)
    ```

    1. This adds the `programName`-field to all handlers of the root-logger. This way you can use `logging.getLogger(__name__)` in sub-packages without getting an error because of a missing field.
    2. Example output
