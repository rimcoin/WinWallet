#!/usr/bin/python

import subprocess,os

print("""Rimcoin Wallet
for custom nodes - default is genesis node. """)

node="67.241.245.218:8080/"
us=input("input Rimcoin wallet address (put n if you don't have one) - ")
if us=="n":
    cr=input("enter desired wallet address: ")
    os.system("(curl "+node+"create*"+cr+" -s)>"+cr+"_wallet.rim")
    us=cr
balance=subprocess.check_output(("curl "+node+"bal*"+us+" -s").split(" "))

print("You currently have "+balance.decode("latin1")+" RC. ")

print("That is $"+str((float(balance.decode("latin1"))*float(subprocess.check_output(("curl https://pastebin.com/raw/bMW33BUC -s").split(" "))))))

print("Type 'help' (w/o quotes) for commands")

while True:
    cmd=input("Rimcoin # ")
    try:
        cmd=cmd.split(" ")
    except:
        cmd=[cmd]
    if cmd[0]=="help":
        try:
            if cmd[1]=="send":
                print("send (OUTGOING ADDRESS) (AMOUNT)")
            elif cmd[1]=="balance":
                print("balance (ADDRESS)")
                print("or")
                print("balance")
            else:
                print("""
____ help ____

help            shows help message
send            send Rimcoin
balance         get balance of yourself or others

help (COMMAND)  get help on a particular command""")
        except:
            print("""
____ help ____

help            shows help message
send            send Rimcoin
balance         get balance of yourself or others

help (COMMAND)  get help on a particular command""")
    elif cmd[0]=="send":
        try:
            os.system("curl "+node+"send*"+us+"*"+cmd[1]+"*"+cmd[2]+"*"+open(us+"_wallet.rim",'r').read()+" -s")
        except:
            print("usage:")
            print("send (OUTGOING ADDRESS) (AMOUNT")
    elif cmd[0]=="balance":
        try:
            os.system("curl "+node+"bal*"+cmd[1]+" -s")
            print()
        except:
            os.system("curl "+node+"bal*"+us+"")
            print()
    else:
        print("unknown command - run 'help' (w/o quotes) for help. ")
