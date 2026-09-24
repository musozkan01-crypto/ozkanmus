# -*- coding: utf-8 -*-
"""ozkanmus.com.tr icin OG (link onizleme) gorseli + favicon ikonu uretir."""
from PIL import Image, ImageDraw, ImageFont
import os
OUT = r"C:\Nevas Destek"

def font(sz, bold=True):
    for p in [r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
              r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()

def rrect(d, xy, r, fill):
    d.rounded_rectangle(xy, radius=r, fill=fill)

# ---------- OG IMAGE 1200x630 ----------
W,H=1200,630
img=Image.new("RGB",(W,H),(9,17,31))
d=ImageDraw.Draw(img)
# kirmizi glow (sag ust) - basit radial taklit
glow=Image.new("RGB",(W,H),(9,17,31)); gd=ImageDraw.Draw(glow)
for i,rad in enumerate(range(520,0,-26)):
    a=int(36*(1-i/20)) if i<20 else 0
    col=(min(9+ a*3,90), 17+a//3, 31+a//4)
    gd.ellipse([W-260-rad, -180-rad, W-260+rad, -180+rad], fill=col)
img=Image.blend(img,glow,0.5); d=ImageDraw.Draw(img)
# ince grid cizgileri
for x in range(0,W,60): d.line([(x,0),(x,H)],fill=(255,255,255,6) and (18,28,44),width=1)
for y in range(0,H,60): d.line([(0,y),(W,y)],fill=(18,28,44),width=1)
# logo kare ÖM (kirmizi)
lx,ly,ls=80,70,96
rrect(d,[lx,ly,lx+ls,ly+ls],24,(220,38,38))
rrect(d,[lx,ly,lx+ls,ly+int(ls*0.5)],24,(239,68,68))
fom=font(46); t="ÖM"; bb=d.textbbox((0,0),t,font=fom)
d.text((lx+(ls-(bb[2]-bb[0]))/2, ly+(ls-(bb[3]-bb[1]))/2-bb[1]),t,font=fom,fill=(255,255,255))
d.text((lx+ls+22, ly+16),"ÖZKAN MUŞ",font=font(30),fill=(255,255,255))
d.text((lx+ls+22, ly+56),"IT Uzmanı · Yazılım Geliştirici",font=font(22,False),fill=(148,163,184))
# ana baslik
d.text((80,250),"Kurumsal Yazılım",font=font(78),fill=(255,255,255))
d.text((80,338),"& ERP Entegrasyon",font=font(78),fill=(239,68,68))
# alt aciklama
d.text((80,448),"Web üzerinden canlı veri · Nebim V3 / SQL · e-Dönüşüm · Özel paneller",font=font(26,False),fill=(203,213,225))
# alt pill: site adresi
pill="ozkanmus.com.tr"; fp=font(26); pb=d.textbbox((0,0),pill,font=fp)
pw=(pb[2]-pb[0])+44
rrect(d,[80,520,80+pw,572],26,(220,38,38))
d.text((80+22,520+ (52-(pb[3]-pb[1]))/2 - pb[1]),pill,font=fp,fill=(255,255,255))
img.save(os.path.join(OUT,"og.png"),"PNG")
print("og.png uretildi", img.size)

# ---------- ICON 512x512 (apple-touch / png favicon) ----------
S=512; ic=Image.new("RGB",(S,S),(127,29,29)); idr=ImageDraw.Draw(ic)
for y in range(S):
    t=y/S; r=int(220-(220-127)*t); g=int(38-(38-29)*t); b=int(38-(38-29)*t)
    idr.line([(0,y),(S,y)],fill=(r,g,b))
fi=font(300); t="Ö"; bb=idr.textbbox((0,0),t,font=fi)
idr.text(((S-(bb[2]-bb[0]))/2 - bb[0], (S-(bb[3]-bb[1]))/2 - bb[1]),t,font=fi,fill=(255,255,255))
ic.save(os.path.join(OUT,"icon.png"),"PNG")
print("icon.png uretildi", ic.size)
