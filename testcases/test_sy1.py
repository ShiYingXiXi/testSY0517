from selenium import webdriver

# brower = webdriver.Firefox()
brower = webdriver.Chrome()
brower.get('https://www.baidu.com')
assert "那英"
