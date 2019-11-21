from peewee import *

database = MySQLDatabase('test', **{'charset': 'utf8', 'use_unicode': True, 'host': 'localhost', 'user': 'root', 'password': 'Cc1993'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AuthGroup(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = 'auth_group'

class DjangoContentType(BaseModel):
    app_label = CharField()
    model = CharField()

    class Meta:
        table_name = 'django_content_type'
        indexes = (
            (('app_label', 'model'), True),
        )

class AuthPermission(BaseModel):
    codename = CharField()
    content_type = ForeignKeyField(column_name='content_type_id', field='id', model=DjangoContentType)
    name = CharField()

    class Meta:
        table_name = 'auth_permission'
        indexes = (
            (('content_type', 'codename'), True),
        )

class AuthGroupPermissions(BaseModel):
    group = ForeignKeyField(column_name='group_id', field='id', model=AuthGroup)
    permission = ForeignKeyField(column_name='permission_id', field='id', model=AuthPermission)

    class Meta:
        table_name = 'auth_group_permissions'
        indexes = (
            (('group', 'permission'), True),
        )

class AuthUser(BaseModel):
    date_joined = DateTimeField()
    email = CharField()
    first_name = CharField()
    is_active = IntegerField()
    is_staff = IntegerField()
    is_superuser = IntegerField()
    last_login = DateTimeField(null=True)
    last_name = CharField()
    password = CharField()
    username = CharField(unique=True)

    class Meta:
        table_name = 'auth_user'

class AuthUserGroups(BaseModel):
    group = ForeignKeyField(column_name='group_id', field='id', model=AuthGroup)
    user = ForeignKeyField(column_name='user_id', field='id', model=AuthUser)

    class Meta:
        table_name = 'auth_user_groups'
        indexes = (
            (('user', 'group'), True),
        )

class AuthUserUserPermissions(BaseModel):
    permission = ForeignKeyField(column_name='permission_id', field='id', model=AuthPermission)
    user = ForeignKeyField(column_name='user_id', field='id', model=AuthUser)

    class Meta:
        table_name = 'auth_user_user_permissions'
        indexes = (
            (('user', 'permission'), True),
        )

class CrawlData(BaseModel):
    content = CharField(null=True)
    crawl_time = DateTimeField(null=True)
    emotion = IntegerField(null=True)
    is_agriculture = IntegerField(null=True)
    keywords = CharField(null=True)
    publish_time = DateTimeField(null=True)
    source = CharField(null=True)
    summary = CharField(null=True)
    title = CharField(null=True)
    url = CharField(null=True)

    class Meta:
        table_name = 'crawl_data'

class CrawlDataCopy(BaseModel):
    content = CharField(null=True)
    crawl_time = DateTimeField(null=True)
    emotion = IntegerField(null=True)
    is_agriculture = IntegerField(null=True)
    keywords = CharField(null=True)
    publish_time = DateTimeField(null=True)
    source = CharField(null=True)
    summary = CharField(null=True)
    title = CharField(null=True)
    url = CharField(null=True)

    class Meta:
        table_name = 'crawl_data_copy'

class DjangoAdminLog(BaseModel):
    action_flag = IntegerField()
    action_time = DateTimeField()
    change_message = TextField()
    content_type = ForeignKeyField(column_name='content_type_id', field='id', model=DjangoContentType, null=True)
    object_id = TextField(null=True)
    object_repr = CharField()
    user = ForeignKeyField(column_name='user_id', field='id', model=AuthUser)

    class Meta:
        table_name = 'django_admin_log'

class DjangoMigrations(BaseModel):
    app = CharField()
    applied = DateTimeField()
    name = CharField()

    class Meta:
        table_name = 'django_migrations'

class DjangoSession(BaseModel):
    expire_date = DateTimeField(index=True)
    session_data = TextField()
    session_key = CharField(primary_key=True)

    class Meta:
        table_name = 'django_session'

class HomeArea(BaseModel):
    city = CharField(null=True)
    code = CharField(null=True)
    county = CharField(null=True)
    province = CharField(null=True)
    lat = FloatField(null=True)
    lng = FloatField(null=True)

    class Meta:
        table_name = 'home_area'

class HomeCrawldata(BaseModel):
    area = CharField(null=True)
    content = TextField(null=True)

    emotion = IntegerField(null=True)
    industry = CharField(null=True)
    is_agriculture = IntegerField(null=True)
    keywords = CharField(null=True)
    product_name = CharField(null=True)
    publish_time = CharField(null=True)
    source = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT -1")], null=True)
    summary = CharField(null=True)
    title = CharField(null=True)
    url = CharField(null=True)

    class Meta:
        table_name = 'home_crawldata'

class HomeCrawmodel(BaseModel):
    crawl_max_page = IntegerField(null=True)
    crawl_start_url = CharField(null=True)
    level_1 = CharField(null=True)
    level_2 = CharField(null=True)
    level_3 = CharField(null=True)
    web_name = CharField(null=True)

    class Meta:
        table_name = 'home_crawmodel'

class HomeProductnametocate(BaseModel):
    keyname = CharField(null=True)
    product_name = CharField(null=True)

    class Meta:
        table_name = 'home_productnametocate'



'''
for i in ['http://www.zgncpw.com/nongyezixun/','http://www.zgncpw.com/nongchanpin/']:
    p = HomeCrawmodel(crawl_start_url=i,web_name='中国农产品网',crawl_max_page=20)
    p.save()
'''



