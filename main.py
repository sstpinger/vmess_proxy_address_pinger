import ipaddress
import socket
import ssl

def check_tls_connection(ip, port=443, timeout=3):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    
    try:
        with socket.create_connection((ip, port), timeout=timeout) as sock:
            with context.wrap_socket(sock, server_hostname=ip) as ssock:
                # Try to complete the TLS handshake
                ssock.do_handshake()
                return True
    except (ssl.SSLCertVerificationError, ssl.SSLError, socket.timeout):
        # Handle SSL errors, timeouts, and certificate mismatches gracefully
        return False
    except (ConnectionResetError, OSError):
        # Handle errors such as connection reset by peer or other OS-related network errors
        return False
    except Exception as e:
        # General exception handling to catch anything unexpected
        print(f"An unexpected error occurred: {e}")
        return False

def list_successful_tls_ips_from_range(ip_range):
    successful_ips = []
    network = ipaddress.ip_network(ip_range)
    for ip in network.hosts():  # Exclude network and broadcast addresses
        if check_tls_connection(str(ip)):
            successful_ips.append(str(ip))
            print(f"Successful TLS connection at {ip}")
        # else:
        #     print(f"Failed TLS connection at {ip}")
    return successful_ips

def list_successful_tls_ips(ips):
    successful_ips = []
    for ip in ips:  # Exclude network and broadcast addresses
        if check_tls_connection(str(ip)):
            successful_ips.append(str(ip))
            print(f"Successful TLS connection at {ip}")
        # else:
        #     print(f"Failed TLS connection at {ip}")
    return successful_ips

# Example usage
ip_range = '151.101.64.0/21'  # Replace with your specific IP range
ips = [
'151.101.64.79',
'151.101.64.81',
'151.101.64.82',
'151.101.64.84',
'151.101.64.93',
'151.101.64.97',
'151.101.64.114',
'151.101.64.116',
'151.101.64.124',
'151.101.64.134',
'151.101.64.138',
'151.101.64.144',
'151.101.64.152',
'151.101.64.153',
'151.101.64.155',
'151.101.64.157',
'151.101.64.158',
'151.101.64.159',
'151.101.64.160',
'151.101.64.167',
'151.101.64.172',
'151.101.64.174',
'151.101.64.193',
'151.101.64.194',
'151.101.64.195',
'151.101.64.200',
'151.101.64.203',
'151.101.64.208',
'151.101.64.223',
'151.101.64.228',
'151.101.64.238',
'151.101.64.239',
'151.101.65.12',
'151.101.65.16',
'151.101.65.29',
'151.101.65.30',
'151.101.65.36',
'151.101.65.38',
'151.101.65.42',
'151.101.65.44',
'151.101.65.50',
'151.101.65.54',
'151.101.65.57',
'151.101.65.59',
'151.101.65.60',
'151.101.65.66',
'151.101.65.67',
'151.101.65.72',
'151.101.65.73',
'151.101.65.74',
'151.101.65.80',
'151.101.65.81',
'151.101.65.87',
'151.101.65.106',
'151.101.65.108',
'151.101.65.111',
'151.101.65.114',
'151.101.65.119',
'151.101.65.120',
'151.101.65.122',
'151.101.65.124',
'151.101.65.125',
'151.101.65.126',
'151.101.65.135',
'151.101.65.136',
'151.101.65.137',
'151.101.65.140',
'151.101.65.145',
'151.101.65.148',
'151.101.65.151',
'151.101.65.153',
'151.101.65.154',
'151.101.65.156',
'151.101.65.158',
'151.101.65.160',
'151.101.65.164',
'151.101.65.188',
'151.101.65.190',
'151.101.65.193',
'151.101.65.202',
'151.101.65.203',
'151.101.65.204',
'151.101.65.210',
'151.101.65.215',
'151.101.65.220',
'151.101.65.224',
'151.101.65.227',
'151.101.65.229',
'151.101.65.244',
'151.101.65.245',
'151.101.65.249',
'151.101.65.253',
'151.101.65.254',
'151.101.66.3',
'151.101.66.10',
'151.101.66.16',
'151.101.66.21',
'151.101.66.27',
'151.101.66.29',
'151.101.66.35',
'151.101.66.38',
]
successful_ips = list_successful_tls_ips(ips)
