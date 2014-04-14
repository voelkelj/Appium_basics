import os
from random import randint
from selenium import webdriver

script_path = os.getcwd()#get current working directory

app = os.path.join(os.path.dirname(__file__), script_path + '/HelloWorldAppiumTest.app')
app = os.path.abspath(app)
driver = webdriver.Remote(command_executor = 'http://127.0.0.1:4723/wd/hub', desired_capabilities={'browserName':'iOS','device':'iPhone Simulator', 'platform':'Mac', 'version':'7.1', 'app':app})#set selenium server address and capabilities

button = driver.find_element_by_name('Click me!!')#find the app's button by its name
button.click()#tap the button

