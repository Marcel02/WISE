import socket
import threading

class TCPServer:
    def __init__(self, host='0.0.0.0', port=5000):
        """Inicializa el servidor TCP con la IP y puerto especificados."""
        self.host = host  # Dirección IP del servidor
        self.port = port  # Puerto en el que el servidor escuchará las conexiones
        self.server_socket = None  # Socket del servidor

    def start_server(self, message):
        """Inicia el servidor TCP y espera conexiones entrantes."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))  # Vincula la IP y el puerto
        self.server_socket.listen(5)  # Permite hasta 5 conexiones en espera
        print(f"Servidor TCP iniciado en {self.host}:{self.port}")

        while True:
            
            
            # Inicia un hilo para manejar la comunicación con el cliente
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, message))
            client_thread.start()

    def handle_client(self, client_socket, message):
        """Maneja la comunicación con un cliente conectado."""
        try:
            # Aquí podrías realizar alguna lógica con el mensaje si fuera necesario
            # En este caso, simplemente lo enviamos de vuelta
            self.send_response(client_socket, f"Mensaje recibido: {message}")

        except Exception as e:
            print(f"Error al manejar cliente: {e}")

        finally:
            client_socket.close()

    def send_response(self, client_socket, message):
        """Envía una respuesta al cliente conectado."""
        client_socket.sendall(message.encode('utf-8'))
        print(f"Respuesta enviada: {message}")

    def stop_server(self):
        """Detiene el servidor TCP (si es necesario)."""
        if self.server_socket:
            self.server_socket.close()
            print("Servidor TCP detenido.")

# Función main para ejecutar el servidor
def main(message):
    # Crear una instancia del servidor TCP
    tcp_server = TCPServer(host='127.0.0.1', port=5000)
    
    # Iniciar el servidor en un hilo para que no bloquee el flujo principal
    server_thread = threading.Thread(target=tcp_server.start_server(message))
    server_thread.daemon = True  # Permite que el hilo termine cuando termine el programa principal
    server_thread.start()

    try:
        while True:
            # El servidor sigue ejecutándose en segundo plano.
            pass
    except KeyboardInterrupt:
        print("Servidor detenido por el usuario.")
        tcp_server.stop_server()

if __name__ == "__main__":
    main()
