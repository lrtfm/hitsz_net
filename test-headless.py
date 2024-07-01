import os
import sys
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print('PATH = ', os.environ['PATH'])

home_url = 'https://www.baidu.com'

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--safe-mode')

# profile = webdriver.FirefoxProfile()
# profile.set_preference("javascript.enabled", False)
# options.profile = profile

service = webdriver.FirefoxService(
    log_output='ffservice.log',
    service_args=['--log-no-truncate', '--log', 'debug'])

driver = webdriver.Firefox(options=options, service=service)

driver.get(home_url)

# 等待页面加载
time.sleep(1)


