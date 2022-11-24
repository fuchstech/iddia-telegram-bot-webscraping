from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from telegram.ext import Updater, CommandHandler, MessageHandler
from time import sleep
service = Service(executable_path="/home/fuchs/Desktop/salih_project/chromedriver")
options = webdriver.ChromeOptions()
#options.add_argument('headless')
driver = webdriver.Chrome(options=options, service=service)

# Hangi Browserı kullanmak istediğinize göre değiştirebilirsiniz örn.webdriver.Firefox()
# Chrome:https://sites.google.com/chromium.org/driver/
# Edge:https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Firefox:https://github.com/mozilla/geckodriver/releases
# Safari:https://webkit.org/blog/6900/webdriver-support-in-safari-10/

def main(arama):
    url = "https://footystats.org/tr/" #Girmek istediğiniz sitenin adresi
    driver.get(url)

    search = driver.find_element(By.XPATH, '//*[@id="searchBar"]/input')
    search.send_keys(arama)
    sleep(0.5)
    clickable = driver.find_element(By.XPATH,'//*[@id="searchBarPreview"]/ul/li/a')
    takim_url = clickable.get_attribute("href")
    print(takim_url)
    driver.get(takim_url)

    sleep(0.1)

    ev_sahibi = driver.find_element(By.XPATH, '//*[@id="clubContent1"]/div[5]/div[3]/div[1]/div[1]/div/table/tbody/tr[2]')
    deplasman = driver.find_element(By.XPATH, '//*[@id="clubContent1"]/div[5]/div[3]/div[1]/div[1]/div/table/tbody/tr[3]')
    ev_sahibi = ev_sahibi.text.split()
    deplasman = deplasman.text.split()
    sleep(1)
    print(deplasman)
    ev_data = f" Ev\n Yenilen Gol:{ev_sahibi[2]}\n Atilan Gol:{ev_sahibi[3]}\n Ortalama:{ev_sahibi[4]}"
    deplasman_data = f" \nDeplasman\n Yenilen Gol:{deplasman[1]}\n Atilan Gol:{deplasman[2]}\n Ortalama:{deplasman[3]}"
    print(ev_data)
    
    return ev_data+" "+deplasman_data
#print(main("Uruguay Milli Takımı"))
def help(update, context):
    yardim_mesaji = """
/mac    
    """
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=yardim_mesaji)   
def mac(update, args):
    i = args.args[0] + " " + args.args[1] + " " + args.args[2]
    update.message.reply_text("requesting") 

    update.message.reply_text(main(i))    
TOKEN = '5661610725:AAFHMkoak1-AEIoWOJ63bYoBkNlPL3v_LYg'

updater = Updater(TOKEN, use_context = True)

# Get the dispatcher to register handlers
dp = updater.dispatcher
dp.add_handler(CommandHandler("help", help))
dp.add_handler(CommandHandler("start", help))
dp.add_handler(CommandHandler("mac", mac))
# log all errors
updater.start_polling()
