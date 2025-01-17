#!/bin/bash

echo -e "\n\n\033[32mConversor SA-MP para Open.MP\n\e[0m"

yes | pkg update && pkg upgrade
pkg install -y python
pip install convertomp

echo -e "\n\e[32mInstalação concluída com sucesso!\e[0m"
echo -e "Você pode usar o comando executando:\n\e[33mconvertomp <arquivo\-L> optional:[pasta_modulos]\e[0m"
