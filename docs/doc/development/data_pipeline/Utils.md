# /data_pipeline/Utils.py

> Edited By: Smars Hu
> Date: 05 Mar 2025

这个类是Python OOP的工具类
核心代码如下
[Utils.py](../../../../data_pipeline/utils.py)

## OracleDatabaseUtils 组件开发

> Edited By: Smars Hu
> Date: 05 Mar 2025

### 代码依赖库：

1. 用到jaydebeapi模块。
2. 代码要用到logging用于生成日志
3. 用到config（自定义类），读取常量信息

### 代码逻辑：

[Utils.py](../../../../data_pipeline/utils.py)

- 启动日志
- 用jaybeapi连接Oracle数据库，从config类中读取常量信息（数据库连接信息，比如driver，URL，username，password，JDBC driver path等）
- 连接Oracle数据库，尝试运行SQL
- 如果没异常就返回True，异常就返回False

```python

```
### `test_oracle_connection()` Development

#### 注意事项

> 三个nodemanager节点需要提前安装 pip install JayDeBeApi。因为他们本地的python环境需要这个package才能跑脚本

```bash
(pyspark_env) root@hadoop-worker2:~# pip install JayDeBeApi
```

#### 单元测试：



在Spark容器上，运行上面的python单元测试代码，连接oracle，返回成功：

```bash
(pyspark_env) root@spark:/opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/test/unit_test/data_pipeline# python test_oracle_connect.py 
debug111
Attempting to connect to Oracle Database...
Successfully retrieved row: (1,)
Debug: Oracle Database Connected!
```

#### 故障处理：
暂无

## HDFSUtils  组件开发

> Edited By: Smars Hu
> Date: 05 Mar 2025

###

### 代码依赖库：


#### 注意事项

#### 单元测试代码链接：

#### 故障处理：

## LoggingUtils 组件开发

> Edited By: Smars Hu
> Date: 06 Mar 2025

### 代码依赖库：

1. logging - Provides core logging functionalities.
   
### 代码逻辑：

[Utils.py](../../../../data_pipeline/utils.py)

```python
class LoggingUtils:
    """Utility class for customized logging operations."""

    @staticmethod
    def setup_custom_logger(log_name:str, log_level:int, level_name:str):
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
```

### `setup_custom_logger()` Development

#### Usage Example

#### ``
```python
from logging_utils import LoggingUtils

# Define custom log level
SMARS_DEV_LEVEL = 25
logger = LoggingUtils.setup_custom_logger(SMARS_DEV_LEVEL, "SMARS_DEV")

# Use the custom log level
logger.smars_dev("This is a custom log message.")
logger.info("This is an INFO level log.")  # Standard logging still works
```

#### 注意事项

1. Custom Log Levels Must Be Unique

    Ensure that `level_name` is not a built-in log level (`DEBUG`, `INFO`, `WARNING`, etc.).

2. Logging Configuration Affects All Loggers
   
    The `basicConfig()` method applies globally. If multiple logging configurations exist in a project, ensure they don’t conflict.

3. Custom Log Levels Are Accessible Like Built-in Levels
   
    Once registered, the new log level can be used as `logger.<level_name.lower()>("Message")`


#### 单元测试代码链接：

[Utils.py](../../testing/setup_custom_logger.md)

#### 故障处理：

None