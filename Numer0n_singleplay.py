import tkinter as tk
import tkinter.font
import time


import random
import Numer0n_common #共通

start = time.time()
turn =0
def input_singleplay():
    Numer0n_common.history="*****ヌメロン(一人対戦)を開始します。*****\n"
    Numer0n_common.playFrame_button_enter["command"] = lambda:play_single(Numer0n_common.ans)
    Numer0n_common.playFrame_button_0["command"] = lambda:Numer0n_common.changenumber(0,"playFrame")
    Numer0n_common.playFrame_button_1["command"] = lambda:Numer0n_common.changenumber(1,"playFrame")
    Numer0n_common.playFrame_button_2["command"] = lambda:Numer0n_common.changenumber(2,"playFrame")
    Numer0n_common.playFrame_button_3["command"] = lambda:Numer0n_common.changenumber(3,"playFrame")
    Numer0n_common.playFrame_button_4["command"] = lambda:Numer0n_common.changenumber(4,"playFrame")
    Numer0n_common.playFrame_button_5["command"] = lambda:Numer0n_common.changenumber(5,"playFrame")
    Numer0n_common.playFrame_button_6["command"] = lambda:Numer0n_common.changenumber(6,"playFrame")
    Numer0n_common.playFrame_button_7["command"] = lambda:Numer0n_common.changenumber(7,"playFrame")
    Numer0n_common.playFrame_button_8["command"] = lambda:Numer0n_common.changenumber(8,"playFrame")
    Numer0n_common.playFrame_button_9["command"] = lambda:Numer0n_common.changenumber(9,"playFrame")
    Numer0n_common.playFrame_button_back["command"] = lambda:Numer0n_common.deletenumber("playFrame")
    Numer0n_common.playFrame_button_slash["command"] = lambda:Numer0n_common.slash()
    Numer0n_common.playFrame_button_hilo["command"] = lambda:Numer0n_common.hilo()
    Numer0n_common.flag = "False"
    Numer0n_common.playFrame_button_end["state"]="disabled"
    Numer0n_common.playFrame_button_quit["state"]="active"
    Numer0n_common.playFrame_button_enter["state"]="active"
    Numer0n_common.playFrame_button_1["state"]="active"
    Numer0n_common.playFrame_button_2["state"]="active"
    Numer0n_common.playFrame_button_3["state"]="active"
    Numer0n_common.playFrame_button_4["state"]="active"
    Numer0n_common.playFrame_button_5["state"]="active"
    Numer0n_common.playFrame_button_6["state"]="active"
    Numer0n_common.playFrame_button_7["state"]="active"
    Numer0n_common.playFrame_button_8["state"]="active"
    Numer0n_common.playFrame_button_9["state"]="active"
    Numer0n_common.playFrame_button_0["state"]="active"
    Numer0n_common.playFrame_button_hilo["state"]="active"
    Numer0n_common.playFrame_button_slash["state"]="active"
    start = time.time()
    print(start)
    landom()
    show_screen_playFrame()
#一人対戦へ
def show_screen_playFrame():
    Numer0n_common.selectFrame.pack_forget()
    #一人対戦のフレーム
    #フレームサイズ固定
    Numer0n_common.playFrame.propagate(False)
    #フレームサイズ固定
    Numer0n_common.playFrame.propagate(False)
    Numer0n_common.skillok()
    if Numer0n_common.player_number==["","",""]:
        landom()

    #for number in range(len(history)):
        #history_text=history_text+str(history[number])
        #str(number+1)+":"+str(history[number][0])+" BITE:"+str(history[number][1])+" EAT:"+str(history[number][2])+"\n"

        
    
    if Numer0n_common.flag =="True":
        Numer0n_common.playFrame_button_end["state"]="active"
        Numer0n_common.playFrame_button_quit["state"]="disabled"
        Numer0n_common.playFrame_button_enter["state"]="disabled"
        Numer0n_common.playFrame_button_1["state"]="disabled"
        Numer0n_common.playFrame_button_2["state"]="disabled"
        Numer0n_common.playFrame_button_3["state"]="disabled"
        Numer0n_common.playFrame_button_4["state"]="disabled"
        Numer0n_common.playFrame_button_5["state"]="disabled"
        Numer0n_common.playFrame_button_6["state"]="disabled"
        Numer0n_common.playFrame_button_7["state"]="disabled"
        Numer0n_common.playFrame_button_8["state"]="disabled"
        Numer0n_common.playFrame_button_9["state"]="disabled"
        Numer0n_common.playFrame_button_0["state"]="disabled"
        Numer0n_common.playFrame_button_hilo["state"]="disabled"
        Numer0n_common.playFrame_button_slash["state"]="disabled"
    Numer0n_common.playFrame_label_result["text"] =Numer0n_common.history
    # ウィジェットの配置
    Numer0n_common.playFrame_label_result.grid(row=0,column=0,columnspan=4,rowspan=6)
    Numer0n_common.playFrame_button_ans1.grid(row=0,column=5,sticky=tkinter.E)
    Numer0n_common.playFrame_button_ans2.grid(row=0,column=6,sticky=tkinter.E)
    Numer0n_common.playFrame_button_ans3.grid(row=0,column=7,sticky=tkinter.E)

    Numer0n_common.playFrame_label_blankrow.grid(row = 1, column = 5, columnspan = 3, sticky = tk.E)
    #ナンバー
    Numer0n_common.playFrame_button_1.grid(row=2,column=5,sticky=tkinter.E)
    Numer0n_common.playFrame_button_2.grid(row=2,column=6,sticky=tkinter.E)
    Numer0n_common.playFrame_button_3.grid(row=2,column=7,sticky=tkinter.E)
    Numer0n_common.playFrame_button_4.grid(row=3,column=5,sticky=tkinter.E)
    Numer0n_common.playFrame_button_5.grid(row=3,column=6,sticky=tkinter.E)
    Numer0n_common.playFrame_button_6.grid(row=3,column=7,sticky=tkinter.E)
    Numer0n_common.playFrame_button_7.grid(row=4,column=5,sticky=tkinter.E)
    Numer0n_common.playFrame_button_8.grid(row=4,column=6,sticky=tkinter.E)
    Numer0n_common.playFrame_button_9.grid(row=4,column=7,sticky=tkinter.E)
    Numer0n_common.playFrame_button_0.grid(row=5,column=5,sticky=tkinter.E)
    Numer0n_common.playFrame_button_back.grid(row=5,column=6,sticky=tkinter.E)
    Numer0n_common.playFrame_button_enter.grid(row=5,column=7,sticky=tkinter.E)
    Numer0n_common.playFrame_label_blankcol_r.grid(row = 0, column = 8, rowspan = 6, sticky = tk.E)
    Numer0n_common.playFrame_label_blankcol_l.grid(row = 0, column=4, rowspan = 6, sticky = tk.E)
    Numer0n_common.playFrame_button_hilo.grid(row=2,column=9,sticky=tkinter.E)
    Numer0n_common.playFrame_button_slash.grid(row=2,column=10,sticky=tkinter.E)
    Numer0n_common.playFrame_button_end.grid(row=5,column=9,sticky=tkinter.E)
    Numer0n_common.playFrame_button_quit.grid(row=5,column=10,sticky=tkinter.E)
  
    Numer0n_common.playFrame.pack()

def landom():
    ramdom_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number=random.sample(ramdom_list, 3)
    for i in range(3):
        Numer0n_common.player_number[i]=number[i]   

def play_single(ans):
    i=0
    while not ans[i]=="null" and i<len(ans)-1:
        i=i+1
    if ans[i]=="null":
        Numer0n_common.history=Numer0n_common.history+"エラー:3桁を入力してください。\n"
        return show_screen_playFrame()
        
    if(len(ans) != len(set(ans))):
        Numer0n_common.history=Numer0n_common.history+("エラー:各桁に違う数字を入力してください。\n")
        return show_screen_playFrame()
    eat=0
    bite=0
    number=0
    for i in range(3):
        number=number*10+int(ans[i])

        if(int(ans[i]) == Numer0n_common.player_number[i]):
            eat=eat+1
        elif Numer0n_common.player_number[i] in ans:
            bite=bite+1
    if number<100:
        number="0"+str(number)       
    global turn
    turn += 1
    Numer0n_common.history=Numer0n_common.history+(str(turn)+"回目:"+str(number)+" BITE:"+str(bite)+" EAT:"+str(eat)+"\n")
    Numer0n_common.ans = ["null","null","null"]
    Numer0n_common.playFrame_button_ans1["text"]="null"
    Numer0n_common.playFrame_button_ans2["text"]="null"
    Numer0n_common.playFrame_button_ans3["text"]="null"
    Numer0n_common.playFrame_button_ans1.update()
    Numer0n_common.playFrame_button_ans2.update()
    Numer0n_common.playFrame_button_ans3.update()
    Numer0n_common.skillok()
    #正解したら
    if eat==3:
        Numer0n_common.flag="True"
        end=time.time()
        if end<start:
            end=end+86400
        re_time=format(end-start, '.3f')
        print(end)
        i=0
        while len(Numer0n_common.rank)>i:
            if Numer0n_common.rank[i][1]==turn:
                while Numer0n_common.rank[i][1]==turn and float(Numer0n_common.rank[i][2])<float(re_time):
                    i=i+1
                    if len(Numer0n_common.rank)==i:
                        break
                break
            elif Numer0n_common.rank[i][1]>turn:
                i=i-1
                break
            i=i+1
        print(Numer0n_common.name)
        Numer0n_common.rank.insert(i, [Numer0n_common.name,turn,re_time])
        Numer0n_common.history=Numer0n_common.history+("正解！\n回数:"+str(turn)+ " 経過時間:"+re_time+" 順位:"+str(i+1)+"位\n終了ボタンを押してください。\n")
    show_screen_playFrame()