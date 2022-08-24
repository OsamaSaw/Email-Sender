import yagmail as yagmail


def print_emails_dict(email_dict):
    print("Email\tName ".expandtabs(50))
    print('-'*100)
    for k, v in email_dict.items():
        print(f"{k}\t{v}".expandtabs(50))


def get_email_dict():
    newEmail_dict = {}
    with open('emails.txt', 'r') as emails:
        for email in emails:
            userEmail = email.split(':')[0].strip()
            userName = email.split(':')[1].strip()
            newEmail_dict[userEmail] = userName
    return newEmail_dict


def get_email_body(name):
    subject = 'This is the subject'
    body = '''
    '''
    receiver = ''
    title = False
    person = False
    with open('body.txt', 'r',  encoding="utf8") as emailb:
        for line in emailb:
            if not title:
                subject = line
                title = True
            elif not person:
                receiver = line.strip()
                receiver += f' {name}'
                person = True
            else:
                body = body + line
    body = receiver + body
    return subject, receiver, body


if __name__ == '__main__':

    email_list = get_email_dict()
    print_emails_dict(email_list)
    img = 'image.jpg'

    input("\nSend Emails? ")

    yag = yagmail.SMTP("testing.email.git@gmail.com", oauth2_file="oauth2_creds.json")  # feel free to use this test Email, password :Testing!123
    for email, name in email_list.items():
        subject, rec, body = get_email_body(name)
        input("wait")
        yag.send(to=email, subject=subject, contents=[body, img])  # [body, img, html]
        print(f"mail Sent To {email}")

