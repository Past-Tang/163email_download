# 163邮箱附件下载工具

![维护状态](https://img.shields.io/badge/维护状态-停止维护-red.svg)
![Python版本](https://img.shields.io/badge/Python-3.6+-blue.svg)
![许可证](https://img.shields.io/badge/许可证-MIT-green.svg)

## 项目概述

此工具是一个简单的Python脚本，用于自动连接163邮箱并下载所有邮件中的附件。该项目已不再维护。

### 主要特点

- 自动连接到163邮箱的IMAP服务器
- 批量下载收件箱中所有邮件的附件
- 自动处理文件名编码问题
- 将所有附件保存到本地目录

## 技术栈

- Python 3.6+
- imapclient：用于IMAP邮件协议处理
- pyzmail：用于解析邮件内容
- email.header：用于处理邮件头编码

## 安装说明

1. 克隆仓库：

```bash
git clone https://github.com/yourusername/163_email_file_download.git
cd 163_email_file_download
```

2. 安装依赖：

```bash
pip install imapclient pyzmail36
```

## 使用方法

1. 编辑`main.py`文件，填入您的163邮箱账号和密码：

```python
email_user = 'your_email@163.com'  # 替换为您的邮箱地址
email_pass = 'your_password'       # 替换为您的邮箱密码
```

2. 运行脚本：

```bash
python main.py
```

3. 所有附件将被下载到`attachments`目录中。

## 配置选项

脚本中可以修改的配置项：

- `email_user`：163邮箱账号
- `email_pass`：163邮箱密码或授权码
- `attachment_dir`：附件保存的本地目录，默认为`attachments`

## 依赖项

- Python 3.6+
- imapclient
- pyzmail36

## 常见问题

### 登录失败

如果遇到登录失败的问题，请确认：

1. 邮箱地址和密码是否正确
2. 163邮箱是否开启了IMAP服务
3. 是否需要使用授权码而非登录密码

### 文件名乱码

脚本已包含编码处理逻辑，但如果仍遇到文件名乱码问题，可能需要修改解码部分的代码以适应特定编码。

## 许可证

MIT

## 维护者

此项目已不再维护。

## 免责声明

使用此工具下载邮件附件时，请确保您有权限访问和下载这些内容。作者不对任何可能的滥用负责。 