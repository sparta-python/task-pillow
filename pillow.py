from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

image_path = "image/konjikido_01.jpg"
konjiki = Image.open(image_path)
text = "平泉 最高"

konjiki_resize = konjiki.resize((1000, 1000))

font_path = "/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc"
font_size = 100  # 文字の大きさ
color = (255, 255, 255)  # 文字の色
font = ImageFont.truetype(font_path, font_size)  # フォントの指定
draw = ImageDraw.Draw(konjiki_resize)
(font_w, font_h), (offset_x, offset_y) = font.font.getsize(text)
img_w, img_h = konjiki_resize.size
pos = ((img_w - font_w) / 2, (img_h - font_h) / 2)

draw.text(pos, text, font=font, fill=color)
konjiki_resize.save("image/konjiki_resize_02.jpg")
