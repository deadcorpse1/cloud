QN 1 VIRTUAL INSTANCES
Install Apache on each clone
1.sudo apt update
2.sudo apt install apache2 -y
3.sudo systemctl enable apache2
4.sudo systemctl status apache2
5.sudo nano /var/www/html/index.html(Add the name Apache2 Clone 1[for each clone])
6.sudo apt install net-tools
7.ifconfig

QN 2 LOAD BALANCING
Load Balancing with HAProxy
1.sudo apt install net-tools
2.sudo apt install haproxy -y
3.sudo nano /etc/haproxy/haproxy.cfg
4.Add this configuration at the end of the file(system's generated ip address)
frontend http_front
    bind *:80
    default_backend http_back
backend http_back
    balance roundrobin
    server ubuntu1 192.168.44.165:80 check
    server ubuntu2 192.168.44.166:80 check
5.sudo systemctl restart haproxy
6.sudo systemctl enable haproxy
7.sudo systemctl status haproxy

QN 3 SERVER CONSOLIDATION
In vm1 :
1.free -h
2.top
3.go to web browser (type the ip address of vm2)[eg.192.168.234.137/vm2]
In vm2 : 
1.free -h
2.top
IN VM1
1.sudo mkdir -p /var/www/html/index.html
2.sudo mkdir -p /var/www/html/vm2
3.sudo cp /var/www/html/index.html /var/www/html/vm2/index.html
4.sudo nano /var/www/html/vm2/index.html
Chnage to consolidated vm
Then ifconfig address/vm2


QN 4 TASK SCHEDULING

nano script.sh

for i in {1..6}; do
    echo "Hello" >> /home/ubuntu/output.log
    sleep 10
done
chmod +x script.sh
crontab -e
End of the file
* * * * * /home/ubuntu/script.sh

tail -f /home/ubuntu/output.log

cat /home/ubuntu/output.log (Verification)