sudo apt update

# Установка git
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common git
echo "git install success"

# Установка docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install -y docker-ce
sudo usermod -aG docker $USER
echo "docker install success"

# Установка Docker Compose
DOCKER_COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep tag_name | cut -d '"' -f 4)
sudo curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo apt update
echo "docker-compose install success"

# Установка Nginx
sudo apt install -y nginx
sudo systemctl start nginx
sudo systemctl enable nginx
sudo ufw allow 'Nginx Full'
echo "nginx install success"


read -p "Введите ваш домен (например, example.com): " DOMAIN
read -p "Введите ваш email для уведомлений Let's Encrypt (SSL SERTIFICATE): " EMAIL
# Установка Certbot
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d $DOMAIN -m $EMAIL --agree-tos --no-eff-email --redirect 
echo "certbot install success"

# автообновление сертификатов
echo "0 0 * * * root certbot renew --quiet" | sudo tee -a /etc/crontab > /dev/null
echo "The automatic certificate update was installed successfully"


echo "Проверка установки компонентов:"
echo " ------S------"
nginx -v
sudo systemctl status nginx
git --version
docker --version
docker-compose --version
echo " ------E------"

sudo systemctl stop nginx

read -p "Введите ссылку с токеном для доступа к репозиторию проекта : " REPO_URL
git clone "$REPO_URL"

if [ $? -eq 0 ]; then
    echo "Репозиторий успешно клонирован."
    if [ $? -eq 0 ]; then
        cd project
        docker-compose up -d 
    else
       echo "Произошла ошибка при развертывании проекта. Установка не была завершена успешно, попробуйте еще раз"
    fi 
else
    echo "Произошла ошибка при клонировании репозитория. Установка не была завершена успешно, попробуйте еще раз"
fi

echo "--------------"
echo "Установка завершена"


# Сделать скрипт исполняемым
# chmod +x install_docker.sh