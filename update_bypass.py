import requests

# Источники бесплатных конфигураций для обхода белых списков
SOURCES = [
    "https://githubusercontent.com",
    "https://githubusercontent.com",
    "https://githubusercontent.com"
]

def fetch_configs():
    valid_configs = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    for url in SOURCES:
        try:
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code == 200:
                lines = response.text.splitlines()
                for line in lines:
                    line = line.strip()
                    if line.startswith("vless://"):
                        if line not in valid_configs:
                            valid_configs.append(line)
        except Exception as e:
            print(f"Ошибка при скачивании из {url}: {e}")
            
    return valid_configs

def save_and_format(configs):
    with open("whitelist_subscription.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(configs))
    print(f"Успешно обновлено! Собрано серверов: {len(configs)}")

if __name__ == "__main__":
    servers = fetch_configs()
    save_and_format(servers)
