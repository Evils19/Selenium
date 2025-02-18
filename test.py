# from seleniumbase import SB
# import pandas as pd
# import time
#
#
# def citeste_idno(nume_fisier, foaie="Sheet1", coloana="IDNO"):
#     try:
#         data = pd.read_excel(nume_fisier, sheet_name=foaie)
#         if coloana not in data.columns:
#             raise ValueError(f"Coloana '{coloana}' nu a fost găsită în fișier.")
#         return data[coloana].dropna().astype(str).tolist()
#     except Exception as e:
#         print(f"Eroare la citirea fișierului: {e}")
#         return []
#
#
# def HackIopta():
#     listCompany = citeste_idno(r"D:\Python\Selenium\IDNO.xlsx")
#
#     for i in range(len(listCompany)):
#         url = f"https://b2bhint.com/ru/company/md/asociatia-liceului-teoretic-vasile-alecsandri-ba--{listCompany[i]}"
#
#         with SB(uc=True, test=True, locale_code="en") as sb:
#             try:
#                 sb.activate_cdp_mode(url)
#                 sb.uc_gui_click_captcha()
#                 sb.sleep(2)
#                 sb.open(url)
#                 sb.sleep(5)
#
#                 script = """
#                 var element = document.evaluate(
#                     "//dt[text()='Код административно-территориальной единицы']/following-sibling::dd",
#                     document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null
#                 ).singleNodeValue;
#                 if (element) { element.textContent.trim(); } else { '' }
#                 """
#                 value = sb.execute_script(script)
#
#                 print(f"{listCompany[i]}: {value}")
#             except Exception as e:
#                 print(f"Eroare la procesarea IDNO {listCompany[i]}: {e}")
#
#
# HackIopta()






