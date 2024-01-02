import bcrypt
import secrets

def makeSecretCode() :
    # 아무거나 상관없는 비밀번호 생성
    password = secrets.token_urlsafe(256)
    # 난수 솔트 생성
    salt = bcrypt.gensalt()
    # 비밀번호와 솔트를 결합하여 해싱
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password