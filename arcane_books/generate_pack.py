#!/usr/bin/env python3
"""Generate the bundled custom-item-model pack without third-party libraries."""
from pathlib import Path
import json, struct, zlib, zipfile, math

root=Path(__file__).parent
resources=root.parent
files={"pack.mcmeta":json.dumps({"pack":{"description":"ArcaneBooks Magic Books - Minecraft 1.21.11","min_format":75,"max_format":75}}).encode()}
colors={"fire":((219,62,35),(255,213,65)),"frost":((50,151,225),(205,240,255)),"storm":((120,55,185),(251,228,58)),"heal":((42,163,91),(235,248,153))}

def png(width,height,rgba):
    def chunk(tag,body):
        return struct.pack(">I",len(body))+tag+body+struct.pack(">I",zlib.crc32(tag+body)&0xffffffff)
    scan=b"".join(b"\x00"+bytes(sum((list(px) for px in rgba[y*width:(y+1)*width]),[])) for y in range(height))
    return b"\x89PNG\r\n\x1a\n"+chunk(b"IHDR",struct.pack(">IIBBBBB",width,height,8,6,0,0,0))+chunk(b"IDAT",zlib.compress(scan,9))+chunk(b"IEND",b"")

for name,(base,accent) in colors.items():
    pixels=[]
    for y in range(32):
        for x in range(32):
            p=(0,0,0,0)
            if 5<=x<=27 and 4<=y<=27:
                p=(*base,255) if 9<=x<=25 and 6<=y<=24 else (37,25,45,255)
                if x in (8,25) or y in (6,24):p=(*accent,255)
                if 13<=x<=22 and 10<=y<=21 and (x in (13,22) or y in (10,21)):p=(*accent,255)
                if name=="fire" and (abs(x-18)*2+abs(y-16)<6):p=(*accent,255)
                if name=="frost" and ((x==18 and 12<=y<=19) or (y==16 and 14<=x<=22) or (abs(x-18)==abs(y-16) and 14<=x<=22)):p=(*accent,255)
                if name=="storm" and ((y in (13,14) and 17<=x<=21) or (y in (15,16) and 15<=x<=19) or (y in (17,18) and 16<=x<=18)):p=(*accent,255)
                if name=="heal" and ((x in (17,18,19) and 12<=y<=20) or (y in (15,16,17) and 14<=x<=22)):p=(*accent,255)
            pixels.append(p)
    files[f"assets/arcane_books/textures/item/{name}_book.png"]=png(32,32,pixels)
    files[f"assets/arcane_books/models/item/{name}_book.json"]=json.dumps({"parent":"minecraft:item/generated","textures":{"layer0":f"arcane_books:item/{name}_book"}}).encode()
    files[f"assets/arcane_books/items/{name}_book.json"]=json.dumps({"model":{"type":"minecraft:model","model":f"arcane_books:item/{name}_book"}}).encode()

files["pack.png"]=files["assets/arcane_books/textures/item/storm_book.png"]
output=resources/"ArcaneBooks-ResourcePack.zip"
with zipfile.ZipFile(output,"w",zipfile.ZIP_DEFLATED) as z:
    for filename,data in files.items():z.writestr(filename,data)
print("Created",output)
