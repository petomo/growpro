from django.db import models
import json
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.contrib.admin.models import LogEntry,LogEntryManager
from django.contrib.contenttypes.models import ContentType
from django.utils.text import get_text_list
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

# Create your models here.
ADDITION = 1
CHANGE = 2
DELETION = 3

ACTION_FLAG_CHOICES = (
    (ADDITION, _("Addition")),
    (CHANGE, _("Change")),
    (DELETION, _("Deletion")),
)

Status_choise=(
    ('Create','Create'),
    ('Cancel','Cancel'),
    ('Accept','Accept'),
    ('Complete','Complete'),
)

Status_chat=(
    ('send','send'),
    ('read','read'),
    ('cancel','cancel'),
    ('delete','delete'),
)

Status_item=(
    ('Private','Private'),
    ('Internal','Internal'),
    ('Public','Public'),
)

class User(AbstractUser):
    avatar=models.ImageField(upload_to='static/upload/user/%Y/%m',null=True,blank=True)
    phone=models.CharField(max_length=255,null=True,blank=True,default="")
    address=models.CharField(max_length=255,null=True,blank=True,default="")
    coin=models.IntegerField(null=True,blank=True,default=0)

    def __str__(self) :
        return str(self.id) +" : "+ self.first_name+" "+self.last_name   
    def addCoin(self,coinadd):
        self.coin=self.coin+int(coinadd)
        self.save   
    def creat_Seller(selt):
        u=Seller()
        u.user=selt
        u.save   
    def creat_Supplier(selt):
        u=Supplier()
        u.user=selt
        u.save
    def creat_Buyer(selt):
        u=Buyer()
        u.user=selt
        u.save
    def creat_Invoice_buyer(selt):
        i=Invoice()
        i.verifier=selt
        i.status_now='create'
        i.save
        ih=Invoice_history()
        ih.user=selt
        ih.invoice=i
        ih.status=i.status_now
        ih.save
        return i
   
class Seller(models.Model):
    total_sales=models.IntegerField(null=False,blank=True,default=0)
    month_sales=models.IntegerField(null=False,blank=True,default=0)
    year_sales=models.IntegerField(null=False,blank=True,default=0)
    typeuser=models.IntegerField(null=False,blank=True,default=1)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False,unique=False)

    def __str__(self) :
        return str(self.id) +" : "+ self.user+" : "+self.typeuser
    def update_month_sales(self,x):
        self.month_sales=int(x)
        self.save
    def update_year_sales(self,x):
        self.year_sales=int(x)
        self.save
    def update_total_sales(self,x):
        self.total_sales=self.total_sales +int(x)
        self.save
    def update_typeuser(self,x):
        self.total_sales=self.typeuser +int(x)
        self.save

class Supplier(models.Model):
    total_sales=models.IntegerField(null=False,blank=True,default=0)
    month_sales=models.IntegerField(null=False,blank=True,default=0)
    year_sales=models.IntegerField(null=False,blank=True,default=0)
    typeuser=models.IntegerField(null=False,blank=True,default=1)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False,unique=False)

    def __str__(self) :
        return str(self.id) +" : "+ self.user+" : "+self.typeuser
    def update_month_sales(self,x):
        self.month_sales=int(x)
        self.save
    def update_year_sales(self,x):
        self.year_sales=int(x)
        self.save
    def update_total_sales(self,x):
        self.total_sales=self.total_sales +int(x)
        self.save
    def update_typeuser(self,x):
        self.total_sales=self.typeuser +int(x)
        self.save

class Buyer(models.Model):
    total_spending=models.IntegerField(null=False,blank=True,default=0)
    month_spending=models.IntegerField(null=False,blank=True,default=0)
    year_spending=models.IntegerField(null=False,blank=True,default=0)
    typeuser=models.IntegerField(null=False,blank=True,default=1)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False,unique=False)

    def __str__(self) :
        return str(self.id) +" : "+ self.user+" : "+self.typeuser
    def update_total_spending(self,x):
        self.total_spending=self.total_spending+int(x)
        self.save
    def update_month_spending(self,x):
        self.month_spending=int(x)
        self.save
    def update_year_spending(self,x):
        self.year_spending=int(x)
        self.save
    def update_typeuser(self,x):
        self.total_sales=self.typeuser +int(x)
        self.save

class Content(models.Model):
    class Meta:
        abstract=True
    title=models.CharField(max_length=250,null=True,blank=True)
    title_stype=models.CharField(max_length=250,null=True,blank=True)
    show=models.BooleanField(default=True)
    active=models.BooleanField(default=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    name_styte=models.CharField(max_length=255,null=True,blank=True)
    def __str__(self) :
        return str(self.id) +" : "+ self.title

class Page(Content):
    style=models.CharField(max_length=250,null=True,blank=True)

class Menu(Content):
    class Meta:
        unique_together=['title']
        ordering=["parent","priority"]
    priority=models.IntegerField(null=True,blank=True)
    parent=models.CharField(max_length=250,null=True,blank=True)
    page=models.ForeignKey(Page,on_delete=models.SET_DEFAULT,null=True,default="")
    avatar=models.ImageField(upload_to='static/upload/Menu/%Y/%m',null=True,blank=True,default="")

class Layout_catergory(models.Model):
    style=models.CharField(max_length=250,null=False,unique=True)
    groud=models.CharField(max_length=250,null=False,blank=True)
    def __str__(self) :
        return str(self.id) +" : "+ self.style+" : "+ self.groud

class Layout(Content):
    class Meta:
        ordering=["parent","priority"]
    priority=models.IntegerField(null=True,blank=True,unique=False)
    dest=RichTextField(null=True)
    dest_style=models.CharField(max_length=250,null=True,blank=True)
    styte=models.TextField(null=True,blank=True)
    parent=models.CharField(max_length=255,null=True,blank=True,default='0')
    catergory=models.ForeignKey(Layout_catergory,on_delete=models.SET_NULL,null=True,blank=True)
    background=models.ImageField(upload_to='static/upload/background/%Y/%m',null=True,blank=True)
    interval=models.IntegerField(null=True,blank=True,unique=False,default=5000)

class Layout_img(Content):
    layout=models.ForeignKey(Layout,on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to='static/upload/Layout_img/%Y/%m')
    dest=RichTextField(null=True)
    priority=models.IntegerField(null=True,blank=True,unique=False)
    dest_style=models.CharField(max_length=250,null=True,blank=True)
    style=models.CharField(max_length=250,null=True,blank=True)

class Page_layout(models.Model):
    page=models.ForeignKey(Page,on_delete=models.SET_NULL,null=True,blank=False)
    layout=models.ForeignKey(Layout,on_delete=models.CASCADE,null=False,blank=False)
    def __str__(self) :
        return str(self.id) +" : "+ self.page.title+" : "+ self.layout.title

class Item(Content):
    avatar=models.ImageField(upload_to='static/upload/product/%Y/%m',null=False,blank=False)
    created_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    price=models.FloatField(max_length=255,null=False,blank=False)
    price_promotion=models.FloatField(max_length=255,null=False,blank=False,default=price)
    number=models.CharField(max_length=50,null=False,blank=False,default=0)
    dest=RichTextField(null=True)
    dest_style=models.CharField(max_length=250,null=True,blank=True)
    supplier=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    stastus=models.CharField(max_length=250,choices=Status_item,null=True,blank=True)

class Items_seller(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE,null=False,blank=False)
    title_i_s_stype=models.CharField(max_length=250,null=True,blank=True)
    seller=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    seller_stype=models.CharField(max_length=250,null=True,blank=True)
    stastus=models.CharField(max_length=250,choices=Status_item,null=True,blank=True)
    sale_time=models.DateTimeField(null=True,blank=True)
    number=models.IntegerField(null=False,blank=False,default=0)
    price_sell=models.FloatField(max_length=50,null=False,blank=False,default=0)
    def __str__(self) :
        return str(self.id) +" : "+ self.item.title+" : "+ self.number+" : "+ self.stastus

class Item_layout(models.Model):
    items_seller=models.ForeignKey(Items_seller,on_delete=models.SET_NULL,null=True,blank=True)
    layout=models.ForeignKey(Layout,on_delete=models.CASCADE,null=False,blank=False)
    def __str__(self) :
        return str(self.id) +" : "+ self.items_seller+" : "+ self.layout
    
class Catergory(Content):
    parent=models.CharField(max_length=250,null=True,blank=True,default='0')
    avatar=models.ImageField(upload_to='static/upload/Catergory/%Y/%m',null=True,blank=True)

class Tag_catergory(models.Model):
    item=models.ForeignKey(Item,on_delete=models.SET_NULL,null=True,blank=False)
    catergory=models.ForeignKey(Catergory,on_delete=models.CASCADE,null=False,blank=False)
    def __str__(self) :
        return str(self.id) +" : "+ self.item+" : "+ self.catergory

class Invoice(models.Model):
    verifier=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=False)
    created_time=models.DateTimeField(auto_now_add=True)
    approval_date=models.DateTimeField(auto_now=True)
    cause=models.CharField(max_length=255,null=True,blank=True)
    status_now=models.CharField(choices=Status_choise,max_length=50,null=False,blank=False,default='create')
    buyer=models.ForeignKey(Buyer,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.id)+" : "+self.status_now 
    def update_buyer(selt,u):
        selt.buyer=u
        selt.save
    def update_verifier(selt,u):
        selt.verifier=u
        selt.save
    def update_cause(selt,s):
        selt.cause=s
        selt.save
    def update_status_now(selt,status):
        selt.status_now=status
        selt.save
    def creat_Invoice_item(self,_item,_number,_price):
        ii=Invoice_item()
        ii.invoice=self
        ii.item=_item
        ii.number=_number
        ii.total_price=_price
        ii.save

class Invoice_history(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=False)
    datetime=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=Status_choise,max_length=50,null=False,blank=False,default='create')
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self) -> str:
        return str(self.id) +" ,invoice: "+str(self.invoice.id)+" : "+str(self.datetime)+" : "+self.status
    
class Invoice_item(models.Model):
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE,null=False,blank=False)
    item=models.ForeignKey(Items_seller,on_delete=models.DO_NOTHING,null=False,blank=False)
    number=models.FloatField(max_length=20,null=False,blank=False)
    total_price=models.FloatField(max_length=200,null=False,blank=False)

    def __str__(self) -> str:
        return str(self.id)+" : "+self.invoice+" : "+self.item.title 

class Group_join(models.Model):
    name=models.CharField(max_length=200,blank=False,null=False)
    dest=models.CharField(max_length=200,blank=True,null=True)
    def __str__(self) -> str:
        return str(self.id)+" : "+self.name

class Chat(models.Model):
    user=models.ForeignKey(User,models.CASCADE,null=False,blank=False)
    dest=models.CharField(max_length=250,blank=True,null=True)
    groups=models.ForeignKey(Group_join,models.CASCADE,null=False,blank=False)
    time=models.DateTimeField(auto_now_add=True)
    stastus=models.CharField(choices=Status_chat,max_length=50,null=False,blank=False,default='create')

    def __str__(self) -> str:
        return str(self.id)+" : "+self.user.get_full_name()+" : "+str(self.groups) +" : "+ str(self.time) +" : "+ self.stastus

class Group_user_join(models.Model):
    user=models.ForeignKey(User,models.CASCADE,null=False,blank=False)
    group_join=models.ForeignKey(Group_join,models.CASCADE,null=False,blank=False)
    type_group=models.IntegerField(blank=True,null=False,default=0)
    last_chat=models.ForeignKey(Chat,models.SET_NULL,null=True,blank=True)
    def __str__(self) -> str:
        return str(self.id)+" : "+self.user.get_full_name()+" : "+str(self.group_join)


class HistoryView(models.Model):
    item=models.ForeignKey(Items_seller,on_delete=models.CASCADE,null=False,blank=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    view_time=models.DateTimeField(auto_now_add=True,null=True)

class HistoryMutation(models.Model):
    action_time=models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(
        User,
        models.SET_NULL,
        verbose_name=_("user"),
        null=True,blank=True
    )
    content_type = models.ForeignKey(
        ContentType,
        models.SET_NULL,
        verbose_name=_("content type"),
        blank=True,
        null=True,
    )
    object_id = models.TextField(_("object id"), blank=True, null=True)
    object_repr = models.CharField(_("object repr"), max_length=200)
    action_flag = models.PositiveSmallIntegerField(
        _("action flag"), choices=ACTION_FLAG_CHOICES
    )
    change_message = models.TextField(_("change message"), blank=True)

    objects = LogEntryManager()
    def __repr__(self):
        return str(self.action_time)

    def __str__(self):
        if self.is_addition():
            return gettext("Added “%(object)s”.") % {"object": self.object_repr}
        elif self.is_change():
            return gettext("Changed “%(object)s” — %(changes)s") % {
                "object": self.object_repr,
                "changes": self.get_change_message(),
            }
        elif self.is_deletion():
            return gettext("Deleted “%(object)s.”") % {"object": self.object_repr}

        return gettext("LogEntry Object")

    def is_addition(self):
        return self.action_flag == ADDITION

    def is_change(self):
        return self.action_flag == CHANGE

    def is_deletion(self):
        return self.action_flag == DELETION

    def get_change_message(self):
        """
        If self.change_message is a JSON structure, interpret it as a change
        string, properly translated.
        """
        if self.change_message and self.change_message[0] == "[":
            try:
                change_message = json.loads(self.change_message)
            except json.JSONDecodeError:
                return self.change_message
            messages = []
            for sub_message in change_message:
                if "added" in sub_message:
                    if sub_message["added"]:
                        sub_message["added"]["name"] = gettext(
                            sub_message["added"]["name"]
                        )
                        messages.append(
                            gettext("Added {name} “{object}”.").format(
                                **sub_message["added"]
                            )
                        )
                    else:
                        messages.append(gettext("Added."))

                elif "changed" in sub_message:
                    sub_message["changed"]["fields"] = get_text_list(
                        [
                            gettext(field_name)
                            for field_name in sub_message["changed"]["fields"]
                        ],
                        gettext("and"),
                    )
                    if "name" in sub_message["changed"]:
                        sub_message["changed"]["name"] = gettext(
                            sub_message["changed"]["name"]
                        )
                        messages.append(
                            gettext("Changed {fields} for {name} “{object}”.").format(
                                **sub_message["changed"]
                            )
                        )
                    else:
                        messages.append(
                            gettext("Changed {fields}.").format(
                                **sub_message["changed"]
                            )
                        )

                elif "deleted" in sub_message:
                    sub_message["deleted"]["name"] = gettext(
                        sub_message["deleted"]["name"]
                    )
                    messages.append(
                        gettext("Deleted {name} “{object}”.").format(
                            **sub_message["deleted"]
                        )
                    )

            change_message = " ".join(msg[0].upper() + msg[1:] for msg in messages)
            return change_message or gettext("No fields changed.")
        else:
            return self.change_message