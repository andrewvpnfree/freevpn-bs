import re
import os

def fetch_igareck_configs():
    all_content = ""
    vless_list = []
    vmess_list = []
    trojan_list = []
    ss_list = []
    
    # 1. Читаем файлы из скачанного репозитория igareck
    igareck_path = "igareck_repo"
    if os.path.exists(igareck_path):
        for root, dirs, files in os.walk(igareck_path):
            for file in files:
                # Нас интересуют только текстовые файлы конфигураций
                if file.endswith(".txt"):
                    try:
                        with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                            all_content += f.read() + "\n"
                    except Exception:
                        pass

    # 2. Читаем файлы из нашей старой базы zieng2 (для максимального количества VLESS)
    zieng_file = "zieng_repo/vless_universal.txt"
    if os.path.exists(zieng_file):
        try:
            with open(zieng_file, "r", encoding="utf-8", errors="ignore") as f:
                all_content += f.read() + "\n"
        except Exception:
            pass

    # Очищаем от Windows переносов строк
    all_content = all_content.replace('\r', '')
    
    # Строго раскидываем ключи по протоколам без дубликатов
    vless_list = list(set(re.findall(r'(vless://[^\s]+)', all_content)))
    vmess_list = list(set(re.findall(r'(vmess://[^\s]+)', all_content)))
    trojan_list = list(set(re.findall(r'(trojan://[^\s]+)', all_content)))
    ss_list = list(set(re.findall(r'((?:ss|shadowsocks)://[^\s]+)', all_content)))
    
    # Сохраняем строго разделенные файлы подписок в ваш репозиторий
    with open("vless.txt", "w", encoding="utf-8") as f: f.write("\n".join(vless_list[:300]))
    with open("vmess.txt", "w", encoding="utf-8") as f: f.write("\n".join(vmess_list[:150]))
    with open("trojan.txt", "w", encoding="utf-8") as f: f.write("\n".join(trojan_list[:150]))
    with open("shadowsocks.txt", "w", encoding="utf-8") as f: f.write("\n".join(ss_list[:150]))
    
    # Создаем общий огромный микс всего
    mix = vless_list[:200] + vmess_list[:50] + trojan_list[:50] + ss_list[:50]
    with open("whitelist_subscription.txt", "w", encoding="utf-8") as f: f.write("\n".join(mix))
    
    print(f"Сортировка завершена! Найдено уникальных: VLESS: {len(vless_list)}, VMess: {len(vmess_list)}, Trojan: {len(trojan_list)}, SS: {len(ss_list)}")

if __name__ == "__main__":
    fetch_igareck_configs()
