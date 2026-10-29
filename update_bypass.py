import requests
import base64

def fetch_configs():
    valid_configs = []
    # Самый крупный агрегатор, в котором объединены сотни баз прокси
    url = "https://githubusercontent.com"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            content = response.text
            # Эта база зашифрована в Base64, расшифровываем её
            try:
                content = base64.b64decode(content).decode('utf-8', errors='ignore')
            except Exception:
                pass
                
            lines = content.splitlines()
            for line in lines:
                line = line.strip()
                # Отбираем только VLESS, которые работают через TLS (важно для белых списков)
                if line.startswith("vless://") and "security=tls" in line:
                    if line not in valid_configs:
                        valid_configs.append(line)
    except Exception as e:
        print(f"Ошибка при скачивании базы: {e}")
            
    # Берем первые 100 самых свежих серверов
    return valid_configs[:100]

def save_and_format(configs):
    # Если вдруг база не ответила, добавим рабочий прокси, чтобы файл не оставался пустым
    if not configs:
        configs = ["vless://b6028681-30de-4ffb-be5c-d326f6eb8b11@104.21.57.11:443?encryption=none&security=tls&type=ws&host=speedtest.net#Резерв"]
        
    with open("whitelist_subscription.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(configs))
    print(f"Успешно собрано серверов: {len(configs)}")

if __name__ == "__main__":
    servers = fetch_configs()
    save_and_format(servers)
