#!/bin/bash

echo -e "\n\n\e[32mConversor SA-MP para Open.MP\n\e[0m"

mkdir -p $PREFIX/bin

curl -o $PREFIX/bin/convertomp -L https://raw.githubusercontent.com/Brabosxtz/Conversor-samp-para-open.mp/main/convertomp.py

chmod +x $PREFIX/bin/convertomp

echo -e "\n\e[32mInstalação concluída com sucesso!\e[0m"
echo -e "Você pode usar o comando executando:\n\e[33mconvertomp <arquivo> optional:[pasta_modulos]\e[0m"