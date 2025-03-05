import subprocess
import sys
import time
import threading
from tqdm import tqdm

# Função para a animação da barra de progresso
def show_progress_bar():
    with tqdm(total=100, desc="Installing", ncols=100, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}") as pbar:
        while installing:
            pbar.update(1)
            time.sleep(0.1)

# Função para executar o pip install
def install_package():
    global installing
    try:
        # Rodando o pip install em um processo separado e redirecionando a saída para PIPE para não mostrar no terminal
        subprocess.check_call([sys.executable, "-m", "pip", "install", "convertomp"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("\nErro ao instalar o pacote.")
    finally:
        installing = False
        print("\rInstallation complete!")

# Variável global que controla a animação
installing = True

def main():
    print("Iniciando instalação do pacote 'convertomp'...\n")
    
    # Inicia a barra de progresso em uma thread separada
    animation_thread = threading.Thread(target=show_progress_bar)
    animation_thread.start()
    
    # Executa o pip install
    install_package()
    
    # Espera a animação terminar
    animation_thread.join()

if __name__ == "__main__":
    main()
