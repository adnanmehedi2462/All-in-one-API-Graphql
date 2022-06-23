# urls.py/////////////
# all in one 
from rest_framework import routers
route=routers.DefaultRouter()
route.register("allnewpost",allnewpost,basename="postallaction")
# end allin one

 urlpatterns = [
    # all in one 
    path('apipost',include(route.urls)),
    

    	
]
    
    
# views.py//////////////////////////////////



# all in one simple way ==== get post delete update

 
class allnewpost(ModelViewSet):
    serializer_class=mypostserializer
    queryset=Post.objects.all()
  
  
  
  
  
# serializer.py//////////////////////////////
from rest_framework import serializers
class mypostserializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=["title",'image']