FilaSimples — Sistema Simplificado de Distribuição e Chamada de Senhas

1. Descrição do problema

    Em locais que realizam atendimento ao público, como clínicas, laboratórios e repartições públicas, é necessário organizar a ordem de atendimento das pessoas. Quando não existe um controle adequado, podem ocorrer situações como desorganização das filas, chamadas fora de ordem e dificuldades para diferenciar atendimentos normais e prioritários.
    Pensando nesse problema, o projeto FilaSimples propõe o desenvolvimento de um sistema básico de distribuição e chamada de senhas, permitindo organizar os atendimentos de forma simples.
    O programa será desenvolvido em Python, utilizando o paradigma imperativo, com execução por meio de um menu no terminal. O sistema permitirá emitir senhas normais e prioritárias, chamar a próxima senha disponível e consultar a quantidade de pessoas aguardando atendimento.
    O funcionamento será baseado em uma sequência de instruções, utilizando variáveis para armazenar informações, estruturas condicionais para verificar as regras de atendimento e estruturas de repetição para manter o programa em funcionamento.

2. Objetivo geral

    Desenvolver um sistema simples de gerenciamento de senhas de atendimento utilizando Python e os conceitos do paradigma imperativo, permitindo controlar a emissão e a chamada de senhas normais e prioritárias.

3. Objetivos específicos

    * Implementar um menu textual para interação com o usuário.

    * Permitir a emissão de senhas normais e prioritárias.

    * Organizar a chamada das senhas conforme a ordem de emissão e o tipo de atendimento.

    * Priorizar as senhas de atendimento prioritário em relação às senhas normais.

    * Permitir a consulta da quantidade de senhas que ainda aguardam atendimento.

    * Aplicar variáveis, atribuições, estruturas condicionais, estruturas de repetição e funções na implementação do programa.

4. Requisitos funcionais


    RF01 — O sistema deverá permitir a emissão de senhas para atendimento normal, atribuindo uma numeração sequencial a cada nova senha.

    RF02 — O sistema deverá permitir a emissão de senhas prioritárias, utilizando uma sequência de numeração própria para diferenciá-las das senhas normais.

    RF03 — O sistema deverá permitir a chamada da próxima senha, respeitando a ordem de emissão dentro de cada categoria e dando preferência às senhas prioritárias.

    RF04 — O sistema deverá apresentar a quantidade de senhas normais e prioritárias que ainda aguardam atendimento.

    RF05 — O sistema deverá apresentar uma mensagem quando o usuário tentar chamar uma senha e não houver pessoas aguardando atendimento.

    RF06 — O sistema deverá disponibilizar uma opção para encerrar sua execução.


5. Regras de funcionamento


    1. As senhas normais serão identificadas pela letra N, seguida de uma numeração sequencial, como N001, N002 e N003.

    2. As senhas prioritárias serão identificadas pela letra P, seguida de uma numeração sequencial, como P001, P002 e P003.

    3. As senhas serão chamadas respeitando a ordem em que foram emitidas dentro de cada categoria.

    4. Havendo senhas prioritárias pendentes, elas serão chamadas antes das senhas normais.

    5. Após a chamada, a senha será retirada da fila de espera.

    6. Caso não existam senhas pendentes, o programa deverá informar que a fila está vazia.

    7. O sistema continuará funcionando até que o usuário selecione a opção de encerramento.




