# check if today is a deadline for a new training cycle and if so, send mail to given emails
# cron needs to be set up to run this script once a day => 0 0 * * * /path/to/python /path/to/this/script.py
#
# prereq:
#       - mail server on linux machine
#       - cron

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import os

from datetime import timedelta, date

def sendMail(to, fro, subject, text, files=[],server="localhost"):
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = fro
    msg['To'] = to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    #for file in files:
    #    part = MIMEBase('application', "octet-stream")
    #    part.set_payload( open(file,"rb").read() )
    #    encoders.encode_base64(part)
    #    part.add_header('Content-Disposition', 'attachment; filename="%s"'
    #                   % os.path.basename(file))
    #    msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(fro, to, msg.as_string() )
    smtp.close()
    # Example: sendMail(['maSnun <masnun@gmail.com>'],'phpGeek <masnun@leevio.com>','Hello Python!','Heya buddy! Say hello to Python! :)')

def daterange(start_date):
    for n in range(0, NUM_OF_CYCLES * DAYS_IN_CYCLE, DAYS_IN_CYCLE):
        yield start_date + timedelta(n)

FIRST_CYCLE_START_DATE = date(2019, 11, 4)
NUM_OF_CYCLES = 13
DAYS_IN_CYCLE = 28

def main():
    recipients = ['otakar.hirs@gmail.com']
    subject = "Vyplň deníček"
    msg ="""
        Ahoj,
        včera skončil další cyklus. Pokud nechceš smutného či naštveného Šéďu, měl bys vyplnit deníček.
        http://reprezentace.orientacnibeh.cz/treninkovy-denik
        
        skončil cyklus číslo {cycle_number}
        {start_date} - {end_date}
        
        PeepPoop"""
    dateformat = "%-d.%-m.%Y" 

    for i, cycle_start_date in enumerate(daterange(FIRST_CYCLE_START_DATE)):
        if cycle_start_date + timedelta(DAYS_IN_CYCLE) == date.today():
            msg = msg.format(
                cycle_number = i + 1, 
                start_date = cycle_start_date.strftime(dateformat), 
                end_date = (cycle_start_date + timedelta(DAYS_IN_CYCLE) - 1).strftime(dateformat)                )
            for mail in recipients:
                sendMail(mail, 'RepreBot <reprebot@hirot.eu>', subject, msg)

if __name__ == "__main__":
    main()
