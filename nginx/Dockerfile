FROM nginx:alpine

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./web/app/static /usr/share/nginx/html/static
COPY ./web/app/media /usr/share/nginx/html/media

# Копируем сертификаты SSL (обновите путь в зависимости от вашей конфигурации)
COPY ./ssl /etc/letsencrypt/live/laianbotrus.ru

# Открываем порты 80 и 443
EXPOSE 80 443

# Стартуем Nginx
CMD ["nginx", "-g", "daemon off;"]