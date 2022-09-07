import os
import colorama
import platform
from colorama import Fore
systemdet = platform.system()

errormsg = "¡Algo anda mal!, si crees que es un error por favor repórtalo en discord: KPatch_#7564"
title = Fore.RED+"""                                                                                      
                                                
██╗░░██╗██████╗░░█████╗░████████╗░█████╗░██╗░░██╗███████╗███████╗░█████╗░░░██╗██╗
██║░██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░██║╚════██║██╔════╝██╔═══╝░░██╔╝██║
█████═╝░██████╔╝███████║░░░██║░░░██║░░╚═╝███████║░░░░██╔╝██████╗░██████╗░██╔╝░██║
██╔═██╗░██╔═══╝░██╔══██║░░░██║░░░██║░░██╗██╔══██║░░░██╔╝░╚════██╗██╔══██╗███████║
██║░╚██╗██║░░░░░██║░░██║░░░██║░░░╚█████╔╝██║░░██║░░██╔╝░░██████╔╝╚█████╔╝╚════██║
╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░╚═╝░░░╚═════╝░░╚════╝░░░░░░╚═╝"""


menu = Fore.WHITE+"""
     ╔═════════════════════════════════════════════╦═══════════════════════════════════════════════════╗
     ║                Executor                     ║                    Function                       ║
     ║                                             ║                                                   ║
     ║═════════════════════════════════════════════║═══════════════════════════════════════════════════║ 
     ║  scan (escaneo nmap)                        ║    use nmap para escanear un puerto ip/rango      ║
     ║  qubo (solo para puertos de minecraft       ║    use el escáner qubo para escanear ip(mc ports) ║
     ║  subdomains (Disponible en v1.x)            ║    escanear una lista de subdominios en un dominio║
     ║  poisoning (Disponible en v1.x)             ║    Cree una conexión proxy que redirija a un      ║
     ║                                             ║    servidor y captura comandos                    ║
     ║  clear                                      ║    Clear screen                                   ║
     ╚═════════════════════════════════════════════╩═══════════════════════════════════════════════════╝
                                    https://github.com/KPatch7564                              """

menuscan = Fore.WHITE+"""
     ╔═════════════════════════════════════════════╦═══════════════════════════════════════════════════╗
     ║                Executor                     ║                    Function                       ║
     ║                                             ║                                                   ║
     ║═════════════════════════════════════════════║═══════════════════════════════════════════════════║ 
     ║  fast: (1-100,25565-25600)                  ║    Escaneo rápido - rangos/ip                     ║
     ║  medium: (1-10000,25000-30000)              ║    escaneo medio - no recomendado para rangos     ║
     ║  slow: (1-65535)                            ║    escaneo lento - no recomendado para rangos     ║
     ║  custom                                     ║    escaneo personalizado: usted selecciona        ║
     ║                                             ║    el rango de puertos                            ║
     ║  clear                                      ║    Clear screen                                   ║
     ╚═════════════════════════════════════════════╩═══════════════════════════════════════════════════╝
                                    https://github.com/KPatch7564                               """

def clear():
    if systemdet=="Linux":
        os.system("clear")
    else:
        os.system("cls")

def main():
    if systemdet=="Linux":
        os.system("clear")
    else:
        os.system("cls")

    print(title)
    print(menu)
    cmd = input('Selecciona tu opción: ')

    if cmd=="scan":
        clear()
        scan()
        pass
    elif cmd=="qubo":
        clear()
        qubo()
        pass
    elif cmd=="clear":
        clear()
        print(menu)
        pass
    else:
        main()
        pass

def scan():
    print(title)
    print(menuscan)
    cmd = input('Selecciona tu opción: ')
    if cmd=="fast":
        ipz = input('Insert ip: ')
        if systemdet=="Linux":
            os.system("mkdir output")
            os.system("touch output/"+ipz+"_fast.txt")
            print(Fore.RED+"ADVERTENCIA"+Fore.WHITE+": Scan will be printed in output/"+ipz+"_fast.txt")
            os.system("nmap -p 1-100,25565-25600 -T4 -A --open -v -Pn "+ipz+" >>output/"+ipz+"_fast.txt")
            exitit = input('¿Quieres continuar?: <y/n>> ')
            if exitit=="y":
                main()
            elif exitit=="n":
                exit()
            else:
                main()
            pass
        else:
            print(Fore.RED+"ADVERTENCIA"+Fore.WHITE+": Scan will be printed in "+ipz+"_output_fast.txt")
            f = open(ipz+"_output_fast.txt", "w+")
            f.close()
            os.system("nmap -p 1-100,25565-25600 -T4 -A --open -v -Pn "+ipz+" >>"+ipz+"_output_fast.txt")
            exitit = input('¿Quieres continuar?: <y/n>> ')
            if exitit=="y":
                main()
            elif exitit=="n":
                exit()
            else:
                main()
            pass
            pass
        pass
    elif cmd=="medium":
        ipz = input('Insert ip: ')
        if systemdet=="Linux":
            os.system("mkdir output")
            os.system("touch output/"+ipz+"_medium.txt")
            print(Fore.RED+"ADVERTENCIA"+Fore.WHITE+": Scan will be printed in output/"+ipz+"_medium.txt")
            os.system("nmap -p 1-10000,25000-30000 -T4 -A --open -v -Pn "+ipz+" >>output/"+ipz+"_medium.txt")
            exitit = input('¿Quieres continuar?: <y/n>> ')
            if exitit=="y":
                main()
            elif exitit=="n":
                exit()
            else:
                main()
            pass
        else:
            print(Fore.RED+"ADVERTENCIA"+Fore.WHITE+": Scan will be printed in "+ipz+"_output_medium.txt")
            f = open(ipz+"_output_medium.txt", "w+")
            f.close()
            os.system("nmap -p 1-10000,25000-30000 -T4 -A --open -v -Pn "+ipz+" >>"+ipz+"_output_medium.txt")
            exitit = input('¿Quieres continuar?: <y/n>> ')
            if exitit=="y":
                main()
            elif exitit=="n":
                exit()
            else:
                main()
            pass
            pass
        pass
    elif cmd=="slow":
        ipz = input('Insert ip: ')
        if systemdet=="Linux":
            os.system("mkdir output")
            os.system("touch output/"+ipz+"_slow.txt")
            print(Fore.RED+"ADVERTENCIA"+Fore.WHITE+": Scan will be printed in output/"+ipz+"_slow.txt")
            os.system("nmap -p 1-10000,25000-30000 -T4 -A --open -v -Pn "+ipz+" >>output/"+ipz+"_slow.txt")
            exitit = input('¿Quieres continuar?: <y/n>> ')
            if exitit=="y":
                main()
            elif exitit=="n":
                exit()
            else:
                main()
            pass
        else:
            print(Fore.RED+"ADVERTENCIA"+Fore.WHITE+": Scan will be printed in "+ipz+"_output_slow.txt")
            f = open(ipz+"_output_slow.txt", "w+")
            f.close()
            os.system("nmap -p 1-10000,25000-30000 -T4 -A --open -v -Pn "+ipz+" >>"+ipz+"_output_slow.txt")
            exitit = input('¿Quieres continuar?: <y/n>> ')
            if exitit=="y":
                main()
            elif exitit=="n":
                exit()
            else:
                main()
            pass
            pass
        pass
    elif cmd=="custom":
        ipz = input('Insert ip: ')
        portr = input('Insert ports: ')
        if systemdet=="Linux":
            os.system("mkdir output")
            os.system("touch output/"+ipz+"_slow.txt")
            print(Fore.RED+"ADVERTENCIA"+Fore.WHITE+": Scan will be printed in output/"+ipz+"_slow.txt")
            os.system("nmap -p "+portr+" -T4 -A --open -v -Pn "+ipz+" >>output/"+ipz+"_slow.txt")
            exitit = input('¿Quieres continuar?: <y/n>> ')
            if exitit=="y":
                main()
            elif exitit=="n":
                exit()
            else:
                main()
            pass
        else:
            print(Fore.RED+"ADVERTENCIA"+Fore.WHITE+": Scan will be printed in "+ipz+"_output_slow.txt")
            f = open(ipz+"_output_slow.txt", "w+")
            f.close()
            os.system("nmap -p "+portr+" -T4 -A --open -v -Pn "+ipz+" >>"+ipz+"_output_slow.txt")
            exitit = input('¿Quieres continuar?: <y/n> ')
            if exitit=="y":
                main()
                pass
            elif exitit=="n":
                exit()
                pass
            else:
                main()
                pass
            pass
        pass
    else:
        main()
        pass


def qubo():
    print(Fore.RED+"ADVERTENCIA"+Fore.WHITE+": quboscanner solo funciona con puertos de minecraft")
    quboopt = input('¿Tiene qubo.jar en la carpeta?: <y/n> ')
    if quboopt=="y":
        iprange = input('Insert ip/range: ')
        portrange = input('Insert ports range: ')
        timeout = input('Insert ti: ')
        threats = input('Insert th: ')
        os.system("java -Dfile.encoding=UTF-8 -jar qubo.jar -noping -ports "+portrange+" -th "+threats+" -ti "+timeout+" -all -range "+iprange)
        pass
    elif quboopt=="n":
        main()
        pass
    else:
        main()
        pass

def subdomains():
    print("No disponible en esta versión")

def poisoning():
    print("se añadirá en el futuro")

main()