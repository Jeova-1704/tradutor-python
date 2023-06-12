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
### Primeiro passo:
![Captura de tela_20230610_200301](https://github.com/Jeova-1704/tradutor-python/assets/127805808/06254052-897b-43f5-8d4f-bc14057255a7)
- Inicializar o uso do programa e abrir ele.

### Segundo passo:
![Captura de tela_20230610_200319](https://github.com/Jeova-1704/tradutor-python/assets/127805808/a148a3b3-8aa1-40c5-a9d7-87b57e31aea6)
- Escolhar qual o idioma de origem e para qual idioma você deseja fazer a tradução.

### Terceiro passo:
![Captura de tela_20230610_200357](https://github.com/Jeova-1704/tradutor-python/assets/127805808/fef53a98-7252-44d2-a701-4260e8597e77)
- Apertar em 'Traduzir' e esperar o sistema processar o requeremento da API, para poder traduzir e fazer aparecer na tela.

### Quarto passo:
![Captura de tela_20230610_200429](https://github.com/Jeova-1704/tradutor-python/assets/127805808/e5618b5a-b278-4cda-932d-f4a8de0e66cb)
- Após isso você pode fazer o sistema de copia para a sua área de tranferência e assim poder usar a sua frase traduzida.

## Funcionalidades:
- O programa permite selecionar o idioma de origem e o idioma de destino para a tradução.
- Digite o texto que deseja traduzir no campo de entrada e clique no botão "Traduzir" para obter a tradução.
- O texto traduzido será exibido no campo de saída.
- O botão "Copiar" permite copiar o texto traduzido para a área de transferência.

## Idiomas suportados:
- `en` - Inglês
- `pt` - Português
- `fr` - Frances
- `de` - Alemão
- `it` - Italiano
- `ja` - Japonês
- `ru` - Russo
- `es` - Espanhol



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

## Notas
- Certifique-se de estar conectado à Internet para que o programa possa acessar a API do Google Translate.
- Nem todos os idiomas são suportados pela API do Google Translate. Verifique a documentação para obter a lista completa dos idiomas suportados.

Espero que esta documentação ajude você a entender e utilizar o JB Tradutor. Em caso de dúvidas ou problemas, sinta-se à vontade para entrar em contato.

<h2>Sinta-se traduzido!</h2>