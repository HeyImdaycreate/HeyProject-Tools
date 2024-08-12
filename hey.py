from colorama import init, Fore
from faker import Faker
from pprint import pprint
import time
import pprint
import progress.bar as pb
import random
import string
import socket
import phonenumbers
from phonenumbers import timezone, carrier, geocoder
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import sys
import subprocess

init()
deepfake = Faker("RU")


def Opening():
    txte = Fore.LIGHTMAGENTA_EX + '''.
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⡀
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣶⣿⣿⣿⣿⣦⡀
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣴⣿⣿⣿⣿⣿⣿⣿⣷
⠄⠄⠄⠄⠄⠄⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤⣤⣤⣄⡀
⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦
⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⠄⠄⠄⢠⠔⠒⠴⡿⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠄⠄⠄⠸⡀⠄⡤⠤⡀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠄⠄⠄⣰⠁⠄⠳⠔⠁⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠄⠄⣴⣿⣦⣤⣶⣷⣦⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆
⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
⢀⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠛⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣿⠋⣡⣤⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠙⠿⣿⣿⣿⣿⣿⣿⡇
⠄⣿⣿⣿⣿⠁⠄⣿⣿⡇⠄⠄⠄⠄⣀⠄⠄⠄⠄⠄⣾⣿⡆⠘⣿⣿⣿⣿⣿⠃
⠄⠘⣿⣿⣿⠄⠄⠉⠋⠄⠄⠄⠄⠸⣍⡵⠄⠄⠄⠄⠻⡿⠇⠄⢸⣿⣿⣿⠏
⠄⠄⠈⠻⣿⣦⡀⠄⠄⠄⠄⠄⠄⠄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⣼⣿⡿⠋
⠄⠄⠄⠄⠄⠉⢻⣶⡶⠴⢲⣄⣀⣀⣁⠄⠄⠄⠄⣀⣀⣀⣤⠾⠟⠋
⠄⠄⠄⠄⠄⢶⣿⣿⠄⠄⠄⢹⣿⠋⠉⠙⣿⣿⣿⣿⣿⣿⣿⡆
⠄⠄⠄⠄⠄⠄⣼⠋⠄⠄⣴⣿⠏⠄⠄⠄⠹⣿⣿⣿⠿⢛⠉⢳⣀
⠄⠄⠄⠄⠄⠄⢻⣀⣀⡴⠃⠄⠄⠄⠄⠄⠄⠉⠉⠄⠄⢸⡄⠄⠈⢳
⠄⠄⠄⠄⠄⠄⠄⠈⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⡧⣄⣠⠞
⠄⠄⠄⠄⠄⠄⠄⠄⢹⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣾
⠄⠄⠄⠄⠄⠄⠄⠄⢸⠃⠄⢀⣤⣀⠄⣴⡄⣠⣤⡄⠄⠸⡇
⠄⠄⠄⠄⠄⠄⠄⠄⣼⠄⠄⠄⠄⠄⠈⣷⠋⠄⠄⠄⠄⠄⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠙⢦⣀⣀⣀⣀⣠⠟⢤⣀⣀⣀⣀⡴⠃
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠉⠉⠄⠄⠄⠈⠉⠉


HEYPRODUCTION_0

'''
    for p in txte:
        time.sleep(0.001)
        print(p, end='', flush=True)
        
    txt = Fore.WHITE + 'hp'
    for i in txt:
        time.sleep(0.04)
        print(i, end='', flush=True)
    

def Choosing():
    print(Fore.LIGHTMAGENTA_EX + '''
Выберите функцию HeyProduction
1. Не настоящий профиль
2. OSINT
3. Узнать местоположение по ip
4. HLR-запрос на номер 
5. Генератор сильных паролей
6. Useragents generator
7. Найти открытый порт
8. WEB-CRAWLER
9. Exit
''')
    Choose = input(Fore.WHITE + 'Номер функции: ')
    if Choose == '1':
        txt = Fore.WHITE + '[RANDOM DEEPFAKE] Генерация ненастоящего профиля...'
        for i in txt:
            time.sleep(0.04)
            print(i, end='', flush=True)
        bar = pb.ChargingBar('...', max=100)
        for o in range(100):
            bar.next()
            time.sleep(0.01)

        bar.finish()
        print(deepfake.name(), deepfake.address())
        quest = input('Расширенный дипфейк? Y/N: ')
        if quest == 'Y':
            dickfake()
            time.sleep(10)
            Choosing()
    if Choose == '2':
        txt = Fore.WHITE + '[OSINT] Введите никнейм для поиска'
        for p in txt:
            time.sleep(0.04)
            print(p, end='', flush=True)
        osintname()
        time.sleep(10)
        Choosing()
    if Choose == '8':
        starting_url = input('Ссылка: ')
        web_crawler(starting_url)
        time.sleep(10)
        Choosing()
    if Choose == '7':
        turiip = input('IP-адрес: ')
        checkports(turiip)
        time.sleep(10)
        Choosing()
    if Choose == '4':
        hlr_request()
        time.sleep(10)
        Choosing()
    if Choose == '5':
        genpass()
        time.sleep(10)
        Choosing()
    if Choose == '6':
        generate_user_agents(100)
        print(Fore.WHITE + '100 рандомных юзерагентов было успешно сгенерированно')
        time.sleep(10)
        Choosing()
    if Choose == '3':
        aipe = input('IP: ')
        coords(aipe)


def genpass():
            variable = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM&/₽)[.₽/@@_<>$|-"
            length = int(input("Введите длину пароля: "))
            password = ""
            for i in range(length):
                password += random.choice(variable)
            print(password)
def checkports(ip):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.09)
            try:
                connect = sock.connect((ip, i))
                print("Найден открытый порт:", i)
                sock.close()
            except:
                pass
def web_crawler(url, depth=2):
    visited = set()
    queue = [(url, 0)]

    while queue:
        current_url, current_depth = queue.pop(0)
        
        if current_url in visited or current_depth > depth:
            continue
        
        visited.add(current_url)
        print("HEY3 CRAWLING:", current_url)
        
        try:
            response = requests.get(current_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for link in soup.find_all('a', href=True):
                absolute_url = urljoin(current_url, link['href'])
                queue.append((absolute_url, current_depth + 1))
        except Exception as e:
            print("Ошибка:", e)

def coords(ip):
            try:
                for i in ip:
                    if i in "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщьыъэюя":
                        import socket
                        ip = socket.gethostbyname(ip)
                        break
                import geocoder
                coord = geocoder.ipinfo(ip)
                print("Координаты IP-адреса:", coord.latlng)
                print("Примерное местоположение IP:", coord.city)
            except:
                pass
            
def dickfake():
    target_info = {
        "Имя": deepfake.name(),
        "Дата рождения": deepfake.date_of_birth(),
        "Email": deepfake.email(),
        "Телефон": deepfake.phone_number(),
        "Адрес": deepfake.address()
    }
    pprint.pprint(target_info)

def hlr_request():
    phone_number = input("Введите номер телефона в международном формате: ")
    parsed_number = phonenumbers.parse(phone_number, None)
    
    if phonenumbers.is_valid_number(parsed_number):
        print("Номер действителен")
        print("Страна:", geocoder.description_for_number(parsed_number, "en"))
        print("Оператор:", carrier.name_for_number(parsed_number, "en"))
        print("Часовой пояс:", timezone.time_zones_for_number(parsed_number))
    else:
        print("Номер недействителен")
def search_social_media_profiles(name):
    social_media_urls = {
        "Facebook": f"https://www.facebook.com/public/{name.replace(' ', '-')}",
        "Instagram": f"https://www.instagram.com/{name.replace(' ', '_')}/",
        "Twitter": f"https://twitter.com/{name.replace(' ', '')}"
    }

    results = {}

    for platform, url in social_media_urls.items():
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            if platform == "Facebook":
                if "No results found for" not in soup.text:
                    results[platform] = url
            elif platform == "Instagram":
                if "Page Not Found" not in soup.text:
                    results[platform] = url
            elif platform == "Twitter":
                if soup.find("div", {"data-testid": "primaryColumn"}) is not None:
                    results[platform] = url

    return results

def osintname():
    name = input("Ник/псевдоним для поиска: ")
    profiles = search_social_media_profiles(name)
    
    if profiles:
        print("Социальные сети:")
        for platform, url in profiles.items():
            print(f"{platform}: {url}")
    else:
        print("Не найденно соц сетей по данному нику.")

def generate_user_agents(num_agents=100):
    versions = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{0}; rv:{1}.0) Gecko/20{2:02d}{3:02d} Firefox/{1}.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
    ]
    
    for _ in range(num_agents):
        version = random.randint(60, 90)
        year = random.randint(10, 21)
        month = random.randint(1, 12)
        
        user_agent = random.choice(versions).format(version, year, year, month)
        print(user_agent)
        
Opening()
Choosing()
          

