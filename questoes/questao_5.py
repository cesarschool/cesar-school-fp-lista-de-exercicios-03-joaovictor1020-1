## QUESTÃO 5 ##
#
# Crie uma implementação da cifra rotacional, às vezes também chamada de cifra de César.
# 
# A cifra de César é uma simples cifra de deslocamento que se baseia na transposição 
# de todas as letras do alfabeto usando uma chave inteira entre 0 e 26. 
# O uso da chave 0 ou 26 sempre produzirá a mesma saída devido à aritmética modular. 
# A letra é deslocada para tantos valores quanto o valor da chave.
#
# A notação geral para cifras rotacionais é ROT + <chave>. A cifra rotacional mais comumente usada é a ROT13.
#
# Um ROT13 no alfabeto latino seria o seguinte:
# 	Normal:  abcdefghijklmnopqrstuvwxyz
#	Cifrado: nopqrstuvwxyzabcdefghijklm
#
# Exemplos:
#	Entrada: ROT5 omg 
#          Saída: trl
#	Entrada: ROT0 c 
#          Saída: c
#	Entrada: ROT26 Cool 
#          Saída: Cool
#	Entrada: ROT13 The quick brown fox jumps over the lazy dog. 
#          Saída: Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
#	Entrada: ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. 
#          Saída: The quick brown fox jumps over the lazy dog.
#
# Se um valor de entrada inválido for digitado, a seguinte mensagem 
# deve ser impressa: 'Erro'. 
# Entradas inválidas podem ser entradas que contém códigos de rotações 
# inválidos ou mensagens contendo caracteres que não estão no alfabeto. 
# Exemplos:
# 	Entrada: RARA abc Saída: Erro
# 	Entrada: ROT5 c99 Saída: Erro
#
# As entradas devem ser sempre compostas por ROT + <chave> + ' ' + 'mensagem', 
# ou seja, a cifra rotacional e a mensagem a ser cifrada separados por vírgula.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    
maximo = 26
 
 
def getTranslatedMessage(mensagem, chave):
    traducao = ''
 
    for simbolo in mensagem:
         if simbolo.isalpha():
             num = ord(simbolo)
             num += chave
             if simbolo.isupper():

                if num > ord('Z'):
                     num -= 26
 
                elif num < ord('A'):
                     num += 26
 
            elif simbolo.islower():
 
                if num > ord('z'):
                     num -= 26
 
                elif num < ord('a'):
                     num += 26
             traducao += chr(num)
 
        else:
 
            traducao += simbolo
 
    return traducao
 
 
check = 0
chaveinput = input('Digite o ROT que deseja + a frase que deseja codificar: ')
rot = chaveinput.split(' ', 1)
chaves = rot[0].split('ROT', 1)
if chaves[0] != '':
    print('Error')
 
else:
    chave1 = chaves[1]
    die = rot[1]
    for i in rot[1]:
        if i.isnumeric() == True:
            check = 1
        else:
            continue
    if (chave1.isnumeric() == False) or (int(chave1) < 0 or int(chave1) > maximo) or (check == 1):
        print('Error')
 
 
    else:
        chave = int(chave1)
        print(getTranslatedMessage(die, chave))


    
if __name__ == '__main__':
    main()
