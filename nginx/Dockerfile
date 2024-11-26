FROM nginx:alpine

COPY nginx/nginx.conf /etc/nginx/nginx.conf

COPY web/app/static /usr/share/nginx/html/static

# Открываем порт 80 для доступа
EXPOSE 80

# Стартуем Nginx
CMD ["nginx", "-g", "daemon off;"]