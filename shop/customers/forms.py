from wtforms import Form, StringField, BooleanField, TextAreaField, PasswordField, SubmitField, validators, \
    ValidationError, \
    RadioField
from flask_wtf.file import FileRequired, FileAllowed, FileField
from flask_wtf import FlaskForm
from flask import Markup
from .models import Register
import phonenumbers


class CustomerRegisterForm(FlaskForm):
    username = StringField('Tên người dùng: ', [validators.DataRequired(), validators.Length(min=4, max=20)])
    first_name = StringField('Họ: ')
    last_name = StringField('Tên: ')
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    phone_number = StringField('Số điện thoại: ', [validators.DataRequired()])
    gender = RadioField('Giới tính:', default='M', choices=[('M', 'Nam'), ('F', 'Nữ')])
    password = PasswordField('Mật khẩu: ', [validators.DataRequired(),
                                            validators.EqualTo('confirm', message=' Cả 2 mật khẩu phải trùng nhau! ')])
    confirm = PasswordField('Nhập lại mật khẩu: ', [validators.DataRequired()])

    submit = SubmitField('Đăng ký')

    def validate_username(self, username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError("Tên đăng nhập đã tồn tại!")

    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError("Địa chỉ email này đã được sử dụng!")

    def validate_phone_number(self, phone_number):
        if Register.query.filter_by(phone_number=phone_number.data).first():
            raise ValidationError("Số điện thoại này đã được sử dụng!")

        try:
            input_number = phonenumbers.parse(phone_number.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Số điện thoại không hợp lệ.')
        except:
            input_number = phonenumbers.parse("+84" + phone_number.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Số điện thoại không hợp lệ.')


class CustomerLoginFrom(FlaskForm):
    # email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    username = StringField('Tên người dùng: ', [validators.DataRequired()])
    password = PasswordField('Mật khẩu: ', [validators.DataRequired()])


