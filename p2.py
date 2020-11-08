import os

print("\n\n\t\t\t***Welcome to docker project***")
print("\t\t---------------------------------------------")

os.system("systemctl stop firewalld")
os.system("setenforce 0")
while True:
    print("""\n\n\tMenu:
         \tpress 1:Create your own webserver in just one click 
         \tpress 2:
         \tpress 3:
         \tpress 4:
         \tpress 5:
         \tpress 6:
         \tpress 7:
         \tpress 8:To exit""")

    
    ch = int(input("\nPlz enter your choice:"))
    print(ch)
    
    if ch == 1:
        main_ip = input("\n\nPlease give ip of your system : ")
        name = input("Give any name to your OS : ")
        portno = int(input("please give any four digit unique number don't repeat this number anywhere : "))
        os.system("docker run -dit --name {}  -p {}:80 centos".format(name ,portno))
        os.system("docker exec -dit {} yum install httpd -y".format(name))
        os.system("tput setaf 3")
        print("Write the content you want to show to your client and to save press ctrl+d : ")
        os.system("cat > /root/index.html")
        os.system("tput setaf 7")
        os.system("iptables -F")
        os.system("iptables -P FORWARD ACCEPT")
        os.system("tput setaf 2")
        print("wait...")
        os.system("sleep 60")
        os.system("docker exec -it {} sed -ie '$a/usr/sbin/httpd' /root/.bashrc".format(name))
        os.system("sleep 2")
        os.system("docker restart {}".format(name))
        os.system("docker cp /root/index.html {}:/var/www/html".format(name))
        print("you had successfully create your service ")
        os.system("tput setaf 3")
        print("Your URL : http://{}:{}/index.html".format(main_ip,portno))
        os.system("tput setaf 7")
        print("Try it on your browser")
    elif ch == 8:
        exit()
    else:
        print("option not supported")
    input("Enter to continue........")
os.system("clear")

