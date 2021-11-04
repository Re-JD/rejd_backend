MY_DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'rejd_db',
        'USER':'rejd',
        'PASSWORD':'rejd1234',
        'HOST':'rejd.cf4qwapddws1.ap-northeast-2.rds.amazonaws.com',
        'PORT':'3306',
         'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
MY_EMAIL_HOST_USER ='ansungho22@gmail.com',
MY_EMAIL_HOST_PASSWORD = 'zx2046cv:)',
MY_SECRET_KEY = 'django-insecure-q)cg*&96epx2n+o@hz2-b5a6-8eg95jd@e0yu+kt%+aeqmpcud'