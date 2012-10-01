# Create the database engine
import seppubs.config

url = seppubs.config.get('sqlalchemy', 'url')
engine = create_engine(url, echo=False, pool_recycle=30) 

# configure Session class with desired options.
Session = scoped_session(sessionmaker())
Session.configure(bind=engine)

metadata = MetaData()
