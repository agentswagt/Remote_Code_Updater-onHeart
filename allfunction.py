import requests
import subprocess



def sdp(url): #source downloader and print

    source = requests.get(url).text
    print(("[+]Source Code Downloaded"))
    return source
    

def file_saver(file_name, file_data): 

    file_saver_program = open(file_name, "w")
    file_saver_program.write(file_data)
    file_saver_program.close()
    print("[+]File Saved as {}".format(file_name))
def silentcmd(command): #for windows only
    
    import subprocess
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.call(command, startupinfo=si)


