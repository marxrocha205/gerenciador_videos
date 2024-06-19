import os
import subprocess

def convert_ts_to_mp4(input_file, output_file):
    cmd = ['ffmpeg', '-y','-i', input_file, '-c', 'copy', output_file]
    subprocess.run(cmd, capture_output=True, text=True)

def main():
    input_dir = 'file' 
    output_dir = 'file'  

    for file in os.listdir(input_dir):
        if file.endswith('.ts'):
            input_file = os.path.join(input_dir, file)
            output_file = os.path.join(output_dir, file.replace('.ts', '.mp4'))
            convert_ts_to_mp4(input_file, output_file)
            print(f'Converting {input_file} to {output_file}')

if __name__ == "__main__":
    main()
