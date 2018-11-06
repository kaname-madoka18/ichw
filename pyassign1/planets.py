def main():
    import turtle,math
    Sun=turtle.Pen()
    Sun.dot(20,'yellow')
    Sun.hideturtle()

    Mercury=turtle.Pen()
    Venus=turtle.Pen()
    Earth=turtle.Pen()
    Mars=turtle.Pen()
    Jupiter=turtle.Pen()
    Saturn=turtle.Pen()
    names=Mercury,Venus,Earth,Mars,Jupiter,Saturn
    colors='blue','green','red','black','brown','violet'
    a=[0.3,0.7,1.3,2,2.9,4]
    e=0.5,0.2,0.3,0.1,0.25,0.3
    T=[]
    b=[]
    c=[]
    degree=[]
    for i in range(6):
        names[i].pencolor(colors[i])
        names[i].speed(0)
        names[i].shape('circle')
        names[i].shapesize((i+1)/5)
        names[i].pensize(((i+1)**2)/4)
        names[i].delay=0
        a[i]=100*a[i]
        c.append(a[i]*e[i])
        b.append(a[i]*math.sqrt(1-e[i]**2))
        T.append(30*1.6**i)
        degree.append(math.pi*2/T[i])
        names[i].penup()
        names[i].goto(a[i]-c[i],0)
        names[i].pendown()
    for i in range(1,1000):
        for k in range(6):
            names[k].goto(a[k]*math.cos(i*degree[k])-c[k],b[k]*math.sin(i*degree[k]))

if __name__=='__main__':
    main()




