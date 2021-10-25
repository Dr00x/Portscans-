import socket

portas = [80,2222,4444,81,20,40,44,8080,2020,3030,4040,23,84,8888,53,443,8443]

print("-"*10,'Portscan ctrl+C kill',"-"*10)
endereco = str(input('endereço pra scaneamento (sem www.)\n>:'))


for i in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.1)
    try:
        code = cliente.connect_ex((endereco, i))
        serv = socket.getservbyport(i);
        protocol = socket.getprotobyname(serv)
    except:
        pass
        
    
    if code == 0:
        print(f"।porta:{format(i)}=OPEN   ।Codigo={format(code)}    ।Serviço={format(serv)}।")


print("-"*60)

