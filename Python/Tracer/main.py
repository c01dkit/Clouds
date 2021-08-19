
import os
import random
import time
import tkinter
import threading,datetime

def show_end():
    window = tkinter.Tk()
    # width = window.winfo_screenwidth()
    # height = window.winfo_screenheight()
    # window.geometry(f'{width//2}x{height//2}')
    window.state('zoomed')
    window.configure(bg=f'#{random.randint(0,16777215):06x}')
    # word = tkinter.Label(window,text='时间到！',font=('华文行楷',20),anchor='center')
    # word.pack()
    window.mainloop()


def create_task():
    file = open('log.txt', 'a+', encoding='utf-8')

    while True:
        task_name = input('请输入要做的任务名\t')
        if len(task_name) > 0:
            break

    while True:
        try:
            time_expected = int(input('请输入预计完成时间（分钟）\t'))*60
            break
        except:
            pass

    timer = threading.Timer(time_expected,show_end)
    timer.start()
    start = datetime.datetime.now()

    while True:
        end_task = input('任务已启动。完成后请输入 finish 并按回车\t')
        if end_task == 'finish':
            timer.cancel()
            break
        elif end_task == 'time':
            print(f'已进行{datetime.datetime.now()-start}')

    end = datetime.datetime.now()
    cost = end - start
    log = f'{start:%Y-%m-%d %H:%M:%S}<>计划完成{task_name}<>计划用时{time_expected//60}分钟<>实际用时{cost}'
    print(log.replace('<>',' '))
    print(log,file=file)
    file.close()

if __name__ == '__main__':
    create_task()
