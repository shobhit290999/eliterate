from django.urls import path
from . import views

urlpatterns = [
    path("",views.index), #"" --> localhost/user, domain/user
    path("home/",views.home), # localhost/user/home --> home function
     #localhost/user/index --> myhome
    path("login/",views.login),
    path("afterlogin/",views.afterlogin),
    path("signup/",views.signup),
    path("aftersignup/",views.aftersignup.as_view()),
    path("logout/",views.logout),
    path("forgot/",views.getform),
    path("getotp/",views.forgot),
    path("afterotp/",views.afterotp),
    path("about/",views.about),
    path("terms/",views.terms),
    path("program/",views.program),
     path("jee/",views.jee),
      path("neet/",views.neet),
       path("cet/",views.cet),
        path("gate/",views.gate),
         path("gatecse/",views.gatecse),
          path("gateece/",views.gateece),
           path("gateee/",views.gateee),
            path("gatece/",views.gatece),
             path("gateme/",views.gateme),
             path("gatech/",views.gatech),
              path("studymaterial/",views.studymaterial),
              path("pyp/",views.pyp),
               path("interns/",views.interns),
             
                 path("team/",views.team),
                  path("contact/",views.contact),
                    path("register/",views.register),
                    path("registerpro/",views.registerpro),
                      path("contactpro/",views.contactpro),
             
    
    
    path("getpass/",views.change)
]
#till aftersignup the view was our function now we have to change
#we want our view to be a class