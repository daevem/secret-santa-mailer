import os.path
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from person import Person

santa = "saint.nick.thereal@gmail.com"
pwd = "secre7santa."
preset_mail = ' <div style="width:70%; margin:auto; background-color: #faf6eb; border:15px solid #c91e18; border-width: 5px;  border-radius: 0px; position:relative; padding:15px;">\
<h1 style="color: #5e9ca0;">Ho! Ho! Ho!</h1> \
<h2 style="color: #2e6c80;">{} {},</h2> \
<p>Quest\'anno ho bisogno del tuo aiuto per portare la magia del Natale nel cuore delle persone. Ho pescato dalla mia lista di chi si &egrave; comportato bene un nome e il tuo compito sar&agrave; quello di trovare il regalo perfetto!</p> \
<p>Mi raccomando, &egrave; molto importante che tu trovi qualcosa che non costi pi&ugrave; di {} &euro;, non voglio mica mandarti in rovina!</p> \
<p>La persona in questione &egrave; <span style="background: #317a45; color: #fff; display: inline-block; padding: 3px 10px; font-weight: bold; border-radius: 5px;">{}&nbsp;{}</span> .</p>\
<p>Se dovessi avere qualche difficolt&agrave; a trovare un qualcosa di adeguato, non preoccuparti, ecco qui alcune idee prese dalla liste di regali che mi ha mandato gli anni scorsi ;)</p>\
<h2 style="color: #2e6c80;">A {} piace:</h2>'

likes_list_el = '<ol style="list-style: none; font-size: 14px; line-height: 32px; font-weight: bold;"> \
<li style="clear: both;"><img style="float: left;width: 30px" src="https://www.freeiconspng.com/uploads/classic-red-baubles-png-0.png" alt="interactive connection" width="45" />{}</li>\
</ol>'

preset_mail_end = "<p>Conto su di te!</p><p>Un abbraccio, </p><p>Claus</p> <p>P.S. Ricordati di stampare il bigliettino!</p>\
<p style=\"color: gray;font-size: 8pt;\">CONFIDENTIALITY NOTICE: The information contained in this e-mail message may be privileged, confidential and protected from disclosure. If you are not the intended recipient, any use, disclosure, dissemination, distribution or copying of any portion of this message or any attachment is strictly prohibited. If you think you have received this e-mail message in error, please notify the santa at the above e-mail address, and delete this e-mail along with any attachments. Thank you.</p>\
<hr><p>Saint Nicholas (Santa Claus)</p> \
<p style=\"color: gray;font-size: 8pt;\">BSc Veterinary Nursing, BEng Mechanical Engineering<br> \
MEng Aerospace Engineering, MSc Communications<br> \
PhD Advanced Physics</p>\
"


class SecretSantaSender:

    def __init__(self, santas_email, santas_pwd, smtp_server="smtp.gmail.com"):
        self.santas_email = santas_email
        self.santas_pwd = santas_pwd
        self.smtp_server = smtp_server

    def send_to(self, santa_helper: Person, recipient: Person, max_expense=10, likes_sep=";",
                attachments_paths=None, email_object="Secret Santa"):
        text_msg = "Ho! Ho! Ho!"
        dear = "Cara"
        if santa_helper.gender == "m":
            dear = "Caro"
        elif santa_helper.gender != "f":
            dear = "Caro/a"

        html_msg = preset_mail.format(dear, santa_helper.name, max_expense,
                                      recipient.name, recipient.surname, recipient.name)
        likes = ""
        for like in recipient.likes.split(likes_sep):
            likes += likes_list_el.format(like)

        html_msg += likes + preset_mail_end
        part1 = MIMEText(text_msg, "text")
        part2 = MIMEText(html_msg, "html")

        message = MIMEMultipart("alternative")
        message["Subject"] = email_object
        message["From"] = "Santa Claus" + "<"+santa+">"
        message["To"] = santa_helper.name + "<"+santa_helper.email+">"
        message.attach(part1)
        message.attach(part2)

        if attachments_paths is not None:
            for path in attachments_paths:
                with open(path, "rb") as opened:
                    openedfile = opened.read()
                attachedfile = MIMEApplication(openedfile, _subtype="pdf")
                attachedfile.add_header('content-disposition', 'attachment', filename=os.path.basename(path))
                message.attach(attachedfile)

        ctx = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, 465, context=ctx) as server:
            server.login(self.santas_email, self.santas_pwd)
            server.sendmail(
                santa, santa_helper.email, message.as_string()
            )
            print(f"Secret Santa participation sent to {santa_helper.name} {santa_helper.surname}.")
