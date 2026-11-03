import fitz,io,json,os
from PIL import Image
src='/mnt/data/Ногайский_8 класс(1).pdf'; doc=fitz.open(src)
texts=[]
for i,p in enumerate(doc):
 pix=p.get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False)
 im=Image.open(io.BytesIO(pix.tobytes('png')))
 im.save(f'/mnt/data/nogay_reader/pages/{i+1:03d}.webp','WEBP',quality=83,method=4)
 texts.append(p.get_text('text')[:12000])
with open('/mnt/data/nogay_reader/search.json','w',encoding='utf-8') as f:json.dump(texts,f,ensure_ascii=False)
print('rendered',len(doc))
