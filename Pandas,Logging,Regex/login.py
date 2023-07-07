import logging

logging.basicConfig(filename='loging.log',style='{',level=logging.DEBUG,format='{levelname}--{asctime}--{message}')
def login(username,password):
        logging.info(f'Attempting login using username: {username}')

        if(username=='admin' and password=='admin123'):
                logging.debug({'Credentials validating successfully!'})
      

        else:
                logging.error('Invalid username or password!')

#invalid
login('rehan','123')

#valid
login('admin','admin123')


