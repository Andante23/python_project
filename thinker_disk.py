import psutil

from tkinter import ttk
import tkinter as tk
from config import root



# gui 제목
root.title("디스크 사용량 모니터")


# 콤보 박스 바
partitions = psutil.disk_partitions()
combo = ttk.Combobox(root, width=10 , height=10 , values =[p.device for p in partitions] )
combo.pack(pady=10 , padx=10)
combo.current(1)


# 프로그레스 바
progress = ttk.Progressbar(root, length=400, maximum=400)
progress.pack(pady=10 , padx=10)



# 디스크 사용률, 총용량 , 사용중 , 남은 용량 label 생성

labels = {}
for text, name in [("디스크 사용률", "diUse_label"), 
                   ("디스크 총용량", "ditot_label"), 
                   ("디스크 사용중", "diUsed_label"), 
                   ("디스크 남은", "diFree_label")]:
    
    labels[name] = tk.Label(root, text=f"{text}: 0")
    labels[name].pack(pady=5)
    
    

# 디스크 사용률, 총용량 , 사용중 , 남은 용량 나타내는 함수 
# 인 disk_label 선언
    def display_disk_capicity(disk,labels):
      labels["diUse_label"].config(text=f"디스크 사용률: {disk.percent}%")
      labels["ditot_label"].config(text=f"디스크 총용량: {disk.total} ")
      labels["diUsed_label"].config(text=f"디스크 사용중: {disk.used} ")
      labels["diFree_label"].config(text=f"디스크 남은: {disk.free} ")




# 디스크와 관련 정보를 보여주는 대시보드 함수 선언 
def disk_dashboard():
  
    #1. 콤보박스에서 디스크 선택하면  디스크 정보를 가져옴
    select_combo = combo.get() 
    disk = psutil.disk_usage(select_combo)
    
    # 프로그레스로 나타냄
    progress["value"] = disk.percent
    
    # 디스크 용량 정보 나타내는 함수 작동       
    display_disk_capicity(disk,labels)
    
    root.after(1000, disk_dashboard)  # 정보를 1초마다 갱신


disk_dashboard()
root.mainloop()


