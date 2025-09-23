import psutil
import tkinter as tk
from tkinter import ttk


# 디스크 상태를 보여주는 함수
def update_usage():
    disk = psutil.disk_usage('c:')
    print(disk)
    progress["value"] = disk.percent   
    diUse_label.config(text=f"디스크 사용률: {disk.percent}%")
    ditot_label.config(text=f"디스크 총용량: {int(disk.total/(1024**3))}GB ")
    diUsed_label.config(text=f"디스크 사용중: {int(disk.used/(1024**3))}GB ")
    diFree_label.config(text=f"디스크 남은: {int(disk.free/(1024**3))}GB ")
    root.after(1000, update_usage)  # 1초마다 갱신






# 파이썬에서 기본적으로 지원하는 gui 모듈
root = tk.Tk()
root.title("디스크 사용량 모니터")
progress = ttk.Progressbar(root, length=400, maximum=400)
progress.pack(pady=10 , padx=10)

ditot_label = tk.Label(root, text="디스크 총용량:0")
ditot_label.pack(pady=10)
diUsed_label = tk.Label(root, text="디스크 사용중:0")
diUsed_label.pack(pady=10)
diFree_label = tk.Label(root, text="디스크 여유량:0")
diFree_label.pack(pady=10)
diUse_label = tk.Label(root, text="디스크 사용률:0%")
diUse_label.pack(pady=10)

btn = ttk.Button(root, text="최적화", command=opti_usage)
btn.pack(pady=5)

update_usage()
root.mainloop()


