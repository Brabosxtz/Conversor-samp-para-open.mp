# ⚙️ **Conversor samp para open.mp**  

**convertomp** é uma solução prática para converter sua gamemode samp para open.mp

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
curl https://raw.githubusercontent.com/Brabosxtz/Conversor-samp-para-open.mp/main/install.sh | bash
```
### 2️⃣ **Modifique a linguagem**  
Troque a linguagem do conversor:  

```bash
convertomp -L 
```
Aparecerá:
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

## 📘 **Configuração do Conversor**  

O Conversor oferece 2  opções para uso

### 🛠️ **Opções**  
| **Opção** | **Comando**                                                                                                                                      | **Serventia**                                                                 |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| `arquivo.pwn`     |  `comvertomp <arquivo.pwn>`                                                    | Utilize esse comando para converter a gamemode pro open.mp |
| `-L`      | Idioma do conversor: `1` (ingles), `2` (português), `3` (espanhol), `4` (russo).                                                     | Utilize `-L 2` para usar o idioma **Português Brasileiro**. |
| `pasta modulos`      | opcional,ele ja tem a configuração para buscar tanto a pasta `modulos` ou `modules`   | **Ative** (`convertomp <arquivo.pwn> <../pasta>`) se o nome do modulos for diferente de modulos/modules                               |
## 📜 **Licença**  
Este projeto está sob a licença **MIT**.  
