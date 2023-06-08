from django.shortcuts import render,HttpResponse
from .models import Students
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore


# # Application Default credentials are automatically created.
# # app = firebase_admin.initialize_app()
# # db = firestore.client()
# # Create your views here.


# # Use the application default credentials.
# cred = credentials.Certificate('./mobihive-ebf11-firebase-adminsdk-75yzr-cf2ea1d11d.json')
# print(cred,'-cred')
# firebase_admin.initialize_app(cred)
# db = firestore.client()


# doc_ref = db.collection('students')

# auto_gen_key = doc_ref.document()

# auto_gen_key.set({
#     'name': 'Akshay',
#     'marks': 100,
#     'born': 1815
# })



# firebaseConfig = {
#   "apiKey": "AIzaSyCbo0Yx_UhaxFYK_O_11vv_o2aBw8XEywA",
#   "authDomain": "mobihive-labs-b6518.firebaseapp.com",
#   "projectId": "mobihive-labs-b6518",
#   "storageBucket": "mobihive-labs-b6518.appspot.com",
#   "messagingSenderId": "22555000448",
#   "appId": "1:22555000448:web:452a853f164037d1feb065",
#   "measurementId": "G-WNXKQYW1YV"
# }

# firebase=pyrebase.initialize_app(firebaseConfig)
# authe = firebase.auth()
# database=firebase.database()
    
def home_views(request):
    model = Students()
    data = model.save()
    print(data,'---model')
    return HttpResponse("Mayur")