import os
#导入 dev环境的配置，每次导入不同环境时，更改此导入文件
from djan.settings.dev import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = '(s2!_ay+u0@^crndl4d&#nk*0c+&&f7$nv8ca=*77b)okqn_u9'
import memcache_toolbar.panels.memcache

# celery
import djcelery

djcelery.setup_loader()
# BROKER_URL = 'amqp://guest@localhost//'
# CELERY_RESULT_BACKEND = 'amqp://guest@localhost//'

BROKER_URL = 'redis://127.0.0.1:6379/5'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/4'
CELERY_ACCEPT_CONTENT = ['json']
ALLOWED_HOSTS = ['*']

# Application definition
# 防止windows系统下链接mysql出错
import pymysql

pymysql.install_as_MySQLdb()

# 非空链接，却发生404错误，发送通知MANAGERS
SEND_BROKEN_LINK_EMAILS = True
# Email设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'rgc',
	'blog',
	'djcelery',
	'debug_toolbar',  # 添加的
	'memcache_toolbar',
	'django.contrib.sitemaps',
]

MIDDLEWARE = [
	# 'django.middleware.cache.UpdateCacheMiddleware',
	'djan.middleware.BlackIpMiddleware',
	'debug_toolbar.middleware.DebugToolbarMiddleware',  # 添加的
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	# 'django.middleware.cache.FetchFromCacheMiddleware',
]
# SECURE_SSL_REDIRECT = True  #主动跳到https协议
ROOT_URLCONF = 'djan.urls'
APPEND_SLACH = False

# 配置缓存
CACHES = {
	'default': {
		'BACKEND': 'django_redis.cache.RedisCache',
		'LOCATION': 'redis://127.0.0.1:6379/1',
		'KEY_PREFIX': 'key',  #
		'TIMEOUT': 6,
		'OPTIONS': {
			'CLIENT_CLASS': 'django_redis.client.DefaultClient',
			# 'CLIENT_CLASS': 'redis.client.Redis',
			'PICKLE_VERISON': -1,  # 序列化版本
			'SOCKET_CONNECT_TIMEOUT': 5,  # socket简历连接超时时间
			'SOCKET_TIMEOUT': 5,  # 建立连接后的读写操作超时时间
		}
	},
	'origin_redis': {  # 用于存储redis的业务常量值
		'BACKEND': 'django_redis.cache.RedisCache',
		'LOCATION': 'redis://127.0.0.1:6379/2',
		'OPTIONS': {
			'CLIENT_CLASS': 'django_redis.client.DefaultClient',
			# 'CLIENT_CLASS': 'redis.client.Redis',
			'PICKLE_VERISON': -1,  # 序列化版本
			'SOCKET_CONNECT_TIMEOUT': 5,  # socket简历连接超时时间
			'SOCKET_TIMEOUT': 5,  # 建立连接后的读写操作超时时间
		}
	}
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
DJANGO_REDIS_LOGGER = 'log.log'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'djan.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False

USE_I18N = True

USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
# 加载json数据到数据库的目录
FIXTURE_DIRS = [os.path.join(BASE_DIR, 'fixture_dir')]
# debug toolbar
CONFIG_DEFAULTS = {
	# 因为默认使用google的jquery，国内访问不到
	'JQUERY_URL': '//cdn.bootcss.com/jquery/2.1.4/jquery.min.js',
	'RESULTS_CACHE_SIZE': 3,
	'SHOW_COLLAPSED': True,
	'SQL_WARNING_THRESHOLD': 100,  # milliseconds
}
INTERNAL_IPS = ("127.0.0.1",)

DEBUG_TOOLBAR_PANELS = [
	'debug_toolbar.panels.versions.VersionsPanel',
	'debug_toolbar.panels.timer.TimerPanel',
	'debug_toolbar.panels.settings.SettingsPanel',
	'debug_toolbar.panels.headers.HeadersPanel',
	'debug_toolbar.panels.request.RequestPanel',
	'debug_toolbar.panels.sql.SQLPanel',
	'debug_toolbar.panels.staticfiles.StaticFilesPanel',
	'debug_toolbar.panels.templates.TemplatesPanel',
	'debug_toolbar.panels.cache.CachePanel',
	'debug_toolbar.panels.signals.SignalsPanel',
	'debug_toolbar.panels.logging.LoggingPanel',
	'debug_toolbar.panels.redirects.RedirectsPanel',
	'ddt_request_history.panels.request_history.RequestHistoryPanel',
	'memcache_toolbar.panels.memcache.MemcachePanel',
]

# https://blog.csdn.net/haeasringnar/article/details/82053714
# https://blog.csdn.net/sinat_29699167/article/details/79690889
# https://www.jb51.net/article/105563.htm
# https://www.cnblogs.com/luohengstudy/p/6890395.html
LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {  # 日志格式
		'standard': {
			'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s]'
					  ' [%(levelname)s]- %(message)s'
		},  # 日志格式
	},
	'handlers': {  # 处理器
		'default': {
			'level': 'DEBUG',
			'class': 'logging.handlers.RotatingFileHandler',
			'filename': BASE_DIR + '/logs/debug.log',
			'maxBytes': 1024 * 1024 * 5,
			'formatter': 'standard',
			'backupCount': 5,
		},
		'time': {
			'level': 'DEBUG',
			'class': 'logging.handlers.TimedRotatingFileHandler',
			'filename': BASE_DIR + '/logs/debug.log',
			'when': 'D',
			'formatter': 'standard',
			'backupCount': 5,
		},
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
			# 'stream': open(BASE_DIR + '/logs/debug.log', 'w+'),
			'formatter': 'standard',
		},
		'error': {
			'level': 'ERROR',
			'class': 'logging.handlers.RotatingFileHandler',
			'filename': BASE_DIR + '/logs/error.log',
			'maxBytes': 1024 * 1024 * 5,
			'backupCount': 5,
			'formatter': 'standard',
		},
		'mail_admins': {
			'level': 'INFO',
			'class': 'django.utils.log.AdminEmailHandler',
			'include_html': True,
		},
	},
	'loggers': {  # 日志记录器
		'django': {
			'handlers': ['default', 'console'],
			'level': 'INFO',
			'propagate': True
		},
		'django.server': {
			'handlers': ['error'],
			'level': 'DEBUG',
			'propagate': False
		},
		# 'django.request': {  # 这些名字不能随意写
		# 	'handlers': ['default', 'mail_admins'],
		# 	'level': 'DEBUG',
		# 	'propagate': True
		# },
	}
}

DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i:s'