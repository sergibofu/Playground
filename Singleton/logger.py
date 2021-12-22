
def write_log(level, msg):
    with open('log/filename.log', mode='a', encoding='utf-8') as log_file:
        log_file.write('[{0}] {1}\n'.format(level, msg))   

#Not cool repeating same code again and again...
def critical(msg):
    with open('log/filename.log', mode='a', encoding='utf-8') as log_file:
        log_file.write('[CRITICAL] {0}\n'.format(msg))   

def error(msg):
    with open('log/filename.log', mode='a', encoding='utf-8') as log_file:
        log_file.write('[ERROR] {0}\n'.format(msg))   

def warn(msg):
    with open('log/filename.log', mode='a', encoding='utf-8') as log_file:
        log_file.write('[WARNING] {0}\n'.format(msg))   

def info(msg):
    with open('log/filename.log', mode='a', encoding='utf-8') as log_file:
        log_file.write('[INFO] {0}\n'.format(msg))   

def debug(msg):
    with open('log/filename.log', mode='a', encoding='utf-8') as log_file:
        log_file.write('[DEBUG] {0}\n'.format(msg))   

