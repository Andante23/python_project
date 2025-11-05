import psutil

from tkinter import ttk
import tkinter as tk
from config import root



# gui 제목
root.title("모니터링 데모")


# 콤보 박스 바
partitions = psutil.disk_partitions()


print(partitions)

# 드라이브 접근 에러 해결 

available_drives = []

for part in psutil.disk_partitions(all=True):
    try:
        psutil.disk_usage(part.mountpoint)
       
        
    except (PermissionError,OSError):
        print(f"  ⚠️ 접근 권한 없음: {part.device}")
        continue
        
    except OSError as e:
        if "장치가 준비되지 않았습니다" in str(e):
            print("  ⚠️ 장치가 준비되지 않음 (CD-ROM 등)")
        else:
            print(f"  ⚠️ 기타 OS 오류: {e}")
        continue
    
    else:
        available_drives.append(part.device)
        
        
        



# 콤보박스
combo = ttk.Combobox(root, width=10, height=10)
combo.pack(pady=10, padx=10)

# 조회 가능한 드라이브 개수가 1라면
if len(available_drives) > 0:  
    
    combo['values'] = available_drives
    combo.current(0)

else:  # 그게 아니라면
    
    # combo 리스트에 첫번째 인덱스 값으로  "이용 가능한 드라이브 없음" 추가
    combo['values'] = ["이용 가능한 드라이브 없음"]
    
    combo.current(0)
    
    # 콤보 비활성화 

    combo.config(state="disabled")
     
    
# 프로그레스 바
progress = ttk.Progressbar(root, length=400, maximum=400)
progress.pack(pady=10 , padx=10)

labels = {}
for text, name in [("디스크 사용률", "diUse_label"), 
                   ("디스크 총용량", "ditot_label"), 
                   ("디스크 사용중", "diUsed_label"), 
                   ("디스크 남은", "diFree_label")
                   ]:
    
    labels[name] = tk.Label(root, text=f"{text}: 0")
    labels[name].pack(pady=5)

# 디스크 사용률, 총용량 , 사용중 , 남은 용량 label 생성

def display_disk_capacity(any,labels):
    labels["diUse_label"].config(text=f"디스크 사용률: {any.percent}%")
    labels["ditot_label"].config(text=f"디스크 총용량: {any.total} ")
    labels["diUsed_label"].config(text=f"디스크 사용중: {any.used} ")
    labels["diFree_label"].config(text=f"디스크 남은: {any.free} ")
    

    
    

# 디스크 사용률, 총용량 , 사용중 , 남은 용량 나타내는 함수 
# 인 disk_label 선언





# 디스크와 관련 정보를 보여주는 대시보드 함수 선언 
def dashboard():
    
 if len(available_drives) < 0 :
       select_combo = combo.get()
       try:
           disk = psutil.disk_usage(select_combo)
           progress["value"] = disk.percent  # 퍼센트 반영
           display_disk_capacity(disk, labels)
       except Exception as e:
            print(f"⚠️ 디스크 접근 오류: {e}")
       finally:
            root.after(1000, dashboard)  # 1초마다 갱신
    
 else:
        for label in labels.values():
         label.config(state="disable")
    
      
  
   
   
   
   
dashboard()
root.mainloop()



