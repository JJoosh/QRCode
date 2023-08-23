import qrcode
import os
from colorama import Fore, Style
import pyfiglet

def crear_codigo_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_file_path = "codigo_qr.png"
    qr_img.save(qr_file_path)
    
    return qr_file_path

def main():
    print(Fore.GREEN + pyfiglet.figlet_format("QRcodess", font="slant") + Style.RESET_ALL)
    print(Fore.CYAN + "Bienvenido a QRcodess" + Style.RESET_ALL)
    print("------------------------------------By Josh")   
    while True:
        print("\n[1]. Crear código QR")
        print("[2]. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            data = input("Ingresa los datos para el código QR: ")
            qr_file_path = crear_codigo_qr(data)
            print(f"El código QR se ha generado y guardado en {qr_file_path}")
            os.system(f"xdg-open {qr_file_path}")  # Esto abre el archivo en el visor de imágenes predeterminado
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")

if __name__ == "__main__":
    main()

