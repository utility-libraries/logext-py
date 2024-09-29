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
