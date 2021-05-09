from django.contrib.auth.modesl import User
user= User.objects.create_user('john','lennon@thebeatles.com', 'johnpassword')
user.last_name ='Lennon'
user.save()

