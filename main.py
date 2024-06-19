from url import init
import requests
import os

def download_files(http_links):
    if not http_links:
        print("Nenhum link HTTP encontrado.")
        return
    
   
    save_dir = 'file'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    try:
        for http_link in http_links:
          
            response = requests.get(http_link)
            if response.status_code == 200:
               
                filename = os.path.join(save_dir, os.path.basename(http_link))
                
                
                with open(filename, 'wb') as f:
                    f.write(response.content)
                
                print(f"Arquivo baixado e salvo em: {filename}")
            else:
                print(f"Erro ao baixar o arquivo para o link '{http_link}': Status {response.status_code}")
    
    except Exception as e:
        print(f"Erro ao baixar os arquivos: {e}")

if __name__ == "__main__":
    
    http_links = init()
    
    
    download_files(http_links)
