import smtplib

EMAIL_ADRESS = 'ferkovladimir24@gmail.com'
EMAIL_PASSWORD = 'Di0r?yes'

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    smtp.sendmail(EMAIL_ADRESS, 'vladoferko3@gmail.com', 'cukes')