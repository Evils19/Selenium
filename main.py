# from click import option
# from  selenium import  webdriver
# import  time
# from fake_useragent import UserAgent
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import pickle
# from selenium.webdriver.support import expected_conditions as EC
#
#
# from selenium.webdriver.support.wait import WebDriverWait
#
# url=["https://www.instagram.com/",
#      "https://www.whatismybrowser.com/detect/what-is-my-user-agent/",
#      "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html",
#      "https://999.md/ro/list/real-estate/apartments-and-rooms?hide_duplicates=no&applied=1&ef=33,30,2307,2203&o_33_1=776&eo=12900,12912,12885,13859"
#      ]
#
# useragent = UserAgent()
# # options
# options = webdriver.ChromeOptions()
# options.add_argument(f"user-agent={useragent.Chrome}")
# options.add_argument("--disable-blink-features=AutomationControlled")
#
# driver = webdriver.Chrome(options=options)
# try:
#
#
#
#     driver.get(url[3])
#     driver.execute_script("""
#         document.querySelectorAll('.slick-list').forEach(element => element.remove());
#     """)
#     item=driver.find_elements(By.CLASS_NAME,"ads-list-photo-item-thumb")
#     time.sleep(5)
#     # for i in range(0,len(item)):
#     #     item[i].click()
#     #     h1=driver.find_element(By.TAG_NAME,"h1")
#     #     data = {}
#     #
#     #     key = driver.find_element(By.CLASS_NAME, "adPage__content__features__key").text.strip()
#     #     value = driver.find_element(By.CLASS_NAME, "adPage__content__features__value").text.strip()
#     #     data[key] = value
#     #     driver.save_screenshot("test.png")
#     #     Autor=data.get("Autorul anunțului", "N/A")
#     #     LocParcare = data.get("Loc de parcare", "N/A")
#     #     Etaj = data.get("Etaj", "N/A")
#     #     print(f"Autorul anunțului: {Autor}")
#     #     print(f"Loc de parcare: {LocParcare}")
#     #     print(f"Etaj: {Etaj}")
#     #
#     #     time.sleep(5)
#     #     driver.back()
#     #
#     #     # Așteptăm ca lista de anunțuri să se încarce din nou
#     #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ads-list-photo-item-thumb")))
#     #
#     #     # Reîncărcăm lista de anunțuri
#     #     item = driver.find_elements(By.CLASS_NAME, "ads-list-photo-item-thumb")
#     #     time.sleep(1)
#     #
#
#
#
#     # item=driver.find_element(By.XPATH, "//a[@class='item']")
#
#     # email_input = driver.find_element(By.NAME, "username")
#     # email_input.clear()
#     # email_input.send_keys("posel tu nahui")
#
# except Exception as e:
#     print(f"A aparut o exceptie: {e}")
# finally:
#     driver.close()
#     driver.quit()


from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en") as sb:
    url = "https://demoqa.com/register"
    sb.activate_cdp_mode(url)
    sb.uc_gui_click_captcha()
    sb.sleep(10)