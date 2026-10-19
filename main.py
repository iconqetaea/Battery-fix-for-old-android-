import os
import subprocess
import time

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except Exception as e:
        pass

def optimize_battery():
    print("Starting Battery Master Optimization...")
    
    # 1. ยุบแถบการแจ้งเตือนลง
    run_cmd("cmd statusbar collapse")
    
    # 2. บังคับเปิดโหมดประหยัดพลังงาน (Low Power Mode)
    run_cmd("settings put global low_power 1")
    
    # 3. ปรับระดับแสงหน้าจอให้อยู่ในระดับประหยัดแบต
    run_cmd("settings put system screen_brightness 50")
    
    # 4. ลดเวลาปิดหน้าจออัตโนมัติเป็น 30 วินาที
    run_cmd("settings put system screen_off_timeout 30000")
    
    print("Optimization Complete!")

if __name__ == "__main__":
    optimize_battery()
