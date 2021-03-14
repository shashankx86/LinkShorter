import pyshorteners


LightCyan = '\033[96m'
RED = '\u001b[31m'
YELLOW = '\33[93m'

print(RED + ' ██╗     ██╗███╗   ██╗██╗  ██╗███████╗██╗  ██╗ ██████╗ ██████╗ ████████╗███████╗██████╗ ')
print(RED + ' ██║     ██║████╗  ██║██║ ██╔╝██╔════╝██║  ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗')
print(RED + ' ██║     ██║██╔██╗ ██║█████╔╝ ███████╗███████║██║   ██║██████╔╝   ██║   █████╗  ██████╔╝')
print(RED + ' ██║     ██║██║╚██╗██║██╔═██╗ ╚════██║██╔══██║██║   ██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗')
print(RED + ' ███████╗██║██║ ╚████║██║  ██╗███████║██║  ██║╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║')
print(RED + ' ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝')

print(RED + 'Note:' + YELLOW + "Type --help for help")
loopx = True

while loopx:

    try:
        link = input(LightCyan + '[?] ' + YELLOW + 'Enter the link : ' + RED)
        if link == "--Quit":
            break
        elif link == "--quit":
            break
        elif link == "--Help":
            print("##########################################")
            print("#        --Quit to quit program          #")
            print("#       --Con to restart program         #")
            print("##########################################")
            continue
        elif link == "--help":
            print("##########################################")
            print("#        --Quit to quit program          #")
            print("#       --Con to restart program         #")
            print("##########################################")
            continue
        elif link == "--Con":
            continue
        res = link
        shortener = pyshorteners.Shortener()
        x = shortener.tinyurl.short(link)
        print(LightCyan + '[=]', YELLOW + "Shorted Link :",LightCyan+ x)
    except:
        print("<<<< Unable to Short link >>>>")
        continue
