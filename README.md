---

# 🚀 ConvertOMP

Ferramenta para converter projetos SA:MP em Open.MP com suporte multilíngue, backup automático, organização de includes/plugins e muito mais.

---

## ✅ Requisitos

- Python 3.8+
- Conexão com a internet
- Executar dentro da pasta `gamemodes`

---

## 🧠 Instalação

```bash
pkg install python
python install convertomp
```
---

🌍 Idioma

Defina o idioma com:
```bash
python convertomp.py -L <número>

Número	Idioma

1	Inglês
2	Português
3	Espanhol
4	Russo

```

---

⚙️ Como usar
```bash
cd /sdcard/download/MyProject/gamemodes

convertomp <arquivo.pwn> opcional:[pasta_modulos]
```
---

🛠️ O que ele faz

📦 Cria backup automático (/backups/)

🔁 Converte funções SA:MP → Open.MP

🧩 Instala plugins do GitHub (via server.cfg)

📁 Organiza pastas:

qawno/include

plugins/

components/


🧼 Converte includes, filterscripts, plugins 

📝 Atualiza config.json



---

✨ Exemplo de Conversão

// Antes
SetTimer("Func", 1000, 0);

// Depois
SetTimer("Func", 1000, false);


---

🧩 Plugins e Includes

Detecta plugins do server.cfg e baixa automaticamente

Converte .inc e .pwn em filterscripts/ e pawno/include/



---

⚠️ Importante

Execute dentro da pasta gamemodes

Includes como dini e DOF2 são bloqueados

Verifique permissões e caminhos



---
