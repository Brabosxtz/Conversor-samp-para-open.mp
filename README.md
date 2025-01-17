# ⚙️ **Conversor samp para open.mp**  

**Termux Pawn** é uma solução prática para converter sua gamemode samp para open.mp

## ✨ **Funcionalidades Principais**  
- **Gamemodes**: Converte a pasta gamemodes.
- **Filterscripts**: Converte a pasta gamemodes.
- **Plugins**: Converte os plugins para open.mp.
- **Includes**: Converte as includes.
- **Server.cfg**: Converte o server.cfg para config.json.
- **Backup**: Cria backup da gamemode antes da conversão.
- **Linguagens**: Disponivel em 4 linguagens português,ingles,espanhol,russo.
---

## 🔧 **Pré-requisitos**  
1. **Termux**: Baixe e instale a versão mais recente do Termux.  
   **[Baixar o Termux aqui](https://f-droid.org/repo/com.termux_1020.apk)**  
## 📥 **Instalação**  

### 1️⃣ **Instalação**  
Execute o comando abaixo no Termux para adicionar o conversor:

```bash
curl https://raw.githubusercontent.com/Brabosxtz/ /install.sh | bash
```
### 2️⃣ **Modifique a linguagem**  
Troque a linguagem do conversor:  

```bash
convertomp -L 
```
Aparecerar:
```bash
convertomp -L                               ─╯
Please specify a language number after -L.
Available options are:

1. Inglês

2. Português

3. Espanhol

4. Russo
```
Para traduzir para português:
```bash
convertomp -L 2
```
---

## 📘 **Configuração do Compilador PAWN**  

O PAWN oferece diversas opções para personalizar o comportamento do compilador. Você pode configurá-las usando um arquivo de especificação.

### 🛠️ **Opções do Compilador**  
| **Opção** | **Comando**                                                                                                                                      | **Serventia**                                                                 |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| `arquivo.pwn`     |  `comvertomp <arquivo.pwn>`                                                    | Utilize esse comando para converter a gamemode pro open.mp |
| `-L`      | Idioma do compilador: `1` (ingles), `2` (português), `3` (espanhol), `4` (russo).                                                     | Utilize `-L 2` para usar o idioma **Português Brasileiro**. |
| `pasta modulos`      | Compatibilidade com modulos antigos. Permite incluir arquivos várias vezes, útil para includes como `y_hooks`.                                    | **Ative** (`-Z+`) se usar includes antigos.                                      |
## 📜 **Licença**  
Este projeto está sob a licença **MIT**.  
