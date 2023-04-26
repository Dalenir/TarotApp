import secrets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import digits
from typing import Annotated

from fastapi import APIRouter, Form

from database.Cashing import RedCache
from security.UserManager import register_user
from settings import main_settings

router = APIRouter(prefix="/security")


# TODO: Can be a separate service for sending email.
#  Unjustified on this scale, so perhaps with additional (messaging?) logic.
#   Separate service only for users will be nice I think.
#    Tho I do not like idea of separating databases at all, I need both for game and users data.
#     So if I want separate service, I'm better find much cooler idea, or it will be just show off.


@router.post("/email_code_verify")
async def email_code_verify(username: Annotated[str, Form()],
                            email: Annotated[str, Form()],
                            password: Annotated[str, Form()],
                            code: Annotated[str, Form()]):
    cache = RedCache(email)
    if await cache.get('verification_code') == code:
        await register_user(username=username, email=email, password=password)
        await cache.delete(f'potential_mail:{username}')
        return {'success': True}
    return {'success': False}


@router.post("/new_user_reg")
async def registration_first_step(email: Annotated[str, Form()]):

    secret_code = ''.join(secrets.choice(digits) for i in range(7))

    smtp_obj = smtplib.SMTP(host='smtp.elasticemail.com', port=2525)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.ehlo()
    smtp_obj.login(main_settings.EMAIL_LOGIN, main_settings.EMAIL_PASSW)

    msg = MIMEMultipart()
    msg['From'] = main_settings.EMAIL_LOGIN
    msg['To'] = email
    msg['Subject'] = 'simple email in python'
    msg.attach(MIMEText('<h3>Your code is:</h3><br><h1>' + secret_code + '</b></h1>', 'html'))
    smtp_obj.sendmail(main_settings.EMAIL_LOGIN, email, msg.as_string())
    smtp_obj.quit()

    cache = RedCache(email)
    expire_seconds = 350
    await cache.set('verification_code', secret_code, expire_seconds)

    return {'exp_s': expire_seconds}
