from django.contrib import admin
from .models import site_User,Post,Comment


class post(admin.ModelAdmin):
    list_display =  [field.name for field in Post._meta.fields]
class site_user(admin.ModelAdmin):
    list_display =  [field.name for field in site_User._meta.fields]
class comment(admin.ModelAdmin):
    list_display =   [field.name for field in Comment._meta.fields]

admin.site.register(Post,post)
admin.site.register(site_User ,site_user)
admin.site.register(Comment , comment)


"""

class opinion(admin.ModelAdmin):
    list_display = ('user', 'comment_id', 'product')
class shop(admin.ModelAdmin):
    list_display = ('track_id', 'cart')

class track(admin.ModelAdmin):
    list_display = ('id' , 'track_id')
      

admin.site.register(CustomUser,customUser)
admin.site.register(Product,product)
admin.site.register(Token)
admin.site.register(Cart)
admin.site.register(CartItem)
"""