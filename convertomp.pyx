#!/usr/bin/env python3

import re
import sys
import os
import time
import threading
import requests
import zipfile
from bs4 import BeautifulSoup
from datetime import datetime
import shutil

conversion_map = {
    r'TextDrawAlignment\(\s*([^,]+),\s*1\)': r'TextDrawAlignment(\1, TEXT_DRAW_ALIGN_LEFT)',
    r'TextDrawAlignment\(\s*([^,]+),\s*2\)': r'TextDrawAlignment(\1, TEXT_DRAW_ALIGN_CENTER)',
    r'TextDrawAlignment\(\s*([^,]+),\s*3\)': r'TextDrawAlignment(\1, TEXT_DRAW_ALIGN_RIGHT)',
    
    r'TextDrawFont\(\s*([^,]+),\s*0\)': r'TextDrawFont(\1, TEXT_DRAW_FONT_0)',
    r'TextDrawFont\(\s*([^,]+),\s*1\)': r'TextDrawFont(\1, TEXT_DRAW_FONT_1)',
    r'TextDrawFont\(\s*([^,]+),\s*2\)': r'TextDrawFont(\1, TEXT_DRAW_FONT_2)',
    r'TextDrawFont\(\s*([^,]+),\s*3\)': r'TextDrawFont(\1, TEXT_DRAW_FONT_3)',
    r'TextDrawFont\(\s*([^,]+),\s*4\)': r'TextDrawFont(\1, TEXT_DRAW_FONT_SPRITE_DRAW)',
    r'TextDrawFont\(\s*([^,]+),\s*5\)': r'TextDrawFont(\1, TEXT_DRAW_FONT_MODEL_PREVIEW)',
    
    r'TextDrawSetProportional\(\s*([^,]+),\s*1\)': r'TextDrawSetProportional(\1, true)',
    r'TextDrawSetProportional\(\s*([^,]+),\s*0\)': r'TextDrawSetProportional(\1, false)',

    r'TextDrawSetSelectable\(\s*([^,]+),\s*1\)': r'TextDrawSetSelectable(\1, true)',
    r'TextDrawSetSelectable\(\s*([^,]+),\s*0\)': r'TextDrawSetSelectable(\1, false)',
    
    r'TextDrawColor': r'TextDrawColour',
    r'TextDrawBoxColor': r'TextDrawBoxColour',
    r'TextDrawBackgroundColor': r'TextDrawBackgroundColour',
    
    r'PlayerTextDrawAlignment\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*1\)': r'PlayerTextDrawAlignment(\1, \2[\3][\4], TEXT_DRAW_ALIGN_LEFT)',
    r'PlayerTextDrawAlignment\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*2\)': r'PlayerTextDrawAlignment(\1, \2[\3][\4], TEXT_DRAW_ALIGN_CENTER)',
    r'PlayerTextDrawAlignment\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*3\)': r'PlayerTextDrawAlignment(\1, \2[\3][\4], TEXT_DRAW_ALIGN_RIGHT)',
    
    r'PlayerTextDrawFont\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*0\)': r'PlayerTextDrawFont(\1, \2[\3][\4], TEXT_DRAW_FONT_0)',
    r'PlayerTextDrawFont\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*1\)': r'PlayerTextDrawFont(\1, \2[\3][\4], TEXT_DRAW_FONT_1)',
    r'PlayerTextDrawFont\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*2\)': r'PlayerTextDrawFont(\1, \2[\3][\4], TEXT_DRAW_FONT_2)',
    r'PlayerTextDrawFont\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*3\)': r'PlayerTextDrawFont(\1, \2[\3][\4], TEXT_DRAW_FONT_3)',
    r'PlayerTextDrawFont\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*4\)': r'PlayerTextDrawFont(\1, \2[\3][\4], TEXT_DRAW_FONT_SPRITE_DRAW)',
    r'PlayerTextDrawFont\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*5\)': r'PlayerTextDrawFont(\1, \2[\3][\4], TEXT_DRAW_FONT_MODEL_PREVIEW)',
    
    r'PlayerTextDrawSetProportional\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*1\)': r'PlayerTextDrawSetProportional(\1, \2[\3][\4], true)',
    r'PlayerTextDrawSetProportional\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*0\)': r'PlayerTextDrawSetProportional(\1, \2[\3][\4], false)',

    r'PlayerTextDrawSetSelectable\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*1\)': r'PlayerTextDrawSetSelectable(\1, \2[\3][\4], true)',
    r'PlayerTextDrawSetSelectable\((\w+)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\[([^]]+)\]\[(\d+)\]\s*,\s*0\)': r'PlayerTextDrawSetSelectable(\1, \2[\3][\4], false)',
    
    r'PlayerTextDrawColor': r'PlayerTextDrawColour',
    r'PlayerTextDrawBoxColor': r'PlayerTextDrawBoxColour',
    r'PlayerTextDrawBackgroundColor': r'PlayerTextDrawBackgroundColour',
    
    r'OnPlayerDeath\(([^,\)]+),\s*([^,\)]+),\s*([^,\)]+)\)': r'OnPlayerDeath(\1, \2, WEAPON:\3)',
    r'OnPlayerStateChange\(([^,\)]+),\s*([^,\)]+),\s*([^,\)]+)\)': r'OnPlayerStateChange(\1, PLAYER_STATE:\2, PLAYER_STATE:\3)',
    r'OnPlayerKeyStateChange\(([^,\)]+),\s*([^,\)]+),\s*([^,\)]+)\)': r'OnPlayerKeyStateChange(\1, KEY:\2, KEY:\3)',
    r'OnPlayerClickPlayer\(([^,\)]+),\s*([^,\)]+),\s*([^,\)]+)\)': r'OnPlayerClickPlayer(\1, \2, CLICK_SOURCE:\3)',

    r'db_open': r'DB_Open',
    r'db_close': r'DB_Close',
    r'db_query': r'DB_ExecuteQuery',
    r'db_free_result': r'DB_FreeResultSet',
    r'db_num_rows': r'DB_GetRowCount',
    r'db_next_row': r'DB_SelectNextRow',
    r'db_num_fields': r'DB_GetFieldCount',
    r'db_field_name': r'DB_GetFieldName',
    r'db_get_field': r'DB_GetFieldString',
    r'db_get_field_int': r'DB_GetFieldInt',
    r'db_get_field_float': r'DB_GetFieldFloat',
    r'db_get_field_assoc': r'DB_GetFieldStringByName',
    r'db_get_field_assoc_int': r'DB_GetFieldIntByName',
    r'db_get_field_assoc_float': r'DB_GetFieldFloatByName',
    r'db_get_mem_handle': r'DB_GetMemHandle',
    r'db_get_result_mem_handle': r'DB_GetLegacyDBResult',
    r'db_debug_openfiles': r'DB_GetDatabaseConnectionCount',
    r'db_debug_openresults': r'DB_GetDatabaseResultSetCount',
 
    r'a_samp': r'open.mp',
    r'SHA256_PassHash': r'SHA256_Hash',
    r'^\s*#include\s*<YSF>\s*$': r'',
    r'([A-Za-z_][A-Za-z0-9_]*)\[\]': r'const \1[]'
}

#31vermelho | 32verde | 33amarelo 
#34azul | 35roxo | 36ciano 37Branco 

def color(text, color_code):
    return print(f"\n\033[{color_code}m{text}\033[0m")

def plugin_check(plugin_name, download_url, zip_name):
    try:
        with open('server.cfg', 'r') as cfg:
            plugins_line = None
            for line in cfg:
                if line.strip().startswith('plugins'):
                    plugins_line = line.strip()
                    break

            if not plugins_line:
                color('plugins line not found in server.cfg', 31)
                return False

            if plugin_name not in plugins_line:
                color(f'{plugin_name} not found in plugins line', 31)
                return False

        response = requests.get(download_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        download_link = soup.find('a', {'class': 'input'})['href']

        file_response = requests.get(download_link)
        zip_path = zip_name

        with open(zip_path, 'wb') as f:
            f.write(file_response.content)

        root_path = os.path.abspath(os.path.join(os.getcwd(), "../components"))
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(root_path)

        os.remove(zip_path)
        color(f'Plugin {plugin_name} downloaded and extracted successfully in components', 32)
        return True

    except Exception as e:
        color(f'Error processing plugin: {e}', 31)
        return False

def extract_gamemode(mediafire_url):
    try:
        response = requests.get(mediafire_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        download_link = soup.find('a', {'class': 'input'})['href']
        
        file_response = requests.get(download_link)
        zip_path = "Server.zip"
        
        with open(zip_path, 'wb') as f:
            f.write(file_response.content)
        
        root_path = os.path.dirname(os.path.dirname(os.getcwd()))
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(root_path)
        
        os.remove(zip_path)
        color(f'File downloaded and extracted to: {root_path}', 32)
        return True
        
    except Exception as e:
        color(f'Error extracting includes: {e}', 31)
        return False
        
        
def create_backup(source_path):
    try:
        source_path = os.path.abspath(source_path)
        parent_dir = os.getcwd()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_{timestamp}.zip"
        backup_dir = os.path.join(parent_dir, "backups")
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        backup_path = os.path.join(backup_dir, backup_name)
        with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            base_folder = os.path.basename(source_path)
            for root, _, files in os.walk(source_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.join(base_folder, os.path.relpath(file_path, source_path))
                    zipf.write(file_path, relative_path)
                    color(f'Adding to zip: {relative_path}', 34)
        color(f'Backup created successfully: {backup_path}', 32)
        return True
    except Exception as e:
        color(f'Error creating backup: {e}', 31)
        return False
        
def safe_sub(pattern, replacement, text):
    try:
        if callable(replacement):
            return re.sub(pattern, replacement, text)
        return re.sub(pattern, replacement, text)
    except Exception as e:
        color(f'Error in safe_sub: {e}', 31)
        return text

def convert_code(input_code):
    for pattern, replacement in conversion_map.items():
        input_code = safe_sub(pattern, replacement, input_code)

    patterns = {
        r'ShowNameTags\((.*?)\)': replace_bool,
        r'EnableStuntBonusForAll\((.*?)\)': replace_bool,
        r'ShowPlayerMarkers\((.*?)\)': replace_bool,
        r'TogglePlayerControllable\(\s*([^,]+)\s*,\s*(.*?)\)': replace_bool,
        r'SetTimerEx\((.*?,.*?,.*?,.*?)\s*,\s*(1|0)\)': replace_bool,
        r'SetTimer\((.*?,.*?,.*?)\s*,\s*(1|0)\)': replace_bool,
        r'ApplyAnimation\((.*?),\s*(\d+)\)': replace_sync
    }

    for pattern, handler in patterns.items():
        input_code = safe_sub(pattern, handler, input_code)

    return input_code

def replace_bool(match):
    try:
        params = match.group(1)
        params = re.sub(r'1', 'true', params)
        params = re.sub(r'0', 'false', params)
        function_name = match.group(0).split('(')[0]
        return f"{function_name}({params})"
    except Exception as e:
        color(f'Error in replacing bool: {e}', 31)
        return match.group(0)

def replace_sync(match):
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
        color(f'Error in replacing sync and bool: {e}', 31)
        return match.group(0)   
        
def animation(base_text, max_dots=3, interval=0.2, stop_event=None):
    dots = 0
    increasing = True

    while not stop_event.is_set():
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

def convert_file(input_file, stop_event):
    try:
        if not create_backup(input_file):
            color('Failed to create backup. Conversion canceled',32)
            return False
            
        if not os.path.isfile(input_file):
            color(f'Error: file not found {input_file}', 31)
            return
        
        color(f'samp to open.mp converter 1.0.0\n', 34)
        animation_thread = threading.Thread(target=animation, args=(f"\033[33mLoading gamemode:\033[0m \033[34m{input_file}\033[0m", 3, 0.2, stop_event))
        animation_thread.daemon = True
        animation_thread.start()

        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        converted_content = convert_code(content)
        
        if content != converted_content:
            with open(input_file, 'w', encoding='utf-8') as file:
                file.write(converted_content)
            color(f'Converted file: {input_file}', 32)
        else:
            color(f'File without changes: {input_file}', 32)
        
        stop_event.set()
        animation_thread.join()

    except Exception as e:
        color(f'Error: {str(e)}', 31)
        
def process_directory(modules_dir, stop_event):
    for root, _, files in os.walk(modules_dir):
        for file in files:
            if file.endswith(".pwn") or file.endswith(".inc"):
                convert_file(os.path.join(root, file), stop_event)

    if len(sys.argv) < 2:
        print(f"Usage: convertomp.py arquivo.pwn optional:[pasta_modulos]")
        sys.exit(1)

    main_file = sys.argv[1]
    if not os.path.isfile(main_file):
        color(f'Error: file not found: {main_file}',31)
        sys.exit(1)

    base_dir = os.path.dirname(main_file)

    start_time = time.time()

    stop_event = threading.Event()

    convert_file(main_file, stop_event)
    extract_gamemode("https://www.mediafire.com/file/hp3jrdelra2bvif/Server.zip/file")
    plugin_check('sscanf', 'https://www.mediafire.com/file/sscanf.zip', 'sscanf.zip')

    if len(sys.argv) == 3:
        modules_dir = sys.argv[2]
        if os.path.isdir(modules_dir):
            process_directory(modules_dir, stop_event)
        else:
            color(f'Error: directory not found: {modules_dir}',32)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    color(f'Conversion completed file: {main_file} in {elapsed_time:.2f} seconds.',32)