# Tradutor em python

<div align="center">
<h1>--JB Tradutor--</h1>
</div>

## Descrição:
Um programa de tradução com interface grafica, sendo feita a utilização da API googletran,para a tradução do texto, pyperclip, para fazer a copia da tradução para a área de tranferência e a biblioteca do TKinter, para ser desenvolvida a interface grafica do projeto.

## Pré-requisitos:
Certifica-se de ter os seguintes pacotes instalados antes de executar o programa:
- `Googletrans`
-  `TKinter`
-  `pyperclip`

## Como usar:


## Funcionalidades:
- O programa permite selecionar o idioma de origem e o idioma de destino para a tradução.
- Digite o texto que deseja traduzir no campo de entrada e clique no botão "Traduzir" para obter a tradução.
- O texto traduzido será exibido no campo de saída.
- O botão "Copiar" permite copiar o texto traduzido para a área de transferência.


## importações:
- `Googletrans` - API do gooogle para traduçao de texto em diversos idiomas. 
- `TKinter` - Biblioteca para desenvolvimento de interface gráfica, sendo utilizada de forma para melhor visualização e compreensão do projeto.
- `Pyperclip` - Biblioteca para usar um metodo, contido na biblioteca para copiar a tradução para a área de transferência.

## Como funciona o código:
O código é feito em sistema com interface gráfica.
 - O código começa com um a varivael janela sendo inciada com um TK(), que inicia a interface 
 - Encerra com um main.loop() que é onde reinicia o loop da janela e atualliza a interface.

## Cores:
São cinco váriaveis, onde nelas estão contidas as cores em hexadecimal, que são usadas na interface:
- Cor1 - Cor preta
- Cor2 - Cor branca  
- Cor3 - Cor azul fosco
- Cor4 - Cor azul escuro
- Cor5 - Cor azul claro 

## Metodos:
São três metodos que são utilizados para organização, implementação e de forma funcional para desenvolver o sistama, são eles:
- `centralizar_janela` - função que centraliza a abertura da janela no meio da tela, por meio de um calculo e de informações da sua tela e que se adapta de acordo com o tamanho do seu monitor.
- `traducao` - Função que faz todo o sistama de tradução do programa, onde faz o uso da API e recebe os idiomas selecionados por meio do metodo get e faz a sua tradução
- `copiar` - Fução que faz a copia da tradução para a sua área de tranferência quando presionado o botão de copia.

