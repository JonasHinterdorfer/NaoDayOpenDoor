
from http.server import BaseHTTPRequestHandler, HTTPServer
from gtts import gTTS
import os
from pydub import AudioSegment

def remove_extra_semicolons(input_string):
    first_semicolon_index = input_string.find(':')
    if first_semicolon_index == -1 or first_semicolon_index == len(input_string) - 1:
        return input_string
    result_string = input_string[:first_semicolon_index + 1] + input_string[first_semicolon_index + 1:].replace(':', '')

    return result_string

def increase_loudness(input_file, output_file, target_loudness):
    song = AudioSegment.from_mp3(input_file)
    louder_song = song + 10
    louder_song.export(output_file, format='mp3')


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self._set_headers()
        mytext = str(post_data).replace("You: {message:", "").replace("You:", "").replace("Assistant: ", "")
        mytext = remove_extra_semicolons(mytext)
        mytext = mytext.split(":")[1].strip().replace("}'", "").replace("\"", "").replace(":", "")
        mytext = mytext.replace("\\\\u00e4", "ä").replace("\\\\u00f6", "ö").replace("\\\\u00fc", "ü").replace("\\\\u00c4", "Ä").replace("\\\\u00d6", "Ö").replace("\\\\u00dc", "Ü").replace("\\\\u00df", "ß")
        print(mytext)
        language = 'de'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("/home/poci/Desktop/Nao/example.mp3")
        print(myobj)
        increase_loudness("/home/poci/Desktop/Nao/example.mp3", "/home/poci/Desktop/Nao/example.mp3", 20)
        os.system("sshpass -p 'nao' scp /home/poci/Desktop/Nao/example.mp3 nao@10.0.0.24:/data/home/nao/.local/share/PackageManager/apps/.lastUploadedChoregrapheBehavior/responce.mp3")
        #os.system("rm /home/poci/Desktop/Nao/example.mp3")
        print(post_data)

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('10.0.0.132', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()