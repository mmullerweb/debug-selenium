from flask import Flask, render_template, request, redirect, session, flash, url_for
from time import sleep
from selenium import webdriver
import os
from sys import platform


application = Flask(__name__)

##################

if platform == "linux" or platform == "linux2":
	chromeDriverPath = "./driver/linux/chromedriver"
elif platform == "darwin":
	chromeDriverPath = "./driver/osX/chromedriver"
else:
	chromeDriverPath = "./driver/win/chromedriver"

##################
##################

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_settings.popups": 0,"download.default_directory": os.getcwd() + "/tmp","directory_upgrade": True}
options.add_experimental_option("prefs", prefs)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
driver = webdriver.Chrome(executable_path=chromeDriverPath, options=options)

##### Lib
exec(open("./lib/libs.py").read(), globals()) 
##################

@application.route('/', methods=['GET'])
def index():
	return render_template('debug.html',codigo='')

@application.route('/codigo', methods=['POST'])
def codigo():
	#exec(open("./marreta-code.py").read(), globals())
	codigo = request.form.get('codigo')
	exec(codigo,globals())
	return render_template('debug.html',codigo=codigo)


# running application
if(__name__) == '__main__':
  application.run(threaded=True, debug=False, port=3000)
