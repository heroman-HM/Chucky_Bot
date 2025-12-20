import requests
import random

def send(cc, last, username, time_taken):
    ii = cc[:6]

    random_amount1 = random.randint(1, 4)
    random_amount2 = random.randint(1, 99)

    try:
        response = requests.get(f'https://bins.antipublic.cc/bins/{ii}')
        data = response.json()

        if response.status_code == 200:
            bank = data.get("bank", "Unknown")
            emj = data.get("country_flag", "🏳️")
            do = data.get("country", "Unknown")
            dicr = data.get("brand", "Unknown")
            typ = data.get("type", "Unknown")
        else:
            print(f"API Error: {data.get('error', 'Unknown error')}")
            bank = emj = do = dicr = typ = 'Unknown'
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        bank = emj = do = dicr = typ = 'Unknown'

    msg1 = f"""
<b>CARD</b> ⌁ <code>{cc}</code>

<b>RESPONSE</b> ⌁ {last}

<b>BIN</b> ⌁ {ii} - {dicr.upper()} - {typ.upper()}
<b>BANK</b> ⌁ {bank.upper()}  
<b>COUNTRY</b> ⌁ {do.upper()} {emj}              

<b>Check by</b> ⌁ @{username}
<b>Bot By</b> ⌁ @Chuckyforu4
"""
    return msg1
