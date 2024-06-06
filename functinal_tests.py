from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8080')

assert 'To-Do' in browser.title

browser.quit()