Simular um sistema de painel de atendimento

Cenário

 - Senhas sequenciais vão sendo obtidas, ao passo que são enfileiradas pelo sistema
 - O sistema acumula essas senhas em uma fila do tipo FIFO
 - A medida que são 'chamadas' as senhas, estas vão sendo removidas e armazenadas em uma lista auxiliar

Implementação
- Criar um menu com as opções:
 1) Obter nova senha
 2) Chamar próxima senha
 3) Mostrar senhas chamadas

Detalhamento
- Obter nova senha
  - Deverá ter um contador no app que começo com o valor zero
  - Ao chamar uma senha, deverá enfileirar o próximo valor na estrutura Fila e incrementar este contador

- Chamar próxima senha
  - Acrescentar numa variável (list) no app, antes de remover da Fila, qual a senha que será chamada.
  - Remover da Fila (usar o método dequeue)

- Mostrar senhas chamadas
  - Apresentar o valor armazenado em uma lista (list) durante a remoção do item da Fila
