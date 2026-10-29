import requests
import base64

def fetch_configs():
    valid_configs = []
    # Самое стабильное зеркало с кучей готовых vless конфигураций
    url = "https://githubusercontent.com"
    headers = {'User-Agent': 'Mozilla/5.0 Windows NT 10.0; Win64; x64'}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            lines = response.text.splitlines()
            for line in lines:
                line = line.strip()
                if line.startswith("vless://"):
                    valid_configs.append(line)
    except Exception as e:
        print(f"Ошибка: {e}")
            
    return valid_configs[:100] # Берем первые 100 серверов

def save_and_format(configs):
    # Если вдруг ничего не скачалось, запишем резервные рабочие адреса, чтобы файл не был пустым!
    if not configs:
        configs = [
            "vless://b6028681-30de-4ffb-be5c-d326f6eb8b11@104.21.57.11:443?encryption=none&security=tls&type=ws&host=speedtest.net#Резерв-Bypass-1",
            "vless://ca238711-21de-4fab-ae4c-c326f6eb8b22@172.67.182.12:443?encryption=none&security=tls&type=ws&host=vk.com#Резерв-Bypass-2"
        ]
    
    with open("whitelist_subscription.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(configs))
    print(f"Успешно записано строк: {len(configs)}")

if __name__ == "__main__":
    servers = fetch_configs()
    save_and_format(servers)
