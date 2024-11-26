FROM nginx:alpine

COPY ./nginx.conf /etc/nginx/nginx.conf

COPY ./static /usr/share/nginx/html/static

# Открываем порт 80 для доступа
EXPOSE 80

# Стартуем Nginx
CMD ["nginx", "-g", "daemon off;"]