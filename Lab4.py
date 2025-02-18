from seleniumbase import SB
import pandas as pd
import time
import os


def citeste_idno(nume_fisier, foaie="Sheet1", coloana="IDNO"):
    try:
        data = pd.read_excel(nume_fisier, sheet_name=foaie)
        if coloana not in data.columns:
            raise ValueError(f"Coloana '{coloana}' nu a fost găsită în fișier.")
        return data[coloana].dropna().astype(str).tolist()
    except Exception as e:
        print(f"Eroare la citirea fișierului: {e}")
        return []


def salveaza_rezultat(rezultat, output_file):
    """Salvează sau actualizează rezultatul în fișierul Excel."""
    try:
        if os.path.exists(output_file):
            # Citește datele existente
            df_existent = pd.read_excel(output_file)
            # Adaugă noul rezultat
            df_nou = pd.concat([df_existent, pd.DataFrame([rezultat])], ignore_index=True)
        else:
            # Creează un nou DataFrame cu primul rezultat
            df_nou = pd.DataFrame([rezultat])

        # Salvează rezultatele actualizate
        df_nou.to_excel(output_file, index=False)
        print(f"Rezultat salvat cu succes pentru IDNO {rezultat['IDNO']}")
    except Exception as e:
        print(f"Eroare la salvarea rezultatului: {e}")


def hack_b2bhin():
    listCompany = citeste_idno(r"D:\Python\Selenium\IDNO.xlsx")
    output_file = "D:\\Python\\Selenium\\rezultate_scraping.xlsx"

    # Începem de la poziția 669
    start_position = 1705

    for i in range(start_position, len(listCompany)):
        url = f"https://b2bhint.com/ru/company/md/asociatia-liceului-teoretic-vasile-alecsandri-ba--{listCompany[i]}"

        print(f"Procesăm poziția {i} din {len(listCompany)}")  # Adăugat pentru a urmări progresul

        with SB(uc=True, test=True, locale_code="en") as sb:
            try:
                sb.activate_cdp_mode(url)
                sb.uc_gui_click_captcha()
                sb.sleep(2)
                sb.open(url)
                sb.sleep(5)

                script = """
                var element = document.evaluate(
                    "//dt[text()='Код административно-территориальной единицы']/following-sibling::dd",
                    document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null
                ).singleNodeValue;
                if (element) { element.textContent.trim(); } else { '' }
                """
                value = sb.execute_script(script)

                rezultat_curent = {
                    'IDNO': listCompany[i],
                    'Administrative territorial unit code': value
                }

                salveaza_rezultat(rezultat_curent, output_file)
                print(f"Procesat cu succes: {listCompany[i]}: {value}")

            except Exception as e:
                rezultat_curent = {
                    'IDNO': listCompany[i],
                    'Administrative territorial unit code': f"Eroare: {str(e)}"
                }
                salveaza_rezultat(rezultat_curent, output_file)
                print(f"Eroare la procesarea IDNO {listCompany[i]}: {e}")

            time.sleep(2)

    print(f"\nProcesarea s-a încheiat. Toate rezultatele au fost salvate în {output_file}")


if __name__ == "__main__":
    hack_b2bhin()