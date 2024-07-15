# Metrics Models

## Como Executar

### Pré-requisitos
Antes de executar o script, certifique-se de ter o seguinte instalado no seu sistema:
- Python 3.12.2
- Visual Studio Code ou qualquer outro editor de texto com suporte a terminal (por exemplo, Sublime Text, Atom)
- Acesso ao prompt de comando (Windows) ou terminal (macOS/Linux)

### Configurações do Script

O arquivo `utils.py` contém algumas constantes que podem ser alteradas para atender às suas necessidades específicas. Estas constantes estão relacionadas ao caminho dos arquivos de entrada e saída, bem como às colunas e classificadores utilizados.


Aqui estão as constantes que podem ser alteradas:

<span style="color: red;">**Importante:** </span> Somente este bloco de código deve ser alterado para modificar as configurações do script. Não altere outras partes do código para evitar possíveis erros de execução.

`INPUT_PATH`: Caminho onde está o arquivo .csv de saída do WEKA.

`OUTPUT_PATH`: Caminho para salvar o arquivo com as médias e desvios calculados.

`COLUMNS_TARGET`: Lista de colunas para as quais as métricas serão calculadas.

`LABELS_ROWS`: Ordem dos classificadores utilizados.

`SIZE_INTERACTION`: Número de interações por classificador (número de repetições x folds).

### Passos para Executar avg_std.py

1. **Abra o Editor de Texto**;
    
2. **Abra a Pasta do Projeto**;

3. **Abra o Terminal**;

5. **Execute o Script**:
    - Execute o script digitando o seguinte comando:
      ```bash
      python3 avg_std.py
      ```

## Resolução de Problemas

- **Python Não Encontrado**:
  - Certifique-se de que o Python está instalado e adicionado ao PATH do seu sistema.
  - Verifique a instalação executando:
    ```bash
    python --version
    ```
    ou
    ```bash
    python3 --version
    ```

- **Problemas de Permissão**:
  - Certifique-se de que você tem as permissões necessárias para executar o script. Pode ser necessário usar `sudo` no macOS/Linux:
    ```bash
    sudo python3 avg_std.py
    ```

- **Erros no Script**:
  - Se o script não funcionar, verifique as mensagens de erro no terminal para obter pistas. Problemas comuns incluem erros de sintaxe, módulos ausentes ou caminhos incorretos.