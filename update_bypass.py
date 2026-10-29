import requests
import base64

def fetch_and_sort():
    # Собираем данные из огромного авто-обновляемого агрегатора
    url = "https://githubusercontent.com"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    vless_list = []
    vmess_list = []
    trojan_list = []
    ss_list = []
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            content = response.text
            # Декодируем Base64, если база зашифрована
            try:
                content = base64.b64decode(content).decode('utf-8', errors='ignore')
            except Exception:
                pass
                
            lines = content.splitlines()
            for line in lines:
                line = line.strip()
                # Сортируем по спискам и убираем дубликаты
                if line.startswith("vless://") and line not in vless_list:
                    vless_list.append(line)
                elif line.startswith("vmess://") and line not in vmess_list:
                    vmess_list.append(line)
                elif line.startswith("trojan://") and line not in trojan_list:
                    trojan_list.append(line)
                elif (line.startswith("ss://") or line.startswith("shadowsocks://")) and line not in ss_list:
                    ss_list.append(line)
                    
    except Exception as e:
        print(f"Ошибка: {e}")

    # Записываем каждый протокол в свой файл (если пусто, запишется пустой файл)
    with open("vless.txt", "w", encoding="utf-8") as f: f.write("\n".join(vless_list[:150]))
    with open("vmess.txt", "w", encoding="utf-8") as f: f.write("\n".join(vmess_list[:150]))
    with open("trojan.txt", "w", encoding="utf-8") as f: f.write("\n".join(trojan_list[:150]))
    with open("shadowsocks.txt", "w", encoding="utf-8") as f: f.write("\n".join(ss_list[:150]))
    
    # Общий микс
    all_configs = vless_list[:100] + vmess_list[:50] + trojan_list[:50] + ss_list[:50]
    with open("whitelist_subscription.txt", "w", encoding="utf-8") as f: f.write("\n".join(all_configs))
    
    print("Сортировка успешно завершена!")

if __name__ == "__main__":
    fetch_and_sort()
