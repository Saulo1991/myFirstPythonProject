import socket
import sys

def portScanning(remote_host):
    try:
        for port in range(1, 254 + 1):
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_socket.settimeout(1)  # Define um timeout para evitar bloqueios
            data = tcp_socket.connect_ex((remote_host, port))
            if data == 0:
                try:
                    service = socket.getservbyport(port)
                except OSError:
                    service = "Unknown service"
                print(f"[+] Open {port}:::{service}")
            tcp_socket.close()  # Fecha o socket após a conexão
    except socket.gaierror:
        print("[-] Host remoto não encontrado [-]")
        exit()
    except socket.error:
        print("[-] Erro durante o socket [-]")
    return

def main():
    if len(sys.argv) != 2:
        print("Uso: python portscanning.py [host]")
    elif sys.argv[1] == "-h":
        print("python portscanning.py [host]")
    else:
        remote_host = sys.argv[1]
        portScanning(remote_host)
        
if __name__ == "__main__":
    main()
