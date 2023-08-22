FROM ubuntu:22.04

COPY /facebook.com/ /var/www/html/

RUN apt-get update && apt-get install -y apache2

EXPOSE 80

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
