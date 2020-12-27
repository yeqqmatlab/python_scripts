import turtle


def draw(strength):
    if strength > 0:
        turtle.fd(strength)
        turtle.rt(20)  # 右转20°
        draw(strength - 5)  # 每一节树枝比前一节短5

        turtle.lt(40)  # 之前右转了20°，所以这里要左转40°。
        draw(strength - 5)
        if (strength < 25):
            turtle.pencolor("green")  # 如果树枝的长度小于25，那么就设置画笔的颜色为绿色
        turtle.rt(20)
        turtle.backward(strength)  # 放回
        turtle.pencolor("black")

if __name__ == '__main__':
    strenght = 80  # 设置树的长度
    turtle.penup()
    turtle.goto(-50, -100)  # 向下移动画笔
    turtle.pendown()
    
    # turtle.letf(90)  # 开始画笔的方向为朝右，转到向上
    draw(strenght)
    turtle.exitonclick()  # 设置画完后不立即结束程序