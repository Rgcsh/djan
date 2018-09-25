"""
Django settings for djan project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(s2!_ay+u0@^crndl4d&#nk*0c+&&f7$nv8ca=*77b)okqn_u9'
import memcache_toolbar.panels.memcache

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition
# 防止windows系统下链接mysql出错
import pymysql

pymysql.install_as_MySQLdb()

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'rgc',
	'debug_toolbar',  # 添加的
	'memcache_toolbar',
]

MIDDLEWARE = [
	# 'django.middleware.cache.UpdateCacheMiddleware',
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

# LOGGING = {
# 	'version': 1,
# 	'disable_existing_loggers': False,
# 	'handlers': {
# 		'console': {
# 			'class': 'logging.StreamHandler',
# 		},
# 	},
# 	'loggers': {
# 		'django.db.backends': {
# 			'handlers': ['console'],
# 			'level': 'DEBUG' if DEBUG else 'INFO',
# 		},
# 	},
# }

LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'standard': {
			'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s]'
					  ' [%(levelname)s]- %(message)s'
		},  # 日志格式
	},
	'handlers': {
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
		}
	},
	'loggers': {
		'django': {
			'handlers': ['default','console'],
			'level': 'DEBUG',
			'propagate': False
		},
		# 'django.server': {
		# 	'handlers': ['console', 'default'],
		# 	'level': 'DEBUG',
		# 	'propagate': True
		# }
	}
}

DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i:s'
