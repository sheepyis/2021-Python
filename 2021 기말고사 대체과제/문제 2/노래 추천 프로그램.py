from tkinter import *
from tkinter import messagebox
import random
import pygame

root=Tk()
root.title("오늘의 추천 곡")
root.geometry("800x700+500+300")

pygame.init()
pygame.mixer.music.load("Loote-85.mp3")
pygame.mixer.music.play(0)
    
    

def 재생(event):
    mixer.music.play(-1)
    lb_update()

def 정지(event):
    mixer.music.stop()

def lb_update():
    global index
    lb_string.set(ls_music[index])

def 팝송():
    pop=["Birthday","Goodbyes","Liability","85%"]
    if random.choice(pop)=="Birthday":
        la2.configure(text="Birthday - Anne-Marie", font="고딕 12")
        la3.configure(image=photo1)
        la4.configure(text="오늘의 팝송 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: Don't Play(2021.01.15)")
    elif random.choice(pop)=="Goodbyes":
        la2.configure(text="Goodbyes - Post Malon", font="고딕 12")
        la3.configure(image=photo2)
        la4.configure(text="오늘의 팝송 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: Goodbyes(2019.07.04)")
    elif random.choice(pop)=="Liability":
        la2.configure(text="Liability - Lorde", font="고딕 12")
        la3.configure(image=photo3)
        la4.configure(text="오늘의 팝송 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: Melodrama(2017.06.16)")
    elif random.choice(pop)=="85%":
        la2.configure(text="85% - Loote", font="고딕 12")
        la3.configure(image=photo4)
        la4.configure(text="오늘의 팝송 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: lost(2019.06.14)")

def 케이팝():
    kpop=["우아하게","Universe","Dynamite","으르렁"]
    if random.choice(kpop)=="우아하게":
        la2.configure(text="우아하게 - TWICE", font="고딕 12")
        la3.configure(image=photo5)
        la4.configure(text="오늘의 케이팝 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: THE STORY BEGINS(2015.10.20)")
    elif random.choice(kpop)=="Universe":
        la2.configure(text="Universe - 민현(뉴이스트)", font="고딕 12")
        la3.configure(image=photo6)
        la4.configure(text="오늘의 케이팝 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: Single 'Universe'(2019.04.03)")
    elif random.choice(kpop)=="Dynamite":
        la2.configure(text="Dynamite - 방탄소년단", font="고딕 12")
        la3.configure(image=photo7)
        la4.configure(text="오늘의 케이팝 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: Dynamite(DayTime Version(2020.08.21)")
    elif random.choice(kpop)=="으르렁":
        la2.configure(text="으르렁 - EXO", font="고딕 12")
        la3.configure(image=photo8)
        la4.configure(text="오늘의 케이팝 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: The 1st Album 'XOXO(Kiss&Hug)' Repackage(2013.08.05)")

def 발라드():
    ballad=["신촌을 못가","바람이 불었으면 좋겠어","초록빛","눈사람"]
    if random.choice(ballad)=="신촌을 못가":
        la2.configure(text="신촌을 못가 - 포스트맨", font="고딕 12")
        la3.configure(image=photo9)
        la4.configure(text="오늘의 발라드 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: 신촌을 못가(2013.01.21)")
    elif random.choice(ballad)=="바람이 불었으면 좋겠어":
        la2.configure(text="바람이 불었으면 좋겠어 - 길구봉구", font="고딕 12")
        la3.configure(image=photo10)
        la4.configure(text="오늘의 발라드 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: 바람이 불었으면 좋겠어(2014.01.03)")
    elif random.choice(ballad)=="초록빛":
        la2.configure(text="초록빛 - 폴킴", font="고딕 12")
        la3.configure(image=photo11)
        la4.configure(text="오늘의 발라드 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: 초록빛(2019.01.17)")
    elif random.choice(ballad)=="눈사람":
        la2.configure(text="눈사람 - 정승환", font="고딕 12")
        la3.configure(image=photo12)
        la4.configure(text="오늘의 발라드 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: 그리고 봄(2018.02.19)")

def 랩():
    rap=["사람","우리서로사랑하지는말자","Achoo","시차"]
    if random.choice(rap)=="사람":
        la2.configure(text="사람 - 지코", font="고딕 12")
        la3.configure(image=photo13)
        la4.configure(text="오늘의 랩/힙합 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: THINKING Part.1(2019.09.30)")
    elif random.choice(rap)=="우리서로사랑하지는말자":
        la2.configure(text="우리서로사랑하지는말자 - 기리보이", font="고딕 12")
        la3.configure(image=photo14)
        la4.configure(text="오늘의 랩/힙합 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: 영화같게(2020.10.04)")
    elif random.choice(rap)=="Achoo":
        la2.configure(text="Achoo - 미란이", font="고딕 12")
        la3.configure(image=photo15)
        la4.configure(text="오늘의 랩/힙합 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: 쇼미더머니 9 Episode 3(2020.12.05)")
    elif random.choice(rap)=="METEOR":
        la2.configure(text="시차 - 우원재", font="고딕 12")
        la3.configure(image=photo16)
        la4.configure(text="오늘의 랩/힙합 추천 곡은?", font="고딕 15 bold")
        messagebox.showinfo("곡 정보","앨범명: 시차(We Are)(2017.09.04)")

photo0=PhotoImage(file="그림자리.png")
photo1=PhotoImage(file="1.png")
photo2=PhotoImage(file="2.png")
photo3=PhotoImage(file="3.png")
photo4=PhotoImage(file="4.png")
photo5=PhotoImage(file="5.png")
photo6=PhotoImage(file="6.png")
photo7=PhotoImage(file="7.png")
photo8=PhotoImage(file="8.png")
photo9=PhotoImage(file="9.png")
photo10=PhotoImage(file="10.png")
photo11=PhotoImage(file="11.png")
photo12=PhotoImage(file="12.png")
photo13=PhotoImage(file="13.png")
photo14=PhotoImage(file="14.png")
photo15=PhotoImage(file="15.png")
photo16=PhotoImage(file="16.png")

la1=Label(root, text="<오늘의 추천 곡>", font="고딕 20")
la2=Label(root, text="")
la3=Label(root, image=photo0)
la4=Label(root, text="")


bt1=Button(root, text="팝송", bg="yellow", command=팝송, width=30)
bt2=Button(root, text="케이팝", bg="pink", command=케이팝, width=30)
bt3=Button(root, text="발라드", bg="skyblue", command=발라드, width=30)
bt4=Button(root, text="랩/힙합", bg="lightgreen", command=랩, width=30)
bt5=Button(root, text="재생", bg="orange", width=13)
bt6=Button(root, text="정지", bg="wheat", width=13)

la1.place(x=290, y=20)
la3.place(x=380, y=80)
la2.place(x=60, y=450)
la4.place(x=60, y=400)
bt1.place(x=60, y=100)
bt2.place(x=60, y=150)
bt3.place(x=60, y=200)
bt4.place(x=60, y=250)
bt5.place(x=60, y=500)
bt6.place(x=190, y=500)

bt5.bind("<Button-1>", 재생)
bt6.bind("<Button-1>", 정지)

root.mainloop()
