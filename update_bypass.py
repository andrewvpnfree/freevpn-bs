import requests
import re

def fetch_configs():
    valid_configs = []
    
    # Крупнейшие открытые базы со свежими VLESS серверами
    sources = [
        "https://githubusercontent.com",
        "https://githubusercontent.com",
        "https://githubusercontent.com",
        "https://githubusercontent.com"
    ]
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    for url in sources:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                # Ищем все строки, начинающиеся с vless://
                found = re.findall(r'(vless://[^\s]+)', response.text)
                for link in found:
                    # Убираем дубликаты и лишний мусор
                    if link not in valid_configs and "security=tls" in link:
                        valid_configs.append(link)
        except Exception as e:
            print(f"Пропущена база {url}: {e}")
            
    # Ограничим до 150 самых свежих серверов, чтобы приложение на телефоне не лагало
    return valid_configs[:150]

def save_and_format(configs):
    with open("whitelist_subscription.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(configs))
    print(f"Успешно собрано серверов: {len(configs)}")

if __name__ == "__main__":
    servers = fetch_configs()
    save_and_format(servers)
