# Arquitetura de Redes e Internet das Coisas (IoT): Guia de Conteúdo Técnico

## 1. Conteúdo de Aula: Infraestrutura de Redes

### Componentes de Hardware
* Dispositivos finais para consumo e geração de dados.
* Dispositivos intermediários para roteamento e comutação de pacotes.
* Meios de transmissão físicos cabeados e tecnologias sem fio.

### Topologias e Meios
* Organização física e lógica dos nós na rede.
* Cabos de par trançado e fibra óptica para conexões estruturadas.
* Espectro de radiofrequência para comunicação de dados móveis.

---

## 2. Conteúdo de Aula: Arquitetura de Redes

### Modelo OSI e TCP/IP
* Divisão da comunicação em camadas lógicas independentes.
* Modelo OSI com sete camadas para padronização conceitual.
* Modelo TCP/IP com quatro camadas focado na internet.

### Endereçamento e Roteamento
* Protocolo IP para identificação única de hosts na rede.
* Transição global do protocolo IPv4 para o padrão IPv6.
* Roteadores para encaminhamento de pacotes entre sub-redes distintas.

---

## 3. Conceitos de Internet das Coisas (IoT)

### Fundamentos
* Conexão de objetos físicos do mundo real à internet.
* Integração entre sistemas embarcados, sensores e redes de dados.
* Coleta de dados em tempo real para tomada de decisões.

### Componentes de um Sistema IoT
* Sensores para captação de grandezas físicas do ambiente.
* Atuadores para execução de ações mecânicas ou elétricas.
* Microcontroladores para processamento local e envio de dados.

---

## 4. Comunicação e Protocolo MQTT

### Arquitetura do Protocolo
* Protocolo leve baseado no modelo de publicação e assinatura.
* Broker central para gerenciamento e distribuição de mensagens.
* Clientes IoT atuando como publicadores ou assinantes de tópicos.

### Qualidade de Serviço (QoS)
* Nível 0: Entrega padrão sem confirmação de recebimento.
* Nível 1: Garantia de entrega de pelo menos uma vez.
* Nível 2: Garantia de entrega exata de apenas uma vez.