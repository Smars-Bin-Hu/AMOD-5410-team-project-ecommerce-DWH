import logging
from batch_processing.configs import LoggingConfig


class LoggingUtils:
    """Initialize for customized logging operations."""

    @staticmethod
    def setup_custom_logger(log_name:str, log_level:int, level_name:str) -> logging.getLogger:
        """
        Setup a customized logger with a new log level.

        Args:
            log_name(str) : Custom log name. Use the file name `__name__` by default
            log_level (int): Custom log level (e.g., 25).
            level_name (str): Name for the custom log level.

        Returns:
            logging.Logger: Configured logger instance.
        """

        # Register the new log level
        logging.addLevelName(log_level, level_name)

        # customize logging method: for logger.smars_dev("log content")
        # bind the smars_dev() to Logger Class
        def smars_dev(self, message, *args, **kwargs):
            """
            Custom log function bound to logging.Logger.
            Logs messages at the specified custom log level.

            Args:
                self (logging.Logger): Logger instance.
                message (str): Log message.
                *args: Additional arguments.
                **kwargs: Additional keyword arguments.
            """
            if self.isEnabledFor(log_level):
                self._log(log_level, message, args, **kwargs)

        # Attach the custom logging method to the Logger class dynamically
        setattr(logging.Logger, level_name.lower(), smars_dev)

        # Config the certain logger level for its format, handlers etc.
        logging.basicConfig(
            level=log_level,
            format="%(asctime)s - %(name)s - %(levelname)s: - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[logging.StreamHandler()]  # Console output handler
        )

        # Return the logger instance for the current module with custom name
        return logging.getLogger(log_name)

# create a logger for the spark etl job only
logger = LoggingUtils.setup_custom_logger(
    "SPARK_ETL_LOGGER",
    int(LoggingConfig.get_smars_dev_log_level()),
    LoggingConfig.get_smars_dev_log_level_name()
)
