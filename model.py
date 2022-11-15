from .setup import *


class ModelFPKtvItem(ModelBase):
    P = P
    __tablename__ = 'fp_ktv_item'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    __bind_key__ = P.package_name

    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.DateTime)

    call_module = db.Column(db.String)
    filename_original = db.Column(db.String)
    foldername = db.Column(db.String)
    filename_pre = db.Column(db.String)
    entity_data = db.Column(db.JSON)
    meta_find = db.Column(db.Boolean)
    status = db.Column(db.String) # REMOVE_BY_PRE  MOVE_BY_PRE MOVE_BY_META 
    # MOVE_BY_FTV  MOVE_BY_NOMETA MOVE_BY_NOTV
    result_folder = db.Column(db.String)
    result_filename = db.Column(db.String)
    is_dry = db.Column(db.Boolean)
    log = db.Column(db.String)


    def __init__(self, call_module, filename_original, foldername, is_dry):
        self.call_module = call_module
        self.filename_original = filename_original
        self.result_filename = filename_original
        self.filename_pre = filename_original
        self.foldername = foldername
        self.is_dry = is_dry
        self.created_time = datetime.now()
        self.log = ''

    
    @classmethod
    def make_query(cls, req, order='desc', search='', option1='all', option2='all'):
        with F.app.app_context():
            query1 = cls.make_query_search(F.db.session.query(cls), search, cls.filename_original)
            #query2 = cls.make_query_search(F.db.session.query(cls), search, cls.result_folder)
            #query = query1.union(query2)
            query = query1 
            if option1 != 'all':
                query = query.filter(cls.call_module == option1)
            if option2 != 'all':
                query = query.filter(cls.status == option2)
            
            if order == 'desc':
                query = query.order_by(desc(cls.id))
            else:
                query = query.order_by(cls.id)
            return query
