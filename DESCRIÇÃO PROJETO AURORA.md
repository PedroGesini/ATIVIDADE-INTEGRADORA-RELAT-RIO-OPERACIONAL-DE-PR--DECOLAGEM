MISSÃO AURORA SIGER

Introdução

O projeto de decolagem da Aurora Siger consiste em um sistema de telemetria autonômo, desenvolvido na linguagem Python e no ambiente do Google Colab, que realiza análises de riscos para a missão. Esse projeto visa uma precisão absoluta na fiscalização das variáveis externas e operacionais, de modo que a integridade da tripulação e do hardware sejam preservadas.

Especificações técnicas e geração de dados

O sistema utilzou uma lógica avançada de programação que opera com base em um banco de baterias de alta densidade, contendo uma voltagem de 400V, capacidade de 25.000 Ah, a energia total de 36 bilhões de Joules e uma biblioteca para a simulação dos dados de sensores, a fim de que o sistema autônomo desenvolvido seja capaz de avaliar se a nave deve ou não realizar a decolagem.

Lógica do algoritmo

O projeto aplica dois conceitos fundamentais de engenharia e computação:

- Fail-Safe: todos as variáveis analisadas devem estar dentro dos conformes, caso contrário, a decolagem é abortada imediatamente para preservar a tripulação.
- Autonomia pós-voo: o algoritmo realiza dois processos de conversão, primeiro transforma a carga atual, que está em porcentagem, em valores absolutos de kWh. Posteriormente, ocorre a devida conversão para Joules, se enquadrando no Sistema Internacional de Unidades. Com a carga atual em kWh, o sistema realiza o cálculo de autonomia, em que se subtrai da carga atual, as perdas energéticas e o consumo de decolagem. Para a missão ser realizada, a carga atual não deve ser inferior a 6.000 kWh (60%) e a autonomia deve ser maior que zero.

Cenário A: abortagem da missão

<img width="793" height="733" alt="Cenário A - Aborto (print_aborto" src="https://github.com/user-attachments/assets/d4c3ff18-d326-4494-a88e-5151263d1f51" />

Cenário B: missão bem-sucedida

<img width="781" height="678" alt="Cenário B - Sucesso (print_sucesso" src="https://github.com/user-attachments/assets/4ffe4963-ccc9-4e18-8ae6-a00db7e73a42" />

Instruções de execução

Acesse o arquivo Missão_Aurora_Siger.ipynb neste repositório.

- Clique no botão "Open in Colab" ou faça o upload do arquivo no Google Colab.

- Vá em Ambiente de Execução > Executar tudo.

- O sistema gerará dados aleatórios via biblioteca random e apresentará o painel de controle final com o veredito de segurança.
