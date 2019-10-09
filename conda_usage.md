https://foofish.net/compatible-py2-and-py3.html
https://zhuanlan.zhihu.com/p/22678445
https://blog.csdn.net/apsvvfb/article/details/86703107

多版本切换


## 基于 python3.6 创建一个名为test_py3 的环境

> conda create --name test_py3 python=3.7 

## 基于 python2.7 创建一个名为test_py2 的环境

> conda create --name test_py2 python=2.7

## 至少需要指定python版本或者要安装的包. 后一种情况下，自动安装最新python版本

同时安装必要的包

> conda create -n env_name numpy matplotlib python=3.7

## 激活 test 环境

> activate test_py2  # windows

> source activate test_py2 # linux/mac

## 切换到python3

> activate test_py3

## 查看当前系统下的环境

> conda info -e

## 移除环境

用户安装的不同python环境都会被放在目录~/anaconda/envs下，可以在命令中运行conda info -e 查看已安装的环境，当前被激活的环境会显示有一个星号或者括号。

> conda remove -n env_name --all

更多命令，可查看帮助 conda -h

# 包管理工具

conda 的包管理功能是对 pip 的一种补充，如果当前已经激活了某个Python环境，那么就可以在当前环境开始安装第三方包。

给某个特定环境安装package有两个选择，一是切换到该环境下直接安装，二是安装时指定环境参数-n

> activate env_name

> conda install pandas

安装anaconda发行版中所有的包

> conda install anaconda
> conda install -n env_name pandas



## 安装 matplotlib 

> conda install matplotlib

## 查看已安装的包

> conda list 

指定查看某环境下安装的package

> conda list -n env_name

## 包更新

> conda update matplotlib

## 查找包

> conda search pyqtgraph

## 删除包

> conda remove matplotlib

对于那些用 pip 无法安装成功的模块你都可以尝试用 conda 来安装，如果用 conda 找不到相应的包，当然你继续选择 pip 来安装包也是没问题的。

## conda清理瘦身

anaconda就像一个相对独立的生态，所有被安装的包都在anaconda的安装目录下客观存在者，客观占用着我们的硬盘空间，随着使用到的包越来越多，一次次伴随安装的依赖包也越来越多，还有Python每个版本都对应了自身的一整套包，例如Python3.5和3.6就分别对应了各自的一整套包，anaconda文件夹的体积也越来越大，突发奇想查看一下呗，7.8G，瞬间被吓倒，怎么解决呢，很简单！

conda clean就可以轻松搞定！
第一步：通过conda clean -p来删除一血没用的包，这个命令会检查哪些包没有在包缓存中被硬依赖到其他地方，并删除它们。
第二步：通过conda clean -t可以将conda保存下来的tar包。
经过上面两步，我的anaconda便变成了4.3G，几乎瘦身一半。有一点要注意的是，conda clean命令是对所有anaconda下的包进行搜索，当然也包括构建的其他Python环境中的包，这一点还是很高效的，不用再进入其他环境重复操作。

## 配置 Pycharm
File | Settings | Project: mclearning | Project Interpreter | Show All… 
然后进入 Add Python Interpreter，先选左侧Conda Environment ，然后勾选 Existing environment，选择之前配好的py环境
比如需要配置py2.7就 /home/veyron/anaconda3/envs/py2/bin/python
比如需要配置py2.7就 /home/veyron/anaconda3/envs/py3/bin/python

# 提高下载速度

Anaconda 的镜像地址默认在国外，用 conda 安装包的时候会很慢，目前可用的国内镜像源地址是清华大学提供的。修改 ~/.condarc (Linux/Mac) 或 C:\Users\当前用户名.condarc (Windows) 配置

> channels:
 - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
 - defaults
show_channel_urls: true

如果命令行方法添加不上，可以在用户目录下的.condarc中添加https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/：

如果没有该文件可以直接创建，
Windows为C://Users/username/.condarc
Linux/Mac为~/.condarc

除此之外，你也可以把 pip 的镜像源地址也换成国内的，豆瓣源速度比较快。修改 ~/.pip/pip.conf (Linux/Mac) 或 C:\Users\当前用户名\pip\pip.ini (Windows) 配置：

> [global]
trusted-host =  pypi.douban.com
index-url = http://pypi.douban.com/simple