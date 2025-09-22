import psutil
import tkinter as tk
from tkinter import ttk

# 디스크 상태를 보여주는 함수
def update_usage():
    disk = psutil.disk_usage('/')
    progress["value"] = disk.percent
    label.config(text=f"디스크 사용률: {disk.percent}%")
    root.after(1000, update_usage)  # 1초마다 갱신


# 파이썬에서 기본적으로 지원하는 gui 모듈
root = tk.Tk()
root.title("디스크 사용량 모니터")

progress = ttk.Progressbar(root, length=300, maximum=100)
progress.pack(pady=10)

label = tk.Label(root, text="디스크 사용률: 0%")
label.pack(pady=5)

update_usage()
root.mainloop()


