# [loggext.formatting][]

loggext offers some pre-defined formats in [loggext.formatting.default_formats][].

## [LoggingFormatBuilder][loggext.formatting.LoggingFormatBuilder]

If you like your own format you can use the [LoggingFormatBuilder][loggext.formatting.LoggingFormatBuilder] to create the logging-format in a more humane or dynamic way.

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
