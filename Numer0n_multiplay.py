import Numer0n_common
import socket
import time
import threading
import select
import datetime
import tkinter as tk
BUFSIZE = 4096  # 受信バッファの大きさ
PORT =50001  # ポート番号
sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
is_recv =True
unknownnumber = ["?","?","?"]
clientFrame_button_enter=None
oppoment_name = ""
addr = None
dbeflg = False
#イベントのフラグが立つまで待機
event = threading.Event()
flont = None
def show_screen_clientFrame():
    global clientFrame_button_enter
    Numer0n_common.clientFrame.pack()
    Numer0n_common.clientFrame_label_title.pack(pady=(200,20))
    Numer0n_common.clientFrame_box_name.pack()
    clientFrame_button_enter = tk.Button(Numer0n_common.clientFrame, text = "決定",width = 16,command=lambda:client_main(Numer0n_common.clientFrame_box_name.get()))
    clientFrame_button_enter.pack(pady=(50,20))
    Numer0n_common.multiselectFrame.pack_forget()

def send_number(side):
    global dbeflg
    sock.sendto(str(Numer0n_common.ans).encode(encoding='utf-8'),addr)
        
    if side == "Client":
        data = sock.recv(BUFSIZE)
    else:
        data ,i = sock.recvfrom(BUFSIZE)
    if  "エラー" in data.decode('utf-8'):     
        Numer0n_common.history=Numer0n_common.history+data.decode('utf-8')
        return inputon(),show_screen_playFrame()
    #判定結果を受け取る
    result = eval(data.decode('utf-8'))
    if result[2]==3:
        Numer0n_common.history=Numer0n_common.history+(oppoment_name+"さんの勝ち\n終了ボタンを押してください。\n")
        Numer0n_common.playFrame_label_result["text"] = Numer0n_common.history
        Numer0n_common.playFrame_button_end.grid(row=5,column=9,sticky=tk.E)
        Numer0n_common.playFrame.update()
        sock.close()
        return
    Numer0n_common.history=Numer0n_common.history+(Numer0n_common.name+"のコール:"+str(result[0])+" BITE:"+str(result[1])+" EAT:"+str(result[2])+"\n")
    result_update()
    Numer0n_common.ans = ["null","null","null"]
    Numer0n_common.playFrame_button_ans1["text"]="null"
    Numer0n_common.playFrame_button_ans2["text"]="null"
    Numer0n_common.playFrame_button_ans3["text"]="null"
    Numer0n_common.playFrame_button_ans1.update()
    Numer0n_common.playFrame_button_ans2.update()
    Numer0n_common.playFrame_button_ans3.update()
    if dbeflg == False:
        show_screen_playFrame()
        play_multi("Server")
    else :
        dbeflg = False
        inputon()
        show_screen_playFrame()

def reflog(side):
    if side == "Client":
        data = sock.recv(BUFSIZE)
    else:
        data ,n = sock.recvfrom(BUFSIZE)
    Numer0n_common.history = Numer0n_common.history+(data.decode('utf-8'))
    result_update()
    Numer0n_common.skilllos()
    
def result_update():
    Numer0n_common.playFrame_label_result["text"] = Numer0n_common.history
    Numer0n_common.playFrame_label_result.update()

def target_update():
    Numer0n_common.selecttargetFrame_button_0["text"] = str(0)+"\n"+Numer0n_common.targetnum[0]
    Numer0n_common.selecttargetFrame_button_1["text"] = str(1)+"\n"+Numer0n_common.targetnum[1]
    Numer0n_common.selecttargetFrame_button_2["text"] = str(2)+"\n"+Numer0n_common.targetnum[2]
    Numer0n_common.selecttargetFrame_button_3["text"] = str(3)+"\n"+Numer0n_common.targetnum[3]
    Numer0n_common.selecttargetFrame_button_4["text"] = str(4)+"\n"+Numer0n_common.targetnum[4]
    Numer0n_common.selecttargetFrame_button_5["text"] = str(5)+"\n"+Numer0n_common.targetnum[5]
    Numer0n_common.selecttargetFrame_button_6["text"] = str(6)+"\n"+Numer0n_common.targetnum[6]
    Numer0n_common.selecttargetFrame_button_7["text"] = str(7)+"\n"+Numer0n_common.targetnum[7]
    Numer0n_common.selecttargetFrame_button_8["text"] = str(8)+"\n"+Numer0n_common.targetnum[8]
    Numer0n_common.selecttargetFrame_button_9["text"] = str(9)+"\n"+Numer0n_common.targetnum[9]

#評価
def play_multi(side):
    global dbeflg
    while True:
        if side == "Client":
            data = sock.recv(BUFSIZE)
        else:
            data ,n = sock.recvfrom(BUFSIZE)
        print(data.decode('utf-8'))
        try:
            if type(eval(data.decode('utf-8'))) == list:
                ans = eval(data.decode('utf-8'))
                break
        except Exception as ex:
            print('Exception: time={}, desc={}'.format(datetime.datetime.now(), ex))
            pass

        if "change" in data.decode('utf-8'):
            Numer0n_common.changenumber(int((data.decode('utf-8')).replace("change","")),"playFrame")
        elif "delete" in data.decode('utf-8'):
            Numer0n_common.deletenumber("playFrame")
        elif "skill" in data.decode('utf-8'):
            eval('Numer0n_common.'+(data.decode('utf-8')).replace("skill",""))()
            if data.decode('utf-8').replace("skill","") == "double":
                return
            elif "slash" in data.decode('utf-8') or "hilo" in data.decode('utf-8'):
                sendsu(Numer0n_common.skilllog)
        elif "targetans" in data.decode('utf-8'):
            number = int(data.decode('utf-8').replace("targetans",""))
            if 9 == number % 10:
                Numer0n_common.targetnum[int(number/10)] = "✕"
                Numer0n_common.history = Numer0n_common.history+"TARGET発動！\n"+str(int(number/10))+"は"+oppoment_name+"のナンバーに含まれていません！\n"
            else:
                Numer0n_common.targetnum[int(number/10)] = "〇"
                unknownnumber[number%10] = int(number/10)
                Numer0n_common.history = Numer0n_common.history+"TARGET発動！\n"+Numer0n_common.name+"のナンバーが開示されました！:"+str(unknownnumber)+"\n"
            target_update()
            result_update()
            Numer0n_common.selecttargetFrame.pack_forget()
            Numer0n_common.playFrame.pack()
            Numer0n_common.skilllos()
            return
        elif "ans" in data.decode('utf-8'):
            unknownnumber[int(data.decode('utf-8').replace("ans",""))] = Numer0n_common.player_number[int(data.decode('utf-8').replace("ans",""))]
            #sock.sendto(str(Numer0n_common.ans).encode(encoding='utf-8'),addr)
        
            Numer0n_common.history = Numer0n_common.history+"DOUBLE発動！\n"+Numer0n_common.name+"のナンバー開示！："+str(unknownnumber)+"\n"
            Numer0n_common.playFrame_label_result["text"] = Numer0n_common.history
            Numer0n_common.playFrame_label_result.update()
            # デコードして "ans" を削除し、インデックスを取得
            index = int(data.decode('utf-8').replace("ans", ""))
            message = "number" + str(Numer0n_common.player_number[index])
            sock.sendto(message.encode(encoding='utf-8'),addr)
            dbeflg = True
            return
        elif "number" in data.decode('utf-8'):
            Numer0n_common.oppoment_number[Numer0n_common.requestnum] = data.decode('utf-8').replace("number","")
            dbeflg = True
            Numer0n_common.history = Numer0n_common.history+"DOUBLE発動！\n"+oppoment_name+"のナンバー開示！："+str(Numer0n_common.oppoment_number)+"\n"
            Numer0n_common.playFrame_label_result["text"] = Numer0n_common.history
            Numer0n_common.playFrame_label_result.update()
        elif "target" in data.decode('utf-8'):
            logh = ""
            if data.decode('utf-8').replace("target","") in str(Numer0n_common.player_number):
                for i in range(3):
                    if str(Numer0n_common.player_number[i]) == data.decode('utf-8').replace("target",""):
                        unknownnumber[i] = Numer0n_common.player_number[i]
                        logh = "TARGET発動！\n"+Numer0n_common.name+"のナンバーが開示されました！:"+str(unknownnumber)+"\n"
                        sendsu("targetans"+data.decode('utf-8').replace("target","")+str(i))
            else:
                logh = "TARGET発動！\n"+str(data.decode('utf-8').replace("target",""))+"は"+Numer0n_common.name+"のナンバーに含まれていません！\n"
                sendsu("targetans"+data.decode('utf-8').replace("target","")+str(9))#9はunknownnumberの要素番号外なのでNULLとする
            Numer0n_common.history = Numer0n_common.history+logh
            result_update()
        elif "shuffle" == data.decode('utf-8'):
            Numer0n_common.history = Numer0n_common.history + "SHUFFLE発動！\n"+oppoment_name+"さんのナンバーが変更されました\n" 



            

    time.sleep(1)
    for m in range(3):
        if ans[m]=="null":
            sock.sendto("エラー:3桁を入力してください。\n".encode(encoding='utf-8'),addr)
            Numer0n_common.history=Numer0n_common.history+"エラー:3桁を入力してください。\n"
            Numer0n_common.playFrame_label_result["text"] = Numer0n_common.history
            Numer0n_common.playFrame_label_result.update()
            return play_multi(side)
        
    if(len(ans) != len(set(ans))):
        Numer0n_common.history=Numer0n_common.history+("エラー:各桁に違う数字を入力してください。\n")
        sock.sendto("エラー:各桁に違う数字を入力してください。\n".encode('utf-8'),addr)
        result_update()
        return play_multi(side)
    result = jmtnum(ans)
    Numer0n_common.history=Numer0n_common.history+(oppoment_name+"のコール:"+str(result[0])+" BITE:"+str(result[1])+" EAT:"+str(result[2])+"\n")
    Numer0n_common.ans = ["null","null","null"]
    Numer0n_common.playFrame_button_ans1["text"]="null"
    Numer0n_common.playFrame_button_ans2["text"]="null"
    Numer0n_common.playFrame_button_ans3["text"]="null"
    Numer0n_common.playFrame_button_ans1.update()
    Numer0n_common.playFrame_button_ans2.update()
    Numer0n_common.playFrame_button_ans3.update()
    result_update()
    if dbeflg == False:
        inputon()
        Numer0n_common.playFrame.update()
        show_screen_playFrame()
    else:
        dbeflg = False
        play_multi(side)

def jmtnum(ans):
    #数字・byte・eat
    result = [0,0,0]

    for i in range(3):
        result[0]=result[0]*10+int(ans[i])

        if(int(ans[i]) == Numer0n_common.player_number[i]):
            result[2]+=1
        elif Numer0n_common.player_number[i] in ans:
            result[1]+=1
    if result[0]<100:
        result[0]="0"+str(result[0])
    sock.sendto(str(result).encode(encoding='utf-8'),addr)
        #正解したら
    if result[2]==3:
        Numer0n_common.history=Numer0n_common.history+(oppoment_name+"さんの勝ち\n終了ボタンを押してください。\n")
        Numer0n_common.playFrame_label_result["text"] = Numer0n_common.history
        Numer0n_common.playFrame_button_end.grid(row=5,column=9,sticky=tk.E)
        Numer0n_common.playFrame.update()
        sock.close()
    return result
#サーバーを立てる_Server
def Server_create():
    global sock,is_recv
    is_recv = True
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((Numer0n_common.ip_address,PORT))
    rfds = [sock]
    print(rfds)
    print('create socket')
    while is_recv:
            try:
                r, _, _ = select.select(rfds, [], [], 0.5)
                print("受付中")
                for rs in r:
                    print("入った")
                    global oppoment_name,addr
                    while True:
                        sock.settimeout(300)
                        data, addr = sock.recvfrom(4096)
                        #Clientが受信待ちになるまで待つため
                        time.sleep(1)
                        if data.decode('utf8', 'ignore') == "client_OK":
                            Numer0n_common.history="*****ヌメロン(一人対戦)を開始します。*****\n"
                            Numer0n_common.preparationFrame.pack_forget()
                            Numer0n_common.preparationFrame_button_enter["state"] = "active"
                            Numer0n_common.playFrame_button_0["command"] = lambda:[Numer0n_common.changenumber(0,"playFrame"),sendsu("change0")]
                            Numer0n_common.playFrame_button_1["command"] = lambda:[Numer0n_common.changenumber(1,"playFrame"),sendsu("change1")]
                            Numer0n_common.playFrame_button_2["command"] = lambda:[Numer0n_common.changenumber(2,"playFrame"),sendsu("change2")]
                            Numer0n_common.playFrame_button_3["command"] = lambda:[Numer0n_common.changenumber(3,"playFrame"),sendsu("change3")]
                            Numer0n_common.playFrame_button_4["command"] = lambda:[Numer0n_common.changenumber(4,"playFrame"),sendsu("change4")]
                            Numer0n_common.playFrame_button_5["command"] = lambda:[Numer0n_common.changenumber(5,"playFrame"),sendsu("change5")]
                            Numer0n_common.playFrame_button_6["command"] = lambda:[ Numer0n_common.changenumber(6,"playFrame"),sendsu("change6")]
                            Numer0n_common.playFrame_button_7["command"] = lambda:[ Numer0n_common.changenumber(7,"playFrame"),sendsu("change7")]
                            Numer0n_common.playFrame_button_8["command"] = lambda:[ Numer0n_common.changenumber(8,"playFrame"),sendsu("change8")]
                            Numer0n_common.playFrame_button_9["command"] = lambda: [Numer0n_common.changenumber(9,"playFrame"),sendsu("change9")]
                            Numer0n_common.selecttargetFrame_button_0["command"] = lambda:[sendsu("target0"),play_multi("Server"),Numer0n_common.target_af(0)]
                            Numer0n_common.selecttargetFrame_button_1["command"] = lambda:[sendsu("target1"),play_multi("Server"),Numer0n_common.target_af(1)]
                            Numer0n_common.selecttargetFrame_button_2["command"] = lambda:[sendsu("target2"),play_multi("Server"),Numer0n_common.target_af(2)]
                            Numer0n_common.selecttargetFrame_button_3["command"] = lambda:[sendsu("target3"),play_multi("Server"),Numer0n_common.target_af(3)]
                            Numer0n_common.selecttargetFrame_button_4["command"] = lambda:[sendsu("target4"),play_multi("Server"),Numer0n_common.target_af(4)]
                            Numer0n_common.selecttargetFrame_button_5["command"] = lambda:[sendsu("target5"),play_multi("Server"),Numer0n_common.target_af(5)]
                            Numer0n_common.selecttargetFrame_button_6["command"] = lambda:[ sendsu("target6"),play_multi("Server"),Numer0n_common.target_af(6)]
                            Numer0n_common.selecttargetFrame_button_7["command"] = lambda:[ sendsu("target7"),play_multi("Server"),Numer0n_common.target_af(7)]
                            Numer0n_common.selecttargetFrame_button_8["command"] = lambda:[ sendsu("target8"),play_multi("Server"),Numer0n_common.target_af(8)]
                            Numer0n_common.selecttargetFrame_button_9["command"] = lambda: [sendsu("target9"),play_multi("Server"),Numer0n_common.target_af(9)]
                            Numer0n_common.playFrame_button_slash["command"] = lambda:[sendsu("skillslash"),reflog("Server")]
                            Numer0n_common.playFrame_button_hilo["command"] = lambda:[sendsu("skillhilo"),reflog("Server")]
                            Numer0n_common.playFrame_button_double["command"] = lambda:[sendsu("skilldouble"),play_multi("Server"),Numer0n_common.skilllos()]
                            Numer0n_common.playFrame_button_target["command"] = lambda:[Numer0n_common.target()]
                            Numer0n_common.playFrame_button_shuffle["command"] = lambda:[Numer0n_common.shuffle()]
                            Numer0n_common.playFrame_button_change["command"] = lambda:[]
                            Numer0n_common.playFrame_button_back["command"] = lambda:[ Numer0n_common.deletenumber("playFrame"),sendsu("delete")]
                            Numer0n_common.playFrame_button_enter["command"] = lambda:[inputoff(),show_screen_playFrame(),send_number("Server")]
                            Numer0n_common.selectnumFrame_button_oppans1["command"] = lambda:[Numer0n_common.double_af(0),play_multi("Server")]
                            Numer0n_common.selectnumFrame_button_oppans2["command"] = lambda:[Numer0n_common.double_af(1),play_multi("Server")]
                            Numer0n_common.selectnumFrame_button_oppans3["command"] = lambda:[Numer0n_common.double_af(2),play_multi("Server")]
                            Numer0n_common.playFrame_label_result.grid(row=0,column=0,columnspan=4,rowspan=6)
                            Numer0n_common.playFrame_button_ans1.grid(row=0,column=5,sticky=tk.E)
                            Numer0n_common.playFrame_button_ans2.grid(row=0,column=6,sticky=tk.E)
                            Numer0n_common.playFrame_button_ans3.grid(row=0,column=7,sticky=tk.E)

                            Numer0n_common.playFrame_label_blankrow.grid(row = 1, column = 5, columnspan = 3, sticky = tk.E)
                            #ナンバー
                            Numer0n_common.playFrame_button_1.grid(row=2,column=5,sticky=tk.E)
                            Numer0n_common.playFrame_button_2.grid(row=2,column=6,sticky=tk.E)
                            Numer0n_common.playFrame_button_3.grid(row=2,column=7,sticky=tk.E)
                            Numer0n_common.playFrame_button_4.grid(row=3,column=5,sticky=tk.E)
                            Numer0n_common.playFrame_button_5.grid(row=3,column=6,sticky=tk.E)
                            Numer0n_common.playFrame_button_6.grid(row=3,column=7,sticky=tk.E)
                            Numer0n_common.playFrame_button_7.grid(row=4,column=5,sticky=tk.E)
                            Numer0n_common.playFrame_button_8.grid(row=4,column=6,sticky=tk.E)
                            Numer0n_common.playFrame_button_9.grid(row=4,column=7,sticky=tk.E)
                            Numer0n_common.playFrame_button_0.grid(row=5,column=5,sticky=tk.E)
                            Numer0n_common.playFrame_button_back.grid(row=5,column=6,sticky=tk.E)
                            Numer0n_common.playFrame_button_enter.grid(row=5,column=7,sticky=tk.E)
                            Numer0n_common.playFrame_label_blankcol_r.grid(row = 0, column = 8, rowspan = 6, sticky = tk.E)
                            Numer0n_common.playFrame_label_blankcol_l.grid(row = 0, column=4, rowspan = 6, sticky = tk.E)
                            Numer0n_common.playFrame_button_double.grid(row=2,column=9,sticky=tk.E)
                            Numer0n_common.playFrame_button_hilo.grid(row=2,column=10,sticky=tk.E)
                            Numer0n_common.playFrame_button_target.grid(row=3,column=9,sticky=tk.E)
                            Numer0n_common.playFrame_button_slash.grid(row=3,column=10,sticky=tk.E)
                            Numer0n_common.playFrame_button_shuffle.grid(row=4,column=9,sticky=tk.E)
                            Numer0n_common.playFrame_button_change.grid(row=4,column=10,sticky=tk.E)
                            Numer0n_common.playFrame_button_enter["state"]="active"
                            Numer0n_common.playFrame.pack()
                            show_screen_playFrame()
                            break
                        oppoment_name = data.decode('utf8', 'ignore')
                        print('received from={}, len={}'.format(addr, len(oppoment_name)))
                        print(f'Received message is [{oppoment_name}]')
                        # ④Clientへ受信完了messageを送信
                        sock.sendto(Numer0n_common.name.encode(encoding='utf-8'),addr)
                        Numer0n_common.serverFrame.pack_forget()
                        Numer0n_common.history="ナンバーを入力してください\n"
                        input_number("serverFrame")
                    is_recv = False
            except TimeoutError:
                Numer0n_common.playFrame.pack_forget()
                server_Error() 
                break
            except Exception as ex:
                print(ex)
                print('Exception: time={}, desc={}'.format(datetime.datetime.now(), ex))
                server_Error()
                break
            finally:
                time.sleep(0.1)

def sendsu(num):
    print(num)
    sock.sendto(num.encode(encoding='utf-8'),addr)

def flont_server():
    Numer0n_common.multiselectFrame.pack_forget()
    Numer0n_common.serverFrame_label_title.pack(pady=(200,20))
    Numer0n_common.serverFrame_label_ip["text"]="参加する相手に入力してもらってください。\n\n"+Numer0n_common.ip_address
    Numer0n_common.serverFrame_label_ip.pack(pady = (0,20))
    Numer0n_common.serverFrame_button_single.pack()
    Numer0n_common.serverFrame.pack()
    Numer0n_common.root.update()
    if is_recv == False:
        return


def show_screen_serverFrame():
    time.sleep(0.5)
    global flont
    flont=threading.Thread(target=flont_server)
    flont.setDaemon(True)
    # スレッドスタート
    flont.start()
    # スレッドの生成
    wait_server = threading.Thread(target=Server_create)
    wait_server.setDaemon(True)
    wait_server.start()

def input_number(Frame):
    # ウィジェットの配置
    Numer0n_common.preparationFrame_button_enter["command"] = lambda:set_number(Numer0n_common.ans,Frame)
    Numer0n_common.preparationFrame_label_result["text"] =Numer0n_common.history
    Numer0n_common.preparationFrame_label_result.grid(row=0,column=0,columnspan=4,rowspan=6)
    Numer0n_common.preparationFrame_button_ans1.grid(row=0,column=5,sticky=tk.E)
    Numer0n_common.preparationFrame_button_ans2.grid(row=0,column=6,sticky=tk.E)
    Numer0n_common.preparationFrame_button_ans3.grid(row=0,column=7,sticky=tk.E)

    Numer0n_common.preparationFrame_label_blankrow.grid(row = 1, column = 5, columnspan = 3, sticky = tk.E)
    #ナンバー
    Numer0n_common.preparationFrame_button_1.grid(row=2,column=5,sticky=tk.E)
    Numer0n_common.preparationFrame_button_2.grid(row=2,column=6,sticky=tk.E)
    Numer0n_common.preparationFrame_button_3.grid(row=2,column=7,sticky=tk.E)
    Numer0n_common.preparationFrame_button_4.grid(row=3,column=5,sticky=tk.E)
    Numer0n_common.preparationFrame_button_5.grid(row=3,column=6,sticky=tk.E)
    Numer0n_common.preparationFrame_button_6.grid(row=3,column=7,sticky=tk.E)
    Numer0n_common.preparationFrame_button_7.grid(row=4,column=5,sticky=tk.E)
    Numer0n_common.preparationFrame_button_8.grid(row=4,column=6,sticky=tk.E)
    Numer0n_common.preparationFrame_button_9.grid(row=4,column=7,sticky=tk.E)
    Numer0n_common.preparationFrame_button_0.grid(row=5,column=5,sticky=tk.E)
    Numer0n_common.preparationFrame_button_back.grid(row=5,column=6,sticky=tk.E)
    Numer0n_common.preparationFrame_button_enter.grid(row=5,column=7,sticky=tk.E)
    Numer0n_common.preparationFrame_label_blankcol_r.grid(row = 0, column = 8, rowspan = 6, sticky = tk.E)
    Numer0n_common.preparationFrame_label_blankcol_l.grid(row = 0, column=4, rowspan = 6, sticky = tk.E)
    Numer0n_common.preparationFrame.pack()
    Numer0n_common.root.update()

def change_number(number):
    if "null" in number:
        Numer0n_common.history=Numer0n_common.history+"エラー:3桁を入力してください。\n"
        return
        
    if(len(number) != len(set(number))):
        Numer0n_common.history=Numer0n_common.history+("エラー:各桁に違う数字を入力してください。\n")
        return
    
    for i in range(3):
        Numer0n_common.player_number[i] = number[i]
        print(Numer0n_common.player_number)
    Numer0n_common.ans[0]="null"   
    Numer0n_common.ans[1]="null"   
    Numer0n_common.ans[2]="null" 
    Numer0n_common.preparationFrame_button_ans1.update()
    Numer0n_common.preparationFrame_button_ans2.update()
    Numer0n_common.preparationFrame_button_ans3.update()
    Numer0n_common.preparationFrame.pack_forget()
    Numer0n_common.playFrame.pack()
    Numer0n_common.root.update()

def set_number(number,Frame):
    i=0
    while not Numer0n_common.ans[i]=="null" and i<len(Numer0n_common.ans)-1:
        i=i+1
    if Numer0n_common.ans[i]=="null":
        Numer0n_common.history=Numer0n_common.history+"エラー:3桁を入力してください。\n"
        return input_number(Frame)
        
    if(len(Numer0n_common.ans) != len(set(Numer0n_common.ans))):
        Numer0n_common.history=Numer0n_common.history+("エラー:各桁に違う数字を入力してください。\n")
        return input_number(Frame)
    Numer0n_common.preparationFrame_button_enter["state"] = "disabled"
    for i in range(3):
        Numer0n_common.player_number[i] = number[i]
        print(Numer0n_common.player_number)
    Numer0n_common.ans[0]="null"   
    Numer0n_common.ans[1]="null"   
    Numer0n_common.ans[2]="null" 
    Numer0n_common.preparationFrame_button_ans1["text"]=Numer0n_common.ans[0]
    Numer0n_common.preparationFrame_button_ans2["text"]=Numer0n_common.ans[1]
    Numer0n_common.preparationFrame_button_ans3["text"]=Numer0n_common.ans[2]
    Numer0n_common.preparationFrame_button_ans1.update()
    Numer0n_common.preparationFrame_button_ans2.update()
    Numer0n_common.preparationFrame_button_ans3.update()
    if Frame == "serverFrame":
        # ④Clientへ受信完了messageを送信
        sock.sendto("server_OK".encode(encoding='utf-8'), addr)
        Numer0n_common.history="相手が入力しています。今しばらくお待ちください\n"
        result_update()
    elif Frame == "clientFrame":
        sock.sendto("client_OK".encode("utf-8"),addr)
        time.sleep(0.5)
        Numer0n_common.preparationFrame.pack_forget()
        Numer0n_common.preparationFrame_button_enter["state"] = "active"
        Numer0n_common.playFrame_button_0["command"] = lambda:[Numer0n_common.changenumber(0,"playFrame"),sendsu("change0")]
        Numer0n_common.playFrame_button_1["command"] = lambda:[Numer0n_common.changenumber(1,"playFrame"),sendsu("change1")]
        Numer0n_common.playFrame_button_2["command"] = lambda:[Numer0n_common.changenumber(2,"playFrame"),sendsu("change2")]
        Numer0n_common.playFrame_button_3["command"] = lambda:[Numer0n_common.changenumber(3,"playFrame"),sendsu("change3")]
        Numer0n_common.playFrame_button_4["command"] = lambda:[Numer0n_common.changenumber(4,"playFrame"),sendsu("change4")]
        Numer0n_common.playFrame_button_5["command"] = lambda:[Numer0n_common.changenumber(5,"playFrame"),sendsu("change5")]
        Numer0n_common.playFrame_button_6["command"] = lambda:[ Numer0n_common.changenumber(6,"playFrame"),sendsu("change6")]
        Numer0n_common.playFrame_button_7["command"] = lambda:[ Numer0n_common.changenumber(7,"playFrame"),sendsu("change7")]
        Numer0n_common.playFrame_button_8["command"] = lambda:[ Numer0n_common.changenumber(8,"playFrame"),sendsu("change8")]
        Numer0n_common.playFrame_button_9["command"] = lambda: [Numer0n_common.changenumber(9,"playFrame"),sendsu("change9")]
        Numer0n_common.selecttargetFrame_button_0["command"] = lambda:[sendsu("target0"),play_multi("Client"),Numer0n_common.target_af(0)]
        Numer0n_common.selecttargetFrame_button_1["command"] = lambda:[sendsu("target1"),play_multi("Client"),Numer0n_common.target_af(1)]
        Numer0n_common.selecttargetFrame_button_2["command"] = lambda:[sendsu("target2"),play_multi("Client"),Numer0n_common.target_af(2)]
        Numer0n_common.selecttargetFrame_button_3["command"] = lambda:[sendsu("target3"),play_multi("Client"),Numer0n_common.target_af(3)]
        Numer0n_common.selecttargetFrame_button_4["command"] = lambda:[sendsu("target4"),play_multi("Client"),Numer0n_common.target_af(4)]
        Numer0n_common.selecttargetFrame_button_5["command"] = lambda:[sendsu("target5"),play_multi("Client"),Numer0n_common.target_af(5)]
        Numer0n_common.selecttargetFrame_button_6["command"] = lambda:[ sendsu("target6"),play_multi("Client"),Numer0n_common.target_af(6)]
        Numer0n_common.selecttargetFrame_button_7["command"] = lambda:[ sendsu("target7"),play_multi("Client"),Numer0n_common.target_af(7)]
        Numer0n_common.selecttargetFrame_button_8["command"] = lambda:[ sendsu("target8"),play_multi("Client"),Numer0n_common.target_af(8)]
        Numer0n_common.selecttargetFrame_button_9["command"] = lambda: [sendsu("target9"),play_multi("Client"),Numer0n_common.target_af(9)]
        Numer0n_common.playFrame_button_back["command"] = lambda:[ Numer0n_common.deletenumber("playFrame"),sendsu("delete")]
        Numer0n_common.playFrame_button_slash["command"] = lambda:[sendsu("skillslash"),reflog("Client")]
        Numer0n_common.playFrame_button_hilo["command"] = lambda:[sendsu("skillhilo"),reflog("Client")]
        Numer0n_common.playFrame_button_double["command"] = lambda:[sendsu("skilldouble"),play_multi("Client"),Numer0n_common.skilllos()]
        Numer0n_common.playFrame_button_target["command"] = lambda:[Numer0n_common.target()]
        Numer0n_common.playFrame_button_shuffle["command"] = lambda:[Numer0n_common.shuffle()]
        Numer0n_common.playFrame_button_enter["command"] = lambda:[inputoff(),show_screen_playFrame(),send_number("Client")]
        Numer0n_common.selectnumFrame_button_oppans1["command"] = lambda:[Numer0n_common.double_af(0),play_multi("Client")]
        Numer0n_common.selectnumFrame_button_oppans2["command"] = lambda:[Numer0n_common.double_af(1),play_multi("Client")]
        Numer0n_common.selectnumFrame_button_oppans3["command"] = lambda:[Numer0n_common.double_af(2),play_multi("Client")]
        Numer0n_common.history="*****ヌメロン(一人対戦)を開始します。*****\n"
        Numer0n_common.playFrame_label_result.grid(row=0,column=0,columnspan=4,rowspan=6)
        Numer0n_common.playFrame_button_ans1.grid(row=0,column=5,sticky=tk.E)
        Numer0n_common.playFrame_button_ans2.grid(row=0,column=6,sticky=tk.E)
        Numer0n_common.playFrame_button_ans3.grid(row=0,column=7,sticky=tk.E)

        Numer0n_common.playFrame_label_blankrow.grid(row = 1, column = 5, columnspan = 3, sticky = tk.E)
        #ナンバー
        Numer0n_common.playFrame_button_1.grid(row=2,column=5,sticky=tk.E)
        Numer0n_common.playFrame_button_2.grid(row=2,column=6,sticky=tk.E)
        Numer0n_common.playFrame_button_3.grid(row=2,column=7,sticky=tk.E)
        Numer0n_common.playFrame_button_4.grid(row=3,column=5,sticky=tk.E)
        Numer0n_common.playFrame_button_5.grid(row=3,column=6,sticky=tk.E)
        Numer0n_common.playFrame_button_6.grid(row=3,column=7,sticky=tk.E)
        Numer0n_common.playFrame_button_7.grid(row=4,column=5,sticky=tk.E)
        Numer0n_common.playFrame_button_8.grid(row=4,column=6,sticky=tk.E)
        Numer0n_common.playFrame_button_9.grid(row=4,column=7,sticky=tk.E)
        Numer0n_common.playFrame_button_0.grid(row=5,column=5,sticky=tk.E)
        Numer0n_common.playFrame_button_back.grid(row=5,column=6,sticky=tk.E)
        Numer0n_common.playFrame_button_enter.grid(row=5,column=7,sticky=tk.E)
        Numer0n_common.playFrame_label_blankcol_r.grid(row = 0, column = 8, rowspan = 6, sticky = tk.E)
        Numer0n_common.playFrame_label_blankcol_l.grid(row = 0, column=4, rowspan = 6, sticky = tk.E)
        Numer0n_common.playFrame_button_double.grid(row=2,column=9,sticky=tk.E)
        Numer0n_common.playFrame_button_hilo.grid(row=2,column=10,sticky=tk.E)
        Numer0n_common.playFrame_button_target.grid(row=3,column=9,sticky=tk.E)
        Numer0n_common.playFrame_button_slash.grid(row=3,column=10,sticky=tk.E)
        Numer0n_common.playFrame_button_shuffle.grid(row=4,column=9,sticky=tk.E)
        Numer0n_common.playFrame_button_change.grid(row=4,column=10,sticky=tk.E)
        inputoff()
        Numer0n_common.playFrame.pack()
        show_screen_playFrame()
        return play_multi("Client")
def show_screen_playFrame():
    result_update()
    Numer0n_common.playFrame.update()

def server_Error():
    print("接続できません")
    Numer0n_common.errorFrame.pack()
    Numer0n_common.errorFrame_label_title.pack(pady=(200,20))
    Numer0n_common.errorFrame_button_select.pack()
    return

def show_screen_multiselectFrame(Frame):
    if Frame ==Numer0n_common.serverFrame:
        global is_recv
        is_recv = False
        event.set()
        event.clear()
    # ウィジェットの配置
    Numer0n_common.multiselectFrame.pack()
    Numer0n_common.multiselectFrame_label_title.pack(pady=(190,20))
    Numer0n_common.multiselectFrame_button_server.pack(pady=(0, 20))
    Numer0n_common.multiselectFrame_button_client.pack(pady=(0, 20))
    Numer0n_common.multiselectFrame_button_back.pack()
    Frame.pack_forget()

def  client_main(ip):
    try:
        global addr,sock,oppoment_name
        addr = (ip,PORT)
        clientFrame_button_enter.destroy()
        Numer0n_common.clientFrame.pack_forget()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        Numer0n_common.infomationFrame_label_title.pack(pady=(200,20))
        Numer0n_common.infomationFrame.pack()
        Numer0n_common.root.update()
        sock.sendto(Numer0n_common.name.encode("utf-8"), addr)
        sock.settimeout(5)
        data = sock.recv(BUFSIZE)
        oppoment_name = data.decode('utf8', 'ignore')
        print(oppoment_name)
    except TimeoutError:
        Numer0n_common.infomationFrame.pack_forget()
        server_Error() 
        return
    except Exception as ex:
        print('Exception: time={}, desc={}'.format(datetime.datetime.now(), ex))
        print("接続できません")
        Numer0n_common.infomationFrame.pack_forget()
        Numer0n_common.errorFrame.pack()
        Numer0n_common.errorFrame_label_title.pack(pady=(200,20))
        Numer0n_common.errorFrame_button_select.pack()
        return
    flont = threading.Thread(target=client_flont())
    flont.setDaemon(True)
    flont.start()
    client_con = threading.Thread(target=client_connect())
    client_con.setDaemon(True)
    client_con.start()
    #スレッドの生成


def client_flont():
    Numer0n_common.infomationFrame.pack_forget()
    Numer0n_common.history="相手が入力しています。今しばらくお待ちください\n"
    event.set()
    input_number("clientFrame")


#接続要求_Client
def client_connect():
        while True:
            # サーバからのメッセージの受信
            sock.settimeout(31)
            data = sock.recv(BUFSIZE)
            print(data.decode('utf-8'))
            if data.decode('utf-8') == "server_OK":
                Numer0n_common.history = "30秒以内にナンバーを入力してください\n"
                result_update()
                break
            event.wait()
            
            
def __init__(self):
    Numer0n_common.show_screen_multiselectFrame(Numer0n_common.selectFrame)

def inputoff():
    Numer0n_common.playFrame_button_back["state"]="disabled"
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
    Numer0n_common.skilllos()


def inputon():
    Numer0n_common.playFrame_button_back["state"]="active"
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
    Numer0n_common.skillok()