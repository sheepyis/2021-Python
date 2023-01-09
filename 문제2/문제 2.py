from tkinter import *
from tkinter import messagebox
import random

root=Tk()
root.title("오늘의 메뉴 이미지 보이기")
root.geometry("480x300+500+300")

def 메뉴():
    menu=["떡볶이","계란말이","미역국","고기만두"]
    if random.choice(menu)=="떡볶이":
        la2.configure(text="선택 메뉴: 떡볶이")
        la4.configure(image=photo1)
        messagebox.showinfo("준비 재료","떡 200g, 사각어묵 1장, 물 300ml, 고추장 1.5큰술(45g),고춧가루 1/2큰술, 설탕 2큰술, 대파 1/4대, 고향의 맛 1/4큰술, 식용유 1/2큰술")
    elif random.choice(menu)=="계란말이":
        la2.configure(text="선택 메뉴: 계란말이")
        la4.configure(image=photo2)
        messagebox.showinfo("준비 재료","달걀 3개, 당근 1/4개, 양파 1/4개, 대파 1/4개, 소금 1작은술, 후추 조금")
    elif random.choice(menu)=="미역국":
        la2.configure(text="선택 메뉴: 미역국")
        la4.configure(image=photo3)
        messagebox.showinfo("준비 재료","건 미역 60g, 쇠고기 120g, 참기름 2작은술, 다진 마늘 1/2작은술, 국 간장 2큰술")
    elif random.choice(menu)=="고기만두":
        la2.configure(text="선택메뉴: 고기만두")
        la4.configure(image=photo4)
        messagebox.showinfo("준비 재료","돼지고기 뒷다리 다짐육 300g, 소고기 다짐육 600g, 두부 한모 300g, 표고버섯 3개, 부추(500원 동전 사이즈만큼),숙주 150g, 당면(500원 동전 사이즈만큼), 만두피 270g 3개, 간장 3스푼, 다진 마늘 2스푼, 설탕 2스푼, 소금 1스푼, 참기름 1스푼, 후추 조금")
        
photo1=PhotoImage(file="떡볶이.png")
photo2=PhotoImage(file="계란말이.png")
photo3=PhotoImage(file="미역국.png")
photo4=PhotoImage(file="고기만두.png")
photo5=PhotoImage(file="그림자리.png")

la1=Label(root, text="<오늘의 메뉴 이미지 보이기>", font="고딕 20" )
la2=Label(root, text="메뉴 미정")
la3=Label(root, text="요리사: 2171339 양인서", fg="blue")
la4=Label(root, image=photo5)
bt=Button(root, text="오늘의 메뉴 선택하기", bg="yellow", command=메뉴)

la1.place(x=55, y=30)
la2.place(x=60, y=100)
bt.place(x=60, y=150)
la3.place(x=60, y=200)
la4.place(x=260, y=90)

root.mainloop()
