# [Simple web stack](https://ibb.co/Gtq8cSf)
**Add**
- 1 server
- 1 web server (Nginx)
- 1 application server
- 1 application files (your code base)
- 1 database (MySQL)
- 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8


# [Distributed Web Infrastructure](https://ibb.co/zmyhx1v)
**Add**
- 2 servers
- 1 web server (Nginx)
- 1 application server
- 1 load-balancer (HAproxy)
- 1 set of application files (your code base)
- 1 database (MySQL)


# [Secured and Monitored Web Infrastructure](https://ibb.co/9Nfn9XX)
**Add**
- 3 firewalls
- 1 SSL certificate to serve www.foobar.com over HTTPS
- 3 monitoring clients (data collector for Sumologic or other monitoring services)


# [Scale Up](https://ibb.co/7WNz3Bh)
**Add**
- 1 server
- 1 load-balancer (HAproxy) configured as cluster with the other one
- Split components (web server, application server, database) with their own server
