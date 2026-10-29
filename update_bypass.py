import urllib.request
import re
import os

def fetch_and_sort():
    all_content = ""
    
    # 1. Сначала читаем локальную базу VLESS, которую робот скачал без интернета
    local_file = "source_repo/vless_universal.txt"
    if os.path.exists(local_file):
        try:
            with open(local_file, "r", encoding="utf-8", errors="ignore") as f:
                all_content += f.read() + "\n"
        except Exception as e:
            print(f"Ошибка чтения локального файла: {e}")

    # 2. Список крупнейших интернет-баз (если какая-то забанит или удалится - скрипт НЕ упадет)
    web_sources = [
        "https://githubusercontent.com",
        "https://githubusercontent.com",
        "https://githubusercontent.com",
        "https://githubusercontent.com",
        "https://githubusercontent.com"
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    for url in web_sources:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                html = response.read().decode('utf-8', errors='ignore')
                all_content += html + "\n"
                print(f"Успешно скачан источник: {url}")
        except Exception as e:
            # Если сайт выдал 404 или заблокировал - просто пишем в лог и идем дальше!
            print(f"Источник {url} недоступен (пропущен): {e}")

    # Очищаем скрытые символы Windows
    all_content = all_content.replace('\r', '')
    
    # Строго распределяем ключи по их протоколам без дублирования
    vless = list(set(re.findall(r'(vless://[^\s]+)', all_content)))
    vmess = list(set(re.findall(r'(vmess://[^\s]+)', all_content)))
    trojan = list(set(re.findall(r'(trojan://[^\s]+)', all_content)))
    ss = list(set(re.findall(r'((?:ss|shadowsocks)://[^\s]+)', all_content)))
    
    # Записываем уникальные протоколы в свои файлы
    with open("vless.txt", "w", encoding="utf-8") as f: f.write("\n".join(vless[:500]))
    with open("vmess.txt", "w", encoding="utf-8") as f: f.write("\n".join(vmess[:300]))
    with open("trojan.txt", "w", encoding="utf-8") as f: f.write("\n".join(trojan[:300]))
    with open("shadowsocks.txt", "w", encoding="utf-8") as f: f.write("\n".join(ss[:300]))
    
    # Общий мега-микс всего
    mix = vless[:300] + vmess[:150] + trojan[:150] + ss[:150]
    with open("whitelist_subscription.txt", "w", encoding="utf-8") as f: f.write("\n".join(mix))
    
    print(f"Сортировка завершена! Всего VLESS: {len(vless)}, VMess: {len(vmess)}, Trojan: {len(trojan)}, SS: {len(ss)}")

if __name__ == "__main__":
    fetch_and_sort()
