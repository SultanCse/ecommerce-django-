def confirm_msg(user, transection):   
    email_body ='''
    Hi %s,
    Urer transection id: %s
    Your purchasing completed successfully
    You will get your product within 7 days.
    For any help contact 01833.....
    Thank you
    PSTU Team 
    ''' % (user, transection)
    return email_body