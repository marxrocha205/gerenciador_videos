import paramiko
import re

def init():
    
    host = ''
    port = 2223
    username = ''
    password = ''
    remote_path = '/home//Downloads/teste.sh'

    
    commands_to_execute = [
        f"bash {remote_path} ",
        f"bash {remote_path} ",
        f"bash {remote_path} ",
        f"bash {remote_path} ",
        f"bash {remote_path} "
    ]

    http_links = []

    
    def ssh_command(host, port, username, password, command):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        try:
            
            client.connect(hostname=host, port=port, username=username, password=password)
            
            
            stdin, stdout, stderr = client.exec_command(command)
            
            
            output = stdout.read().decode().strip()  
            
            
            match = re.search(r'http://\S+', output)
            if match:
                http_link = match.group(0)
                http_links.append(http_link)
            else:
                print(f"Link HTTP não encontrado na saída do comando: {command}")
            
        except Exception as e:
            print(f"Erro ao conectar ou executar o comando SSH: {e}")
        
        finally:
            client.close()

   
    for command in commands_to_execute:
        ssh_command(host, port, username, password, command)
    
    return http_links
