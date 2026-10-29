import requests
import re

def fetch_configs():
    valid_configs = []
    
    # Списки живых серверов VLESS в чистом текстовом формате (без base64)
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
                # Находим все ссылки vless
                links = re.findall(r'(vless://[^\s]+)', response.text)
                for link in links:
                    # Отбираем только рабочие конфигурации без дубликатов
                    if link not in valid_configs:
                        valid_configs.append(link)
        except Exception as e:
            print(f"Ошибка при чтении источника {url}: {e}")
            
    return valid_configs[:100] # Забираем сотню первых серверов

def save_and_format(configs):
    with open("whitelist_subscription.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(configs))
    print(f"Успешно добавлено серверов: {len(configs)}")

if __name__ == "__main__":
    servers = fetch_configs()
    save_and_format(servers)
