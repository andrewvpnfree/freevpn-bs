import re
import os

def sort_local_configs():
    all_content = ""
    
    # Задаем список папок, куда робот скачает базы
    folders = ["repo1", "repo2", "repo3", "repo4", "repo5", "repo6"]
    
    # Пробегаемся по всем папкам и собираем файлы в одну огромную кучу
    for folder in folders:
        if os.path.exists(folder):
            for root, dirs, files in os.walk(folder):
                for file in files:
                    # Читаем только текстовые файлы и файлы конфигураций
                    if file.endswith(".txt") or file == "v2ray" or file == "sub":
                        try:
                            with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                                all_content += f.read() + "\n"
                        except Exception:
                            pass

    # Очищаем скрытые символы переноса строк Windows
    all_content = all_content.replace('\r', '')
    
    # Строго распределяем ключи по их протоколам без дублирования (лимиты увеличены!)
    vless = list(set(re.findall(r'(vless://[^\s]+)', all_content)))
    vmess = list(set(re.findall(r'(vmess://[^\s]+)', all_content)))
    trojan = list(set(re.findall(r'(trojan://[^\s]+)', all_content)))
    ss = list(set(re.findall(r'((?:ss|shadowsocks)://[^\s]+)', all_content)))
    
    # Жестко записываем уникальные протоколы в свои файлы
    with open("vless.txt", "w", encoding="utf-8") as f: f.write("\n".join(vless[:500]))
    with open("vmess.txt", "w", encoding="utf-8") as f: f.write("\n".join(vmess[:300]))
    with open("trojan.txt", "w", encoding="utf-8") as f: f.write("\n".join(trojan[:300]))
    with open("shadowsocks.txt", "w", encoding="utf-8") as f: f.write("\n".join(ss[:300]))
    
    # Общий мега-микс всего (до 1000 серверов в одном файле!)
    mix = vless[:400] + vmess[:200] + trojan[:200] + ss[:200]
    with open("whitelist_subscription.txt", "w", encoding="utf-8") as f: f.write("\n".join(mix))
    
    print(f"Сортировка завершена! Собрано VLESS: {len(vless)}, VMess: {len(vmess)}, Trojan: {len(trojan)}, SS: {len(ss)}")

if __name__ == "__main__":
    sort_local_configs()
