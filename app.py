from flask import Flask, render_template, request
import serial

app = Flask(__name__)

# Inisialisasi koneksi serial dengan Arduino
arduino = serial.Serial('COM3', 9600)  # Ganti 'COM3' dengan port serial Arduino Anda

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        # Membaca instruksi dari formulir web
        instruction = request.form['instruction']
        # Mengirim instruksi ke Arduino melalui koneksi serial
        arduino.write(instruction.encode())
        return "Instruksi berhasil dikirim ke Arduino: " + instruction

if __name__ == '__main__':
    app.run(debug=True)
