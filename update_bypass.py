import urllib.request
import re

def fetch_configs():
    # Проверенные временем текстовые базы
    sources = [
        "https://githubusercontent.com",
        "https://githubusercontent.com",
        "https://githubusercontent.com",
        "https://githubusercontent.com"
    ]
    
    # Полная маскировка под домашний браузер Chrome на Windows 11
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5'
    }
    
    valid_configs = []
    
    for url in sources:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as response:
                html = response.read().decode('utf-8', errors='ignore')
                # Ищем любые упоминания протоколов обхода
                links = re.findall(r'((?:vless|vmess|trojan|ss|shadowsocks)://[^\s]+)', html)
                for link in links:
                    if link not in valid_configs:
                        valid_configs.append(link)
        except Exception as e:
            print(f"Пропущен источник {url} из-за защиты: {e}")
            
    return valid_configs

def save_by_protocols(configs):
    # ЗАЩИТА: Если базы выдали пустоту из-за блокировок, МЫ НЕ ЗАТИРАЕМ файлы нулями!
    if len(configs) < 5:
        print("Внимание! Базы заблокировали запрос. Отмена перезаписи во избежание 0 байт.")
        return False
        
    vless = [c for c in configs if c.startswith("vless://")]
    vmess = [c for c in configs if c.startswith("vmess://")]
    trojan = [c for c in configs if c.startswith("trojan://")]
    ss = [c for c in configs if c.startswith("ss://") or c.startswith("shadowsocks://")]
    
    with open("vless.txt", "w", encoding="utf-8") as f: f.write("\n".join(vless[:200]))
    with open("vmess.txt", "w", encoding="utf-8") as f: f.write("\n".join(vmess[:100]))
    with open("trojan.txt", "w", encoding="utf-8") as f: f.write("\n".join(trojan[:100]))
    with open("shadowsocks.txt", "w", encoding="utf-8") as f: f.write("\n".join(ss[:100]))
    with open("whitelist_subscription.txt", "w", encoding="utf-8") as f: f.write("\n".join(configs[:300]))
    
    print(f"Успешно сохранено уникальных ключей: {len(configs)}")
    return True

if __name__ == "__main__":
    all_keys = fetch_configs()
    save_by_protocols(all_keys)
