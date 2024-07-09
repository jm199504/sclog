### sclog（scrcpy log）安卓设备录屏日志工具

#### 1. 安装引导

该工具可通过下载源码后，在`sclog/dist`目录下执行以下命令安装：

```
pip3 install sclog-1.0.tar.gz
```

安装输入输出，若显示`Successfully installed sclog-1.0`表示安装成功：

```cmd
➜  dist pip3 install sclog-1.0.tar.gz 
Processing ./sclog-1.0.tar.gz
  Preparing metadata (setup.py) ... done
Installing collected packages: sclog
  DEPRECATION: sclog is being installed using the legacy 'setup.py install' method, because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. pip 23.1 will enforce this behaviour change. A possible replacement is to enable the '--use-pep517' option. Discussion can be found at https://github.com/pypa/pip/issues/8559
  Running setup.py install for sclog ... done
Successfully installed sclog-1.0

```



#### 2. 使用介绍

该工具主要应用于安卓车机进行debug调试时，发现了error/crash时，考虑复现对车机录屏和日志抓取功能，并将日志和录屏文件进行打包压缩，复现前打开cmd终端输入`sclog`即可运行该脚本。



#### 3. 主函数（功能）介绍

```python
def main():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    logcat_filename = "logcat_{}.log".format(timestamp)
    output_filename = "video_{}.mp4".format(timestamp)
    zip_filename = "logs_and_screen_{}.zip".format(timestamp)

    record_screen(logcat_filename, output_filename)
    create_zip(logcat_filename, output_filename, zip_filename)

```

（1）获取当前时间

（2）在当前目录创建`logcat_{当前时间}.log`日志文件

（3）在当前目录创建`video_{当前时间}.mp4`录屏文件

（4）将日志文件和录屏文件压缩至`logs_and_screen_{当前时间}.zip`压缩文件

