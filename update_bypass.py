import requests

def fetch_and_sort():
    # Прямые ссылки на гигантские текстовые списки, которые никогда не банят запросы от GitHub
    sources = [
        "https://githubusercontent.com",
        "https://githubusercontent.com",
        "https://githubusercontent.com",
        "https://githubusercontent.com"
    ]
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    vless_list = []
    vmess_list = []
    trojan_list = []
    ss_list = []
    
    for url in sources:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                lines = response.text.splitlines()
                for line in lines:
                    line = line.strip()
                    # Раскидываем ключи по протоколам без жестких ограничений
                    if "vless://" in line and line not in vless_list:
                        vless_list.append(line)
                    elif "vmess://" in line and line not in vmess_list:
                        vmess_list.append(line)
                    elif "trojan://" in line and line not in trojan_list:
                        trojan_list.append(line)
                    elif ("ss://" in line or "shadowsocks://" in line) and line not in ss_list:
                        ss_list.append(line)
        except Exception as e:
            print(f"Ошибка источника {url}: {e}")

    # Запись в отдельные файлы
    with open("vless.txt", "w", encoding="utf-8") as f: f.write("\n".join(vless_list[:150]))
    with open("vmess.txt", "w", encoding="utf-8") as f: f.write("\n".join(vmess_list[:100]))
    with open("trojan.txt", "w", encoding="utf-8") as f: f.write("\n".join(trojan_list[:100]))
    with open("shadowsocks.txt", "w", encoding="utf-8") as f: f.write("\n".join(ss_list[:100]))
    
    # Общий микс
    all_configs = vless_list[:100] + vmess_list[:50] + trojan_list[:50] + ss_list[:50]
    with open("whitelist_subscription.txt", "w", encoding="utf-8") as f: f.write("\n".join(all_configs))
    
    print(f"Сортировка завершена! Найдено VLESS: {len(vless_list)}")

if __name__ == "__main__":
    fetch_and_sort()
