#!/bin/bash

# Backup

# Escolhendo o diretório do backup
echo "Caminho do diretório:"
#backup_files="/home /var/spool/mail /etc /root /boot /opt"
read backup_files

# Onde realizar o backup
dest="/home/augusto/backup"

#Excluindo arquivos anteriores

#Gera-se as datas dos arquivos
option1=$(date -d "$date -1 days" +"%Y%m%d")
option2=$(date -d "$date -2 days" +"%Y%m%d")
shopt -s extglob
cd "$dest"
rm -v !("${option1}.tar.gz"|"${option2}.tar.gz")

# Criando nome do arquivo.
day=$(date +%A)
hostname=$(hostname -s)
current_date=$(date -d "$date" +"%Y%m%d")
archive_file="$current_date.tar.gz"

# Mensagem de estado.

echo "Realizando backup de $backup_files para $dest/$archive_file"
date
echo

# Fazendo o backup
tar cvzf $dest/$archive_file $backup_files

# Mensagem de finalizaçao.
echo
echo "Backup finalizado!"
date

# Lista de arquivos em #dest para checagem
ls -lh $dest