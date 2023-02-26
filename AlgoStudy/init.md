```
# Anaconda install
bash <(curl -s https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh)

# Create conda env official 3.8.6, but it's not available, so use 3.8.8
conda create --name algo python=3.8.8

# Activate conda env
conda activate algo
```

如果使用Conda创建了一个名为“alog”的环境，并想在VS Code中使用该环境来编写Python程序，可以按照以下步骤进行配置：

打开VS Code。在左侧边栏中，点击“Explorer”图标，然后打开你的Python项目文件夹。

打开终端。在VS Code中，可以通过按下“Ctrl+Shift+`”组合键打开终端。如果你使用的是Mac系统，则按下“Shift+Command+P”组合键打开命令面板，然后输入“Terminal: Create New Integrated Terminal”并按下回车键即可打开终端。

激活Conda环境。在终端中，可以使用以下命令激活“alog”环境：

Copy code
conda activate alog
这个命令将激活“alog”环境，并将其设置为当前环境。

安装Python扩展。在VS Code中，可以通过点击左侧边栏中的“扩展”图标，搜索并安装Python扩展。安装完成后，VS Code会自动识别Python文件并提供代码补全、语法检查等功能。

配置Python解释器路径。在VS Code中，可以通过按下“Ctrl+Shift+P”组合键打开命令面板(如果没反应的话，点击左下角的设置按钮，菜单第一个就是命令面板)，然后输入“Python: Select Interpreter”并按下回车键，选择“Enter interpreter path”选项，然后输入以下路径：

```bash
/path/to/anaconda/envs/alog/bin/python
```

其中，“/path/to/anaconda”是Anaconda的安装路径，“alog”是你创建的环境名。这个命令将配置VS Code使用“alog”环境中的Python解释器。

配置任务（Task）。按照上面提到的方法，在VS Code中配置一个任务，命令为“python”，参数为当前文件。

运行Python程序。在打开的Python文件中，可以按下“Ctrl+Shift+B”组合键或者使用命令面板（按下“Ctrl+Shift+P”组合键并输入“Tasks: Run Task”）来运行Python程序。

需要注意的是，在使用Conda环境时，需要保证该环境已经正确配置，并且所需的Python模块已经安装。如果遇到问题，可以在任务配置文件中进一步配置任务参数，或者参考VS Code官方文档寻求帮助。


