* #!/usr/bin/python3
# -*- encoding: utf-8 -*-
import whois, time, os
os.system('clear')

print ('\033[35m'+'''


           ▄█     █▄     ▄█    █▄     ▄██████▄   ▄█     ▄████████         
          ███     ███   ███    ███   ███    ███ ███    ███    ███         
          ███     ███   ███    ███   ███    ███ ███▌   ███    █▀          
          ███     ███  ▄███▄▄▄▄███▄▄ ███    ███ ███▌   ███                
          ███     ███ ▀▀███▀▀▀▀███▀  ███    ███ ███▌ ▀███████████         
          ███     ███   ███    ███   ███    ███ ███           ███         
          ███ ▄█▄ ███   ███    ███   ███    ███ ███     ▄█    ███         
           ▀███▀███▀    ███    █▀     ▀██████▀  █▀    ▄████████▀          
                                                                          
   ▄█    █▄    ███    █▄  ███▄▄▄▄       ███        ▄████████    ▄████████ 
  ███    ███   ███    ███ ███▀▀▀██▄ ▀█████████▄   ███    ███   ███    ███ 
  ███    ███   ███    ███ ███   ███    ▀███▀▀██   ███    █▀    ███    ███ 
 ▄███▄▄▄▄███▄▄ ███    ███ ███   ███     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀▀███▀▀▀▀███▀  ███    ███ ███   ███     ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███    ███   ███    ███ ███   ███     ███       ███    █▄  ▀███████████ 
  ███    ███   ███    ███ ███   ███     ███       ███    ███   ███    ███ 
  ███    █▀    ████████▀   ▀█   █▀     ▄████▀     ██████████   ███    ███ 
                                                               ███    ███    
                            
                            
                    (programador: carlosadrianosj)
               (Ferramenta criada para consultas no whois)

\n\n\n\n
''')

#verifica se o programa foi executado em modo root
permissão_do_usuario = os.geteuid()
if permissao_do_usuario != 0:
    for i in range(5):
        print("              Este programa precisa ser executado em modo ROOT!!\n\n")
        time.sleep(0.5)        
    print("                 Exemplo: sudo python3 lazy_nmap_hunter.py")
    os._exit(0)      
else:
    pass

#inicia o laço infinito na ferramenta
dns = True
while dns:
      #captura o texto digitado pelo usuário
      dominio = input("Para finalizar o programa digite exit\n\nALVO (ex: google.com): ")
      #consulta o whois
      consulta_whois = whois.whois(dominio)
      print("\n\n#########################################################################\n\n")
      #printa o resultado
      print(consulta_whois.text)
      print("\n\n#########################################################################\n\n")
      #caso exit for digitado, ele fecha o programa
      if dominio  == "exit":
            print("\n\nVolte Sempre!!")
            time.sleep(2)
            os.system('clear') 
            break
