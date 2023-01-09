import turtle, random, time

s=turtle.Screen()
t1=turtle.Turtle()
t1.ht()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t4.speed(10)
t4.ht()
t5=turtle.Turtle()
t5.ht()
t6=turtle.Turtle()
t6.ht()
t7=turtle.Turtle()
t7.ht()

turtle.colormode(255)
turtle.bgpic("sky.png")
t1.hideturtle()
t1.up()
t1.goto(380,-360)
t1.down()
t1.write("2171339 양인서")

t6.up()
t6.goto(-410,50)
t6.down()
t6.write("입력문장쓰기", font=("고딕", 12))
t2.up()
t2.goto(-200,50)
image1="1.gif"
s.addshape(image1)
t2.shape(image1)

t7.up()
t7.goto(320,50)
t7.down()
t7.write("랜덤 별 그리기", font=("고딕", 12))
t3.up()
t3.goto(200,50)
image2="2.gif"
s.addshape(image2)
t3.shape(image2)

        
def 객체1(x,y):
    입력=turtle.textinput("단어입력","단어를 입력하세요")
    t4.clear()
    t2.ht()
    t3.ht()
    t6.clear()
    t7.clear()
    t5.up()
    t5.goto(-200,200)
    입력.split(' ')
    t5.write((입력), font=("고딕", 20))


def star(length):
        for n in range(5):
            t4.forward(length)
            t4.left(144)
        
def s_draw(x,y):
    for a in range(20):
        x=random.randint(-300,300)
        y=random.randint(-300,300)
        t4.up()
        t4.goto(x,y)
        t4.down()
        t4.begin_fill()
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        t4.color(r,g,b)
        star(random.randint(20,40))
        t4.end_fill()
        
t2.onclick(객체1)
t3.onclick(s_draw)

s.mainloop()
