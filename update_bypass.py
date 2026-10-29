import re
import os

def sort_local_configs():
    # Проверяем, скачался ли внутренний файл базы
    file_path = "source_repo/vless_universal.txt"
    if not os.path.exists(file_path):
        print("Ошибка: Внутренняя база не найдена!")
        return
        
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    # Очищаем скрытые символы Windows
    content = content.replace('\r', '')
    
    # Ищем все ссылки протоколов
    vless = list(set(re.findall(r'(vless://[^\s]+)', content)))
    vmess = list(set(re.findall(r'(vmess://[^\s]+)', content)))
    trojan = list(set(re.findall(r'(trojan://[^\s]+)', content)))
    ss = list(set(re.findall(r'((?:ss|shadowsocks)://[^\s]+)', content)))
    
    # Записываем в файлы репозитория
    with open("vless.txt", "w", encoding="utf-8") as f: f.write("\n".join(vless[:200]))
    with open("vmess.txt", "w", encoding="utf-8") as f: f.write("\n".join(vmess[:100]))
    with open("trojan.txt", "w", encoding="utf-8") as f: f.write("\n".join(trojan[:100]))
    with open("shadowsocks.txt", "w", encoding="utf-8") as f: f.write("\n".join(ss[:100]))
    
    # Общий микс
    mix = vless[:100] + vmess[:50] + trojan[:50] + ss[:50]
    with open("whitelist_subscription.txt", "w", encoding="utf-8") as f: f.write("\n".join(mix))
    
    print(f"Сортировка завершена! Найдено VLESS: {len(vless)}")

if __name__ == "__main__":
    sort_local_configs()
