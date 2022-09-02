from flask import Flask
from flask_mail import Mail,Message

app=Flask(__name__)

app.config['DEBUG']=True
app.config['TESTING']=False
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False
app.config['MAIL_USERNAME']='lolday606@gmail.com'
app.config['MAIL_PASSWORD']=''
app.config['MAIL_DEFAULT_SENDER']=''
app.config['MAIL_MAX_EMAILS']=None
app.config['MAIL_ASCII_ATTACHMENTS']=False

mail = Mail(app)

@app.route('/')
def index():
    msg=Message('Hey there',recipients=[''])
    msg.html='<b> this is a test mail so you dont have to reply</b>'
    with app.open_resource('cat.jpg') as cat:
        msg.attach('cat.jpg','image/jpeg',cat.read())
        
    mail.send(msg)
    
    msg=Message(
        subject='',
        recipients=[],
        body='',
        html='',
        sender='',
        cc=[],
        bcc=[],
        attachments=[],
        reply_to=[],
        date='date',
        charset='',
        extra_headers={'':''},
        mail_options=[],
        rcpt_options=[]
    )
    
@app.route('/mailbulk')
def bulk():
    users=[{'name':'lol','email':'lolday606@gmail.com'}]
    
    with mail.connect() as conn:
        for user in users:
            msg = Message('BULk',recipients=[user.email])
            msg.body='Hey There'
            conn.send(msg)
            
if __name__=='__main__':
    app.run()