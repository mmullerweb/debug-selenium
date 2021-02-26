<h1>Debug Selenium!</h1>


![N|Solid](https://www.python.org/static/img/python-logo@2x.png)


# Propósito
Navegue com o browser que o Selenium inicia e injetar codigos Python em tempo de execução. Marreta boa para desenvolver.

# Help
- Flask + Selenium!
- Chrome Driver precisa ser da mesma versão do Chrome instalado na máquina
- lib/libs.py (Acesso a base, outras infos ou defs que serão usadas em runtime!!!!)

# Requisitos
- Python 3 (https://www.python.org/downloads/)
- Chrome Driver (https://chromedriver.chromium.org/downloads).

# Comece aqui!
1. pip3 install -r requirements.txt
2. python3 -u server.py
3. Aguarde abrir o browser automaticamente
4. Abra uma aba no browser que iniciou e coloque a url ``` http://localhost:3000 ```
5. Coloque no textarea o codigo ``` driver.get("https://google.com.br") ``` ou use  ``` driver.get(url_test) ```
6. Aperte botão enviar e confira na primeira aba!!! :)

# Obs
- A variável ``` url_test ``` vem do arquivo lib/libs.py

