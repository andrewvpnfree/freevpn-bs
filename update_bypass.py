import requests
import re
import os

def fetch_and_save():
    # Проверенные и стабильные открытые базы со свежими ключами
    sources = [
        "https://githubusercontent.com",
        "https://githubusercontent.com",
        "https://githubusercontent.com",
        "https://githubusercontent.com"
    ]
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    all_text = ""
    
    for url in sources:
        try:
            res = requests.get(url, headers=headers, timeout=15)
            if res.status_code == 200:
                all_text += res.text + "\n"
        except Exception as e:
            print(f"Ошибка источника {url}: {e}")
            
    # Убираем Windows-переносы строк
    all_text = all_text.replace('\r', '')
    
    # Ищем и сортируем протоколы
    vless = list(set(re.findall(r'(vless://[^\s]+)', all_text)))
    vmess = list(set(re.findall(r'(vmess://[^\s]+)', all_text)))
    trojan = list(set(re.findall(r'(trojan://[^\s]+)', all_text)))
    ss = list(set(re.findall(r'((?:ss|shadowsocks)://[^\s]+)', all_text)))
    
    # Жестко записываем данные прямо в файлы репозитория
    with open("vless.txt", "w", encoding="utf-8") as f: f.write("\n".join(vless[:150]))
    with open("vmess.txt", "w", encoding="utf-8") as f: f.write("\n".join(vmess[:100]))
    with open("trojan.txt", "w", encoding="utf-8") as f: f.write("\n".join(trojan[:100]))
    with open("shadowsocks.txt", "w", encoding="utf-8") as f: f.write("\n".join(ss[:100]))
    
    # Общий микс
    mix = vless[:100] + vmess[:50] + trojan[:50] + ss[:50]
    with open("whitelist_subscription.txt", "w", encoding="utf-8") as f: f.write("\n".join(mix))
    
    print("Все файлы успешно заполнены скриптом!")

if __name__ == "__main__":
    fetch_and_save()
