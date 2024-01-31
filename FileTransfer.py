import os
from socket import socket, AF_INET, SOCK_DGRAM

class FileTransfer:
    def __init__(self):
        self.own_ip = self.get_own_ip()
        self.nao_user = "nao"
        self.nao_pass = "nao"
        self.nao_ip = f"{self.nao_user}.local"
        self.file_from_rec_nao = f"/home/{self.nao_user}/recordings/microphones/recording.wav"
        self.directory_to_save_nao = f"/data/home/{self.nao_user}/.local/share/PackageManager/apps/.lastUploadedChoregrapheBehavior/responce.mp3"
        self.file_from_rec_local = "./rec.wav"
        self.directory_to_save_local = "./example.mp3"

    def get_recording_from_nao(self):
        print(f"/usr/bin/sshpass -p '{self.nao_pass}' scp {self.nao_user}@{self.nao_ip}:{self.file_from_rec_nao} {self.file_from_rec_local}")
        os.system(f"sshpass -p '{self.nao_pass}' scp {self.nao_user}@{self.nao_ip}:{self.file_from_rec_nao} {self.file_from_rec_local}")
        return self.file_from_rec_local

    def send_audio_to_nao(self):
        os.system(
            f"sshpass -p '{self.nao_pass}' scp {self.directory_to_save_local} {self.nao_user}@{self.nao_ip}:{self.directory_to_save_nao}")
        return self.directory_to_save_nao

    def get_own_ip(self):
        s = socket(AF_INET, SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            ip = s.getsockname()[0]
        except Exception:
            ip = '127.0.0.1'
        finally:
            s.close()
            return ip

if __name__ == "__main__":
    file_transfer = FileTransfer()
    print(file_transfer.get_own_ip())