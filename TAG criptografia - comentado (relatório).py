# -*- coding: utf-8 -*-
import binascii

def decode_hex_ascii(s):
#OBJETIVO: Decodificar os caracteres HEXADECIMAL para os caracteres da tabela ASCII
 
#Avalia s a cada dois caracteres hexadecimais, envia como parâmetro para a função "hex_to_string_ascii" que retorna o caracter ASCII correspondente e, por fim, retorna tudo concatenado quando findada a busca de todos os caracteres de s dois a dois


	s = s.upper()
	prev = "-1"
	final = ""
	for index, value in enumerate(s):	
		if (index+1)%2==0:
			final = final + hex_to_string_ascii(prev + value)
			prev = "-1"
		else:
			prev = value
	return final

def decode_hex_binary(s):

#OBJETIVO: Decodificar os caracteres HEXADECIMAL para os caracteres em BINÁRIO
 
#Avalia s a cada dois caracteres hexadecimais, envia como parâmetro para a função "hex_to_string_binary" que retorna o BINÁRIO correspondente e, por fim, retorna tudo concatenado quando findada a busca de todos os caracteres de s dois a dois

	s = s.upper()
	prev = "-1"
	final = ""
	for index, value in enumerate(s):	
		if (index+1)%2==0:
			final = final + hex_to_string_binary(prev + value)
			prev = "-1"
		else:
			prev = value
	return final
def hex_to_string_binary(entry):

#OBJETIVO: Converte Hexadecimal em Binário

#Simplesmente avalia a entrada de dois caracteres hexadecimais e retorna o binário correspondente


	if entry=="00": return "00000000"
	if entry=="01": return "00000001"
	if entry=="02": return "00000010"
	if entry=="03": return "00000011"
	if entry=="04": return "00000100"
	if entry=="05": return "00000101"
	if entry=="06": return "00000110"
	if entry=="07": return "00000111"
	if entry=="08": return "00001000"
	if entry=="09": return "00001001"
	if entry=="0A": return "00001010"
	if entry=="0B": return "00001011"
	if entry=="0C": return "00001100"
	if entry=="0D": return "00001101"
	if entry=="0E": return "00001110"
	if entry=="0F": return "00001111"
	if entry=="10": return "00010000"
	if entry=="11": return "00010001"
	if entry=="12": return "00010010"
	if entry=="13": return "00010011"
	if entry=="14": return "00010100"
	if entry=="15": return "00010101"
	if entry=="16": return "00010110"
	if entry=="17": return "00010111"
	if entry=="18": return "00011000"
	if entry=="19": return "00011001"
	if entry=="1A": return "00011010"
	if entry=="1B": return "00011011"
	if entry=="1C": return "00011100"
	if entry=="1D": return "00011101"
	if entry=="1E": return "00011110"
	if entry=="1F": return "00011111"
	if entry=="20": return "00100000"
	if entry=="21": return "00100001"
	if entry=="22": return "00100010"
	if entry=="23": return "00100011"
	if entry=="24": return "00100100"
	if entry=="25": return "00100101"
	if entry=="26": return "00100110"
	if entry=="27": return "00100111"
	if entry=="28": return "00101000"
	if entry=="29": return "00101001"
	if entry=="2A": return "00101010"
	if entry=="2B": return "00101011"
	if entry=="2C": return "00101100"
	if entry=="2D": return "00101101"
	if entry=="2E": return "00101110"
	if entry=="2F": return "00101111"
	if entry=="30": return "00110000"
	if entry=="31": return "00110001"
	if entry=="32": return "00110010"
	if entry=="33": return "00110011"
	if entry=="34": return "00110100"
	if entry=="35": return "00110101"
	if entry=="36": return "00110110"
	if entry=="37": return "00110111"
	if entry=="38": return "00111000"
	if entry=="39": return "00111001"
	if entry=="3A": return "00111010"
	if entry=="3B": return "00111011"
	if entry=="3C": return "00111100"
	if entry=="3D": return "00111101"
	if entry=="3E": return "00111110"
	if entry=="3F": return "00111111"
	if entry=="40": return "01000000"
	if entry=="41": return "01000001"
	if entry=="42": return "01000010"
	if entry=="43": return "01000011"
	if entry=="44": return "01000100"
	if entry=="45": return "01000101"
	if entry=="46": return "01000110"
	if entry=="47": return "01000111"
	if entry=="48": return "01001000"
	if entry=="49": return "01001001"
	if entry=="4A": return "01001010"
	if entry=="4B": return "01001011"
	if entry=="4C": return "01001100"
	if entry=="4D": return "01001101"
	if entry=="4E": return "01001110"
	if entry=="4F": return "01001111"
	if entry=="50": return "01010000"
	if entry=="51": return "01010001"
	if entry=="52": return "01010010"
	if entry=="53": return "01010011"
	if entry=="54": return "01010100"
	if entry=="55": return "01010101"
	if entry=="56": return "01010110"
	if entry=="57": return "01010111"
	if entry=="58": return "01011000"
	if entry=="59": return "01011001"
	if entry=="5A": return "01011010"
	if entry=="5B": return "01011011"
	if entry=="5C": return "01011100"
	if entry=="5D": return "01011101"
	if entry=="5E": return "01011110"
	if entry=="5F": return "01011111"
	if entry=="60": return "01100000"
	if entry=="61": return "01100001"
	if entry=="62": return "01100010"
	if entry=="63": return "01100011"
	if entry=="64": return "01100100"
	if entry=="65": return "01100101"
	if entry=="66": return "01100110"
	if entry=="67": return "01100111"
	if entry=="68": return "01101000"
	if entry=="69": return "01101001"
	if entry=="6A": return "01101010"
	if entry=="6B": return "01101011"
	if entry=="6C": return "01101100"
	if entry=="6D": return "01101101"
	if entry=="6E": return "01101110"
	if entry=="6F": return "01101111"
	if entry=="70": return "01110000"
	if entry=="71": return "01110001"
	if entry=="72": return "01110010"
	if entry=="73": return "01110011"
	if entry=="74": return "01110100"
	if entry=="75": return "01110101"
	if entry=="76": return "01110110"
	if entry=="77": return "01110111"
	if entry=="78": return "01111000"
	if entry=="79": return "01111001"
	if entry=="7A": return "01111010"
	if entry=="7B": return "01111011"
	if entry=="7C": return "01111100"
	if entry=="7D": return "01111101"
	if entry=="7E": return "01111110"
	if entry=="7F": return "01111111"

def ascii_to_binary(s):

#OBJETIVO: Transforma o caracter ASCII em BINÁRIO
#Usa-se a função "hexlify" da biblioteca "binascii" para este fim

	return str(bin(int(binascii.hexlify(s), 16)))[:1] + str(bin(int(binascii.hexlify(s), 16)))[2:]

def binary_to_ascii(s):

#OBJETIVO: Transforma o binário em caracter ASCII
#Usa-se a função "unhexlify" da biblioteca "binascii" para este fim

	return binascii.unhexlify(s)

def hex_to_string_ascii(entry):

#OBJETIVO: Converte Hexadecimal em ASCII

#Simplesmente avalia a entrada de dois caracteres hexadecimais e retorna o ASCII correspondente

	if entry=="00": return "NUL"
	if entry=="01": return "SOH"
	if entry=="02": return "STX"
	if entry=="03": return "ETX"
	if entry=="04": return "EOT"
	if entry=="05": return "ENQ"
	if entry=="06": return "ACK"
	if entry=="07": return "BEL"
	if entry=="08": return "BS"
	if entry=="09": return "HT"
	if entry=="0A": return "LF"
	if entry=="0B": return "VT"
	if entry=="0C": return "FF"
	if entry=="0D": return "CR"
	if entry=="0E": return "SO"
	if entry=="0F": return "SI"
	if entry=="10": return "DLE"
	if entry=="11": return "DC1"
	if entry=="12": return "DC2"
	if entry=="13": return "DC3"
	if entry=="14": return "DC4"
	if entry=="15": return "NAK"
	if entry=="16": return "SYN"
	if entry=="17": return "ETB"
	if entry=="18": return "CAN"
	if entry=="19": return "EM"
	if entry=="1A": return "SUB"
	if entry=="1B": return "ESC"
	if entry=="1C": return "FS"
	if entry=="1D": return "GS"
	if entry=="1E": return "RS"
	if entry=="1F": return "US"
	if entry=="20": return " "
	if entry=="21": return "!"
	if entry=="22": return '"'
	if entry=="23": return "#"
	if entry=="24": return "$"
	if entry=="25": return "%"
	if entry=="26": return "&"
	if entry=="27": return "'"
	if entry=="28": return "("
	if entry=="29": return ")"
	if entry=="2A": return "*"
	if entry=="2B": return "+"
	if entry=="2C": return ","
	if entry=="2D": return "-"
	if entry=="2E": return "."
	if entry=="2F": return "/"
	if entry=="30": return "0"
	if entry=="31": return "1"
	if entry=="32": return "2"
	if entry=="33": return "3"
	if entry=="34": return "4"
	if entry=="35": return "5"
	if entry=="36": return "6"
	if entry=="37": return "7"
	if entry=="38": return "8"
	if entry=="39": return "9"
	if entry=="3A": return ":"
	if entry=="3B": return ";"
	if entry=="3C": return "<"
	if entry=="3D": return "="
	if entry=="3E": return ">"
	if entry=="3F": return "?"
	if entry=="40": return "@"
	if entry=="41": return "A"
	if entry=="42": return "B"
	if entry=="43": return "C"
	if entry=="44": return "D"
	if entry=="45": return "E"
	if entry=="46": return "F"
	if entry=="47": return "G"
	if entry=="48": return "H"
	if entry=="49": return "I"
	if entry=="4A": return "J"
	if entry=="4B": return "K"
	if entry=="4C": return "L"
	if entry=="4D": return "M"
	if entry=="4E": return "N"
	if entry=="4F": return "O"
	if entry=="50": return "P"
	if entry=="51": return "Q"
	if entry=="52": return "R"
	if entry=="53": return "S"
	if entry=="54": return "T"
	if entry=="55": return "U"
	if entry=="56": return "V"
	if entry=="57": return "W"
	if entry=="58": return "X"
	if entry=="59": return "Y"
	if entry=="5A": return "Z"
	if entry=="5B": return "["
	if entry=="5C": return "\\"
	if entry=="5D": return "]"
	if entry=="5E": return "^"
	if entry=="5F": return "_"
	if entry=="60": return "`"
	if entry=="61": return "a"
	if entry=="62": return "b"
	if entry=="63": return "c"
	if entry=="64": return "d"
	if entry=="65": return "e"
	if entry=="66": return "f"
	if entry=="67": return "g"
	if entry=="68": return "h"
	if entry=="69": return "i"
	if entry=="6A": return "j"
	if entry=="6B": return "k"
	if entry=="6C": return "l"
	if entry=="6D": return "m"
	if entry=="6E": return "n"
	if entry=="6F": return "o"
	if entry=="70": return "p"
	if entry=="71": return "q"
	if entry=="72": return "r"
	if entry=="73": return "s"
	if entry=="74": return "t"
	if entry=="75": return "u"
	if entry=="76": return "v"
	if entry=="77": return "w"
	if entry=="78": return "x"
	if entry=="79": return "y"
	if entry=="7A": return "z"
	if entry=="7B": return "{"
	if entry=="7C": return "|"
	if entry=="7D": return "}"
	if entry=="7E": return "~"
	if entry=="7F": return "DEL"

def binary_to_char_base64(entry):

#OBJETIVO: Tabela index Base64
#Retorna o caracter do binário 

	if entry=="000000": return "A"
	if entry=="000001": return "B"
	if entry=="000010": return "C"
	if entry=="000011": return "D"
	if entry=="000100": return "E"
	if entry=="000101": return "F"
	if entry=="000110": return "G"
	if entry=="000111": return "H"
	if entry=="001000": return "I"
	if entry=="001001": return "J"
	if entry=="001010": return "K"
	if entry=="001011": return "L"
	if entry=="001100": return "M"
	if entry=="001101": return "N"
	if entry=="001110": return "O"
	if entry=="001111": return "P"
	if entry=="010000": return "Q"
	if entry=="010001": return "R"
	if entry=="010010": return "S"
	if entry=="010011": return "T"
	if entry=="010100": return "U"
	if entry=="010101": return "V"
	if entry=="010110": return "W"
	if entry=="010111": return "X"
	if entry=="011000": return "Y"
	if entry=="011001": return "Z"
	if entry=="011010": return "a"
	if entry=="011011": return "b"
	if entry=="011100": return "c"
	if entry=="011101": return "d"
	if entry=="011110": return "e"
	if entry=="011111": return "f"
	if entry=="100000": return "g"
	if entry=="100001": return "h"
	if entry=="100010": return "i"
	if entry=="100011": return "j"
	if entry=="100100": return "k"
	if entry=="100101": return "l"
	if entry=="100110": return "m"
	if entry=="100111": return "n"
	if entry=="101000": return "o"
	if entry=="101001": return "p"
	if entry=="101010": return "q"
	if entry=="101011": return "r"
	if entry=="101100": return "s"
	if entry=="101101": return "t"
	if entry=="101110": return "u"
	if entry=="101111": return "v"
	if entry=="110000": return "w"
	if entry=="110001": return "x"
	if entry=="110010": return "y"
	if entry=="110011": return "z"
	if entry=="110100": return "0"
	if entry=="110101": return "1"
	if entry=="110110": return "2"
	if entry=="110111": return "3"
	if entry=="111000": return "4"
	if entry=="111001": return "5"
	if entry=="111010": return "6"
	if entry=="111011": return "7"
	if entry=="111100": return "8"
	if entry=="111101": return "9"
	if entry=="111110": return "=+"
	if entry=="111111": return "/"

def hex_to_base64(s):

#OBJETIVO: Converter o 'HEX ENCODED' para 'BASE64 ENCODED'

	s = decode_hex_ascii(s) #Decodificar os caracteres HEXADECIMAL para os caracteres da tabela ASCII
	binary_s = "" #Os caracteres decodificados são concatenados aqui
	for i in s:
		t = ascii_to_binary(i)
		if len(t)==8:
			binary_s = binary_s + ascii_to_binary(i)
		else: 	
			binary_s = binary_s + "0" + ascii_to_binary(i)	
	
	base64_s = "" #Os caracteres convertidos para a BASE64 são concatenados aqui
	temp = "" #String sempre que possível com tamanho 6 para a conversão
	for i in binary_s:
		if len(temp)==6:
			base64_s = base64_s + binary_to_char_base64(temp)

			temp = i
		else:
			temp = temp + i
	if len(temp)==6:
			base64_s = base64_s + binary_to_char_base64(temp)

			temp = ""
	elif len(temp)>0:
		while len(temp)<6:
			temp = temp + "0"
		base64_s = base64_s + binary_to_char_base64(temp)

	return base64_s

def hex_to_binary(entry):

#OBJETIVO: Converter UM caracter Hexadecimal em binário
#Retorna o binário correspondente ao caracter

	if entry=="0": return "0000"
	if entry=="1": return "0001"
	if entry=="2": return "0010"
	if entry=="3": return "0011"
	if entry=="4": return "0100"
	if entry=="5": return "0101"
	if entry=="6": return "0110"
	if entry=="7": return "0111"
	if entry=="8": return "1000"
	if entry=="9": return "1001"
	if entry=="A": return "1010"
	if entry=="B": return "1011"
	if entry=="C": return "1100"
	if entry=="D": return "1101"
	if entry=="E": return "1110"
	if entry=="F": return "1111"

def binary_to_hex (entry):

#OBJETIVO: Converter binário em um caracter hexadecimal
#Retorna o hexadecimal correspondente ao binário

	if entry=="0000": return "0"
	if entry=="0001": return "1"
	if entry=="0010": return "2"
	if entry=="0011": return "3"
	if entry=="0100": return "4"
	if entry=="0101": return "5"
	if entry=="0110": return "6"
	if entry=="0111": return "7"
	if entry=="1000": return "8"
	if entry=="1001": return "9"
	if entry=="1010": return "A"
	if entry=="1011": return "B"
	if entry=="1100": return "C"
	if entry=="1101": return "D"
	if entry=="1110": return "E"
	if entry=="1111": return "F"

def decode_hex_to_binary(s):

#OBJETIVO: Converter a cadeia inteira de caracteres hexadecimais em binário
#Utiliza-se a função "hex_to_binary" para uma conversão individual e retorna os vários resultados de forma concatenada

	s = s.upper()
	binary_s = ""
	for i in s:
		binary_s = binary_s + hex_to_binary(i)
	return binary_s

def fixed_xor(a,b):
# OBJETIVO: Fazer o XOR de duas strings hexadecimais e retornar no mesmo formato

	a_b, b_b = decode_hex_to_binary(a), decode_hex_to_binary(b) #Transformar ambas as strings dadas em binário
	res = "" #É realizada uma verificação conjunta nas duas strings em binário, realizando o xor entre os BITs com o mesmo index na string e concatenando com a descoberta anterior
	for i in range(len(a_b)):
		la, lb = a_b[i], b_b[i]
		if la=="0" and lb=="0": res = res + "0"
		elif la=="0" and lb=="1": res = res + "1"
		elif la=="1" and lb=="0": res = res + "1"
		elif la=="1" and lb=="1": res = res + "0"
	
	splitted_res = [res[i:i+4] for i in range(0, len(res), 4)] #Cria uma lista em que cada 4 caracteres de 'res' correspodente a um item da mesma 
	final_hex = ""
	for i in splitted_res:
		final_hex = final_hex + binary_to_hex(i)
	return final_hex


#Desafio 1
print hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")

#Desafio 2
print fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
