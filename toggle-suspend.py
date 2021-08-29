import tkinter as tk
import psutil as ps
import time

pid = ''
status = None
delay = 10

def proc_gta():
    global pid, status
    found = False

    for proc in ps.process_iter():
        if proc.name() == 'GTA5.exe':
            pid = proc.pid
            status = proc.status()
            found = True

    if not found:
        pid = ''
        status = None

def refresh():
    proc_gta()
    btn_start['state'] = ('normal', 'disabled')[not pid]

    lbl_status.config(
        text = f'Status : {status}'
    )

def start():
    refresh()
    if not pid: return
    
    process = ps.Process(pid)
    process.suspend()
    time.sleep(delay)
    process.resume()

proc_gta()

window = tk.Tk()
window.title('GTA Online solo public session')

lbl_title = tk.Label(
    text = 'GTA Online',
    font = (None, 18)
)
lbl_title.pack()


lbl_status = tk.Label(
    text = f'Status : {status}',
    font = (None, 16)
)
lbl_status.pack()

btn_start = tk.Button(
    window,
    text = f'เริ่ม',
    font = (None, 15),
    state = 'disabled' if not pid else 'normal',
    command = start
)
btn_start.pack()

btn_refresh = tk.Button(
    window,
    text = f'รีเฟรช',
    font = (None, 15),
    command = refresh
)
btn_refresh.pack()

canvas = tk.Canvas(
    window,
    height = 50,
    width = 350
)
canvas.pack()

lbl_author = tk.Label(
    text = f'Github : apiiisit\nEmail : apiiisit@outlook.com'
)
lbl_author.pack()

window.resizable(
    width = False,
    height = False
)
window.mainloop()
