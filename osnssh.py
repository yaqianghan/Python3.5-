#-*-coding:utf-8-*-
import os, sys
sys.path.append("../")
from bin import setting, auto_ssh
path = os.path.dirname(os.path.abspath(sys.argv[0]))
'''
方便在LINUX终端使用ssh,保存使用的IP:PORT , PASSWORD
自动登录
__author__ = 'allen woo'
'''
def main():
    while 1:

        print("==============OSNSSH [Menu]=============")
        print("1.Connection between a host\n2.Add host\n3.Remove host\n4.About\n[Help]: q:quit   clear:clear screen")
        print("="*40)
        c = input("Please select a:")
        if c == 1 or c == "1":
            auto_ssh.choose()
        if c == 2 or c == "2":
            setting.add_host_main()
        if c == 3 or c == "3":
            setting.remove_host()
        if c == 4 or c == "4":
            setting.about()
        elif c == "clear":
            os.system("clear")
        elif c == "q" or c == "Q" or c == "quit":
            print("Bye")
            sys.exit()
        else:
            print("\n")

if __name__ == '__main__':
    try:
        of = open("{}/data/information.d".format(path))
    except:
        of = open("{}/data/information.d".format(path), "w")
    of.close()
    main()
