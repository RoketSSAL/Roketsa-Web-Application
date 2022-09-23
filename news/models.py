from time import time
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import threading
import time

import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# from sections.models import SectionCTA

EMAIL_CREDENTIALS = {
    "email_address": "furkanesen1900@gmail.com",
    "email_password": "dhubglzlisxrmfqu",
}


EMAIL_CONTENT = {
    "head": '<!DOCTYPE html> <html> <head> <meta charset="utf-8" /> <meta http-equiv="x-ua-compatible" content="ie=edge" /> <title>Yeni Haber</title> <meta name="viewport" content="width=device-width, initial-scale=1" /> <style type="text/css"> /** * Google webfonts. Recommended to include the .woff version for cross-client compatibility. */ @media screen { @font-face { font-family: "Source Sans Pro"; font-style: normal; font-weight: 400; src: local("Source Sans Pro Regular"), local("SourceSansPro-Regular"), url(https://fonts.gstatic.com/s/sourcesanspro/v10/ODelI1aHBYDBqgeIAH2zlBM0YzuT7MdOe03otPbuUS0.woff) format("woff"); } @font-face { font-family: "Source Sans Pro"; font-style: normal; font-weight: 700; src: local("Source Sans Pro Bold"), local("SourceSansPro-Bold"), url(https://fonts.gstatic.com/s/sourcesanspro/v10/toadOcfmlt9b38dHJxOBGFkQc6VGVFSmCnC_l7QZG60.woff) format("woff"); } } /** * Avoid browser level font resizing. * 1. Windows Mobile * 2. iOS / OSX */ body, table, td, a { -ms-text-size-adjust: 100%; /* 1 */ -webkit-text-size-adjust: 100%; /* 2 */ } /** * Remove extra space added to tables and cells in Outlook. */ table, td { mso-table-rspace: 0pt; mso-table-lspace: 0pt; } /** * Better fluid images in Internet Explorer. */ img { -ms-interpolation-mode: bicubic; } /** * Remove blue links for iOS devices. */ a[x-apple-data-detectors] { font-family: inherit !important; font-size: inherit !important; font-weight: inherit !important; line-height: inherit !important; color: inherit !important; text-decoration: none !important; } /** * Fix centering issues in Android 4.4. */ div[style*="margin: 16px 0;"] { margin: 0 !important; } body { width: 100% !important; height: 100% !important; padding: 0 !important; margin: 0 !important; } /** * Collapse table borders to avoid space between cells. */ table { border-collapse: collapse !important; width: 100%} a { color: #1a82e2; } img { height: auto; line-height: 100%; text-decoration: none; border: 0; outline: none; } body { background-color: #e9ecef; } td.header { padding: 36px 24px 0; font-family: "Source Sans Pro", Helvetica, Arial, sans-serif; border-top: 3px solid #d4dadf; } td.header h1 { margin: 0; font-size: 32px; font-weight: 700; letter-spacing: -1px; line-height: 48px; } .toptable { max-width: 600px; } .ndtable .ndtd { padding: 24px; font-family: "Source Sans Pro", Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px; } .ndtd p { margin: 0; } .startbtntd { padding: 12px; } .startbtntd td { border-radius: 6px; } p { margin: 0; } .startbtntd a { display: inline-block; padding: 16px 36px; font-family: "Source Sans Pro", Helvetica, Arial, sans-serif; font-size: 16px; color: #ffffff; text-decoration: none; border-radius: 6px; } .copybtntd { padding: 24px; font-family: "Source Sans Pro", Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px; } .copybtntd p { margin: 0; } .cheerstd { padding: 24px; font-family: "Source Sans Pro", Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px; border-bottom: 3px solid #d4dadf; } .cheerstd p { margin: 0; } .footer { padding: 24px; } .footertable { max-width: 600px; width: 100%  } .styleatt { padding: 12px 24px; font-family: "Source Sans Pro", Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; color: #666; } </style> </head>',
    "body": """
  <body>
    <table border="0" cellpadding="0" cellspacing="0" width="100%">
      <tr>
        <td align="center" bgcolor="#e9ecef"></td>
      </tr>
      <tr>
        <td align="center" bgcolor="#e9ecef">
          <table
            class="toptable"
            border="0"
            cellpadding="0"
            cellspacing="0"
            width="100%"
          >
            <tr>
              <td class="header" align="left" bgcolor="#ffffff">
                <h1>{}</h1>
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr>
        <td align="center" bgcolor="#e9ecef">
          <table
            class="toptable ndtable"
            border="0"
            cellpadding="0"
            cellspacing="0"
            width="100%"
          >
            <tr>
              <td class="ndtd" align="left" bgcolor="#ffffff">
                <p>{}</p>
              </td>
            </tr>

    
              <td class="cheerstd" align="left" bgcolor="#ffffff">
                <p>
                  Sevgilerle,<br />
                  {}
                </p>
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr>
        <td class="footer" align="center" bgcolor="#e9ecef">
          <table
            border="0"
            cellpadding="0"
            cellspacing="0"
            width="100%"
            class="footertable"
          >
            <tr>
              <td align="center" bgcolor="#e9ecef" class="styleatt">
                <p>
                  Bu postayı, Roketsa web sitesinin email bültenine kayıt olduğunuz için aldınız. Eğer size mail ile ulaşılmasını istemiyorsanız <a href="http://localhost:8000/mailing_list/remove">buraya</a> tıklayabilirsiniz.
                </p>
              </td>
            </tr>
            <tr>
              <td align="center" bgcolor="#e9ecef" class="styleatt">
                <p>Roketsa 1234. Beşiktaş, İstanbul, Türkiye</p>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>
""",
}

# Create your models here.

WHERE_FOUND_CHOICES = ()


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class MailingListUser(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    where_found = models.TextField(choices=WHERE_FOUND_CHOICES)

    creation_date = models.DateTimeField(default=timezone.now)


class Mail(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()

    send_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        is_created = self.pk is None

        super(Mail, self).save(*args, **kwargs)

        if is_created:
            now = timezone.now()
            if self.send_date > now:
                wait_until = self.send_date - timezone.now()
                wait_until = wait_until.seconds

            else:
                wait_until = 5
            mail_thread = threading.Thread(
                target=self.wait_for_mail, args=(wait_until,)
            )

            mail_thread.start()

    def wait_for_mail(self, secs):
        time.sleep(secs)
        self.send_mail_to_all()

    def send_mail_to_all(self):

        email_message = MIMEMultipart()
        email_message["From"] = EMAIL_CREDENTIALS["email_address"]
        recipients = self.format_user_mails()
        if len(recipients) >= 1:
            email_message["To"] = ", ".join(recipients)
            email_message["Subject"] = "Yeni bir haber var! | Roketsa"

            html_code = EMAIL_CONTENT["head"] + EMAIL_CONTENT["body"].format(
                self.title, self.content, self.author
            )

            email_message.attach(MIMEText(html_code, "html"))

            email_string = email_message.as_string()

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(
                    EMAIL_CREDENTIALS["email_address"],
                    EMAIL_CREDENTIALS["email_password"],
                )
                server.sendmail(
                    EMAIL_CREDENTIALS["email_address"], recipients, email_string
                )

    def format_user_mails(self):
        return [user.email for user in MailingListUser.objects.all()]
