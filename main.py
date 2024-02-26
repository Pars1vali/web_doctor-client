import streamlit as st
import streamlit.components.v1 as components
from google.oauth2 import id_token
from google.auth.transport import requests
import streamlit as st
from google.oauth2 import service_account
import streamlit as st
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import googleapiclient.discovery

# Файл ключа службы
SERVICE_ACCOUNT_FILE = '/service.json'

# Права доступа OAuth 2.0
SCOPES = ['https://www.googleapis.com/auth/userinfo.email',
          'https://www.googleapis.com/auth/userinfo.profile']


# Функция для получения авторизованного пользователя
def get_authenticated_service():
    creds = None
    try:
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    except FileNotFoundError:
        st.error('Файл ключа службы не найден.')
    except Exception as e:
        st.error(f'Произошла ошибка: {e}')

    return creds


# Функция для получения информации о пользователе
def get_user_info(credentials):
    try:
        service = googleapiclient.discovery.build('oauth2', 'v2', credentials=credentials)
        user_info = service.userinfo().get().execute()
        return user_info
    except Exception as e:
        st.error(f'Произошла ошибка при получении информации о пользователе: {e}')
        return None


# Получаем авторизованного пользователя
creds = get_authenticated_service()

if creds:
    # Получаем информацию о пользователе
    user_info = get_user_info(creds)

    if user_info:
        # Выводим информацию о пользователе
        st.title('Информация о пользователе Google')
        st.write(f'Имя: {user_info["name"]}')
        st.write(f'Email: {user_info["email"]}')
else:
    st.error('Не удалось получить авторизацию.')

