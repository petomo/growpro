from django.contrib import admin
from . models import *
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from graphql_auth.models import UserStatus
from django.contrib.admin.models import LogEntry


# Register your models here.
# user

#page
class layoutForm(forms.ModelForm):
    #dest=forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        models=Layout
        fields='__all__'

class layout_imgFormInline(forms.ModelForm):
    dest=forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        models=Layout
        fields='__all__'

class layout_imgInline(admin.StackedInline):
    model=Layout_img
    pk_name='layout'
    form=layout_imgFormInline
    readonly_fields=['img_read']
    def img_read(self,obj):
        return mark_safe(u'<img src="/%s" />' % (obj.avatar))

class page_layoutInline(admin.StackedInline):
    model=Page_layout
    pk_name='layout'

class item_layoutInline(admin.StackedInline):
    model=Item_layout
    pk_name='layout'

class layoutAdmin(admin.ModelAdmin):
    inlines=(layout_imgInline, page_layoutInline, item_layoutInline)
    form =layoutForm   
    #list_display=["id","title","show","active","priority","parent","page","catergory"]
    list_filter=["show","active","parent"]
    search_fields=["id","title","parent"]

#product

class itemForm(forms.ModelForm):
    dest=forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        models=Item
        fields='__all__'

class tag_catergoryInline(admin.StackedInline):
    model=Tag_catergory
    pk_name='item'

class itemAdmin(admin.ModelAdmin):
    inlines =(tag_catergoryInline,)
    form=itemForm
    #list_display=["id","title","show","active","prite","prite_promotion"]
    list_filter=["show","active"]
    search_fields=["id","title"]
    readonly_fields=['img_read']
    def img_read(self,obj):
        return mark_safe(u'<img src="/%s" />' % (obj.avatar))
       
class img_Admin(admin.ModelAdmin):
    readonly_fields=['img_read']
    def img_read(self,obj):
        return mark_safe(u'<img src="/%s" />' % (obj.avatar))


#register
admin.site.register(LogEntry)

#user
admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Supplier)
admin.site.register(Group_user_join)
admin.site.register(Group_join)
admin.site.register(UserStatus)
admin.site.register(Chat)


#page
admin.site.register(Page)
admin.site.register(Menu)
admin.site.register(Layout,layoutAdmin)
admin.site.register(Layout_catergory)
admin.site.register(Items_seller)
admin.site.register(Invoice)
admin.site.register(LikeItems_seller)

#product
admin.site.register(Catergory)
admin.site.register(Tag_catergory)
admin.site.register(Item,itemAdmin)

