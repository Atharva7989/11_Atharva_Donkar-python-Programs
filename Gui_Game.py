from guizero import App,Text,PushButton,Picture
app=App(title="Hello World")
app.bg="yellow"
Wallpaper=Picture(app,image="farcry.jpg")
button=PushButton(app,width=30,height=1,text="Play Game")
button.bg="red"
button2=PushButton(app,width=30,height=1,text="Settings")
button2.bg="red"
button3=PushButton(app,width=30,height=1,text="Store")
button3.bg="red"
button4=PushButton(app,width=30,height=1,text="Quit")
button4.bg="red"
app.display()

