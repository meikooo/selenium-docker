import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#指定运行主机与端口号,也就是上一步在浏览器中输入的地址，只是换了之后的相对路径/grid/console换为/wd/hub

driver = webdriver.Remote(
     command_executor='http://10.4.34.162:4444/wd/hub',
     desired_capabilities=DesiredCapabilities.CHROME)

base_url='https://y.qq.com/n/yqq/song/001VySE80MYPrC.html'
driver.get(base_url)
driver.implicitly_wait(30)
driver.find_element_by_class_name('mod_btn_green js_all_play').click()
time.sleep(60)
driver.close()
