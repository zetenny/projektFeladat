from datetime import datetime
import requests

def logger(uzenet):
    log = f'{datetime.now()}>> {str(uzenet)}'
    print(log)

def downloader(url, fajl):  
    try:
        r = requests.get(url)
        tartalom = r.content.decode("utf-8")
    except requests.ConnectionError:
        logger("Rossz URL-t adtál meg!")
    except requests.Timeout:
        logger("Időtúllépés.")
    except:
        logger("Egyéb hiba.")

    with open(fajl, 'w') as f:
        f.write(tartalom)