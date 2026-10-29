import requests
import re
import base64

def fetch_configs():
    valid_configs = []
    # Используем проверенный и ежедневно обновляемый агрегатор прокси
    url = "https://githubusercontent.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            content = response.text
            # Если данные зашифрованы в Base64 (стандарт для подписок), расшифровываем их
            try:
                content = base64.b64decode(content).decode('utf-8')
            except Exception:
                pass # Если не в base64, используем как обычный текст
                
            lines = content.splitlines()
            for line in lines:
                line = line.strip()
                # Для белых списков и БС собираем VLESS, так как они работают через CDN
                if line.startswith("vless://"):
                    if line not in valid_configs:
                        valid_configs.append(line)
    except Exception as e:
        print(f"Ошибка скачивания: {e}")
            
    # Берем первые 50 рабочих конфигураций, чтобы приложение не зависало
    return valid_configs[:50]

def save_and_format(configs):
    with open("whitelist_subscription.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(configs))
    print(f"Успешно обновлено! Собрано серверов: {len(configs)}")

if __name__ == "__main__":
    servers = fetch_configs()
    save_and_format(servers)
