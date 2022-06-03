# CourseRobber-四川农业大学抢课脚本🙋

⚠️此项目仅供学习使用，请勿用于商业用途

⚠️具体抢课结果和所处网络环境相关，抢课失败的可能性依然存在，请谨慎使用

## 使用方法📖
### 使用发行版本（推荐）✨
从release处下载发布的最新版本，解压，文件夹如下
![1.png](./docs/1.png)
双击main.exe打开，进入抢课界面
<img src="./docs/2.png" alt="2.png" style="zoom:75%;" />

**基础使用**：输入用户名密码，选择相应的学期与课程号，点击抢课即可

**专业面板**

1. 输入用户名和密码后可以直接点击仅登录
2. 选择定时抢课并设置时间，之后按照基础使用进行后会在当日到达时间后进行自动的抢课
3. 点击**不显示浏览器**可以使得Edge浏览器界面不显示（不建议选择）

**注意**：本项目的自动化过程基于Eege浏览器，版本为101.0，一般使用Windows均会预装，你可以如下进行确认

1. 打开Eege并进入设置
2. 点击关于Microsoft Edge
3. 查看版本号
![3.png](./docs/3.png)


### 使用源码🐍
clone本项目到电脑，使用`pip install -r requirements.txt`安装依赖, 并运行`python main.py`, 进入抢课界面，之后步骤与直接下载相同。

## 待完成内容💼
- [ ] 加入选择多门课程的选择
