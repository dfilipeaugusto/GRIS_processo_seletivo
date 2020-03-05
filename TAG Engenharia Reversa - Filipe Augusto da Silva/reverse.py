# -*- coding: utf-8 -*-

#O arquivo denominado reverse.py faz a leitura da chave que está contida no arquivo key, dentro do diretório /tmp, e executa o arquivo .encriptador com o simétrico da chave. Por exemplo, se a chave estiver com o valor “2”, o comando a ser executado será “./.encriptador -2”, ou seja, haverá “incremento negativo” ou, simplesmente, um decremento na mesma ordem do incremento realizado no processo de encriptação. Assim, basta executar o arquivo reverse.py. Tal algoritmo poderia ser aperfeiçoado limpando os arquivos encriptados, mas não faz parte do objetivo proposto.

import os
with open('/tmp/key', 'r') as file:
    data = file.read().replace('\n', '')
os.system('./.encriptador -'+data)
