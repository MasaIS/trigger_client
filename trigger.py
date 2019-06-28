#!/user/bin/python3

from libs import txftp, mtime, argp
import sys, os, logging

if __name__ == "__main__":

    try:
        # output logging
        log_fmt = '%(asctime)s [%(levelname)s] : %(message)s'
        os.makedirs('logs', exist_ok=True)
        logging.basicConfig(filename='logs/trigger.log', level=logging.INFO, format=log_fmt)

        # input arguments
        args = {}
        args = argp.struct_args()

    except FileNotFoundError as err:
        print('logging error:', err)
        sys.exit(1) 
    
    except FileExistsError as err:
        print('logging error:', err)
        sys.exit(1) 
    
    else:
        logging.info('Start script: ' + __file__)
        # make trigger filename
        trigger_filename = mtime.make_trigger_datetime()
        if trigger_filename == False:
            sys.exit(1)

        # Create FTP Instance
        ftp_ins = txftp.ftp_init(args['address'],10)
        if ftp_ins == False:
            sys.exit(1)
        # FTP login
        if txftp.ftp_login(ftp_ins, args['user'], args['passwd']) == False:
            sys.exit(1)
        # FTP change directory
        if txftp.ftp_cwd(ftp_ins, args['dir']) == False:
            sys.exit(1)
        # Transfer temporary file
        if txftp.ftp_transfer(ftp_ins, args['file']) == False:
            sys.exit(1)
        # Rename to trigger filename
        if txftp.ftp_rename(ftp_ins, args['file'], trigger_filename) == False:
            sys.exit(1)
        # FTP logout
        if txftp.ftp_logout(ftp_ins) == False:
            sys.exit(1)
        # Replicate trigger file
        if mtime.replicate_trigger('logs', trigger_filename) == False:
            sys.exit(1)
        
        logging.info('Terminate script: ' + __file__)
        sys.exit(0)
