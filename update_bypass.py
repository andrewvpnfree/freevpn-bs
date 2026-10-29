import requests
import re

def fetch_configs():
    valid_configs = []
    
    # Используем шлюз-зеркало banyun, которое специально создано для обхода блокировок роботов
    url = "https://githubusercontent.com"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            # Вытаскиваем все строчки, содержащие vless://
            lines = response.text.splitlines()
            for line in lines:
                line = line.strip()
                if line.startswith("vless://"):
                    if line not in valid_configs:
                        valid_configs.append(line)
    except Exception as e:
        print(f"Ошибка шлюза: {e}")
            
    return valid_configs[:100]

def save_and_format(configs):
    # Если шлюз вернул пустоту, скрипт не запишет 0 байт, а оставит старые рабочие прокси
    if not configs:
        print("База не ответила, отмена перезаписи во избежание пустой подписки.")
        return
        
    with open("whitelist_subscription.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(configs))
    print(f"Успешно обновлено серверов: {len(configs)}")

if __name__ == "__main__":
    servers = fetch_configs()
    save_and_format(servers)
