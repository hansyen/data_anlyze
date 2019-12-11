from flask_login import UserMixin
from __init__ import db
from sqlalchemy import func
from datetime import datetime

class Role():    #member level
    MEMBER = 1
    VERIFIED = 2
    AGENT = 3
    MANAGER = 4

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    api_code = db.Column(db.String(60))
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.Integer, default=1)

    # def __repr__(self):
    #     return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    def __repr__(self):
        return "User('{self.username}')"

# 用戶表
class BackEndUser(db.Model, UserMixin):
    __tablename__ = 'backend_user'
    id = db.Column(db.Integer, primary_key=True)  #database裡的列, integer整數
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    latest_login = db.Column(db.DateTime)
    is_block = db.Column(db.String(10), nullable=False, default=1)  # 1 : open ; 2 : lock
    role = db.Column(db.Integer, default='1')

# 法幣儲值
class BillingTicket(db.Model):
    __tablename__ = 'billing_ticket'
    id = db.Column(db.Integer, primary_key=True)
    web = db.Column(db.String(12)) # 商家代號
    provider = db.Column(db.String(20)) # 渠道提供商
    channel = db.Column(db.String(10)) # 渠道
    td = db.Column(db.String(20)) # 商家訂單編號
    buysafeno = db.Column(db.String(30)) # 第三方訂單編號
    mn = db.Column(db.Integer) # 交易金額
    name = db.Column(db.String(20)) # 消費者名稱
    note = db.Column(db.String(60)) # 備註
    card_no = db.Column(db.String(4)) # 信用卡後四碼
    term = db.Column(db.Integer) # 分期數
    approve_code = db.Column(db.String(10)) # 信用卡授權碼
    card_type = db.Column(db.Integer) # 信用卡類別 0:信用卡，1:銀聯卡
    errcode = db.Column(db.String(10)) # 交易錯誤碼
    errmsg = db.Column(db.String(60))
    status = db.Column(db.Integer) # 訂單狀態 0:create, 1:pedding, 2:success, 3:fail
    chk_value_my = db.Column(db.String(40)) # 本訂單產生的檢查碼
    chk_value_from = db.Column(db.String(40)) # 本訂單回傳的檢查碼
    create_time = db.Column(db.DateTime, default=func.now())

# 用戶資訊
class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(30))   # used for trans country code with phone
    nationality = db.Column(db.String(30))   # used for id-card verify
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    id_card = db.Column(db.String(128))  # save file path
    bill = db.Column(db.String(60))   # save file path
    family_name = db.Column(db.String(30))  # 姓氏
    first_name = db.Column(db.String(30))   # 本名
    sex = db.Column(db.String(10))
    birthday = db.Column(db.DateTime)

    # def __repr__(self):  #改變輸出時的樣子 repr的输出追求明确性，除了对象内容，还需要展示出对象的数据类型信息，适合开发和调试阶段使用 str的输出追求可读性，输出格式要便于理解，适合用于输出内容到用户终端
    #     return f"UserInfo(UserID='{self.uid}', UserMail='{self.email}', Phone='{self.phone}', ID_card='{self.id_card}', Bill='{self.bill}', family_name='{self.family_name}', first_name='{self.first_name}', sex='{self.sex}', birthday='{self.birthday}')"

class UserVerify(db.Model):
    __tablename__ = 'user_verify'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False)
    email = db.Column(db.Boolean)
    phone = db.Column(db.Boolean)
    id_card = db.Column(db.Boolean)
    bill = db.Column(db.Boolean)

