from mask_site import mail
from flask_mail import Message
from mask_site.emails_package.forms import RegistrationForm


class email_form(RegistrationForm):
    def send_emails(self):
        msg = Message('Nowe zamówienie z Twojej strony', sender = 'maskadlaseniora.serwis@gmail.com',
        recipients=['a.tutakiewicz@gmail.com'] )
        msg.body = f''' 
        Hej

        Maska potrzebna dla seniora: 

        Imię: {self.name.data}
        Nazwisko: {self.surname.data}
        Email: {self.email.data}
        Ulica, numer: {self.address.data}
        Miejscowość: {self.address_2.data}
        Kod pocztowy: {self.post_code.data}
        Ilość: {self.quantity.data}
        
        Dziękujemy. 

        
        Skontaktuj się: maskadlaseniora.serwis@gmail.com
                      '''
        print(f'We are sending masks for ',{self.name.data})
        mail.send(msg)









    """
    def __init__(self, email_name, email_surname, email_email, email_address, email_address_2, email_post_code, email_quantity):
            self.email_name = 'Imię:' +email_name
            self.email_surname = 'Nazwisko:'+email_surname
            self.email_email = 'Adres email: ' + email_email
            self.email_address = 'Ulica, numer domu: ' +email_address
            self.email_address_2 ='Miejscowość: '+ email_address_2
            self.email_post_code = 'Kod pocztowy: ' + email_post_code
            self.email_quantity = 'Ilość maseczek:' + email_quantity
    """
    
    
    








    
