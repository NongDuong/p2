from wtforms import Form, SubmitField, IntegerField, FloatField, StringField, TextAreaField, validators, DecimalField
from flask_wtf.file import FileField, FileRequired, FileAllowed


class Addproducts(Form):
    name = StringField('Tên sản phẩm', [validators.DataRequired()])
    price = DecimalField('Giá', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Số lượng', [validators.DataRequired()])
    colors = StringField('Màu sắc', [validators.DataRequired()])
    description = TextAreaField('Mô tả', [validators.DataRequired()])

    image_1 = FileField('Ảnh 1',
                        validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'], 'Chọn 1 ảnh'), FileRequired()])
    image_2 = FileField('Ảnh 2',
                        validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'], 'Chọn 1 ảnh'), FileRequired()])
    image_3 = FileField('Ảnh 3',
                        validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'], 'Chọn 1 ảnh'), FileRequired()])


class Rates(Form):
    register_id = IntegerField('Register_id', [validators.DataRequired()])
    product_id = IntegerField('Product_id', [validators.DataRequired()])
    desc = TextAreaField('Desc', [validators.DataRequired()])
