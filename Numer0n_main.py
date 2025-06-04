import tkinter as tk
import socket
#循環インポート関係:関数であれば回避可能?
import Numer0n_singleplay
import Numer0n_multiplay
import Numer0n_common

# グローバル変数
#最初から次

def single_play():
    Numer0n_singleplay.input_singleplay()
#self=任意の変数？
#関数一覧
#共通関数
def multi_play():
    Numer0n_multiplay.show_screen_multiselectFrame(Numer0n_common.selectFrame)

if __name__ == "__main__":
    sock_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_ip.connect(("8.8.8.8",80))
    # IPアドレスを取得
    Numer0n_common.ip_address = sock_ip.getsockname()[0]
    sock_ip.close()
    # ウィジェットの配置
    Numer0n_common.top_text_title.pack(pady=(150,20),side=tk.TOP)
    Numer0n_common.top_button_start.pack(expand = True,side=tk.BOTTOM)
    Numer0n_common.top_label_rank.pack(pady=(0,0),side=tk.TOP)
    Numer0n_common.topFrame.pack()
    def delfunc():
        print('delfunc() execution')
    Numer0n_common.root.wm_protocol('WM_DELETE_WINDOW', delfunc)
    Numer0n_common.root.mainloop()