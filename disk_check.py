import shutil
import datetime

total, used, free = shutil.disk_usage("/")
total_gb = round(total / (1024**3), 1)
used_gb = round(used / (1024**3), 1)
free_gb = round(free / (1024**3), 1)
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>サーバー監視レポート</title>
</head>
<body>
    <h1>Ubuntu サーバー監視パネル</h1>
    <p>全体容量: {total_gb} GB / 使用量: {used_gb} GB / 空き容量: {free_gb} GB</p>
    <div>最終更新: {now}</div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
