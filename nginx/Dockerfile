FROM nginx:alpine

# Копируем конфигурацию Nginx
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

# Копируем статические файлы
COPY ./web/app/static /usr/share/nginx/html/static

# Копируем сертификаты SSL (обновите путь в зависимости от вашей конфигурации)
COPY ./ssl /etc/letsencrypt/live/laianbotrus.ru

# Открываем порты 80 и 443
EXPOSE 80 443

# Стартуем Nginx
CMD ["nginx", "-g", "daemon off;"]