import json
import requests

def main():
    print("Bienvenido a Cheeps!!")
    print(" 1. Quieres realizar publicaciones? ")
    print(" 2. Quieres ver publicaciones?")
    opcion= int (input(" Elige una de las opciones: "))
    
    if opcion == 1 : 
        mensaje = input(" Ingresa tu publicacon: ")
        respuesta= send_cheep(mensaje)
        print(respuesta)
        if respuesta == 200: 
            print("Se ha enviado con éxito ")
        else:
            print("Error!! ")

    if opcion == 2 : 
        pub = get_cheeps()
        ad = json.loads(pub)
        for lista in ad : 
            print(lista)


def send_cheep(mensaje): 
    data= {"message": mensaje}
    envio= requests.post("https://e7afcbe6-0da8-4f39-b8f1-a7786f299f72-00-275ee89ixgu51.kirk.replit.dev/send_cheep", json = data)
    return envio.status_code

def get_cheeps(): 
    respuesta= requests.get ("https://e7afcbe6-0da8-4f39-b8f1-a7786f299f72-00-275ee89ixgu51.kirk.replit.dev/get_cheeps") 
    return respuesta.content
main()  