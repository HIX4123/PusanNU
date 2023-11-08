# configuration
title = "KwonMG Office"
telephone = "010-4482-1947"
email = "rnjsalsrb6666@naver.com"
address = "푸산대학교"
bgcolor = "black"
fontcolor = "white"
transparentcolor = "red"
window_size = (1280, 720)
allow_unclicking_limit = 30

# module settings
from datetime import datetime
from threading import Thread
from time import time
from tkinter import (
    BOTTOM,
    LEFT,
    NE,
    NW,
    RAISED,
    RIGHT,
    TOP,
    Button,
    Checkbutton,
    Entry,
    Frame,
    IntVar,
    Label,
    PhotoImage,
    Tk,
)
from tkinter.font import Font
from tkinter.messagebox import showerror

# window initialization
window = Tk()
window.configure(background=bgcolor)
window.geometry(
    f"{window_size[0]}x{window_size[1]}+{(window.winfo_screenwidth()-window_size[0])//2}+{(window.winfo_screenheight()-window_size[1])//2}"
)
window.resizable(True, True)
window.title(title)


# font config
class Font_Families:
    title = Font(family="Helvetica", size=24, weight="bold")
    paragraph = Font(family="Dotum", size=12)


# 영화 등록
class Movies:
    try:
        movie1 = {"title": "Wall-E", "image": PhotoImage(file="img/wall-e.png")}
    except:
        pass
    try:
        movie2 = {"title": "엑시트", "image": PhotoImage(file="img\Exit.png")}
    except:
        pass
    try:
        movie3 = {
            "title": "이별의 아침에 약속의 꽃을 장식하자",
            "image": PhotoImage(file="img\MAQUIA.png"),
        }
    except:
        pass


# 구획 나누기용 Frame들
class Masters:
    header = Frame(master=window, bg=transparentcolor)
    customer_info = Frame(master=window, bg=bgcolor)
    tickets_info = Frame(master=window, bg=bgcolor)
    purchase = Frame(master=window, bg=bgcolor)
    footer = Frame(master=window, bg=transparentcolor)


# KwonMG Office
class Title:
    master = Frame(master=Masters.header, bg=bgcolor)

    label = Label(
        master=master,
        text="KwonMG Office",
        fg=fontcolor,
        bg=transparentcolor,
        font=Font_Families.title,
    )


# 이름:
class Name:
    master = Frame(master=Masters.customer_info, bg=bgcolor)

    label = Label(
        master=master,
        text="이름:",
        fg=fontcolor,
        bg=bgcolor,
        font=Font_Families.paragraph,
    )

    entry = Entry(master=master)


# 전화번호:
class Phone:
    master = Frame(master=Masters.customer_info, bg=bgcolor)

    label = Label(
        master=master,
        text="전화번호:",
        fg=fontcolor,
        bg=bgcolor,
        font=Font_Families.paragraph,
    )

    entry = Entry(master=master)


# "재학 중" Checkbutton Toggle variation
is_student = IntVar()


# "재학 중" Checkutton Toggle Event
def toggle_student():
    if is_student.get():
        Student_number.master.pack(side=TOP, anchor=NE)
        Student_number.label.pack(side=LEFT)
        Student_number.entry.pack(side=LEFT)
    else:
        Student_number.master.pack_forget()
        Student_number.label.pack_forget()
        Student_number.entry.pack_forget()


# 재학 중 버튼
class Is_student:
    master = Frame(master=Masters.customer_info, bg=bgcolor)

    checkbutton = Checkbutton(
        master=master,
        variable=is_student,
        text="재학 중",
        font=Font_Families.paragraph,
        command=lambda: toggle_student(),
    )


# 학번:
class Student_number:
    master = Frame(master=Masters.customer_info, bg=bgcolor)

    label = Label(
        master=master,
        text="학번:",
        fg=fontcolor,
        bg=bgcolor,
        font=Font_Families.paragraph,
    )

    entry = Entry(master=master)


# 영화 티켓 수
amount1 = IntVar()
amount1.set(0)

amount2 = IntVar()
amount2.set(0)

amount3 = IntVar()
amount3.set(0)


def plus(x):
    x.set(x.get() + 1) if x.get() < 5 else None


def minus(x):
    x.set(x.get() - 1) if x.get() > 0 else None


class Ticket1:
    master = Frame(master=Masters.tickets_info, bg=bgcolor)
    try:
        image = Label(master=master, image=Movies.movie1["image"])
    except:
        image = Frame(master=master, bg=transparentcolor)
    finally:
        image.configure(width=300, height=400)

    label = Label(
        master=master,
        text=Movies.movie1["title"],
        fg=fontcolor,
        bg=bgcolor,
        font=Font_Families.paragraph,
    )

    buttons = Frame(master=master, bg=bgcolor)

    add = Button(
        master=buttons,
        text="▲",
        bd=4,
        fg=fontcolor,
        bg=bgcolor,
        command=lambda: plus(amount1),
    )

    number = Label(
        master=buttons,
        textvariable=amount1,
        fg=fontcolor,
        bg=bgcolor,
        font=Font_Families.paragraph,
    )

    subtract = Button(
        master=buttons,
        text="▼",
        bd=4,
        fg=fontcolor,
        bg=bgcolor,
        command=lambda: minus(amount1),
    )


class Ticket2:
    master = Frame(master=Masters.tickets_info, bg=bgcolor)

    try:
        image = Label(master=master, image=Movies.movie2["image"])
    except:
        image = Frame(master=master, bg=transparentcolor)
    finally:
        image.configure(width=300, height=400)

    label = Label(
        master=master,
        text=Movies.movie2["title"],
        fg=fontcolor,
        bg=bgcolor,
        font=Font_Families.paragraph,
    )

    buttons = Frame(master=master, bg=bgcolor)

    add = Button(
        master=buttons,
        text="▲",
        bd=4,
        relief=RAISED,
        fg=fontcolor,
        bg=bgcolor,
        command=lambda: plus(amount2),
    )

    number = Label(
        master=buttons,
        textvariable=amount2,
        fg=fontcolor,
        bg=bgcolor,
        font=Font_Families.paragraph,
    )

    subtract = Button(
        master=buttons,
        text="▼",
        bd=4,
        relief=RAISED,
        fg=fontcolor,
        bg=bgcolor,
        command=lambda: minus(amount2),
    )


class Ticket3:
    master = Frame(master=Masters.tickets_info, bg=bgcolor)

    try:
        image = Label(master=master, image=Movies.movie3["image"])
    except:
        image = Frame(master=master, bg=transparentcolor)
    finally:
        image.configure(width=300, height=400)

    label = Label(
        master=master,
        text=Movies.movie3["title"],
        fg=fontcolor,
        bg=bgcolor,
        font=Font_Families.paragraph,
    )

    buttons = Frame(master=master, bg=bgcolor)

    add = Button(
        master=buttons,
        text="▲",
        bd=4,
        relief=RAISED,
        fg=fontcolor,
        bg=bgcolor,
        command=lambda: plus(amount3),
    )

    number = Label(
        master=buttons,
        textvariable=amount3,
        fg=fontcolor,
        bg=bgcolor,
        font=Font_Families.paragraph,
    )

    subtract = Button(
        master=buttons,
        text="▼",
        bd=4,
        relief=RAISED,
        fg=fontcolor,
        bg=bgcolor,
        command=lambda: minus(amount3),
    )


# "구매 완료" Button Click Event
def done():
    dat = {
        "name": Name.entry.get(),
        "phone": Phone.entry.get(),
        "amounts": [amount1.get(), amount2.get(), amount3.get()],
        "student_number": Student_number.entry.get(),
    }

    # 미입력 감지
    blanks = []
    if dat["name"] == "":
        blanks.append("이름")
    if dat["phone"] == "":
        blanks.append("전화번호")
    if blanks:
        showerror("ValueError", " 및 ".join(blanks) + " 항목이 입력되지 않았습니다.")
        return

    # 전화번호 처리
    phone_prefixes = [
        "010",
        "031",
        "032",
        "033",
        "041",
        "042",
        "043",
        "044",
        "051",
        "052",
        "053",
        "054",
        "055",
        "061",
        "062",
        "063",
        "064",
        "070",
    ]
    phone = dat["phone"]

    # 문자 감지
    try:
        int(phone)
    except ValueError:
        showerror("ValueError", "전화번호는 숫자만을 이용해 작성해 주십시오.")
        return

    # 번호 필터링
    if (
        phone[:3] in phone_prefixes
        or (phone[:2] == "02" and phone[2] != "1")
        or len(phone) not in [10, 11]
    ):
        showerror("ValueError", "올바르지 않은 전화번호입니다.")
        return

    # 학번 처리
    student_number = dat["student_number"]
    try:
        int(student_number)
    except ValueError:
        showerror("ValueError", "올바르지 않은 입력입니다.")
        return
    if student_number and (
        len(student_number) != 9 or int(student_number[:4]) > datetime.now().year
    ):
        showerror("ValueError", "올바르지 않은 학번입니다.")
        return

    # 파일 생성
    with open("userdat.json", "w") as userdat:
        userdat.write("{\n    ")
        userdat.write(",\n    ".join(f'"{key}": "{val}"' for key, val in dat.items()))
        userdat.write("\n}")
    with open("userdat.txt", "w") as userdat:
        userdat.write("{\n    ")
        userdat.write(",\n    ".join(f'"{key}": "{val}"' for key, val in dat.items()))
        userdat.write("\n}")


# 구매 완료
class Done:
    master = Frame(master=Masters.purchase, bg=bgcolor)

    button = Button(
        master=master,
        text="구매 완료",
        font=Font_Families.paragraph,
        bd=4,
        relief=RAISED,
        fg=fontcolor,
        bg=bgcolor,
        command=lambda: done(),
    )


# "취소" Button Click Event
def reset():
    amount1.set(0)
    amount2.set(0)
    amount3.set(0)


# 취소
class Reset:
    master = Frame(master=Masters.purchase, bg=bgcolor)

    button = Button(
        master=master,
        text="취소",
        font=Font_Families.paragraph,
        bd=4,
        relief=RAISED,
        fg=fontcolor,
        bg=bgcolor,
        command=lambda: reset(),
    )


# 전화번호:
class Telephone:
    master = Frame(master=Masters.footer, bg=bgcolor)

    label = Label(
        master=master,
        text=f"TEL: {telephone}",
        fg=fontcolor,
        bg=transparentcolor,
        font=Font_Families.paragraph,
    )


# 이메일
class Email:
    master = Frame(master=Masters.footer, bg=bgcolor)

    label = Label(
        master=master,
        text=f"E-mail: {email}",
        fg=fontcolor,
        bg=transparentcolor,
        font=Font_Families.paragraph,
    )


# 주소
class Address:
    master = Frame(master=Masters.footer, bg=bgcolor)

    label = Label(
        master=master,
        text=f"Address: {address}",
        fg=fontcolor,
        bg=transparentcolor,
        font=Font_Families.paragraph,
    )


# Timer variation
remain_time = IntVar(value=allow_unclicking_limit)


# 우측 하단 타이머
class Time:
    master = Frame(master=Masters.footer, bg=bgcolor)

    label = Label(
        master=master,
        textvariable=remain_time,
        fg=fontcolor,
        bg=transparentcolor,
        font=Font_Families.paragraph,
    )


# 위젯 패킹
Masters.header.pack(side=TOP, fill="x")
Masters.customer_info.pack(side=TOP, anchor=NE)
Masters.tickets_info.pack()
Masters.purchase.pack()
Masters.footer.pack(side=BOTTOM, fill="x")

Title.master.pack()
Title.label.pack()

Name.master.pack(side=TOP, anchor=NE)
Name.label.pack(side=LEFT)
Name.entry.pack(side=LEFT)

Phone.master.pack(side=TOP, anchor=NE)
Phone.label.pack(side=LEFT)
Phone.entry.pack(side=LEFT)

Is_student.master.pack(side=TOP, anchor=NE)
Is_student.checkbutton.pack(side=LEFT)

Ticket1.master.pack(side=LEFT, padx=4)
Ticket1.image.pack(side=TOP)
Ticket1.label.pack(side=TOP)
Ticket1.buttons.pack(side=TOP)
Ticket1.add.pack(side=LEFT)
Ticket1.number.pack(side=LEFT)
Ticket1.subtract.pack(side=LEFT)

Ticket2.master.pack(side=LEFT, padx=4)
Ticket2.image.pack(side=TOP)
Ticket2.label.pack(side=TOP)
Ticket2.buttons.pack(side=TOP)
Ticket2.add.pack(side=LEFT)
Ticket2.number.pack(side=LEFT)
Ticket2.subtract.pack(side=LEFT)

Ticket3.master.pack(side=LEFT, padx=4)
Ticket3.image.pack(side=TOP)
Ticket3.label.pack(side=TOP)
Ticket3.buttons.pack(side=TOP)
Ticket3.add.pack(side=LEFT)
Ticket3.number.pack(side=LEFT)
Ticket3.subtract.pack(side=LEFT)

Done.master.pack(side=LEFT)
Done.button.pack(side=LEFT)

Reset.master.pack(side=LEFT)
Reset.button.pack(side=LEFT)

Telephone.master.pack(anchor=NW)
Telephone.label.pack(side=LEFT)

Email.master.pack(anchor=NW)
Email.label.pack(side=LEFT)

Address.master.pack(side=LEFT)
Address.label.pack(side=LEFT)

Time.master.pack(side=RIGHT)
Time.label.pack(side=RIGHT)

# 타이머 기준시점 variation
init = time()


# 타이머 스레드
def check_time():
    global init
    while True:
        global remain_time
        current_time = time() - init
        remain_time.set(value=allow_unclicking_limit - int(current_time))
        if current_time > allow_unclicking_limit:
            window.destroy()


Thread(target=check_time, daemon=True).start()

# init 재설정
def reset_timer(*args):
    global init
    init = time()


window.bind("<Motion>", reset_timer)
window.bind("<Any-KeyPress>", reset_timer)
window.bind("<Any-ButtonPress>", reset_timer)

window.mainloop()
