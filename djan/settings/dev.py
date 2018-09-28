
DEBUG = True
BLACK_IPS = ['127.0.0.11']

# 管理员邮箱
ADMINS = (
	('rgc', '2020956572@qq.com'),
)
MANAGERS = ADMINS
EMAIL_HOST = 'smtp.qq.com'  # QQ邮箱SMTP服务器(邮箱需要开通SMTP服务)
EMAIL_PORT = 465  # QQ邮箱SMTP服务端口
EMAIL_HOST_USER = '2020956572@qq.com'  # 我的邮箱帐号
EMAIL_HOST_PASSWORD = 'dfkznaktacltdfca'  # 授权码
EMAIL_SUBJECT_PREFIX = 'website'  # 为邮件标题的前缀,默认是'[django]'
# EMAIL_USE_TLS = False  # 开启安全链接
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = SERVER_EMAIL = EMAIL_HOST_USER  # 设置发件人

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
	# 'default': {
	# 	'ENGINE': 'django.db.backends.sqlite3',
	# 	'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	# }
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'djan',
		'USER': 'root',
		'PASSWORD': '',
		'HOST': '127.0.0.1',
		'PORT': '3306'
	}
}