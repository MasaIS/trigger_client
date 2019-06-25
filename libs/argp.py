import argparse

def struct_args():
    """ Struct and check the arguments

        Arguments :
         none
        Return :
         args.address: IP address of FTP server
         args.user: Login user
         args.passwd: Login password
         args.dir: Directory name
         args.file: Temporary filename
    """

    parser = argparse.ArgumentParser(description='Script to transfer a trigger file via FTP')

    parser.add_argument('-a', '--address', type=str, help='IP address of FTP server', required=True)
    parser.add_argument('-u', '--user', type=str, help='Login user for FTP server', required=True)
    parser.add_argument('-p', '--passwd', type=str, help='Login password for FTP server', required=True)
    parser.add_argument('-d', '--dir', type=str, help='Directory name of trigger on FTP server', default='trig')
    parser.add_argument('-f', '--file', type=str, help='Filename of temporary file', default='tmp_trigger')
    parser.add_argument('-M', '--minutes', type=int, help='Maxium minutes of datetime', default=10)
    parser.add_argument('-S', '--seconds', type=int, help='Maxium seconds of datetime', default=59)
    parser.add_argument('-I', '--id', type=int, help='Maxium ids of module', default=3)

    args = parser.parse_args()

    #print('IP Address:' + args.address)
    #print('Login user:' + args.user)
    #print('Login password:' + args.passwd)
    #print('Change directory:' + args.dir)
    #print('Temporary filename:' + args.file)

    return args.address, args.user, args.passwd, args.dir, args.file, args.minutes, args.seconds, args.id
    