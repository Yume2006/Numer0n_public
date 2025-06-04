import ctypes
import tkinter as tk
import tkinter.font
from Numer0n_main import single_play,multi_play
from Numer0n_multiplay import show_screen_multiselectFrame,show_screen_clientFrame,show_screen_serverFrame,sendsu,reflog,jmtnum,change_number,inputon
requestnum = None
ip_address =""
history="*****ヌメロン(一人対戦)を開始します。*****\n"
ans=["null","null","null"]
oppoment_number = ["?","?","?"]
targetnum = ["?","?","?","?","?","?","?","?","?","?"]
player_number = ["","",""]
name =""
flag = ""
skilllog = ""
#最初の画面へ
root = tk.Tk()
#名前、回数、経過時間→insert関数で昇順に並べる
rank=[]
ctypes.windll.shcore.SetProcessDpiAwareness(1)
root.resizable(0,0)
root.title(u"ヌメロン")
root.geometry("800x600")
root.eval('tk::PlaceWindow . center')
#デフォルトのフォント設定
font = tk.font.Font(
    root,
    family="MSゴシック",
    size=14
)
def limit_char(string):
    return len(string) <= 20
#対戦時の共通フレーム
playFrame = tk.Frame(root,width=1000,height=800)
#ロード時のフレーム
infomationFrame = tk.Frame(root,width=1000,height=800)
#選択のフレーム
selectFrame=tk.Frame(root,width=1000,height=800)
#フレームサイズ固定
selectFrame.propagate(False)
#ラベル
selectFrame_label_title = tk.Label(selectFrame,text='',font=font)
selectFrame_button_single = tk.Button(selectFrame, text = "一人対戦",width = 16,command=lambda:single_play())
selectFrame_button_multi = tk.Button(selectFrame, text = "二人対戦", width = 16,command=lambda:multi_play(),)
#フレーム名_種類_名前
#トップフレーム
topFrame = tk.Frame(root,width=1000,height=800)
#フレームサイズ固定
topFrame.propagate(False)
#ラベル
top_text_title = tk.Label(topFrame,text='Numer0n',font=("Helvetica",24))
top_button_start = tk.Button(topFrame,text = "Start",width=16,command=lambda:name_import(topFrame))
top_label_rank = tk.Label(topFrame,text="まだ戦績がありません。",relief=tk.GROOVE,font=("",14))

nameFrame = tk.Frame(root,width=1000,height=200)
vc = root.register(limit_char)
#名前入力
nameFrame_box_name=tk.Entry(nameFrame,width=30,background = '#DFDFFF',font=("",14),validate="key", validatecommand=(vc, "%P"))
nameFrame_label_title=tk.Label(nameFrame,text='お名前入力\n',font=font)
nameFrame_label_text=tk.Label(nameFrame,text="・文字は20字以内\n・上位10位以内に入ると名前が表示されます。\n・個人情報(本名・住所など)は禁止",font=("",14))

#接続待ち
serverFrame=tk.Frame(root,width=1000,height=800)
serverFrame_label_title=tk.Label(serverFrame,text="サーバー作成",font=font)
serverFrame_label_ip = tk.Label(serverFrame,text = "",font=("",14))
serverFrame_button_single = tk.Button(serverFrame, text = "やめる",width = 16,command=lambda:show_screen_multiselectFrame(serverFrame))

#接続サーバー入力画面
clientFrame=tk.Frame(root,width=1000,height=800)
clientFrame_box_name=tk.Entry(clientFrame,width=30,background = '#DFDFFF',font=("",14),validate="key", validatecommand=(vc, "%P"))
clientFrame_label_title=tk.Label(clientFrame,text='サーバー接続先\n',font=font)
#clientFrame_label_text=tk.Label(clientFrame,text="・文字は20字以内\n・上位10位以内に入ると名前が表示されます。\n・個人情報(本名・住所など)は禁止",font=("",14))

#接続エラー
errorFrame=tk.Frame(root,width=1000,height=800)
errorFrame_label_title=tk.Label(errorFrame,text='サーバーへ接続できません\n',font=font)
errorFrame_button_select = tk.Button(errorFrame, text = "選択画面へ",width = 16,command=lambda:show_screen_selectFrame(errorFrame))

#マルチ選択フレーム
multiselectFrame=tk.Frame(root,width=1000,height=800)
multiselectFrame_label_title = tk.Label(multiselectFrame,text=u'二人対戦\n',font=font)
multiselectFrame_button_server = tk.Button(multiselectFrame, text = "サーバーを作る",width = 16,command=lambda:show_screen_serverFrame())
multiselectFrame_button_client = tk.Button(multiselectFrame, text = "サーバーに参加する", width = 16,command=lambda:show_screen_clientFrame())
multiselectFrame_button_back = tk.Button(multiselectFrame, text = "戻る", width = 16,command=lambda:show_screen_selectFrame(multiselectFrame))
#アンサー
playFrame_button_ans1 = tk.Label(playFrame, text = ans[0],relief=tk.SUNKEN,width=4,height=4,font=("",14))
playFrame_button_ans2 = tk.Label(playFrame, text = ans[1],relief=tk.SUNKEN,width=4,height=4,font=("",14))
playFrame_button_ans3 = tk.Label(playFrame, text = ans[2],relief=tk.SUNKEN,width=4,height=4,font=("",14))
playFrame_label_blankrow =tk.Label(playFrame,width=1,height=1)
playFrame_label_result = tk.Label(playFrame,text=history,relief=tk.GROOVE,font=("",14))
#空白の列right,left  
playFrame_label_blankcol_r =tk.Label(playFrame,width=1,height=1)
playFrame_label_blankcol_l =tk.Label(playFrame,width=1,height=1)
#ナンバーボタン
playFrame_button_1 = tk.Button(playFrame, text = "1",width=4,height=5,font=("",16),command=lambda:changenumber(1))
playFrame_button_2 = tk.Button(playFrame, text = "2",width=4,height=5,font=("",16),command=lambda:changenumber(2))
playFrame_button_3 = tk.Button(playFrame, text = "3",width=4,height=5,font=("",16),command=lambda:changenumber(3))
playFrame_button_4 = tk.Button(playFrame, text = "4",width=4,height=5,font=("",16),command=lambda:changenumber(4))
playFrame_button_5 = tk.Button(playFrame, text = "5",width=4,height=5,font=("",16),command=lambda:changenumber(5))
playFrame_button_6 = tk.Button(playFrame, text = "6",width=4,height=5,font=("",16),command=lambda:changenumber(6))
playFrame_button_7 = tk.Button(playFrame, text = "7",width=4,height=5,font=("",16),command=lambda:changenumber(7))
playFrame_button_8 = tk.Button(playFrame, text = "8",width=4,height=5,font=("",16),command=lambda:changenumber(8))
playFrame_button_9 = tk.Button(playFrame, text = "9",width=4,height=5,font=("",16),command=lambda:changenumber(9))
playFrame_button_0 = tk.Button(playFrame, text = "0",width=4,height=5,font=("",16),command=lambda:changenumber(0))
playFrame_button_back = tk.Button(playFrame, text = "一文字\n消す",width=4,height=5,font=("",16),command=lambda:deletenumber())
playFrame_button_enter = tk.Button(playFrame, text = "確定",width=4,height=5,font=("",16),command=lambda:"")

preparationFrame = tk.Frame(root,width=1000,height=800)
preparationFrame_button_1 = tk.Button(preparationFrame, text = "1",width=4,height=5,font=("",16),command=lambda:changenumber(1,"preparationFrame"))
preparationFrame_button_2 = tk.Button(preparationFrame, text = "2",width=4,height=5,font=("",16),command=lambda:changenumber(2,"preparationFrame"))
preparationFrame_button_3 = tk.Button(preparationFrame, text = "3",width=4,height=5,font=("",16),command=lambda:changenumber(3,"preparationFrame"))
preparationFrame_button_4 = tk.Button(preparationFrame, text = "4",width=4,height=5,font=("",16),command=lambda:changenumber(4,"preparationFrame"))
preparationFrame_button_5 = tk.Button(preparationFrame, text = "5",width=4,height=5,font=("",16),command=lambda:changenumber(5,"preparationFrame"))
preparationFrame_button_6 = tk.Button(preparationFrame, text = "6",width=4,height=5,font=("",16),command=lambda:changenumber(6,"preparationFrame"))
preparationFrame_button_7 = tk.Button(preparationFrame, text = "7",width=4,height=5,font=("",16),command=lambda:changenumber(7,"preparationFrame"))
preparationFrame_button_8 = tk.Button(preparationFrame, text = "8",width=4,height=5,font=("",16),command=lambda:changenumber(8,"preparationFrame"))
preparationFrame_button_9 = tk.Button(preparationFrame, text = "9",width=4,height=5,font=("",16),command=lambda:changenumber(9,"preparationFrame"))
preparationFrame_button_0 = tk.Button(preparationFrame, text = "0",width=4,height=5,font=("",16),command=lambda:changenumber(0,"preparationFrame"))
preparationFrame_button_back = tk.Button(preparationFrame, text = "一文字\n消す",width=4,height=5,font=("",16),command=lambda:deletenumber("preparationFrame"))
preparationFrame_button_enter = tk.Button(preparationFrame, text = "確定",width=4,height=5,font=("",16),command=lambda:[])
#アンサー
preparationFrame_button_ans1 = tk.Label(preparationFrame, text = ans[0],relief=tk.SUNKEN,width=4,height=4,font=("",14))
preparationFrame_button_ans2 = tk.Label(preparationFrame, text = ans[1],relief=tk.SUNKEN,width=4,height=4,font=("",14))
preparationFrame_button_ans3 = tk.Label(preparationFrame, text = ans[2],relief=tk.SUNKEN,width=4,height=4,font=("",14))
preparationFrame_label_blankrow =tk.Label(preparationFrame,width=1,height=1)
preparationFrame_label_result = tk.Label(preparationFrame,text=history,relief=tk.GROOVE,font=("",14))
#空白の列right,left  
preparationFrame_label_blankcol_r =tk.Label(preparationFrame,width=1,height=1)
preparationFrame_label_blankcol_l =tk.Label(preparationFrame,width=1,height=1)

#スキル
playFrame_button_double = tk.Button(playFrame, text = "DOUBLE",width=8,height=4,font=("",14),command=lambda:"")
playFrame_button_hilo = tk.Button(playFrame, text = "HIGH\n&\nLOW",width=8,height=4,font=("",14),command=lambda:hilo())
playFrame_button_target = tk.Button(playFrame, text = "TARGET",width=8,height=4,font=("",14),command=lambda:root.destroy())
playFrame_button_slash = tk.Button(playFrame, text = "SLASH",width=8,height=4,font=("",14),command=lambda:slash())
playFrame_button_shuffle = tk.Button(playFrame, text = "SHUFFLE",width=8,height=4,font=("",14),command=lambda:[])
playFrame_button_change = tk.Button(playFrame, text = "CHANGE",width=8,height=4,font=("",14),command=lambda:"")
playFrame_button_end = tk.Button(playFrame, text = "終了",width=8,height=4,font=("",14),command=lambda:[inputon(),show_screen_topFrame(playFrame)])
playFrame_button_quit = tk.Button(playFrame, text = "諦める",width=8,height=4,font=("",14),command=lambda:show_screen_topFrame(playFrame))
#マルチプレイのみ
playFrame_label_timer = tk.Button(playFrame, text = "",width=8,height=4,font=("",14))
#ロード中の画面
infomationFrame_label_title=tk.Label(infomationFrame,text='接続中...\n',font=font)
#相手のナンバー開示選択
#アンサー
selectnumFrame = tk.Frame(root,width=1000,height=800,bg='#808080')
selectnumFrame_label_title = tk.Label(selectnumFrame,text = "開示させたい数字を選んでください。")
selectnumFrame_button_oppans1 = tk.Button(selectnumFrame, text = oppoment_number[0],relief=tk.SUNKEN,width=8,height=8,font=("",14),command=lambda:[double_af(0),multi_play()])
selectnumFrame_button_oppans2 = tk.Button(selectnumFrame, text = oppoment_number[1],relief=tk.SUNKEN,width=8,height=8,font=("",14),command=lambda:[double_af(1),multi_play()])
selectnumFrame_button_oppans3 = tk.Button(selectnumFrame, text = oppoment_number[2],relief=tk.SUNKEN,width=8,height=8,font=("",14),command=lambda:[double_af(2),multi_play()])
#ターゲットの選択
selecttargetFrame = tk.Frame(root,width=1000,height=800)
selecttargetFrame_label_title = tk.Label(selecttargetFrame,text = "開示させたい数字を選んでください。")
selecttargetFrame_button_0 = tk.Button(selecttargetFrame, text = str(0)+"\n"+targetnum[0],relief=tk.SUNKEN,width=8,height=8,font=("",14),command=lambda:[])
selecttargetFrame_button_1 = tk.Button(selecttargetFrame, text = str(1)+"\n"+targetnum[1],relief=tk.SUNKEN,width=8,height=8,font=("",14),command=lambda:[])
selecttargetFrame_button_2 = tk.Button(selecttargetFrame, text = str(2)+"\n"+targetnum[2],relief=tk.SUNKEN,width=8,height=8,font=("",14),command=lambda:[])
selecttargetFrame_button_3 = tk.Button(selecttargetFrame, text = str(3)+"\n"+targetnum[3],relief=tk.SUNKEN,width=8,height=8,font=("",14),command=lambda:[])
selecttargetFrame_button_4 = tk.Button(selecttargetFrame, text = str(4)+"\n"+targetnum[4],relief=tk.SUNKEN,width=8,height=8,font=("",14),command=lambda:[])
selecttargetFrame_button_5 = tk.Button(selecttargetFrame, text = str(5)+"\n"+targetnum[5],relief=tk.SUNKEN,width=8,height=8,font=("",14),command=lambda:[])
selecttargetFrame_button_6 = tk.Button(selecttargetFrame, text = str(6)+"\n"+targetnum[6],relief=tk.SUNKEN,width=8,height=8,font=("",14),command=lambda:[])
selecttargetFrame_button_7 = tk.Button(selecttargetFrame, text = str(7)+"\n"+targetnum[7],relief=tk.SUNKEN,width=8,height=8,font=("",14),command=lambda:[])
selecttargetFrame_button_8 = tk.Button(selecttargetFrame, text = str(8)+"\n"+targetnum[8],relief=tk.SUNKEN,width=8,height=8,font=("",14),command=lambda:[])
selecttargetFrame_button_9 = tk.Button(selecttargetFrame, text = str(9)+"\n"+targetnum[9],relief=tk.SUNKEN,width=8,height=8,font=("",14),command=lambda:[])

#共通関数

def show_screen_topFrame(Frame):
    playFrame_button_end["state"]="disabled"
    Frame.pack_forget()
    rank_text=""
    if len(rank)>0:
        if len(rank)>10:
            s=range(10)
        else:
            s=range(len(rank))
        for number in s:
            #[]はlist型、{}はset型
            rank_text=rank_text+str(number+1)+"位:"+rank[number][0]+"さん 回数:"+str(rank[number][1])+"回 経過時間:"+rank[number][2]+"\n"
        top_label_rank["text"] =rank_text
    topFrame.pack()
def forget():
    playFrame.pack_forget()

def show_screen_selectFrame(Frame):
    # ウィジェットの配置
    selectFrame.pack()
    selectFrame_label_title.pack(pady=(200,20))
    selectFrame_button_single.pack(pady=(0, 20))
    selectFrame_button_multi.pack()
    Frame.pack_forget()

#object=任意のクラス(いい表現あったら変える)
class name_import():
    def __init__(a,Frame):
        Frame.pack_forget()
        nameFrame.pack()
        nameFrame_label_title.pack(pady=(200,20))

        nameFrame_box_name.insert(0,"名無し")
        nameFrame_box_name.pack(pady=(0, 20))
        
        nameFrame_label_text.pack()
        name_import.nameFrame_button_enter = tk.Button(nameFrame, text = "決定",width = 16,command=lambda:[name_import.name_import( object,nameFrame_box_name.get() ),show_screen_selectFrame(nameFrame)])
        name_import.nameFrame_button_enter.pack()
    def name_import(object,pname):
        global name
        name=pname.replace('\n','')
        nameFrame.pack_forget()
        nameFrame_box_name.delete(0, tk.END)
        name_import.nameFrame_button_enter.destroy()
        selectFrame_label_title["text"] = name+"さん、ようこそ！\nメニュー\n"
        selectFrame_label_title.update()

def hilo():
    global skilllog,history
    log = name+"さんの回答:"
    for i in range(len(player_number)):
        cnumber = player_number[i]
        if cnumber >=5:
            log = log+"High:"
        else:
            log = log+"low:"
    skilllog = log +"\n"
    history=history+log+"\n"
    skilllos()
    playFrame_label_result["text"] = history
    playFrame_label_result.update()

def slash():
    maxnum = 0
    minnum = 10
    for i in range(len(player_number)):
        number = player_number[i]           
        if maxnum<number:
            maxnum = number
        if minnum>number:
            minnum = number
    result = maxnum-minnum
    global history,skilllog
    skilllog = "Slash発動！！\nスラッシュナンバー："+str(result)+"\n"
    history=history+skilllog
    skilllos()
    playFrame_label_result["text"] = history
    playFrame_label_result.update()

def double():
    playFrame.pack_forget()
    selectnumFrame_label_title.grid(row=0,column=0,columnspan=5)
    selectnumFrame_button_oppans1.grid(row=1,column=1)
    selectnumFrame_button_oppans2.grid(row=1,column=2)
    selectnumFrame_button_oppans3.grid(row=1,column=3)
    selectnumFrame.pack()
    root.update()
    
def double_af(num):
    global requestnum
    requestnum = num
    sendsu("ans"+str(num))
    selectnumFrame.pack_forget()
    playFrame.pack()
def target():
    playFrame.pack_forget()
    selecttargetFrame_button_0.grid(row=1,column=4,sticky=tk.E)
    selecttargetFrame_button_1.grid(row=0,column=0,sticky=tk.E)
    selecttargetFrame_button_2.grid(row=0,column=1,sticky=tk.E)
    selecttargetFrame_button_3.grid(row=0,column=2,sticky=tk.E)
    selecttargetFrame_button_4.grid(row=0,column=3,sticky=tk.E)
    selecttargetFrame_button_5.grid(row=0,column=4,sticky=tk.E)
    selecttargetFrame_button_6.grid(row=1,column=0,sticky=tk.E)
    selecttargetFrame_button_7.grid(row=1,column=1,sticky=tk.E)
    selecttargetFrame_button_8.grid(row=1,column=2,sticky=tk.E)
    selecttargetFrame_button_9.grid(row=1,column=3,sticky=tk.E)
    selecttargetFrame.pack()
    root.update()

def target_af(num):#何も使わない
    selecttargetFrame.pack_forget()

def shuffle():
    skilllos()
    playFrame.pack_forget()
    preparationFrame_button_enter["command"] = lambda:[change_number(ans),sendsu("shuffle")]
    preparationFrame_label_result["text"] = "変更後のナンバーを入力してください\n"
    preparationFrame_label_result.update()
    preparationFrame_button_enter.update()
    preparationFrame.pack()

def skilllos():
    playFrame_button_double["state"]="disabled"
    playFrame_button_target["state"]="disabled"
    playFrame_button_shuffle["state"]="disabled"
    playFrame_button_change["state"]="disabled"
    playFrame_button_hilo["state"]="disabled"
    playFrame_button_slash["state"]="disabled"

def skillok():
    playFrame_button_double["state"]="active"
    playFrame_button_target["state"]="active"
    playFrame_button_shuffle["state"]="active"
    playFrame_button_change["state"]="active"
    playFrame_button_hilo["state"]="active"
    playFrame_button_slash["state"]="active"
    #数字をけす
def deletenumber(Frame):
    i=0
    while (not ans[i] == "null") and i<len(ans)-1:
        i=i+1
    if ans[i] == "null" and 0<i:
        ans[i-1]="null"
        eval(str(Frame)+"_button_ans"+str((i)))["text"]=str(ans[i])
        eval(str(Frame)+"_button_ans"+str((i+1))).update()
    elif i==2:
        ans[i]="null"
        eval(str(Frame)+"_button_ans"+str((i+1)))["text"]=str(ans[i])
        eval(str(Frame)+"_button_ans"+str((i+1))).update()
    else:
        pass

    #数字を入力
def changenumber(number,Frame):
    i=0
    while (not ans[i] == "null") and i<len(ans)-1:
        i=i+1
    if ans[i] == "null":
        ans[i]=number
        eval(str(Frame)+"_button_ans"+str((i+1)))["text"]=str(ans[i])

    else:
        pass
    eval(str(Frame)+"_button_ans"+str((i+1))).update()
    
    
