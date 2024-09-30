# [loggext.handlers][]

## [ColoredConsoleHandler][loggext.handlers.ColoredConsoleHandler]

The [ColoredConsoleHandler][loggext.handlers.ColoredConsoleHandler] is similar to the `logging.StreamHandler` with the difference of colored output.

The color is dependent on the logging-level.

## [LevelColoredConsoleHandler][loggext.handlers.LevelColoredConsoleHandler]

If you don't like it as colorful there is also the [LevelColoredConsoleHandler][loggext.handlers.LevelColoredConsoleHandler].
This one also colors the output, but only the `%(level)s` part and not the whole message.
