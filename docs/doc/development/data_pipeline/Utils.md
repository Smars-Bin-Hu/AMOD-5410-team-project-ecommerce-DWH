# /data_pipeline/Utils.py

> Edited By: Smars Hu
> Date: 05 Mar 2025

这个类是Python OOP的工具类
核心代码如下
[Utils.py](../../../../data_pipeline/utils.py)

## OracleDatabaseUtils 组件开发

#### 代码依赖库：

1. 用到jaydebeapi模块。
2. 代码要用到logging用于生成日志
3. 用到config（自定义类），读取常量信息

#### 代码逻辑：

- 启动日志
- 用jaybeapi连接Oracle数据库，从config类中读取常量信息（数据库连接信息，比如driver，URL，username，password，JDBC driver path等）
- 连接Oracle数据库，尝试运行SQL
- 如果没异常就返回True，异常就返回False

#### 注意事项

> 三个nodemanager节点需要提前安装 pip install JayDeBeApi。因为他们本地的python环境需要这个package才能跑脚本

```bash
(pyspark_env) root@hadoop-worker2:~# pip install JayDeBeApi
    Collecting JayDeBeApi
    Downloading JayDeBeApi-1.2.3-py3-none-any.whl.metadata (10 kB)
    Collecting JPype1 (from JayDeBeApi)
    Downloading jpype1-1.5.2-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl.metadata (4.9 kB)
    Collecting packaging (from JPype1->JayDeBeApi)
    Downloading packaging-24.2-py3-none-any.whl.metadata (3.2 kB)
    Downloading JayDeBeApi-1.2.3-py3-none-any.whl (26 kB)
    Downloading jpype1-1.5.2-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (467 kB)
    Downloading packaging-24.2-py3-none-any.whl (65 kB)
    Installing collected packages: packaging, JPype1, JayDeBeApi
    Successfully installed JPype1-1.5.2 JayDeBeApi-1.2.3 packaging-24.2
    WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable.It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
```

#### 单元测试代码链接：

[Utils.py](../../../../test/unit_test/data_pipeline/test_oracle_connect.py)

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

。。。