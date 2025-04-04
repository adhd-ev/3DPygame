def rgbs2hex(rgb : tuple):
    r=f"0{hex(rgb[0])[2:]}" if len(hex(rgb[0])[2:])==1 else hex(rgb[0])[2:]
    g=f"0{hex(rgb[1])[2:]}" if len(hex(rgb[1])[2:])==1 else hex(rgb[1])[2:]
    b=f"0{hex(rgb[2])[2:]}" if len(hex(rgb[2])[2:])==1 else hex(rgb[2])[2:]
    return r+g+b

def rgb2hex(r,g,b):
    r=f"0{hex(r)[2:]}" if len(hex(r)[2:])==1 else hex(r)[2:]
    g=f"0{hex(g)[2:]}" if len(hex(g)[2:])==1 else hex(g)[2:]
    b=f"0{hex(b)[2:]}" if len(hex(b)[2:])==1 else hex(g)[2:]
    return r+g+b

def hex2rgb(hex : str):
    if hex.startswith("#"): hex=hex[1:]
    col = (
        int(f"0x{hex[:2]}",16),
        int(f"0x{hex[2:4]}",16),
        int(f"0x{hex[4:6]}",16)
    )
    return col
