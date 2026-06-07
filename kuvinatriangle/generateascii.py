import colorsys, math, sys, numpy as np

def generateKuvinaTri(sz: 1025, mod):
    # calculate hues for color scheme
    colorlist = [colorsys.hsv_to_rgb(i / (mod-1), 1, 1) for i in range(mod-1)]
    colorlist = [(int(i[0]*255), int(i[1]*255), int(i[2]*255)) for i in colorlist]
    colorlist = [(0, 0, 0)] + colorlist
    #print(colorlist)
    # arraying
    row = [1]
    siz = 2*sz-1
    asciitriangl = np.full((sz-1, siz), "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee") # make base asciimage
    # loop and put pixels
    for q in range(0,sz-1):
        rowpad = [0]*((siz-len(row))//2) + row + [0]*((siz-len(row))//2)
        for p in range(len(rowpad)):
            # triangl.putpixel((p, q), colorlist[rowpad[p]])
            asciitriangl[q, p] = f"\033[38;5;0m\033[48;2;{str(colorlist[rowpad[p]][0])};{str(colorlist[rowpad[p]][1])};{str(colorlist[rowpad[p]][2])}m{str(rowpad[p])*(sys.argv[-1] == "-n") + " "*(sys.argv[-1] != "-n")}\033[0m"
            #print(asciitriangl[p, q])
            #print((p, q), rowpad[p], rowpad)
        # vv prepare the row list for the next row
        rrow = [0, 0] + row + [0, 0]
        #print(rowpad, len(rowpad))
        row = [((rrow[k-1]+rrow[k]+rrow[k+1]))%mod for k in range(1,len(rrow)-1)]
    return asciitriangl

triangl = generateKuvinaTri(129, int(sys.argv[1]))
for q in range(0,triangl.shape[0]):
    print("".join(triangl[q]))