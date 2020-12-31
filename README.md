# PythonOps

Scripts desenvolvidos para operações em sistemas Operativos, Docker containers e Cloud.


# Bibliotecas
- São uma coleção de módulos de scripts, desenvolvidos para facilitar o processo de desenvolvimento, evitando a necessidade de reescrever os comandos mais utilizados.

####  Tipos
- Padrão do Python - built-in
- Bibliotecas externas - Podem ser instaladas através do PIP

# PIP
- Gestor de pacotes
- Sintaxe

**python3 -m pip** = chama o módulo pip
**pip install <_NOME_>** = Instala pacote
**pip uninstall <_NOME_>** = Desinstala pacote
**pip list** = Lista os pacotes instalados.
**pip freeze > requirements.txt** = Exporta os pacotes instalados para um ficheiro
**pip install -r requirements.txt** = Instala os pacotes a partir do ficheiro.

# Virtualenv
- Permite que cada ambiente tenha autonomia de instalar bibliotecas de forma que não tenha impacto nos restantes ambientes.

- **Instalação**
		python3 -m pip install virtualenv

- **Criação**
		python3 -m venv .venv

- **Ativar / Desactivar**
		source .venv/bin/activate / deactivate

python3 -m venv .venv
source .venv/bin/activate
deactivate
