import re, sys, os, time, threading, zipfile, requests, mediafire_dl, shutil, json, random, traceback,importlib.resources as pkg_resources
from bs4 import BeautifulSoup
from datetime import datetime

translations = {
    "en": {
        "language_prompt": "Select a language:",
        "invalid_option": "Invalid language option. Available options are:",
        "please_specify": "Please specify a language number after -L.",
        "dof2_1": "DOF2? Really? What a shame...", 
        "dof2_2": "In the middle of 2025 using DOF2? Go back to SA-MP 0.2",
        "dof2_3": "DOF2 is like using Internet Explorer in 2025",
        "dof2_4": "SQLite exists, you know? DOF2 is a thing of the past",
        "dof2_5": "I can't believe you still use DOF2... What a disappointment",
        "dini_1": "DINI? Are you still living in 2010?",  
        "dini_2": "Please, tell me this Dini is a joke",  
        "dini_3": "SQLite, MySQL, ever heard of them? Dini is prehistoric",  
        "dini_4": "Dini in 2025? Do you also use Windows XP?",  
        "dini_5": "I smell outdated includes... Oh, it's Dini!",
        "not_found": "{plugin_name} not found, looking for another...",
        "fatal_error": "FATAL ERROR: ROTTEN INCLUDES FOUND",
        "professional_tip": "Pro tip: Use SQLite or MySQL instead of Dof2 and Dini",
        "advantages": "Advantages",
        "fast_efficient": "Faster and more efficient",
        "safe_reliable": "Safer and more reliable",
        "complex_queries": "Supports complex queries",
        "does_not_corrupt": "Does not corrupt data",
        "industry_standard": "Industry standard",
        "no_rotten_includes": "Congratulations! No rotten includes found.",
        "converting_plugin": "\033[34mConverting plugin {plugin_name} to open.mp\033[0m",
        "plugin_converted": "Plugin {plugin_name} converted to open.mp",
        "error_processing_plugin": "Error processing plugin: {e}",
        "finished": "Finished",
        "downloading_gm": "\033[34mDownloading gamemode from open.mp\033[0m",
        "error_extracting_gm": "Error extracting gamemode: {e}",
        "backup_created": "Backup created successfully: {backup_path}",
        "error_creating_backup": "Failed to create backup file",
        "error_creating_backup_details": "Error creating backup: {e}",
        "converting_filterscripts": "\033[34mConverting filterscripts\033[0m",
        "filterscripts_converted": "Successfully converted {files_converted} filterscript(s)",
        "error_filterscripts": "Error converting filterscripts: {e}",
        "config_not_found": "{search_line} not found in server.cfg",
        "error_updating_config": "Error updating config: {e}",
        "copying_includes": "\033[34mCopying include files\033[0m",
        "includes_copied": "Successfully copied {files_copied} include files to qawno/include",
        "removing_pawno": "\033[34mRemoving pawno directory\033[0m",
        "pawno_removed": "Successfully removed pawno directory",
        "processing_includes": "\033[34mProcessing include files\033[0m",
        "include_converted": "Converted include file: {file}",
        "finished_processing_includes": "Finished processing include files",
        "no_includes_found": "No include files found to copy",
        "error_pawno_directory": "Error processing pawno directory",
        "error_replacing_bool": "Error in replacing bool: {e}",
        "error_sync_bool": "Error in replacing sync and bool: {e}",
        "file_not_found": "Error: file not found {input_file}",
        "loading_gamemode": "\033[33mLoading gamemode:\033[0m \033[34m{input_file}\033[0m",
        "file_converted": "Converted file: {input_file}",
        "no_changes": "File without changes: {input_file}",
        "error_message": "Error: {str(e)}",
        "gamemodes_folder": "This command can only be executed within the gamemodes folder.",
        "usage": "Usage: convertomp <arquivo.pwn> optional:[modules_folder]",
        "main_file_not_found": "Error: file not found: {main_file}",
        "project_name": "samp to open.mp converter 1.0.0\n",
        "creating_backup": "\033[34mCreating backup\033[0m",
        "failed_backup": "Failed to create backup. Conversion canceled",
        "updating_config_lines": "\033[34mChanging lines from server.cfg to config.json\033[0m",
        "modules_directory_not_found": "Error: directory not found: {modules_dir}",
        "converting_folder": "\033[34mConverting folder: {display_path}\033[0m",
        "conversion_complete": "Conversion completed for file: {main_file} in {elapsed_time:.2f} seconds.",
    },
    "pt": {
        "language_prompt": "Selecione um idioma:",
        "invalid_option": "Opção de idioma inválida. As opções disponíveis são:",
        "please_specify": "Por favor, especifique um número de idioma após -L.",
        "dof2_1": "DOF2? Sério mesmo? Que vergonha...", 
        "dof2_2": "Em pleno 2025 usando DOF2? Volta pro SA-MP 0.2",
        "dof2_3": "DOF2 é tipo usar Internet Explorer em 2025",
        "dof2_4": "SQLite existe, sabia? DOF2 é coisa do passado",
        "dof2_5": "Não acredito que você ainda usa DOF2... Que decepção",
        "dini_1": "DINI? Você ainda vive em 2010?",
        "dini_2": "Por favor, me diz que esse Dini é uma piada",
        "dini_3": "SQLite, MySQL, já ouviu falar? Dini é pré-histórico",
        "dini_4": "Dini em 2025? Você também usa Windows XP?",
        "dini_5": "Sinto cheiro de include defasada... Ah, é o Dini!",
        "not_found": "{plugin_name} não encontrado, procurando outro...",
        "fatal_error": "ERRO FATAL: INCLUDES PODRES ENCONTRADAS",
        "professional_tip": "Dica profissional: use SQLite ou MySQL em vez de Dof2 e Dini",
        "advantages": "Vantagens",
        "fast_efficient": "Mais rápido e eficiente",
        "safe_reliable": "Mais seguro e confiável",
        "complex_queries": "Suporta consultas complexas",
        "does_not_corrupt": "Não corrompe dados",
        "industry_standard": "Padrão da indústria",
        "no_rotten_includes": "Parabéns! Nenhuma inclusão podre encontrada.",
        "converting_plugin": "\033[34mConvertendo plugin {plugin_name} para open.mp\033[0m",
        "plugin_converted": "Plugin {plugin_name} convertido para open.mp",
        "error_processing_plugin": "Erro ao processar plugin: {e}",
        "finished": "Concluído",
        "downloading_gm": "\033[34mBaixando o gamemode do open.mp\033[0m",
        "error_extracting_gm": "Erro ao extrair modo de jogo: {e}",
        "backup_created": "Backup criado com sucesso: {backup_path}",
        "error_creating_backup": "Falha ao criar arquivo de backup",
        "error_creating_backup_details": "Erro ao criar backup: {e}",
        "converting_filterscripts": "\033[34mConvertendo filterscript\033[0m",
        "filterscripts_converted": "{files_converted} filterscript(s) convertido(s) com sucesso",
        "error_filterscripts": "Erro ao converter filterscripts: {e}",
        "config_not_found": "{search_line} não encontrado em server.cfg",
        "error_updating_config": "Erro ao atualizar configuração: {e}",
        "copying_includes": "\033[34mCopiando include\033[0m",
        "includes_copied": "Arquivos include {files_copied} copiados com sucesso para qawno/include",
        "removing_pawno": "\033[34mRemovendo diretório pawno\033[0m",
        "pawno_removed": "Diretório pawno removido com sucesso",
        "processing_includes": "\033[34mProcessando arquivos include\033[0m",
        "include_converted": "Arquivo de inclusão convertido: {file}",
        "finished_processing_includes": "Processamento finalizado de arquivos incluídos",
        "no_includes_found": "Nenhum arquivo incluído encontrado para copiar",
        "error_pawno_directory": "Erro ao processar o diretório pawno",
        "error_replacing_bool": "Erro ao substituir bool: {e}",
        "error_sync_bool": "Erro ao substituir sincronização e bool: {e}",
        "file_not_found": "Erro: arquivo não encontrado {input_file}",
        "loading_gamemode": "\033[34mCarregando gamemode:\033[0m \033[34m{input_file}\033[0m",
        "file_converted": "Arquivo convertido: {input_file}",
        "no_changes": "Arquivo sem alterações: {input_file}",
        "error_message": "Erro: {str(e)}",
        "gamemodes_folder": "Este comando só pode ser executado dentro da pasta gamemodes.",
        "usage": "Uso: convertomp <arquivo.pwn> opcional:[pasta_modulos]",
        "main_file_not_found": "Erro: arquivo não encontrado: {main_file}",
        "project_name": "Conversor de SA-MP para open.mp 1.0.0\n",
        "creating_backup": "\033[34mCriando backup\033[0m",
        "failed_backup": "Falha ao criar o backup. Conversão cancelada",
        "updating_config_lines": "\033[34mAlterando linhas de server.cfg para config.json\033[0m",
        "modules_directory_not_found": "Erro: diretório não encontrado: {modules_dir}",
        "converting_folder": "\033[34mConvertendo pasta: {display_path}\033[0m",
        "conversion_complete": "Conversão concluída para o arquivo: {main_file} em {elapsed_time:.2f} segundos.",
    },
    "ru": {
        "language_prompt": "Выберите язык:",
        "invalid_option": "Неверный вариант языка. Доступные варианты:",
        "please_specify": "Пожалуйста, укажите номер языка после -L.",
        "dof2_1": "DOF2? Серьезно? Какой позор...",
        "dof2_2": "В 2025 году использовать DOF2? Вернись к SA-MP 0.2",
        "dof2_3": "DOF2 — это как использовать Internet Explorer в 2025 году",
        "dof2_4": "SQLite существует, знаешь? DOF2 — это прошлое",
        "dof2_5": "Не могу поверить, что ты все еще используешь DOF2... Какое разочарование",
        "dini_1": "DINI? Ты все еще живешь в 2010 году?",
        "dini_2": "Пожалуйста, скажи, что этот Dini — это шутка",
        "dini_3": "SQLite, MySQL, ты слышал об этом? Dini — это доисторическое",
        "dini_4": "Dini в 2025 году? Ты еще используешь Windows XP?",
        "dini_5": "Чувствую запах устаревшего include... А, это же Dini!",
        "not_found": "{plugin_name} не найден, ищем другой...",
        "fatal_error": "ФАТАЛЬНАЯ ОШИБКА: ОБНАРУЖЕНЫ ПРОВАЛЕННЫЕ INCLUDES",
        "professional_tip": "Профессиональный совет: используйте SQLite или MySQL вместо Dof2 и Dini",
        "advantages": "Преимущества",
        "fast_efficient": "Быстрее и эффективнее",
        "safe_reliable": "Безопаснее и надежнее",
        "complex_queries": "Поддержка сложных запросов",
        "does_not_corrupt": "Не портит данные",
        "industry_standard": "Стандарт индустрии",
        "no_rotten_includes": "Поздравляем! Не найдено плохих includes.",
        "converting_plugin": "\033[34mКонвертируем плагин {plugin_name} для open.mp\033[0m",
        "plugin_converted": "Плагин {plugin_name} успешно конвертирован для open.mp",
        "error_processing_plugin": "Ошибка при обработке плагина: {e}",
        "finished": "Завершено",
        "downloading_gm": "\033[34mСкачивание режима игры для open.mp\033[0m",
        "error_extracting_gm": "Ошибка при извлечении режима игры: {e}",
        "backup_created": "Резервная копия успешно создана: {backup_path}",
        "error_creating_backup": "Ошибка при создании резервной копии",
        "error_creating_backup_details": "Ошибка при создании резервной копии: {e}",
        "converting_filterscripts": "\033[34mКонвертирование фильтров-скриптов\033[0m",
        "filterscripts_converted": "{files_converted} фильтров-скрипт(ов) успешно конвертированы",
        "error_filterscripts": "Ошибка при конвертации фильтров-скриптов: {e}",
        "config_not_found": "{search_line} не найдено в server.cfg",
        "error_updating_config": "Ошибка при обновлении конфигурации: {e}",
        "copying_includes": "\033[34mКопирование файлов include\033[0m",
        "includes_copied": "Файлы include {files_copied} успешно скопированы в qawno/include",
        "removing_pawno": "\033[34mУдаление каталога pawno\033[0m",
        "pawno_removed": "Каталог pawno успешно удален",
        "processing_includes": "\033[34mОбработка файлов include\033[0m",
        "include_converted": "Файл include конвертирован: {file}",
        "finished_processing_includes": "Обработка файлов include завершена",
        "no_includes_found": "Не найдено файлов include для копирования",
        "error_pawno_directory": "Ошибка при обработке каталога pawno",
        "error_replacing_bool": "Ошибка при замене bool: {e}",
        "error_sync_bool": "Ошибка при замене синхронизации и bool: {e}",
        "file_not_found": "Ошибка: файл не найден {input_file}",
        "loading_gamemode": "\033[34mЗагрузка режима игры:\033[0m \033[34m{input_file}\033[0m",
        "file_converted": "Файл конвертирован: {input_file}",
        "no_changes": "Файл без изменений: {input_file}",
        "error_message": "Ошибка: {str(e)}",
        "gamemodes_folder": "Эту команду можно выполнить только в папке gamemodes.",
        "usage": "Использование: convertomp <arquivo.pwn> opcional:[pasta_modulos]",
        "main_file_not_found": "Ошибка: файл не найден: {main_file}",
        "project_name": "Конвертер SA-MP для open.mp 1.0.0\n",
        "creating_backup": "\033[34mСоздание резервной копии\033[0m",
        "failed_backup": "Ошибка при создании резервной копии. Конвертация отменена",
        "updating_config_lines": "\033[34mИзменение строк из server.cfg в config.json\033[0m",
        "modules_directory_not_found": "Ошибка: каталог не найден: {modules_dir}",
        "converting_folder": "\033[34mКонвертирование папки: {display_path}\033[0m",
        "conversion_complete": "Конвертация завершена для файла: {main_file} за {elapsed_time:.2f} секунд.",
    },
    "es": {
        "language_prompt": "Selecciona un idioma:",
        "invalid_option": "Opción de idioma no válida. Las opciones disponibles son:",
        "please_specify": "Por favor, especifique un número de idioma después de -L.",
        "dof2_1": "DOF2? En serio? Qué vergüenza...",
        "dof2_2": "Usando DOF2 en pleno 2025? Vuelve a SA-MP 0.2",
        "dof2_3": "DOF2 es como usar Internet Explorer en 2025",
        "dof2_4": "Sabías que existe SQLite? DOF2 es cosa del pasado",
        "dof2_5": "No puedo creer que aún uses DOF2... Qué decepción",
        "dini_1": "DINI? Todavía vives en 2010?",
        "dini_2": "Por favor, dime que este Dini es una broma",
        "dini_3": "SQLite, MySQL, has oído hablar de ellos? Dini es prehistórico",
        "dini_4": "Dini en 2025? También usas Windows XP?",
        "dini_5": "Huele a include obsoleto... Ah, es Dini!",
        "not_found": "{plugin_name} no encontrado, buscando otro...",
        "fatal_error": "ERROR FATAL: INCLUDES ROTOS ENCONTRADOS",
        "professional_tip": "Consejo profesional: usa SQLite o MySQL en lugar de Dof2 y Dini",
        "advantages": "Ventajas",
        "fast_efficient": "Más rápido y eficiente",
        "safe_reliable": "Más seguro y confiable",
        "complex_queries": "Soporta consultas complejas",
        "does_not_corrupt": "No corrompe datos",
        "industry_standard": "Estándar de la industria",
        "no_rotten_includes": "¡Felicidades! No se encontraron includes rotos.",
        "converting_plugin": "\033[34mConvirtiendo el plugin {plugin_name} a open.mp\033[0m",
        "plugin_converted": "Plugin {plugin_name} convertido a open.mp",
        "error_processing_plugin": "Error al procesar el plugin: {e}",
        "finished": "Terminado",
        "downloading_gm": "\033[34mDescargando el modo de juego de open.mp\033[0m",
        "error_extracting_gm": "Error al extraer el modo de juego: {e}",
        "backup_created": "Respaldo creado con éxito: {backup_path}",
        "error_creating_backup": "Error al crear el respaldo",
        "error_creating_backup_details": "Error al crear el respaldo: {e}",
        "converting_filterscripts": "\033[34mConvirtiendo los filtroscripts\033[0m",
        "filterscripts_converted": "{files_converted} filterscript(s) convertido(s) con éxito",
        "error_filterscripts": "Error al convertir los filterscripts: {e}",
        "config_not_found": "{search_line} no encontrado en server.cfg",
        "error_updating_config": "Error al actualizar la configuración: {e}",
        "copying_includes": "\033[34mCopiando los archivos include\033[0m",
        "includes_copied": "Archivos include {files_copied} copiados con éxito a qawno/include",
        "removing_pawno": "\033[34mEliminando el directorio pawno\033[0m",
        "pawno_removed": "Directorio pawno eliminado con éxito",
        "processing_includes": "\033[34mProcesando los archivos include\033[0m",
        "include_converted": "Archivo include convertido: {file}",
        "finished_processing_includes": "Procesamiento de los archivos include finalizado",
        "no_includes_found": "No se encontraron archivos include para copiar",
        "error_pawno_directory": "Error al procesar el directorio pawno",
        "error_replacing_bool": "Error al reemplazar bool: {e}",
        "error_sync_bool": "Error al reemplazar la sincronización y bool: {e}",
        "file_not_found": "Error: archivo no encontrado {input_file}",
        "loading_gamemode": "\033[34mCargando el modo de juego:\033[0m \033[34m{input_file}\033[0m",
        "file_converted": "Archivo convertido: {input_file}",
        "no_changes": "Archivo sin cambios: {input_file}",
        "error_message": "Error: {str(e)}",
        "gamemodes_folder": "Este comando solo puede ejecutarse dentro de la carpeta gamemodes.",
        "usage": "Uso: convertomp <archivo.pwn> opcional:[carpeta_modulos]",
        "main_file_not_found": "Error: archivo no encontrado: {main_file}",
        "project_name": "Convertidor de SA-MP a open.mp 1.0.0\n",
        "creating_backup": "\033[34mCreando respaldo\033[0m",
        "failed_backup": "Error al crear el respaldo. Conversión cancelada",
        "updating_config_lines": "\033[34mActualizando las líneas de server.cfg a config.json\033[0m",
        "modules_directory_not_found": "Error: directorio no encontrado: {modules_dir}",
        "converting_folder": "\033[34mConvirtiendo la carpeta: {display_path}\033[0m",
        "conversion_complete": "Conversión completa para el archivo: {main_file} en {elapsed_time:.2f} segundos.",
    }
}

conversion_map = {
    r'TextDrawAlignment\(\s*([^,]+),\s*1\)': r'TextDrawAlignment(\1, TEXT_DRAW_ALIGN_LEFT)',
    r'TextDrawAlignment\(\s*([^,]+),\s*2\)': r'TextDrawAlignment(\1, TEXT_DRAW_ALIGN_CENTER)',
    r'TextDrawAlignment\(\s*([^,]+),\s*3\)': r'TextDrawAlignment(\1, TEXT_DRAW_ALIGN_RIGHT)',
    #fonte
    r'TextDrawFont\(\s*([^,]+),\s*0\)': r'TextDrawFont(\1, TEXT_DRAW_FONT_0)',
    r'TextDrawFont\(\s*([^,]+),\s*1\)': r'TextDrawFont(\1, TEXT_DRAW_FONT_1)',
    r'TextDrawFont\(\s*([^,]+),\s*2\)': r'TextDrawFont(\1, TEXT_DRAW_FONT_2)',
    r'TextDrawFont\(\s*([^,]+),\s*3\)': r'TextDrawFont(\1, TEXT_DRAW_FONT_3)',
    r'TextDrawFont\(\s*([^,]+),\s*4\)': r'TextDrawFont(\1, TEXT_DRAW_FONT_SPRITE_DRAW)',
    r'TextDrawFont\(\s*([^,]+),\s*5\)': r'TextDrawFont(\1, TEXT_DRAW_FONT_MODEL_PREVIEW)',
    #proportional
    r'TextDrawSetProportional\(\s*([^,]+),\s*1\)': r'TextDrawSetProportional(\1, true)',
    r'TextDrawSetProportional\(\s*([^,]+),\s*0\)': r'TextDrawSetProportional(\1, false)',
    #selectable
    r'TextDrawSetSelectable\(\s*([^,]+),\s*1\)': r'TextDrawSetSelectable(\1, true)',
    r'TextDrawSetSelectable\(\s*([^,]+),\s*0\)': r'TextDrawSetSelectable(\1, false)',
    #color
    r'\bTextDrawColor\b': r'TextDrawColour',
    r'\bTextDrawBoxColor\b': r'TextDrawBoxColour',
    r'\bTextDrawBackgroundColor\b': r'TextDrawBackgroundColour',
    #Player aligment
    r'PlayerTextDrawAlignment\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*1\)': r'PlayerTextDrawAlignment(\1, \2[\3][\4], TEXT_DRAW_ALIGN_LEFT)',
    r'PlayerTextDrawAlignment\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*2\)': r'PlayerTextDrawAlignment(\1, \2[\3][\4], TEXT_DRAW_ALIGN_CENTER)',
    r'PlayerTextDrawAlignment\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*3\)': r'PlayerTextDrawAlignment(\1, \2[\3][\4], TEXT_DRAW_ALIGN_RIGHT)',
    #player font
    r'PlayerTextDrawFont\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*0\)': r'PlayerTextDrawFont(\1, \2[\3][\4], TEXT_DRAW_FONT_0)',
    r'PlayerTextDrawFont\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*1\)': r'PlayerTextDrawFont(\1, \2[\3][\4], TEXT_DRAW_FONT_1)',
    r'PlayerTextDrawFont\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*2\)': r'PlayerTextDrawFont(\1, \2[\3][\4], TEXT_DRAW_FONT_2)',
    r'PlayerTextDrawFont\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*3\)': r'PlayerTextDrawFont(\1, \2[\3][\4], TEXT_DRAW_FONT_3)',
    r'PlayerTextDrawFont\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*4\)': r'PlayerTextDrawFont(\1, \2[\3][\4], TEXT_DRAW_FONT_SPRITE_DRAW)',
    r'PlayerTextDrawFont\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*5\)': r'PlayerTextDrawFont(\1, \2[\3][\4], TEXT_DRAW_FONT_MODEL_PREVIEW)',
    #player proportional
    r'PlayerTextDrawSetProportional\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*1\)': r'PlayerTextDrawSetProportional(\1, \2[\3][\4], true)',
    r'PlayerTextDrawSetProportional\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*0\)': r'PlayerTextDrawSetProportional(\1, \2[\3][\4], false)',
    #player selectable
    r'PlayerTextDrawSetSelectable\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*1\)': r'PlayerTextDrawSetSelectable(\1, \2[\3][\4], true)',
    r'PlayerTextDrawSetSelectable\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*0\)': r'PlayerTextDrawSetSelectable(\1, \2[\3][\4], false)',
    #player color
    r'\bPlayerTextDrawColor\b': r'PlayerTextDrawColour',
    r'\bPlayerTextDrawBoxColor\b': r'PlayerTextDrawBoxColour',
    r'\bPlayerTextDrawBackgroundColor\b': r'PlayerTextDrawBackgroundColour',
    #callback
    r'OnPlayerDeath\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*\)': r'OnPlayerDeath(\1, \2, WEAPON:\3)',
    r'OnPlayerStateChange\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*\)': r'OnPlayerStateChange(\1, PLAYER_STATE:\2, PLAYER_STATE:\3)',
    r'OnPlayerKeyStateChange\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*\)': r'OnPlayerKeyStateChange(\1, KEY:\2, KEY:\3)',
    r'OnPlayerClickPlayer\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*\)': r'OnPlayerClickPlayer(\1, \2, CLICK_SOURCE:\3)',
    r'OnPlayerEditAttachedObject\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*\)': r'OnPlayerEditAttachedObject(\1, EDIT_RESPONSE:\2, \3, \4, \5, Float:\6, Float:\7, Float:\8, Float:\9, Float:\10, Float:\11, Float:\12, Float:\13, Float:\14)',
    r'OnPlayerSelectObject\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*\)': r'OnPlayerSelectObject(\1, SELECT_OBJECT:\2, \3, \4, Float:\5, Float:\6, Float:\7)',
    r'OnPlayerWeaponShot\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*\)': r'OnPlayerWeaponShot(\1, \2, BULLET_HIT_TYPE:\3, \4, Float:\5, Float:\6, Float:\7)',
    r'OnPlayerRequestDownload\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*\)': r'OnPlayerRequestDownload(\1, DOWNLOAD_REQUEST:\2, \3)',
    #sqlite
    r'\bdb_open\b': r'DB_Open',
    r'\bdb_close\b': r'DB_Close',
    r'\bdb_query\b': r'DB_ExecuteQuery',
    r'\bdb_free_result\b': r'DB_FreeResultSet',
    r'\bdb_num_rows\b': r'DB_GetRowCount',
    r'\bdb_next_row\b': r'DB_SelectNextRow',
    r'\bdb_num_fields\b': r'DB_GetFieldCount',
    r'\bdb_field_name\b': r'DB_GetFieldName',
    r'\bdb_get_field\b': r'DB_GetFieldString',
    r'\bdb_get_field_int\b': r'DB_GetFieldInt',
    r'\bdb_get_field_float\b': r'DB_GetFieldFloat',
    r'\bdb_get_field_assoc\b': r'DB_GetFieldStringByName',
    r'\bdb_get_field_assoc_int\b': r'DB_GetFieldIntByName',
    r'\bdb_get_field_assoc_float\b': r'DB_GetFieldFloatByName',
    r'\bdb_get_mem_handle\b': r'DB_GetMemHandle',
    r'\bdb_get_result_mem_handle\b': r'DB_GetLegacyDBResult',
    r'\bdb_debug_openfiles\b': r'DB_GetDatabaseConnectionCount',
    r'\bdb_debug_openresults\b': r'DB_GetDatabaseResultSetCount',
    #funcoes samp
    r'\ba_samp\b': r'open.mp',
    r'\bSHA256_PassHash\b': r'SHA256_Hash',
    r'#include <YSF>': r'',
    r'([A-Za-z_][A-Za-z0-9_]*)\[\]': r'const \1[]',
    r'const const': r'const',
    r'OnRconLoginAttempt\(const ip\[\], const password\[\], success\)': r'OnRconLoginAttempt(ip[], password[], success)',
    r'OnPlayerText\(playerid, const text\[\]\)': r'OnPlayerText(playerid, text[])',
    r'OnPlayerCommandText\(playerid, const cmdtext\[\]\)': r'OnPlayerCommandText(playerid, cmdtext[])',
    r'OnDialogResponse\(playerid, dialogid, response, listitem, const inputtext\[\]\)': r'OnDialogResponse(playerid, dialogid, response, listitem, inputtext[])'
}

default_language = "es"

def get_languagem(key, **kwargs):
    global default_language
    message = translations.get(default_language, {}).get(key, key)
    return message.format(**kwargs)

def language(command_args):
    global default_language
    languages = {
        "1": {"code": "en", "name": "Inglês"},
        "2": {"code": "pt", "name": "Português"},
        "3": {"code": "es", "name": "Espanhol"},
        "4": {"code": "ru", "name": "Russo"}
    }

    if "-L" in command_args:
        try:
            selected_option = command_args[command_args.index("-L") + 1]
            if selected_option in languages:
                language_default2 = languages[selected_option]["code"]
                lang = languages[selected_option]["name"]
                print(f"\033[32mIdioma definido para: {lang}\033[0m")
                modify_language_in_file(language_default2)
                return  
            else:
                color("invalid_option", 31)
                print("Invalid language option. Available options are:")
                for number, lang in languages.items():
                    color(f"{number}. {lang['name']}", 32)
                exit(1)
        except IndexError:
            print("\033[31mPlease specify a language number after -L.\033[0m")
            print("\033[32mAvailable options are:\033[0m")
            for number, lang in languages.items():
                color(f"{number}. {lang['name']}", 32)
            exit(1)
            
def modify_language_in_file(new_language):
    try:
        file_path = os.path.realpath(__file__)  # Substitui o uso de sys.argv[0]

        if not os.path.exists(file_path):
            print(f"Arquivo fonte {file_path} não encontrado.")
            return

        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.readlines()

        updated = False
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in file_content:
                if line.strip().startswith("default_language"):
                    file.write(f'default_language = "{new_language}"\n')
                    updated = True
                else:
                    file.write(line)

        if updated:
            print(f"Linguagem padrão atualizada para: {new_language}")
        else:
            print("Não foi possível atualizar a linguagem. Certifique-se de que 'default_language' está no arquivo.")

    except Exception as e:
        print(f"Erro ao modificar o arquivo: {e}")
        
            #CORES
#30preto | 31vermelho | 32verde 
# 33amarelo | 34azul | 35roxo 
# 36ciano | 37Branco 
def color(message_key, color_code, **kwargs):
    global default_language
    message = get_languagem(message_key, **kwargs)
    print(f"\n\033[{color_code}m{message}\033[0m")

def chek_bosta(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().lower()
        
        for include, msg_key in [('#include <DOF', 'dof2'), ('#include <dini', 'dini')]:
            if include in content:
                color(get_languagem('fatal_error', color_code=31), 31)  # Exibe o erro fatal
                color(random.choice(get_languagem(msg_key)), 31)
                color(get_languagem('professional_tip'), 33)
                color(get_languagem('advantages'), 32)
                for vantagem in [
                    get_languagem('no_rotten_includes'),
                    '✓ ' + get_languagem('advantages')
                ]:
                    color(vantagem, 32)
                sys.exit()
   
def plugins(plugin_name, download_url, zip_name):
    try:
        cfg_path, root_path = '../server.cfg', os.path.abspath(os.path.join(os.getcwd(), "../"))
        with open(cfg_path, 'r', encoding='utf-8') as cfg:
            lines = cfg.readlines()
            line_index = next((i for i, line in enumerate(lines) if line.strip().startswith('plugins')), -1)
        
        if line_index == -1 or plugin_name not in lines[line_index]:
            color("not_found", 31, plugin_name=plugin_name)
            return False

        animp4 = threading.Event()
        threading.Thread(target=animation, args=(get_languagem(f"converting_plugin"), 2, 0.2, animp4), daemon=True).start()
        
        mediafire_dl.download(download_url, zip_name, quiet=True)
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall(root_path)
        os.remove(zip_name)
        
        del lines[line_index]
        with open(cfg_path, 'w', encoding='utf-8') as cfg:
            cfg.writelines(lines)
        
        animp4.set()
        color("plugin_converted", 32)
        return True

    except Exception as e:
        color("error_processing_plugin", 31, e=e)
        return False

def gamemode(mediafire_url):
    try:
        animp3 = threading.Event()
        threading.Thread(target=animation, args=(get_languagem("downloading_gm"), 2, 0.2, animp3), daemon=True).start()
        
        zip_path = "Server.zip"
        mediafire_dl.download(mediafire_url, zip_path, quiet=True)
        root_path = os.path.dirname((os.getcwd()))

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(root_path)

        os.remove(zip_path)
        animp3.set()
        color("finished", 32)
        return True

    except Exception as e:
        color("error_extracting_gm", 31,e=e)
        return False
        
def backup(source_path):
    try:
        current_dir = os.getcwd()
        parent_dir = os.path.dirname(current_dir)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_{timestamp}.zip"
        backup_dir = os.path.join(parent_dir, "backups")

        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        backup_path = os.path.join(backup_dir, backup_name)
        with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(parent_dir):
                if backup_dir in root:
                    continue

                for file in files:
                    file_path = os.path.join(root, file)
                    arc_name = os.path.relpath(file_path, parent_dir) 
                    zipf.write(file_path, arc_name)
                    
        if os.path.exists(backup_path):
            color("backup_created", 32, backup_path=backup_path)
            return True
        else:
            color("error_creating_backup", 31)
            return False

    except Exception as e:
        color("error_creating_backup_details", 31)
        return False  
        
def filterscripts():
    try:
        fs_path = os.path.join("..", "filterscripts")
        if not os.path.exists(fs_path):
            return False

        animp10 = threading.Event()
        threading.Thread(target=animation,args=(get_languagem("converting_filterscripts"), 3, 0.2, animp10),daemon=True).start()

        files_converted = 0
        processed_files = set()

        for file in os.listdir(fs_path):
            if file.endswith('.pwn'):
                file_path = os.path.join(fs_path, file)

                if file_path in processed_files:
                    continue

                if convert_file(file_path):
                    files_converted += 1
                    processed_files.add(file_path)

        animp10.set()

        if files_converted > 0:
            color("filterscripts_converted", 32)
            return True
       
    except Exception as e:
        color("error_filterscripts", 31)
        return False

def config(search_line, json_field, parent_field=None, use_brackets=False):
    try:
        with open('../server.cfg', 'r', encoding='utf-8') as cfg:
            value = None
            for line in cfg:
                if line.strip().startswith(search_line):
                    value = line.strip().split(search_line)[1].strip()
                    break

        if not value:
            color("config_not_found", 31)
            return False

        if use_brackets:
            value = f'[{value}]'
        
        with open('../config.json', 'r', encoding='utf-8') as json_file:
            config = json.load(json_file)

        if parent_field:
            if parent_field in config and json_field in config[parent_field]:
                keys = list(config[parent_field])
                field_index = keys.index(json_field)
                if field_index > 0:
                    previous_field = keys[field_index - 1]
        else:
            if json_field in config:
                keys = list(config)
                field_index = keys.index(json_field)
                if field_index > 0:
                    previous_field = keys[field_index - 1]

        if parent_field:
            if parent_field not in config:
                config[parent_field] = {}
            config[parent_field][json_field] = value
        else:
            config[json_field] = value

        with open('../config.json', 'w', encoding='utf-8') as json_file:
            json.dump(config, json_file, indent=4)

        return True

    except Exception as e:
        color("error_updating_config", 31,e=e)
        return False

def includes():
    try:
        source_paths = [
            os.path.join("..", "pawno", "include"),
            os.path.join("..", "pawno", "includes")
        ]
        dest_path = os.path.join("..", "qawno", "include")

        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        files_copied = 0
        animp6 = threading.Event()
        threading.Thread(target=animation, args=(get_languagem("copying_includes"), 2, 0.2, animp6), daemon=True).start()

        for source_path in source_paths:
            if os.path.exists(source_path):
                for root, dirs, files in os.walk(source_path):
                    relative_path = os.path.relpath(root, source_path)
                    dest_dir = os.path.join(dest_path, relative_path)
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)

                    for file in files:
                        src_file = os.path.join(root, file)
                        dst_file = os.path.join(dest_dir, file)
                        shutil.copy2(src_file, dst_file)
                        files_copied += 1

        animp6.set()

        if files_copied > 0:
            color("includes_copied", 32)

            animp7 = threading.Event()
            threading.Thread(target=animation, args=(get_languagem("removing_pawno"), 2, 0.2, animp7), daemon=True).start()

            pawno_path = os.path.join("..", "pawno")
            if os.path.exists(pawno_path):
                shutil.rmtree(pawno_path)

            animp7.set()
            color("pawno_removed", 32)

            animp8 = threading.Event()
            threading.Thread(target=animation, args=(get_languagem("processing_includes"), 3, 0.2, animp8), daemon=True).start()

            for root, _, files in os.walk(dest_path):
                for file in files:
                    if file.endswith('.inc') and not ('omp_' in file or 'open' in file or '_open'):
                        inc_file = os.path.join(root, file)
                        with open(inc_file, 'r', encoding='utf-8') as f:
                            content = f.read()

                        changes_made = False
                        for pattern, replacement in conversion_map.items():
                            new_content = re.sub(pattern, replacement, content)
                            if new_content != content:
                                changes_made = True
                                content = new_content

                        if changes_made:
                            with open(inc_file, 'w', encoding='utf-8') as f:
                                f.write(content)
                            color("include_converted", 32)

            animp8.set()
            color("finished_processing_includes", 32)
            return True

        else:
            color("no_includes_found", 31)
            return False

    except Exception as e:
        color("error_pawno_directory", 31)
        return False   
        
def safe_sub(pattern, replacement, text):
    try:
        if callable(replacement):
            return re.sub(pattern, replacement, text)
        return re.sub(pattern, replacement, text)
    except Exception as e:
        print(f"Error in safe_sub: {e}")
        traceback.print_exc()  
        return text

def convert_code(input_code):
    for pattern, replacement in conversion_map.items():
        input_code = safe_sub(pattern, replacement, input_code)

    patterns = {
        r'ShowNameTags\((.*?)\)': booll,
        r'EnableStuntBonusForAll\((.*?)\)': booll,
        r'ShowPlayerMarkers\((.*?)\)': booll,
        r'TogglePlayerControllable\(\s*([^,]+)\s*,\s*(.*?)\)': booll,
        r'SetTimerEx\((.*?,.*?,.*?,.*?)\s*,\s*(1|0)\)': booll,
        r'SetTimer\((.*?,.*?,.*?)\s*,\s*(1|0)\)': booll,
        r'ApplyAnimation\((.*?),\s*(\d+)\)': sync
    }

    for pattern, handler in patterns.items():
        input_code = safe_sub(pattern, handler, input_code)

    return input_code

def booll(match):
    try:
        params = match.group(1)
        params = re.sub(r'1', 'true', params)
        params = re.sub(r'0', 'false', params)
        function_name = match.group(0).split('(')[0]
        return f"{function_name}({params})"
    except Exception as e:
        color("error_replacing_bool", 31)
        return match.group(0)

def sync(match):
    try:
        all_params = match.group(1)
        sync_type = match.group(2)
        original_spacing = match.group(0)
        
        had_space = ',' in original_spacing and original_spacing.split(',')[-1].startswith(' ')
        params_list = all_params.split(',')

        for i in range(len(params_list)):
            param = params_list[i].strip()
            if param in ['0', '1']:
                space_prefix = ' ' if (',' + params_list[i]).startswith(', ') else ''
                params_list[i] = f"{space_prefix}{'true' if param == '1' else 'false'}"

        all_params = ','.join(params_list)
        sync_map = {"1": "SYNC_NONE", "2": "SYNC_ALL", "3": "SYNC_OTHER"}

        if sync_type in sync_map:
            space = ' ' if had_space else ''
            return f"ApplyAnimation({all_params},{space}{sync_map[sync_type]})"

        return match.group(0)
    except Exception as e:
        color("error_sync_bool", 31)
        return match.group(0)   
        
def animation(base_text, max_dots=3, interval=0.2, animp=None):
    dots = 0
    increasing = True

    while not animp.is_set():
        formatted_text = f"{base_text}{'.' * dots}"
        print(f"\r{formatted_text}", end="", flush=True)  
        time.sleep(interval)

        if increasing:
            dots += 1
            if dots > max_dots:
                increasing = False
        else:
            dots -= 1
            if dots < 0:
                increasing = True

    print("\r" + " " * (len(base_text) + max_dots), end="\r")

def convert_file(input_file):
    try:
        if not os.path.isfile(input_file):
            color("file_not_found", 31)
            return
        
        animp = threading.Event()
        threading.Thread(target=animation, args=(get_languagem("loading_gamemode",input_file=input_file), 3, 0.2, animp), daemon=True).start()

        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        converted_content = convert_code(content)
        
        if content != converted_content:
            with open(input_file, 'w', encoding='utf-8') as file:
                file.write(converted_content)
                animp.set()
                color("file_converted",32,input_file=input_file)
        else:
            color("no_changes",31,input_file=input_file)
            
    except Exception as e:
        color("error_message", 31,input_file=input_file) 
        
def process_directory(modules_dir):
    for root, _, files in os.walk(modules_dir):
        for file in files:
            if file.endswith(".pwn") or file.endswith(".inc"):
                convert_file(os.path.join(root, file), animp)

def is_in_gamemodes():
    current_directory = os.getcwd()  
    folder_name = os.path.basename(current_directory)
    return folder_name == "gamemodes"  

def main():
    global default_language
    if not is_in_gamemodes():
        color("gamemodes_folder", 31)
        exit(1)
    if len(sys.argv) < 2:
        color("usage", 31)
        sys.exit(1)
        
    main_file = None
    if not sys.argv[1].startswith("-L"):
        main_file = sys.argv[1]

    if "-L" in sys.argv:
        language(sys.argv)
        sys.exit(0)

    if not os.path.isfile(main_file):
        color("main_file_not_found", 31, main_file=main_file)
        sys.exit(1)

    color("project_name", 34)
    chek_bosta(main_file)
    animp2 = threading.Event()

    threading.Thread(target=animation, args=(get_languagem("creating_backup"), 2, 0.2, animp2), daemon=True).start()
    if not backup(main_file):
        color("failed_backup", 32)
        return False
    animp2.set()
    
    base_dir = os.path.dirname(main_file)
    start_time = time.time()
    
    convert_file(main_file)
    # Gamemode base open.mp
    gamemode("https://www.mediafire.com/file/hp3jrdelra2bvif/Server.zip/file")
    # Include
    includes()
    # Filterscripts
    filterscripts()
    # Plugins open.mp
    plugins('sscanf', 'https://www.mediafire.com/file/eilmok7y0c4v094/sscanf.zip/file', 'sscanf.zip')
    plugins('discord-connector', 'https://www.mediafire.com/file/1tw58dja063o47c/discord-connector.zip/file', 'discord-connector.zip')
    plugins('mysql', 'https://www.mediafire.com/file/m332ztu1l4a6hsa/mysql.zip/file', 'mysql.zip')
    plugins('pawn-cmd', 'https://www.mediafire.com/file/pmvh6ztg4c88l10/pawn-cmd.zip/file', 'pawn-cmd.zip')
    plugins('pawn-ranknet', 'https://www.mediafire.com/file/dktfsit5i8877nf/pawn-ranknet.zip/file', 'pawn-ranknet.zip')
    plugins('textdraw-streamer', 'https://www.mediafire.com/file/e0zh0cpx35gp1gd/textdraw-streamer.zip/file', 'textdraw-streamer.zip')
    
    # server.cfg para config.json
    animp5 = threading.Event()
    threading.Thread(target=animation, args=(get_languagem("updating_config_lines"), 3, 0.2, animp5), daemon=True).start()
    config('hostname', 'name')
    config('language', 'language')
    config('discord_bot_token', 'bot_token', 'discord')
    config('maxplayers', 'max_players')
    config('rcon_password', 'password', 'rcon')
    config('weburl', 'website')
    config('filterscripts', 'side_scripts', 'pawn', use_brackets=True)
    config('gamemode0', 'main_scripts', 'pawn', use_brackets=True)
    config('port', 'port', 'network')
    # Passa os plugins que não foram convertidos para o config.json
    config('plugins', 'legacy_plugins', 'pawn', use_brackets=True)
    
    animp5.set()
    
    if len(sys.argv) == 3:
        modules_dir = sys.argv[2]
        if os.path.isdir(modules_dir):
            process_directory(modules_dir, animp)
        else:
            color("modules_directory_not_found", 32,modules_dir=modules_dir)
    else: 
        base_dir = os.path.dirname(main_file)
        dir_moduless = [
            os.path.join(base_dir, "..", "modules"),
            os.path.join(base_dir, "..", "modulos")
        ]
    
        for dir_modules in dir_moduless:
            if os.path.exists(dir_modules):
                display_path = dir_modules.replace(dir_modules, dir_modules)
                animp9 = threading.Event()
                threading.Thread(target=animation, args=(get_languagem("converting_folder"), 3, 0.2, animp9), daemon=True).start()
                process_directory(dir_modules)
                animp9.set()
                break

    end_time = time.time()
    elapsed_time = end_time - start_time
    color("conversion_complete", 32,main_file=main_file,elapsed_time=elapsed_time)

if __name__ == '__main__':
    main()