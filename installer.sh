#!/usr/bin/bash
# 
# configs
# 

# PLEASE DELETE .git BEFORE USE

# lock unlock configs
is_configured=false

# configs to setup
db_addr="address to mysql server"
db_user="username"
db_password="password"
db_name="db name"    # please configure db_install.sql and db_delete.sql

docker_image_name="docker image name"
docker_container_name="docker container name"
docker_port_outside=9888   # check Dockerfile EXPOSE and script to start dev and prod server before
docker_port_inside=9888    # check Dockerfile EXPOSE and script to start dev and prod server before
# PLEASE CONFIG DOCKER FILE

config_file_name="secret.conf"

# 
# check for configured
# 

if [ $is_configured == true ]
then

# 
# main app loop
# 

while [ true ]
do
# clean console
clear

# controll message
echo "ESC: exit"
echo "1: star dev server"
echo "2: start prod server"
echo "3: generate new config file"
echo "5: install db"
echo "6: delete db"
echo "7: install docker"
echo "8: delete docker"
echo "9: install project"
echo "d: delete all settings"

# read user key
read -sn 1 key

# if escape break loop
if [ "$key" = $'\e' ]
then
break
fi

# dev server
if [ "$key" = "1" ]
then
clear
./dev_start.sh
break
fi

# prod server
if [ "$key" = "2" ]
then
clear
./prod_start.sh
break
fi

# generate config file
if [ "$key" = "3" ]
then
rm $config_file_name
echo "db_addr=$db_addr" >> $config_file_name
echo "db_user=$db_user" >> $config_file_name
echo "db_password=$db_password" >> $config_file_name
echo "db_name=$db_name" >> $config_file_name
clear
echo "$config_file_name generated"
break
fi

# install sql script
if [ "$key" = "5" ]
then
clear
mysql -h $db_addr -u $db_user -p$db_password < db_install.sql
echo "SQL file installed"
break
fi

# delete db (exec delete.sql script)
if [ "$key" = "6" ]
then
clear
mysql -h $db_addr -u $db_user -p$db_password < db_delete.sql
echo "DB deleted"
break
fi

# Docker installing
if [ "$key" = "7" ]
then
clear

# build new image and run app
docker build -t $docker_image_name .
docker run -dit -p $docker_port_outside:$docker_port_inside --name $docker_container_name $docker_image_name

echo "Docker container installed"
break
fi

# Docker installing
if [ "$key" = "7" ]
then
clear

# build new image and run app
docker build -t $docker_image_name .
docker run -dit -p $docker_port_outside:$docker_port_inside --name $docker_container_name $docker_image_name

echo "Docker container installed"
break
fi

# Docker removing
if [ "$key" = "8" ]
then
clear

docker container stop $docker_container_name
docker container rm $docker_container_name
docker image rm $docker_image_name

echo "Docker image and container was removed"
break
fi

# Install all
if [ "$key" = "i" ]
then
clear

# config file
rm $config_file_name
echo "db_addr=$db_addr" >> $config_file_name
echo "db_user=$db_user" >> $config_file_name
echo "db_password=$db_password" >> $config_file_name
echo "db_name=$db_name" >> $config_file_name
clear
echo "$config_file_name generated"

# rewrite db
mysql -h $db_addr -u $db_user -p$db_password < db_delete.sql
mysql -h $db_addr -u $db_user -p$db_password < db_install.sql

# rewrite docker
docker container stop $docker_container_name
docker container rm $docker_container_name
docker image rm $docker_image_name

docker build -t $docker_image_name .
docker run -dit -p $docker_port_outside:$docker_port_inside --restart unless-stopped --name $docker_container_name $docker_image_name

echo "Successful installed"
break
fi

# Docker installing
if [ "$key" = "d" ]
then
clear
rm $config_file_name
mysql -h $db_addr -u $db_user -p$db_password < db_delete.sql
docker container stop $docker_container_name
docker container rm $docker_container_name
docker image rm $docker_image_name
echo "Deleting complete"
break
fi

# stop loop
done

# Show message is not configured
else
clear
echo "Before use, please config this file and set variable 'is_configured=true'"
fi