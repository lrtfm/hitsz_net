# 哈工大(深圳)校园网络登陆助手
-- 用于无图形化界面的Linux服务器

## 依赖

请自行安装 Python3 和 Firefox 浏览器. 下面将会叙述如何安装 Selenium 和 Firefox 驱动.

1. Python3

2. Firefox 浏览器

   需要浏览器所在路径在环境变量 PATH 中

3. Selenium

4. Firefox 驱动 [geckodriver](https://github.com/mozilla/geckodriver/releases)

## 安装与使用

1. 下载代码

    ```
    git clone https://github.com/lrtfm/hitsz_net.git
    ```

2. 创建虚拟环境

   ```
   cd hitsz_net
   python3 -m venv --copies venv
   ```

3. 激活环境

   ```
   source venv/bin/activate
   ```

4. 安装 Selenium

   ```
   pip install selenium
   ```

5. 安装 Firefox 驱动

   a. 下载驱动

      下载地址 https://github.com/mozilla/geckodriver/releases

      请根据浏览器版本选择驱动版本下载 https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html

   b. 解压后移动文件 `geckodriver` 到文件夹 `venv/bin`

   命令行下载安装示例:

   ```
   wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz
   tar -zxvf geckodriver-v0.34.0-linux64.tar.gz
   mv geckodriver venv/bin/
   ```

6. 运行
   ```
   python3 hitsz_net.py
   ```
