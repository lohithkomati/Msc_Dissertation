from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent


# -----------------------------------------------------------------------------
# Core
# -----------------------------------------------------------------------------

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv(
        "ALLOWED_HOSTS",
        "127.0.0.1,localhost"
    ).split(",")
]


# -----------------------------------------------------------------------------
# Applications
# -----------------------------------------------------------------------------

DJANGO_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

]

THIRD_PARTY_APPS = [

    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "channels",
    "rest_framework_simplejwt",

]

LOCAL_APPS = [

    "users",
    "cases",
    "patients",
    "consultations",
    "feedback",

]

INSTALLED_APPS = (

    DJANGO_APPS
    + THIRD_PARTY_APPS
    + LOCAL_APPS

)


# -----------------------------------------------------------------------------
# Middleware
# -----------------------------------------------------------------------------

MIDDLEWARE = [

    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.security.SecurityMiddleware",

    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]


ROOT_URLCONF = "core.urls"

WSGI_APPLICATION = "core.wsgi.application"

ASGI_APPLICATION = "core.asgi.application"


# -----------------------------------------------------------------------------
# Templates
# -----------------------------------------------------------------------------

TEMPLATES = [

    {

        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.debug",

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ]

        }

    }

]


# -----------------------------------------------------------------------------
# Database
# -----------------------------------------------------------------------------

DATABASES = {

    "default": {

        "ENGINE": "django.db.backends.postgresql",

        "NAME": os.getenv("DATABASE_NAME"),

        "USER": os.getenv("DATABASE_USER"),

        "PASSWORD": os.getenv("DATABASE_PASSWORD"),

        "HOST": os.getenv("DATABASE_HOST"),

        "PORT": os.getenv("DATABASE_PORT"),

    }

}


# -----------------------------------------------------------------------------
# Password Validation
# -----------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [

    {

        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"

    },

    {

        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator"

    },

    {

        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator"

    },

    {

        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator"

    },

]


# -----------------------------------------------------------------------------
# Internationalization
# -----------------------------------------------------------------------------

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# -----------------------------------------------------------------------------
# Static
# -----------------------------------------------------------------------------

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = (

    "whitenoise.storage.CompressedManifestStaticFilesStorage"

)

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# -----------------------------------------------------------------------------
# Default PK
# -----------------------------------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# -----------------------------------------------------------------------------
# REST Framework
# -----------------------------------------------------------------------------

REST_FRAMEWORK = {

    "DEFAULT_AUTHENTICATION_CLASSES": [

        "rest_framework_simplejwt.authentication.JWTAuthentication",

    ],

    "DEFAULT_PERMISSION_CLASSES": [

        "rest_framework.permissions.IsAuthenticated",

    ],

}


# -----------------------------------------------------------------------------
# JWT
# -----------------------------------------------------------------------------

from datetime import timedelta

SIMPLE_JWT = {

    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),

    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),

}


# -----------------------------------------------------------------------------
# CORS
# -----------------------------------------------------------------------------

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [

    "http://localhost:3000",

]


# -----------------------------------------------------------------------------
# Channels
# -----------------------------------------------------------------------------

CHANNEL_LAYERS = {

    "default": {

        "BACKEND": "channels_redis.core.RedisChannelLayer",

        "CONFIG": {

            "hosts": [

                os.getenv(
                    "REDIS_URL",
                    "redis://localhost:6379"
                )

            ]

        }

    }

}


# -----------------------------------------------------------------------------
# Custom User
# -----------------------------------------------------------------------------

AUTH_USER_MODEL = "users.User"


# -----------------------------------------------------------------------------
# Groq Configuration
# -----------------------------------------------------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = os.getenv(

    "GROQ_MODEL",

    "llama-3.3-70b-versatile"

)


# -----------------------------------------------------------------------------
# Whisper
# -----------------------------------------------------------------------------

WHISPER_MODEL = "medium"


# -----------------------------------------------------------------------------
# Kokoro
# -----------------------------------------------------------------------------

KOKORO_VOICE = "af_sarah"


# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------

LOGGING = {

    "version": 1,

    "disable_existing_loggers": False,

    "handlers": {

        "console": {

            "class": "logging.StreamHandler",

        }

    },

    "root": {

        "handlers": [

            "console"

        ],

        "level": "INFO",

    },

}