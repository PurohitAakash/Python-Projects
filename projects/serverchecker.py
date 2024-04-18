import socket

def is_running(site):
    """"This function attempts to connect to the given server using a socket
    Returns : whether or not it was able to connect to the server."""
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((site, 80))
        return True
    except:
        
        
        return False
    
if __name__ == "__main__":
    while True:
        site = input('Website to check:')
        if is_running(f'{site}.com'):
            print(f'{site}.com is running')
        else:
            print(f'There is problem wtih the {site}.com')

        if input("would you like to try another website(Y/N)?") in {'n','N'}:
            break
