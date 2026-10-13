FilaSimples — Sistema de Distribuição de Senhas

1. Descrição do projeto

O FilaSimples é um programa desenvolvido em Python para organizar a emissão e a chamada de senhas de atendimento. O sistema permite gerar senhas normais e prioritárias, chamar a próxima senha e consultar a quantidade de pessoas aguardando atendimento.
O projeto utiliza o paradigma imperativo e funciona por meio de um menu no terminal, sem necessidade de interface gráfica ou banco de dados.

2. Objetivo

Desenvolver um sistema simples de gerenciamento de senhas, aplicando os conceitos do paradigma imperativo, como variáveis, atribuições, estruturas condicionais e de repetição.

3. Funcionalidades

    * Emitir senhas normais e prioritárias.

    * Gerar senhas com numeração sequencial (N001, N002, P001, P002...).

    * Chamar a próxima senha, dando preferência às prioritárias.

    * Consultar a quantidade de senhas pendentes e atendimentos realizados.

    * Informar quando não houver senhas aguardando atendimento.

    * Encerrar o programa pelo menu principal.


4. Regras de funcionamento

    * As senhas normais começam com N e as prioritárias com P.

    * Cada categoria possui sua própria sequência numérica.

    * As senhas são chamadas na ordem de emissão dentro de cada categoria.

    * As senhas prioritárias são chamadas antes das normais.

    * Após a chamada, a senha é removida da fila.

    * As informações são armazenadas apenas durante a execução do programa.

5. Instruções de uso

Requisito: Python 3 instalado no computador.

Para executar:

Baixe ou clone o repositório do projeto.
Abra a pasta FilaSimples no terminal.

Execute o comando:

python filasimples.py ou dê play no arquivo utilizando o VS Code.

No menu apresentado, escolha uma das opções:

1: Emitir senha normal.

2: Emitir senha prioritária.

3: Chamar próxima senha.

4: Consultar senhas pendentes.

5: Sair do programa.

O menu continuará disponível até que a opção 5 seja selecionada.

6. Lógica imperativa utilizada

O programa utiliza o paradigma imperativo, no qual as instruções são executadas em sequência e modificam os valores armazenados nas variáveis ao longo da execução.

Os principais conceitos utilizados são:

Variáveis e atribuições: armazenam e atualizam os contadores de senhas e o total de atendimentos realizados.

Listas: armazenam as senhas normais e prioritárias que aguardam atendimento.

Estruturas condicionais (if, elif, else): verificam a opção selecionada no menu e determinam qual fila deverá ser atendida.

Estrutura de repetição (while): mantém o programa em funcionamento até que o usuário escolha sair.

Alteração de estado: ocorre quando os contadores são incrementados, novas senhas são adicionadas às listas e senhas chamadas são removidas por meio do método pop(0).

Dessa forma, o FilaSimples demonstra a aplicação do paradigma imperativo na resolução de um problema simples de organização de atendimentos.

7. Melhorias a implementar

* Implementar a possibilidade de impressão da senha.
* Construção de um front-end a fim de melhorar experiência do usuário.