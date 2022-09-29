import smtplib

server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("lolday606@gmail.com","ztskhwqzmvanmjqn")
server.sendmail("lolday606@gmail.com","19nu1a05a1@nsrit.edu.in","rey mowa ayyipoyindhi ra ee mail chuste call cheyy ippude")

server.quit()