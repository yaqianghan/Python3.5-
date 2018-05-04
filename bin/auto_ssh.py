#-*-coding:utf-8-*-
import os, sys, base64
import pexpect
path = os.path.dirname(os.path.abspath(sys.argv[0]))

def choose():
    # 打开我们的数据文件
    of = open("{}/data/information.d".format(path))
    hosts = of.readlines()
    hosts_temp = []
    for h in hosts:
        if h.strip():
            hosts_temp.append(h)
    hosts = hosts_temp[:]
    l = len(hosts)
    if l <= 0:
        os.system("clear")
        print("[Warning]Please add the host server")
        return
    while 1:

        print("=================SSH===================")
        print("+{}+".format("-"*40))
        print("|     Alias   UserName@IP:PORT")
        for i in range(0, l):
            v_list = hosts[i].strip().split(" ")
            print("+{}+".format("-"*40))
            print("| {} | {}   {}@{}:{}".format(i+1, v_list[4], v_list[0], v_list[1], v_list[2]))
        print("+{}+".format("-"*40))
        c = input("[SSH]Choose the number or alias('#q' exit):")
        is_alias = False
        is_y = False
        try:
            c = int(c)
            if c > l or c < 1:
                os.system("clear")
                print("[Warning]:There is no")
                continue
            l_list = hosts[c-1].split(" ")
            name = l_list[0]
            host = l_list[1]
            port = l_list[2]
            password = l_list[3]
            is_y = True

        except:
            is_alias = True
        if is_alias:
            if c.strip() == "#q":
                os.system("clear")
                return
            for h in hosts:
                if c.strip() == h.split(" ")[4].strip():
                    l_list = h.split(" ")
                    name = l_list[0]
                    host = l_list[1]
                    port = l_list[2]
                    password = l_list[3]
                    is_y = True
        if not is_y:
            continue
        # ssh
        # 将加密保存的密码解密
       # password = base64.decodestring(password)
        print("In the connection...")
        # 准备远程连接，拼接ip：port
        print(port)
        print(name)
        print(host)
        print(password) 
        print("{}@{}".format(name, host))
        print("hyq")
        print("{}@{}:{}".format(name, host, port))
        if port == "22":
            connection("ssh {}@{}".format(name, host), password)

        else:
            connection("ssh {}@{} -p {}".format(name, host, port), password)

def connection(cmd, pwd):
    '''
    连接远程服务器
    :param cmd: 
    :param pwd: 
    :return: 
    '''
    child = pexpect.spawn(cmd)
    i = child.expect([".*password.*", ".*continue.*?", pexpect.EOF, pexpect.TIMEOUT])
    print(i)
 #   print(child)
    if( i == 0 ):
        # 如果交互中出现.*password.*，就是叫我们输入密码
        # 我们就把密码自动填入下去
        child.sendline("{}\n".format(pwd))
        child.interact()
    elif( i == 1):
        # 如果交互提示是否继续，一般第一次连接时会出现
        # 这个时候我们发送"yes"，然后再自动输入密码
        child.sendline("yes\n")
        child.sendline("{}\n".format(pwd))

        #child.interact()    
    else:
        # 连接失败
        print("[Error]The connection fails")
