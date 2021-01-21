# Chat-With-Sockets

Projeto final de Redes de computadores (COMP368-M).

* Implementação de um chat com sockets de rede (baseado no protocolo SMTP / Email).
* Dupla: Michael Miller Rodrigues Cardoso, Michel Thomas Gomes Lins.

Tutorial para utilizar o chat:

* 1 - Execute o arquivo `server.py`;
* 2 - Execute os arquivos `client.py`, `client_2.py`, `client_3.py` e `client_4.py`, todos vão iniciar uma interface Tkinter;
* 3 - Cadastre o nome de usuário nos 4 clientes (botão: enviar nome) para ativar o envio de mensagens;
* 4 - Agora você pode trocar mensagens(emails) de um cliente para o outro, ou para si mesmo!
* 5 - No campo destinatário basta inserir o nome do usuário que vai receber o email;
* 6 - O campo assunto é opcional e o campo mensagem é obrigatório.
* 7 - As mensagens(emails) são listadas na caixa de entrada.

Obs: A implementação suporta N clientes, caso queira testar com um número maior, basta duplicar o arquivo `client.py`.
Obs2: Foi aplicado o uso de threads.
