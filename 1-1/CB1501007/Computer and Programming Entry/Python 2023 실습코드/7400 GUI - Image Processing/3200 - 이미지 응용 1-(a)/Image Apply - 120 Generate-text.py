



root = Tk()
root.title("CAPTCHAed Text")
root.geometry("600x500+300+300")

# font = ImageFont.truetype("Arial-Bold.ttf",14)
xfont= ImageFont.truetype("NanumMyeongjo.ttf",24)
img  = Image.new("RGBA", (500,250),(155,255,155))
draw = ImageDraw.Draw(img)
draw.text((50, 60), " 이것은 진짜 한글이다"+ "\n다음 문장",fill="orange",font=xfont)
draw.line((10,20, 250,300), fill="black", width=3)
draw.line((210,20, 20,340), fill="black", width=3)


iobj = ImageTk.PhotoImage( img )
mylabel = Label( root, image=iobj)
mylabel.place( x = 100 , y=100)

root.mainloop( )
