# Usage

## ColoredConsoleHandler

The `ColoredConsoleHandler` is similar to the `logging.StreamHandler` with the difference of colored output.

The color is dependent on the logging-level.

## logging-decorator

The `add_logging` decorator can quickly add logging to a function or method which can help during debugging.

The logging-messages include:

- when the function is called and with which arguments
- when the function returns, how long it took and what was returned
- when the function failed and an exception is raised

```python
import logging
from loggext.decorators import add_logging

logger = logging.getLogger(__name__)

@add_logging(
  logger=logger,  # (1)
  call=True,  # (2)
  call_args=True,  # (3)
  timeit=True,   # (4)
  timeit_precision=2,  # (5)
  result=True,  # (6)
)
def myfn(arg):
    ...  # your code

myfn("value")
# DEBUG:root:<function myfn at 0x7f06a6cc3400> was called with ('value')
# DEBUG:root:<function myfn at 0x7f06a6cc3400> returned None after 65μs+614ns
```

1. species a custom logger
2. whether to log when the function is called
3. whether to log the passed arguments of the function-call.
4. whether to measure the performance of the function
5. number of units when formatting the timing. <br>
   1: 65μs <br>
   2: 65μs+614ns
6. whether to log the returned value

### async functions

The `add_logging` decorator also supports asnyc-functions.

```python
from loggext.decorators import add_logging

@add_logging()
async def async_function():
    ...  # your code
```

### Performance

Worried about the performance? You don't need to!

If your logger is not configured for `logging.DEBUG` messages then they are neither generated nor logged.
This way no computation is wasted to e.g. convert the complex function-arguments to their representative form.

## Extra-Data

The attribute from the normal `logging.LogRecord` are quite good but can be extended.
For that case there are some providers in [loggext.extradata][] which inject additional fields.

This allows you to add for example the hostname of the current device to your log-message.

```python
import logging
from loggext.extradata import HostnameField, UsernameField, ProgramNameField

logging.basicConfig(
   format='%(programName)s | %(message)',
)
logging.getLogger().addFilter(HostnameField() | ProgramNameField())  # (1)
logging.getLogger().addFilter(UsernameField())

logging.info("Hello World")  # "script.py | Hello World"
```

1. by loggext provided fields can be combined with `|` or `&`.

## Format-Builder

The [LoggingFormatBuilder][loggext.formatting.LoggingFormatBuilder] can be used to create the logging-format in a more human way.
Additionally, you could use some pre-defined formats from [loggext.formatting.default_formats][]. 

```python
from loggext.formatting import LoggingFormatBuilder

logging_format: str = LoggingFormatBuilder(separator=" | ") \
     .add_asctime() \
     .add_levelname(".3") \
     .add_module("<10") \
     .add_lineno(">3") \
     .add_message() \
     .build()
# '{asctime} | {levelname:.3} | {module:<10} | {lineno:>3} | {message}'
```
