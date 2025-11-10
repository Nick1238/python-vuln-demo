# vuln_file1.py
import os
import subprocess
import pickle

def insecure_command_injection(user_input):
    # Уязвимость: Command Injection
    os.system(f"echo {user_input}")
    subprocess.call("ls " + user_input, shell=True)


def insecure_deserialization(user_data):
    # Уязвимость: небезопасная десериализация
    return pickle.loads(user_data)


def insecure_eval(expr):
    # Уязвимость: использование eval
    return eval(expr)


def insecure_tmp_file():
    # Уязвимость: использование небезопасного временного файла
    tmp = open('/tmp/tmpfile', 'w')
    tmp.write('Some data')
    tmp.close()
