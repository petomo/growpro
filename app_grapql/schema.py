from graphql_auth.bases import Output,MutationMixin,DynamicArgsMixin,graphene
from graphql_relay import from_global_id
from graphene_django import DjangoObjectType,filter
from app_grapql.models import *

#Types
class UserType(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node, )

class PanerType(DjangoObjectType):
    class Meta:
        model = Paner
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class SellerType(DjangoObjectType):
    class Meta:
        model = Seller
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class BuyerType(DjangoObjectType):
    class Meta:
        model = Buyer
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class SupplierType(DjangoObjectType):
    class Meta:
        model = Supplier
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class PageType(DjangoObjectType):
    class Meta:
        model = Page
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class MenuType(DjangoObjectType):
    class Meta:
        model = Menu
        fields='__all__'
        filter_fields=("id", "title", "show", "active", "name", "page", "parent", "priority")
        interfaces = (graphene.relay.Node, )

class Layout_catergoryType(DjangoObjectType):
    class Meta:
        model = Layout_catergory
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class LayoutType(DjangoObjectType):
    class Meta:
        model = Layout
        fields='__all__'
        filter_fields=("id", "title", "show", "active", "name", "parent", "priority","catergory")
        interfaces = (graphene.relay.Node, )

class Layout_imgType(DjangoObjectType):
    class Meta:
        model = Layout_img
        fields='__all__'
        filter_fields=("id", "title", "show", "active", "name")
        interfaces = (graphene.relay.Node, )

class Page_layoutType(DjangoObjectType):
    class Meta:
        model = Page_layout
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class ItemType(DjangoObjectType):
    class Meta:
        model = Item
        fields='__all__'
        filter_fields=("id", "title", "show", "active", "name","supplier","stastus","price")
        interfaces = (graphene.relay.Node, )

class Items_sellerType(DjangoObjectType):
    class Meta:
        model = Items_seller
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class Item_layoutType(DjangoObjectType):
    class Meta:
        model = Item_layout
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class CatergoryType(DjangoObjectType):
    class Meta:
        model = Catergory
        fields='__all__'
        filter_fields=("id", "title", "show", "active", "name", "parent")
        interfaces = (graphene.relay.Node, )

class Tag_catergoryType(DjangoObjectType):
    class Meta:
        model = Tag_catergory
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class InvoiceType(DjangoObjectType):
    class Meta:
        model = Invoice
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class InvoiceInfoType(DjangoObjectType):
    class Meta:
        model = InvoiceInfo
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class Invoice_historyType(DjangoObjectType):
    class Meta:
        model = Invoice_history
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class Invoice_itemType(DjangoObjectType):
    class Meta:
        model = Invoice_item
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class Group_joinType(DjangoObjectType):
    class Meta:
        model = Group_join
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class Group_user_joinType(DjangoObjectType):
    class Meta:
        model = Group_user_join
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class ChatType(DjangoObjectType):
    class Meta:
        model = Chat
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class HistoryMutationType(DjangoObjectType):
    class Meta:
        model = HistoryMutation
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

class HistoryUploadfileType(DjangoObjectType):
    class Meta:
        model=HistoryFileUp
        fields='__all__'
        filter_fields=("title","user","size","typefile","id")
        interfaces = (graphene.relay.Node, )

class LikeItemSellerType(DjangoObjectType):
    class Meta:
        model = LikeItems_seller
        fields='__all__'
        filter_fields='__all__'
        interfaces = (graphene.relay.Node, )

#action
#user
class ChangeFirtNameAction(Output):
    """
    Change user FirtName without login.

    It needs a token to authenticate.
    """
    class Arguments:
        firtName=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        if user.is_authenticated:
            user.first_name=kwargs.get("firtName")
            user.save()
            return cls(success=True,errors=None)
        return cls(success=False,errors=[{"message":"User does not exist"}])

class ChangeLastNameAction(Output):
    """
    Change user LastName without login.

    It needs a token to authenticate.
    """
    class Arguments:
        lastName=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        if user.is_authenticated:
            user.last_name=kwargs.get("lastName")
            user.save()
            return cls(success=True,errors=None)
        return cls(success=False,errors=[{"message":"User does not exist"}])

class ChangeAddressAction(Output):
    """
    Change user Address without login.

    It needs a token to authenticate.
    """
    class Arguments:
        address=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        if user.is_authenticated:
            user.address=kwargs.get("address")
            user.save()
            return cls(success=True,errors=None)
        return cls(success=False,errors=[{"message":"User does not exist"}])

class ChangePhoneAction(Output):
    """
    Change user Phone without login.
    
    It needs a token to authenticate.
    """
    class Arguments:
        phone=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        if user.is_authenticated:
            user.phone=kwargs.get("phone")
            user.save()
            return cls(success=True,errors=None)
        return cls(success=False,errors=[{"message":"User does not exist"}])
#chat
class CreatRomAction(Output):
    """
    Create Rom without login.

    It needs a token to authenticate.
    """
    rom=graphene.Field(Group_joinType)
    class Arguments:
        member=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        cls.success=False
        cls.errors=[{"message":"User does not exist"}]
        cls.rom=None
        if user.is_authenticated:
            member_name=kwargs.get("member")
            member=User.objects.get(username=member_name)
            if member:
                rom_dest='&'+user.username+'&'+member_name
                rom,_=Group_join.objects.get_or_create(name__contains=rom_dest)
                if _:
                    rom.dest=rom_dest
                    rom.save()
                cls.success=True
                cls.errors=None
                cls.rom=rom             
                return cls
            cls.errors=[{"message":"Member does not exist"}]
        return  cls

class JoinRomAction(Output):
    """
    Join Rom without login.

    It needs a token to authenticate.
    """
    rom=graphene.Field(Group_joinType)
    class Arguments:
        member=graphene.String(required=True)
            
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        cls.success=False
        cls.errors=[{"message":"User does not exist"}]
        if user.is_authenticated:
            romId=kwargs.get("rom")
            _, model_id = from_global_id(romId)
            rom=Group_join.objects.get(id__contains=model_id)
            if rom:
                g=Group_user_join.objects.create(user=user,group_join=rom)
                g.save()
                rom.updateName(str('&'+user.username))
                cls.success=True
                cls.errors=None
                cls.rom=rom               
                return cls
            cls.errors=[{"message":"Rom does not exist"}]
            return cls
        return cls

class ChatRomAction(Output):
    """
    Send a chat to Rom without login.

    It needs a token to authenticate.
    """
    chat=graphene.Field(ChatType)
    class Arguments:
        dest=graphene.String(required=True)
        rom=graphene.String(required=True)
            
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        cls.success=False
        cls.errors=[{"message":"User does not exist"}]
        cls.chat=None
        if user.is_authenticated:
            romId=kwargs.get("rom")
            dest=kwargs.get("dest")
            _, model_id = from_global_id(romId)
            rom=Group_join.objects.get(id=model_id)
            if rom:
                chat=Chat.objects.create(user=user,dest=dest,groups=rom,stastus=6)
                chat.save
                g=Group_user_join.objects.filter(user=user,group_join=rom)
                g.last_chat=chat            
                cls.success=True
                cls.errors=None
                cls.chat=chat
                return cls
            cls.errors=[{"message":"Rom does not exist"}]
            return cls  
        return cls
#cart
class get_or_create_CartAction(Output):
    """
    Get invoice with invoice status = created.

    If the invoice does not exist, the system will create a new invoice.

    It needs a token to authenticate.
    """
    invoice=graphene.Field(InvoiceType)
            
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        cls.errors=[{"message":"User does not exist"}]
        cls.success=False
        cls.invoice=None
        if user.is_authenticated:
            _invoice,_=Invoice.objects.get_or_create(buyer=user,status_now=1)            
            if _invoice:
                _invoice.save()               
                cls.success=True
                cls.errors=None
                cls.invoice=_invoice
                return cls
            cls.errors=[{"message":"Invoice don't create"}]
            return cls 
        return cls

class add_item_CartAction(Output):
    
    """
    add invoice item with invoice `status = created`.

    `item:itemID` , `price: current price`

    It needs a token to authenticate.
    """
    invoice=graphene.Field(InvoiceType)

    class Arguments:
        item=graphene.String(required=True)
        number=graphene.String(required=True)
        price=graphene.String(required=True)   
    
    @classmethod   
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        cls.errors=[{"message":"User does not exist"}]
        cls.success=False
        _number=float(kwargs.get("number")) 
        _item=kwargs.get("item")
        _price=float(kwargs.get("price"))
        print('_number',_number)
        print('_item',_item)
        print('_price',_price)
        if user.is_authenticated:
            _buyer,_=Buyer.objects.get_or_create(user=user)
            invoice,_=Invoice.objects.get_or_create(buyer=_buyer,status_now=1)
            if _:
                invoice.verifier=user
            if invoice:
                invoice.save()
                if _item:
                    _, model_item_id = from_global_id(_item)
                    item=Items_seller.objects.get(id=model_item_id)
                    print(item)
                if item and _number and _price:
                    _iv,_=Invoice_item.objects.get_or_create(item=item,invoice=invoice)
                    if _:
                        _iv.number=0
                    _iv.price=_price
                    _iv.number+=_number
                    if _iv.number>item.number:
                        cls.success=False
                        cls.errors=[{"message":"The quantity of products ordered exceeds the quantity sold"}]
                        cls.invoice=invoice
                        return cls
                    _iv.save()
                    cls.success=True
                    cls.errors=None
                    cls.invoice=invoice
                    return cls
                cls.errors=[{"message":"arguments does not exist"}]
                return cls
            cls.errors=[{"message":"invoice does not exist"}]
            return cls   
        return cls

class remove_item_cartAction(Output):
    
    """
    remove invoice item with invoice `status = created`.

    `item:itemID`

    It needs a token to authenticate.
    """
    invoice=graphene.Field(InvoiceType)

    class Arguments:
        item=graphene.String(required=True) 
    
    @classmethod   
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        cls.errors=[{"message":"User does not exist"}]
        cls.success=False
        _item=kwargs.get("item")

        if user.is_authenticated:
            _, model_item_id = from_global_id(_item)
            it=Invoice_item.objects.get(id=model_item_id)
            _invoice=it.invoice
            if it:
                it.delete()
                cls.invoice=_invoice
                cls.success=True
                cls.errors=None
                return cls 
            else:
                cls.invoice=None
                cls.success=True
                cls.errors=[{"message":"Invoice_item does not exist"}]
                return cls 
        cls.invoice=None
        return cls

class order_cartAction(Output):
    
    """
    order invoice with invoice `status = created`.

    It needs a token to authenticate.
    """
    invoice=graphene.Field(InvoiceType)

    class Arguments:
        fullname=graphene.String(required=True)
        address=graphene.String(required=True)
        phone=graphene.String(required=True)
        email=graphene.String(required=True)
        cause=graphene.String()
    
    @classmethod   
    def resolve_mutation(cls, root, info, **kwargs):
        fullname=kwargs.get("fullname")
        address =kwargs.get("address")
        phone   =kwargs.get("phone")
        email   =kwargs.get("email")
        try: cause=kwargs.get("cause")
        except:cause=""

        user=info.context.user
        cls.errors=[{"message":"User does not exist"}]
        cls.success=False
        cls.invoice=None
        if user.is_authenticated:
            _buyer=Buyer.objects.get(user=user)
            if _buyer:
                _iv=Invoice.objects.get(buyer=_buyer,status_now=1)
                if _iv:
                    _ivi=Invoice_item.objects.filter(invoice=_iv)
                    nb_item=0
                    if _ivi:
                        er=0
                        for i in _ivi:
                            its= i.item
                            if its.number<i.number:
                                er+=1
                                i.number=its.number
                                i.save()
                            nb_item+=i.number
                        if er>0:
                            cls.errors=[{"message":"Order quantity exceeds sale quantity"}]
                            return cls
                        if nb_item>0:
                            _info,_=InvoiceInfo.objects.get_or_create(invoice=_iv)
                            _info.fullname=fullname
                            _info.address=address
                            _info.phone=phone
                            _info.email=email
                            _info.cause=cause
                            _info.save()
                            cls.errors=None
                            cls.success=True
                            cls.invoice=_iv
                            _iv.status_now=8
                            _iv.save()
                            for i in _ivi:
                                its= i.item
                                its.number-=i.number
                                its.save()
                            return cls
                    cls.errors=[{"message":"Cart has no products"}]
                    return cls
                cls.errors=[{"message":"Invoice does not exist"}]
                return cls
            cls.errors=[{"message":"Buyer does not exist"}]
            return cls
        return cls

class cancel_cartAction(Output):
    
    """
    cancel invoice with invoice `status = ORDER/APPROVE`.

    It needs a token to authenticate.
    """

    class Arguments:
        invoice=graphene.String(required=True)
        cause=graphene.String(required=True)
            
    @classmethod   
    def resolve_mutation(cls, root, info, **kwargs):
        _invoiceID=kwargs.get("invoice")
        try:_cause=kwargs.get("cause")
        except:_cause=""

        user=info.context.user
        cls.errors=[{"message":"User does not exist"}]
        cls.success=False
        cls.invoice=None
        if user.is_authenticated:
            _buyer=Buyer.objects.get(user=user)
            if _buyer:
                _, model_item_id = from_global_id(_invoiceID)
                _iv=Invoice.objects.get(buyer=_buyer,id=model_item_id)
                if _iv:
                    _iv.status_now=4
                    _iv.verifier=user
                    _iv.cause=_cause
                    _iv.save()
                    cls.success=True
                    cls.errors=None
                    return cls
                cls.errors=[{"message":"Invoice does not exist"}]
                return cls
            cls.errors=[{"message":"Buyer does not exist"}]
            return cls
        return cls

class add_item_LikeAction(Output):
    
    """
    Add `Like` item with itemID

    It needs a `token` to authenticate.
    """
    likeItems_seller=graphene.Field(LikeItemSellerType)

    class Arguments:
        item=graphene.String(required=True)
    
    @classmethod   
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        cls.errors=[{"message":"User does not exist"}]
        cls.success=False
        cls.likeItems_seller=None
        _item=kwargs.get("item")

        if user.is_authenticated:
            _buyer,_=Buyer.objects.get_or_create(user=user)
            if _buyer:
                _buyer.save()
                if _item:
                    _, model_item_id = from_global_id(_item)
                    item=Items_seller.objects.get(id=model_item_id)
                if item :
                    _i,_=LikeItems_seller.objects.get_or_create(item=item,user=user)
                    if _i:
                        _i.like()
                        _i.save()
                        cls.success=True
                        cls.errors=None
                        cls.likeItems_seller=_i
                        return cls
                    cls.errors=[{"message":"like_item does not exist"}]
                    return cls
                cls.errors=[{"message":"item does not exist"}]
                return cls
            cls.errors=[{"message":"buyer does not exist"}]
            return cls   
        return cls

class add_item_disLikeAction(Output):
    
    """
    Add `DistLike` item with itemID

    It needs a `token` to authenticate.
    """
    likeItems_seller=graphene.Field(LikeItemSellerType)

    class Arguments:
        item=graphene.String(required=True)
    
    @classmethod   
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        cls.errors=[{"message":"User does not exist"}]
        cls.success=False
        cls.likeItems_seller=None
        _item=kwargs.get("item")

        if user.is_authenticated:
            _buyer,_=Buyer.objects.get_or_create(user=user)
            if _buyer:
                _buyer.save()
                if _item:
                    _, model_item_id = from_global_id(_item)
                    item=Items_seller.objects.get(id=model_item_id)
                if item :
                    _i,_=LikeItems_seller.objects.get_or_create(item=item,user=user)
                    if _i:
                        _i.dislike()
                        _i.save()
                        cls.success=True
                        cls.errors=None
                        cls.likeItems_seller=_i
                        return cls
                    cls.errors=[{"message":"like_item does not exist"}]
                    return cls
                cls.errors=[{"message":"item does not exist"}]
                return cls
            cls.errors=[{"message":"buyer does not exist"}]
            return cls   
        return cls
#changeLayout
class ChangeLayoutShowAction(Output):
    """
    
    """
    class Arguments:
        layout=graphene.String(required=True)
        show=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            show=kwargs.get("show")
            layout=kwargs.get("layout")
            if show and layout:
                _, model_item_id = from_global_id(layout)
                _layout=Layout.objects.get(id=model_item_id)
                if _layout:
                    if show=='True':
                        _layout.show=True
                    else:
                        _layout.show=False
                    _layout.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])

class ChangeLayoutActiveAction(Output):
    """
    
    """
    class Arguments:
        layout=graphene.String(required=True)
        active=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            active=kwargs.get("active")
            layout=kwargs.get("layout")
            if active and layout:
                _, model_item_id = from_global_id(layout)
                _layout=Layout.objects.get(id=model_item_id)
                if _layout:
                    if active=='True':
                        _layout.active=True
                    else:    
                        _layout.active=False
                    _layout.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])

class ChangeLayoutCatergoryAction(Output):
    """
    
    """
    class Arguments:
        layout=graphene.String(required=True)
        catergory=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            catergory=kwargs.get("catergory")
            layout=kwargs.get("layout")
            if catergory and layout:
                _, model_lid = from_global_id(layout)
                _, model_cid = from_global_id(catergory)
                _l=Layout.objects.get(id=model_lid)
                _c=Layout_catergory.objects.get(id=model_cid)
                if _l and _c:
                    _l.catergory=_c
                    _l.save()
                    _lcs=Layout.objects.filter(parent=_l.name)
                    if _lcs:
                        for _lc in _lcs:
                            _lc.catergory=_c
                            _lc.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])

class ChangeLayoutNameAction(Output):
    """
    
    """
    class Arguments:
        layout  =graphene.String(required=True)
        name    =graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            name=kwargs.get("name")
            layout=kwargs.get("layout")
            if name and layout:
                _, model_lid = from_global_id(layout)
                _l=Layout.objects.get(id=model_lid)
                if _l:
                    _lcs=Layout.objects.filter(parent=_l.name)
                    _l.name=name
                    _l.save()
                    if _lcs:
                        for _lc in _lcs:
                            _lc.parent=name
                            _lc.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
    
class ChangeLayoutTitleAction(Output):
    """
    
    """
    class Arguments:
        layout  =graphene.String(required=True)
        title    =graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            title=kwargs.get("title")
            layout=kwargs.get("layout")
            if title and layout:
                _, model_lid = from_global_id(layout)
                _l=Layout.objects.get(id=model_lid)
                if _l:
                    _l.title=title
                    _l.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
    
class ChangeLayoutTitleStypeAction(Output):
    """
    
    """
    class Arguments:
        layout  =graphene.String(required=True)
        titlestype    =graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            titlestype=kwargs.get("titlestype")
            layout=kwargs.get("layout")
            if titlestype and layout:
                _, model_lid = from_global_id(layout)
                _l=Layout.objects.get(id=model_lid)
                if _l:
                    _l.title_stype=titlestype
                    _l.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
    
class ChangeLayoutPageAction(Output):
    """
    
    """
    class Arguments:
        layout  =graphene.String(required=True)
        page    =graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            page=kwargs.get("page")
            layout=kwargs.get("layout")
            if page and layout:
                _, model_lid = from_global_id(layout)
                _layout=Layout.objects.get(id=model_lid)
                if _layout:
                    _l,_=Page_layout.objects.get_or_create(layout=_layout)
                    _p=None
                    if page!="Nan":
                        _, model_pid = from_global_id(page)
                        _p=Page.objects.get(id=model_pid)
                    _l.page=_p
                    _l.save()
                    _lcs=Layout.objects.filter(parent=_l.layout.name)
                    if _lcs:
                        for _lc in _lcs:
                            _lp,_=Page_layout.objects.get_or_create(layout=_lc)
                            _lp.page=_p
                            _lp.save()
                    return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
    
class ChangeLayoutItemAction(Output):
    """
    
    """
    class Arguments:
        layout  =graphene.String(required=True)
        item    =graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            item=kwargs.get("item")
            layout=kwargs.get("layout")
            if item and layout:
                _, model_lid = from_global_id(layout)
                _layout=Layout.objects.get(id=model_lid)
                if _layout:
                    _l,_=Item_layout.objects.get_or_create(layout=_layout)
                    _i=None
                    if item!="Nan":
                        _, model_pid = from_global_id(item)
                        _i=Items_seller.objects.get(id=model_pid)
                    _l.items_seller=_i
                    _l.save()
                    _lcs=Layout.objects.filter(parent=_l.layout.name)
                    if _lcs:
                        for _lc in _lcs:
                            _lp,_=Item_layout.objects.get_or_create(layout=_lc)
                            _lp.items_seller=_i
                            _lp.save()
                    return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
    
class ChangeLayoutPriorityAction(Output):
    """
    
    """
    class Arguments:
        layout  =graphene.String(required=True)
        priority=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            priority=kwargs.get("priority")
            layout=kwargs.get("layout")
            if priority and layout:
                _, model_lid = from_global_id(layout)
                _l=Layout.objects.get(id=model_lid)
                if _l:
                    _l.priority=priority
                    _l.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
    
class ChangeLayoutIntervalAction(Output):
    """
    
    """
    class Arguments:
        layout  =graphene.String(required=True)
        interval=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            interval=kwargs.get("interval")
            layout=kwargs.get("layout")
            if interval and layout:
                _, model_lid = from_global_id(layout)
                _l=Layout.objects.get(id=model_lid)
                if _l:
                    _l.interval=interval
                    _l.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
    
class ChangeLayoutStyteAction(Output):
    """
    
    """
    class Arguments:
        layout  =graphene.String(required=True)
        styte=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            styte=kwargs.get("styte")
            layout=kwargs.get("layout")
            if styte and layout:
                _, model_lid = from_global_id(layout)
                _l=Layout.objects.get(id=model_lid)
                if _l:
                    _l.styte=styte
                    _l.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
    
class ChangeLayoutDestAction(Output):
    """
    
    """
    class Arguments:
        layout  =graphene.String(required=True)
        dest=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            dest=kwargs.get("dest")
            layout=kwargs.get("layout")
            if dest and layout:
                _, model_lid = from_global_id(layout)
                _l=Layout.objects.get(id=model_lid)
                if _l:
                    _l.dest=dest
                    _l.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
    
class ChangeLayoutDestStyleAction(Output):
    """
    
    """
    class Arguments:
        layout  =graphene.String(required=True)
        deststyle=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            deststyle=kwargs.get("deststyle")
            layout=kwargs.get("layout")
            if deststyle and layout:
                _, model_lid = from_global_id(layout)
                _l=Layout.objects.get(id=model_lid)
                if _l:
                    _l.dest_style=deststyle
                    _l.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])

class ChangeLayoutImgAction(Output):
    """
    
    """
    class Arguments:
        layout  =graphene.String(required=True)
        img     =graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            img=kwargs.get("img")
            layout=kwargs.get("layout")
            if layout:
                _, model_lid = from_global_id(layout)
                _l=Layout.objects.get(id=model_lid)
                if _l:
                    if img=="Nan":_l.background=None
                    else:_l.background=img
                    _l.save()
                    return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
    
class LayoutDeleteAction(Output):
    """
    
    """
    class Arguments:
        layout  =graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            layout=kwargs.get("layout")
            if layout:
                _, model_lid = from_global_id(layout)
                _l=Layout.objects.get(id=model_lid)
                if _l:
                    _l.delete()
                    return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])

class AddLayoutAction(Output):
    """
    
    """
    class Arguments:
        title       =graphene.String(required=True)
        title_stype =graphene.String(required=True)
        show        =graphene.String(required=True)
        active      =graphene.String(required=True)
        name        =graphene.String(required=True)
        name_styte  =graphene.String(required=True)
        priority    =graphene.String(required=True)
        dest        =graphene.String(required=True)
        dest_style  =graphene.String(required=True)
        styte       =graphene.String(required=True)
        parent      =graphene.String(required=True)
        catergory   =graphene.String(required=True)
        background  =graphene.String(required=True)
        interval    =graphene.String(required=True)
        page        =graphene.String(required=True)
        itemseller  =graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            _show       =False
            _active     =False
            _background =None
            _page       =None
            _itsl       =None
            lp          =None
            title       =kwargs.get("title")
            title_stype =kwargs.get("title_stype")
            show        =kwargs.get("show")
            active      =kwargs.get("active")
            name        =kwargs.get("name")
            name_styte  =kwargs.get("name_styte")
            priority    =kwargs.get("priority")
            dest        =kwargs.get("dest")
            dest_style  =kwargs.get("dest_style")
            styte       =kwargs.get("styte")
            parent      =kwargs.get("parent")
            catergory   =kwargs.get("catergory")
            background  =kwargs.get("background")
            interval    =kwargs.get("interval")
            page        =kwargs.get("page")
            itemseller  =kwargs.get("itemseller")
            if not title        :return cls(success=False,errors=[{"message":"attribute title do not exist"}])
            if not title_stype  :return cls(success=False,errors=[{"message":"attribute title_stype do not exist"}]) 
            if not show         :return cls(success=False,errors=[{"message":"attribute show do not exist"}]) 
            else: 
                if show=="True":_show=True 
            if not active       :return cls(success=False,errors=[{"message":"attribute active do not exist"}]) 
            else:
                if active=="True":_active=True
            if not name         :return cls(success=False,errors=[{"message":"attribute name do not exist"}])
            if not name_styte   :return cls(success=False,errors=[{"message":"attribute name_styte do not exist"}])
            if not priority     :return cls(success=False,errors=[{"message":"attribute priority do not exist"}])
            if not dest         :return cls(success=False,errors=[{"message":"attribute dest do not exist"}])    
            if not dest_style   :return cls(success=False,errors=[{"message":"attribute dest_style do not exist"}])
            if not styte        :return cls(success=False,errors=[{"message":"attribute styte do not exist"}])
            if not parent       :return cls(success=False,errors=[{"message":"attribute parent do not exist"}])
            else:
                if parent=="0" or parent=="Nan":
                    parent="0"
                    if not page :return cls(success=False,errors=[{"message":"attribute page do not exist"}])
                    else:
                        if page=="Nan":
                            _page=None
                            if not itemseller:return cls(success=False,errors=[{"message":"attribute itemseller do not exist"}])
                            else:
                                if itemseller=="Nan":_itemseller=None
                                else:
                                    _, model_itslid = from_global_id(itemseller)
                                    _itsl=Items_seller.objects.get(id=model_itslid)
                                    if not _itsl:return cls(success=False,errors=[{"message":"Items_seller do not exist"}])
                        else:
                            _, model_pid = from_global_id(page)
                            _page=Page.objects.get(id=model_pid)
                            if not _page:return cls(success=False,errors=[{"message":"page do not exist"}])
                else:
                    loc=Layout.objects.get(name=parent)
                    if loc:
                        _lopc=Page_layout.objects.get(layout=loc)
                        if _lopc:
                            _page=_lopc.page
                        else:
                            _loic=Item_layout.objects.get(layout=loc)
                            if _loic:
                                _itsl=_loic.items_seller
                    else:       return cls(success=False,errors=[{"message":"Layout parent do not exist"}])   

            if not catergory    :return cls(success=False,errors=[{"message":"attribute catergory do not exist"}])
            else:
                _, model_lcid   = from_global_id(catergory)
                _lc             =Layout_catergory.objects.get(id=model_lcid)
                if not _lc:     return cls(success=False,errors=[{"message":"Layout_catergory do not exist"}]) 
            if not background   :return cls(success=False,errors=[{"message":"attribute background do not exist"}])
            else:
                if background=="Nan":_background=None
                else:_background=background
            if not interval     :return cls(success=False,errors=[{"message":"attribute interval do not exist"}])    
                       
            l=Layout.objects.create(
                title=title,
                title_stype=title_stype,
                show=_show,
                active=_active,
                name=name,
                name_styte=name_styte,
                priority=priority,
                dest=dest,
                dest_style=dest_style,
                styte=styte,
                parent=parent,
                catergory=_lc,
                background=_background,
                interval=interval,
                user=user
                )
            if l:  
                if _page:
                    lp=Page_layout.objects.create(page=_page,layout=l)
                if lp:
                    return cls(success=True,errors=None)
                else:
                    if _itsl:
                        Item_layout.objects.create(items_seller=_itsl,layout=l)
                return cls(success=True,errors=None)
            else:return cls(success=False,errors=[{"message":"Layout do not create"}])
        return cls(success=False,errors=[{"message":"User does not exist"}]) 
#changeLayoutItem
class ChangeLayoutItemShowAction(Output):
    """
    
    """
    class Arguments:
        layoutItem=graphene.String(required=True)
        show=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            show=kwargs.get("show")
            layoutItem=kwargs.get("layoutItem")
            if show and layoutItem:
                _, model_item_id = from_global_id(layoutItem)
                _layout=Layout_img.objects.get(id=model_item_id)
                if _layout:
                    if show=='True':
                        _layout.show=True
                    else:
                        _layout.show=False
                    _layout.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])

class ChangeLayoutItemActiveAction(Output):
    """
    
    """
    class Arguments:
        layoutItem=graphene.String(required=True)
        active=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            active=kwargs.get("active")
            layoutItem=kwargs.get("layoutItem")
            if active and layoutItem:
                _, model_item_id = from_global_id(layoutItem)
                _layout=Layout_img.objects.get(id=model_item_id)
                if _layout:
                    if active=='True':
                        _layout.active=True
                    else:    
                        _layout.active=False
                    _layout.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])

class ChangeLayoutItemNameAction(Output):
    """
    
    """
    class Arguments:
        layoutItem  =graphene.String(required=True)
        name    =graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            name=kwargs.get("name")
            layoutItem=kwargs.get("layoutItem")
            if name and layoutItem:
                _, model_lid = from_global_id(layoutItem)
                _l=Layout_img.objects.get(id=model_lid)
                if _l:
                    _lcs=Layout.objects.filter(parent=_l.name)
                    _l.name=name
                    _l.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
    
class ChangeLayoutItemTitleAction(Output):
    """
    
    """
    class Arguments:
        layoutItem  =graphene.String(required=True)
        title    =graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            title=kwargs.get("title")
            layoutItem=kwargs.get("layoutItem")
            if title and layoutItem:
                _, model_lid = from_global_id(layoutItem)
                _l=Layout_img.objects.get(id=model_lid)
                if _l:
                    _l.title=title
                    _l.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
    
class ChangeLayoutItemTitleStypeAction(Output):
    """
    
    """
    class Arguments:
        layoutItem  =graphene.String(required=True)
        titlestype    =graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            titlestype=kwargs.get("titlestype")
            layoutItem=kwargs.get("layoutItem")
            if titlestype and layoutItem:
                _, model_lid = from_global_id(layoutItem)
                _l=Layout_img.objects.get(id=model_lid)
                if _l:
                    _l.title_stype=titlestype
                    _l.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
  
class ChangeLayoutItemPriorityAction(Output):
    """
    
    """
    class Arguments:
        layoutItem  =graphene.String(required=True)
        priority=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            priority=kwargs.get("priority")
            layoutItem=kwargs.get("layoutItem")
            if priority and layoutItem:
                _, model_lid = from_global_id(layoutItem)
                _l=Layout_img.objects.get(id=model_lid)
                if _l:
                    _l.priority=priority
                    _l.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
        
class ChangeLayoutItemStyteAction(Output):
    """
    
    """
    class Arguments:
        layoutItem  =graphene.String(required=True)
        styte=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            styte=kwargs.get("styte")
            layoutItem=kwargs.get("layoutItem")
            if styte and layoutItem:
                _, model_lid = from_global_id(layoutItem)
                _l=Layout_img.objects.get(id=model_lid)
                if _l:
                    _l.styte=styte
                    _l.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
    
class ChangeLayoutItemDestAction(Output):
    """
    
    """
    class Arguments:
        layoutItem  =graphene.String(required=True)
        dest=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            dest=kwargs.get("dest")
            layoutItem=kwargs.get("layoutItem")
            if dest and layoutItem:
                _, model_lid = from_global_id(layoutItem)
                _l=Layout_img.objects.get(id=model_lid)
                if _l:
                    _l.dest=dest
                    _l.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
    
class ChangeLayoutItemDestStyleAction(Output):
    """
    
    """
    class Arguments:
        layoutItem  =graphene.String(required=True)
        deststyle=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            deststyle=kwargs.get("deststyle")
            layoutItem=kwargs.get("layoutItem")
            if deststyle and layoutItem:
                _, model_lid = from_global_id(layoutItem)
                _l=Layout_img.objects.get(id=model_lid)
                if _l:
                    _l.dest_style=deststyle
                    _l.save()
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])

class ChangeLayoutItemImgAction(Output):
    """
    
    """
    class Arguments:
        layoutItem  =graphene.String(required=True)
        img     =graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            img=kwargs.get("img")
            layoutItem=kwargs.get("layoutItem")
            if layoutItem and img:
                _, model_lid = from_global_id(layoutItem)
                _l=Layout_img.objects.get(id=model_lid)
                if _l:
                    _l.avatar=img
                    _l.save()
                    return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])
   
class LayoutItemDeleteAction(Output):
    """
    
    """
    class Arguments:
        layoutItem  =graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            layout=kwargs.get("layoutItem")
            if layout:
                _, model_lid = from_global_id(layout)
                _l=Layout_img.objects.get(id=model_lid)
                if _l:
                    _l.delete()
                    return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"attributes do not exist"}])
        return cls(success=False,errors=[{"message":"User does not exist"}])

class AddLayoutItemAction(Output):
    """
    
    """
    class Arguments:
        title       =graphene.String(required=True)
        title_stype =graphene.String(required=True)
        show        =graphene.String(required=True)
        active      =graphene.String(required=True)
        name        =graphene.String(required=True)
        name_styte  =graphene.String(required=True)
        priority    =graphene.String(required=True)
        dest        =graphene.String(required=True)
        dest_style  =graphene.String(required=True)
        styte       =graphene.String(required=True)
        layout      =graphene.String(required=True)
        avatar      =graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user    
        if user.is_authenticated:
            _show       =False
            _active     =False
            _avatar     =None
            _layout     =None
            title       =kwargs.get("title")
            title_stype =kwargs.get("title_stype")
            show        =kwargs.get("show")
            active      =kwargs.get("active")
            name        =kwargs.get("name")
            name_styte  =kwargs.get("name_styte")
            priority    =kwargs.get("priority")
            dest        =kwargs.get("dest")
            dest_style  =kwargs.get("dest_style")
            styte       =kwargs.get("styte")
            layout      =kwargs.get("layout")
            avatar      =kwargs.get("avatar")
            if not title        :return cls(success=False,errors=[{"message":"attribute title do not exist"}])
            if not title_stype  :return cls(success=False,errors=[{"message":"attribute title_stype do not exist"}]) 
            if not show         :return cls(success=False,errors=[{"message":"attribute show do not exist"}]) 
            else: 
                if show=="True":_show=True 
            if not active       :return cls(success=False,errors=[{"message":"attribute active do not exist"}]) 
            else:
                if active=="True":_active=True
            if not name         :return cls(success=False,errors=[{"message":"attribute name do not exist"}])
            if not name_styte   :return cls(success=False,errors=[{"message":"attribute name_styte do not exist"}])
            if not priority     :return cls(success=False,errors=[{"message":"attribute priority do not exist"}])
            if not dest         :return cls(success=False,errors=[{"message":"attribute dest do not exist"}])    
            if not dest_style   :return cls(success=False,errors=[{"message":"attribute dest_style do not exist"}])
            if not styte        :return cls(success=False,errors=[{"message":"attribute styte do not exist"}])
            if not layout       :return cls(success=False,errors=[{"message":"attribute layout do not exist"}])
            else:
                _, model_lid = from_global_id(layout)
                _layout=Layout.objects.get(id=model_lid)
                if not _layout:     return cls(success=False,errors=[{"message":"Layoutdo not exist"}]) 
            if not avatar   :return cls(success=False,errors=[{"message":"attribute background do not exist"}])
            else:
                if avatar=="Nan":_avatar=None
                else:_avatar=avatar
                        
            l=Layout_img.objects.create(
                title=title,
                title_stype=title_stype,
                show=_show,
                active=_active,
                name=name,
                name_styte=name_styte,
                priority=priority,
                dest=dest,
                dest_style=dest_style,
                styte=styte,
                layout=_layout,
                avatar=_avatar
                )
            if l:
                if l:
                    return cls(success=True,errors=None)
                else:
                    return cls(success=False,errors=[{"message":"Layout_img do not create"}])
            else:return cls(success=False,errors=[{"message":"Layout do not create"}])
        return cls(success=False,errors=[{"message":"User does not exist"}]) 


#MutationFunction
#user
class ChangeFirtName(MutationMixin, DynamicArgsMixin, ChangeFirtNameAction, graphene.Mutation):
    __doc__ = ChangeFirtNameAction.__doc__
    _required_args = ["firtName"]

class ChangeLastName(MutationMixin, DynamicArgsMixin, ChangeLastNameAction, graphene.Mutation):
    __doc__ = ChangeLastNameAction.__doc__
    _required_args = ["lastName"]

class ChangeAddressName(MutationMixin, DynamicArgsMixin, ChangeAddressAction, graphene.Mutation):
    __doc__ = ChangeAddressAction.__doc__
    _required_args = ["address"]

class ChangePhone(MutationMixin, DynamicArgsMixin, ChangePhoneAction, graphene.Mutation):
    __doc__ = ChangePhoneAction.__doc__
    _required_args = ["phone"]
#chat
class CreatRom(MutationMixin, DynamicArgsMixin, CreatRomAction, graphene.Mutation):
    __doc__ = CreatRomAction.__doc__
    _required_args = ["member"]

class JoinRom(MutationMixin, DynamicArgsMixin, JoinRomAction, graphene.Mutation):
    __doc__ = JoinRomAction.__doc__
    _required_args = ["rom"]

class ChatRom(MutationMixin, DynamicArgsMixin, ChatRomAction, graphene.Mutation):
    __doc__ = ChatRomAction.__doc__
    _required_args = ["rom","dest"]
#cart
class Get_or_createInvoice(MutationMixin, DynamicArgsMixin, get_or_create_CartAction, graphene.Mutation):
    __doc__ = get_or_create_CartAction.__doc__

class Add_item_cart(MutationMixin, DynamicArgsMixin, add_item_CartAction, graphene.Mutation):
    __doc__ = add_item_CartAction.__doc__
    _required_args = ["item","number","price"]

class Remove_item_cart(MutationMixin, DynamicArgsMixin, remove_item_cartAction, graphene.Mutation):
    __doc__ = remove_item_cartAction.__doc__
    _required_args = ["item"]

class Ordercart(MutationMixin, DynamicArgsMixin, order_cartAction, graphene.Mutation):
    __doc__ = order_cartAction.__doc__
    _required_args = ["fullname","address","phone","email","cause"]

class Cancelcart(MutationMixin, DynamicArgsMixin, cancel_cartAction, graphene.Mutation):
    __doc__ = cancel_cartAction.__doc__
    _required_args = ["invoice","cause"]

class Add_item_Like(MutationMixin, DynamicArgsMixin, add_item_LikeAction, graphene.Mutation):
    __doc__ = add_item_LikeAction.__doc__
    _required_args = ["item"]

class Add_item_disLike(MutationMixin, DynamicArgsMixin, add_item_disLikeAction, graphene.Mutation):
    __doc__ = add_item_disLikeAction.__doc__
    _required_args = ["item"]
#layout
class ChangeLayoutShow(MutationMixin, DynamicArgsMixin, ChangeLayoutShowAction, graphene.Mutation):
    __doc__ = ChangeLayoutShowAction.__doc__
    _required_args = ["layout","show"]

class ChangeLayoutActive(MutationMixin, DynamicArgsMixin, ChangeLayoutActiveAction, graphene.Mutation):
    __doc__ = ChangeLayoutActiveAction.__doc__
    _required_args = ["layout","active"]

class ChangeLayoutCatergory(MutationMixin, DynamicArgsMixin, ChangeLayoutCatergoryAction, graphene.Mutation):
    __doc__ = ChangeLayoutCatergoryAction.__doc__
    _required_args = ["layout","catergory"]

class ChangeLayoutName(MutationMixin, DynamicArgsMixin, ChangeLayoutNameAction, graphene.Mutation):
    __doc__ = ChangeLayoutCatergoryAction.__doc__
    _required_args = ["layout","name"]

class ChangeLayoutTitle(MutationMixin, DynamicArgsMixin, ChangeLayoutTitleAction, graphene.Mutation):
    __doc__ = ChangeLayoutTitleAction.__doc__
    _required_args = ["layout","title"]

class ChangeLayoutTitleStype(MutationMixin, DynamicArgsMixin, ChangeLayoutTitleStypeAction, graphene.Mutation):
    __doc__ = ChangeLayoutTitleStypeAction.__doc__
    _required_args = ["layout","titlestype"]

class ChangeLayoutPage(MutationMixin, DynamicArgsMixin, ChangeLayoutPageAction, graphene.Mutation):
    __doc__ = ChangeLayoutPageAction.__doc__
    _required_args = ["layout","page"]

class ChangeLayoutItem(MutationMixin, DynamicArgsMixin, ChangeLayoutItemAction, graphene.Mutation):
    __doc__ = ChangeLayoutItemAction.__doc__
    _required_args = ["layout","item"]

class ChangeLayoutPriority(MutationMixin, DynamicArgsMixin, ChangeLayoutPriorityAction, graphene.Mutation):
    __doc__ = ChangeLayoutPriorityAction.__doc__
    _required_args = ["layout","priority"]

class ChangeLayoutInterval(MutationMixin, DynamicArgsMixin, ChangeLayoutIntervalAction, graphene.Mutation):
    __doc__ = ChangeLayoutIntervalAction.__doc__
    _required_args = ["layout","interval"]

class ChangeLayoutStyte(MutationMixin, DynamicArgsMixin, ChangeLayoutStyteAction, graphene.Mutation):
    __doc__ = ChangeLayoutStyteAction.__doc__
    _required_args = ["layout","styte"]

class ChangeLayoutDest(MutationMixin, DynamicArgsMixin, ChangeLayoutDestAction, graphene.Mutation):
    __doc__ = ChangeLayoutDestAction.__doc__
    _required_args = ["layout","dest"]

class ChangeLayoutDestStyle(MutationMixin, DynamicArgsMixin, ChangeLayoutDestStyleAction, graphene.Mutation):
    __doc__ = ChangeLayoutDestStyleAction.__doc__
    _required_args = ["layout","deststyle"]

class ChangeLayoutImg(MutationMixin, DynamicArgsMixin, ChangeLayoutImgAction, graphene.Mutation):
    __doc__ = ChangeLayoutImgAction.__doc__
    _required_args = ["layout","img"]

class LayoutDelete(MutationMixin, DynamicArgsMixin, LayoutDeleteAction, graphene.Mutation):
    __doc__ = LayoutDeleteAction.__doc__
    _required_args = ["layout"]

class AddLayout(MutationMixin, DynamicArgsMixin, AddLayoutAction, graphene.Mutation):
    __doc__ = AddLayoutAction.__doc__
    _required_args = ["title","title_stype","show","active","name","name_styte","priority","dest","dest_style","styte","parent","catergory","background","interval","page","itemseller"]
#layoutitem
class ChangeLayoutItemShow(MutationMixin, DynamicArgsMixin, ChangeLayoutItemShowAction, graphene.Mutation):
    __doc__ = ChangeLayoutItemShowAction.__doc__
    _required_args = ["layoutItem","show"]

class ChangeLayoutItemActive(MutationMixin, DynamicArgsMixin, ChangeLayoutItemActiveAction, graphene.Mutation):
    __doc__ = ChangeLayoutItemActiveAction.__doc__
    _required_args = ["layoutItem","active"]

class ChangeLayoutItemName(MutationMixin, DynamicArgsMixin, ChangeLayoutItemNameAction, graphene.Mutation):
    __doc__ = ChangeLayoutItemNameAction.__doc__
    _required_args = ["layoutItem","name"]

class ChangeLayoutItemTitle(MutationMixin, DynamicArgsMixin, ChangeLayoutItemTitleAction, graphene.Mutation):
    __doc__ = ChangeLayoutItemTitleAction.__doc__
    _required_args = ["layoutItem","title"]

class ChangeLayoutItemTitleStype(MutationMixin, DynamicArgsMixin, ChangeLayoutItemTitleStypeAction, graphene.Mutation):
    __doc__ = ChangeLayoutItemTitleStypeAction.__doc__
    _required_args = ["layoutItem","titlestype"]

class ChangeLayoutItemPriority(MutationMixin, DynamicArgsMixin, ChangeLayoutItemPriorityAction, graphene.Mutation):
    __doc__ = ChangeLayoutItemPriorityAction.__doc__
    _required_args = ["layoutItem","priority"]

class ChangeLayoutItemStyte(MutationMixin, DynamicArgsMixin, ChangeLayoutItemStyteAction, graphene.Mutation):
    __doc__ = ChangeLayoutItemStyteAction.__doc__
    _required_args = ["layoutItem","styte"]

class ChangeLayoutItemDest(MutationMixin, DynamicArgsMixin, ChangeLayoutItemDestAction, graphene.Mutation):
    __doc__ = ChangeLayoutItemDestAction.__doc__
    _required_args = ["layoutItem","dest"]

class ChangeLayoutItemDestStyle(MutationMixin, DynamicArgsMixin, ChangeLayoutItemDestStyleAction, graphene.Mutation):
    __doc__ = ChangeLayoutItemDestStyleAction.__doc__
    _required_args = ["layoutItem","deststyle"]

class ChangeLayoutItemImg(MutationMixin, DynamicArgsMixin, ChangeLayoutItemImgAction, graphene.Mutation):
    __doc__ = ChangeLayoutItemImgAction.__doc__
    _required_args = ["layoutItem","img"]

class LayoutItemDelete(MutationMixin, DynamicArgsMixin, LayoutItemDeleteAction, graphene.Mutation):
    __doc__ = LayoutItemDeleteAction.__doc__
    _required_args = ["layoutItem"]

class AddLayoutItem(MutationMixin, DynamicArgsMixin, AddLayoutItemAction, graphene.Mutation):
    __doc__ = AddLayoutItemAction.__doc__
    _required_args = ["title","title_stype","show","active","name","name_styte","priority","dest","dest_style","styte","layout","avatar"]

#Query
class Query(graphene.ObjectType):
    #model
    all_page                =filter.DjangoFilterConnectionField(PageType)
    page                    =graphene.relay.Node.Field(PageType)
    item                    =graphene.relay.Node.Field(ItemType)
    items_seller            =graphene.relay.Node.Field(Items_sellerType)
    all_Page_layoutType     =filter.DjangoFilterConnectionField(Page_layoutType)
    page_layoutType         =graphene.relay.Node.Field(Page_layoutType)
    all_Layout_catergory    =filter.DjangoFilterConnectionField(Layout_catergoryType)
    layout_catergory        =graphene.relay.Node.Field(Layout_catergoryType)
    all_menu                =filter.DjangoFilterConnectionField(MenuType)
    menu                    =graphene.relay.Node.Field(MenuType)
    all_layout              =filter.DjangoFilterConnectionField(LayoutType)
    layout                  =graphene.relay.Node.Field(LayoutType)
    all_Catergory           =filter.DjangoFilterConnectionField(CatergoryType)
    catergory               =graphene.relay.Node.Field(CatergoryType)
    all_Invoice             =filter.DjangoFilterConnectionField(InvoiceType)
    invoice                 =graphene.relay.Node.Field(InvoiceType)
    all_Item_layoutType     =filter.DjangoFilterConnectionField(Item_layoutType)
    invoice_info            =graphene.relay.Node.Field(InvoiceInfoType)
    all_invoiceinfo         =filter.DjangoFilterConnectionField(InvoiceInfoType)
    item_layoutType         =graphene.relay.Node.Field(Item_layoutType)
    all_Invoice_item        =filter.DjangoFilterConnectionField(LayoutType)
    invoice_item            =graphene.relay.Node.Field(Invoice_itemType)
    all_Group_join          =filter.DjangoFilterConnectionField(Group_joinType)
    group_join              =graphene.relay.Node.Field(Group_joinType)
    all_Group_User_join     =filter.DjangoFilterConnectionField(Group_user_joinType)
    group_user_join         =graphene.relay.Node.Field(Group_user_joinType)
    all_Chat                =filter.DjangoFilterConnectionField(ChatType)
    chat                    =graphene.relay.Node.Field(ChatType)
    allBuyer                =filter.DjangoFilterConnectionField(BuyerType)
    buyer                   =graphene.relay.Node.Field(BuyerType)
    allSeller               =filter.DjangoFilterConnectionField(SellerType)
    seller                  =graphene.relay.Node.Field(SellerType)
    allSupplier             =filter.DjangoFilterConnectionField(SupplierType)
    supplier                =graphene.relay.Node.Field(SupplierType)
    allPaner                =filter.DjangoFilterConnectionField(PanerType)
    paner                   =graphene.relay.Node.Field(PanerType)
    allLikeItemSeller       =filter.DjangoFilterConnectionField(LikeItemSellerType)
    likeItemSeller          =graphene.relay.Node.Field(LikeItemSellerType)
    
    #custom
    filterItemSeller        =graphene.List(Items_sellerType,title=graphene.String(required=True),stastus=graphene.String(required=True))
    filterItemSellerCt      =graphene.List(Items_sellerType,catergory=graphene.String(required=True),stastus=graphene.String(required=True),number=graphene.String(required=True),page=graphene.String(required=True))
    all_ItemSeller_order    =filter.DjangoFilterConnectionField(Items_sellerType,order_by_fields=graphene.String())
    all_Items_seller        =filter.DjangoFilterConnectionField(Items_sellerType,order_by_fields=graphene.String())
    page_by_name            =graphene.Field(PageType, name=graphene.String(required=True))

    count_Items_seller = graphene.Int()
    count_Items_seller_catergory = graphene.Int(catergory=graphene.String(required=True),stastus=graphene.String(required=True))
    count_all_Items = graphene.Int()
    count_allSeller = graphene.Int()
    count_allUser = graphene.Int()
    def resolve_count_Items_seller(self, info):
        return Items_seller.objects.filter(stastus='Public').count()
    def resolve_count_all_Items(self, info):
        return Item.objects.count()
    def resolve_count_allSeller(self, info):
        return Seller.objects.count()
    def resolve_count_Items_seller_catergory(self, info, **kwargs):
        total=0
        try:
            c=Catergory.objects.get(name=kwargs.get('catergory'))
            t=Tag_catergory.objects.filter(catergory=c)
            for i in t :
                total+= Items_seller.objects.filter(stastus=kwargs.get('stastus'),item=i.item).count()
        except : pass
        return total
    
    def resolve_filterItemSellerCt(self, info, **kwargs):
        total=[]
        c=Catergory.objects.get(name=kwargs.get('catergory'))
        t=Tag_catergory.objects.filter(catergory=c)
        for i in t :
            items= Items_seller.objects.filter(stastus=kwargs.get('stastus'),item=i.item)
            if items:
                for it in items:
                    if it not in total:
                        total.append(it)
        n=int(kwargs.get('number'))
        p=int(kwargs.get('page')) 
        _s=p*n
        _e=(p+1)*n
        return total[_s:_e]
    
    def resolve_filterItemSeller(self, info ,**kwargs):
        stastus=kwargs.get('stastus')
        title=kwargs.get('title')
        return Items_seller.objects.filter(item__title__contains=title,stastus=stastus)    
        
#Mutation
class Mutation(graphene.ObjectType):
    #user
    changeFirtName=ChangeFirtName.Field()
    changeLastName=ChangeLastName.Field()
    changeAddress=ChangeAddressName.Field()
    changePhone=ChangePhone.Field()
    creatRom=CreatRom.Field()
    joinRom=JoinRom.Field()
    chat=ChatRom.Field()
    #cart
    get_or_createInvoice=Get_or_createInvoice.Field()
    add_item_invoice=Add_item_cart.Field()
    likeItem=Add_item_Like.Field()
    disLikeItem=Add_item_disLike.Field()
    removeItemCart=Remove_item_cart.Field()
    orderCart=Ordercart.Field()
    cancelCart=Cancelcart.Field()
    #layout
    changeLayoutShow=ChangeLayoutShow.Field()
    changeLayoutActive=ChangeLayoutActive.Field()
    changeLayoutCatergory=ChangeLayoutCatergory.Field()
    changeLayoutName=ChangeLayoutName.Field()
    changeLayoutTitle=ChangeLayoutTitle.Field()
    changeLayoutTitleStype=ChangeLayoutTitleStype.Field()
    changeLayoutPage=ChangeLayoutPage.Field()
    changeLayoutPriority=ChangeLayoutPriority.Field()
    changeLayoutInterval=ChangeLayoutInterval.Field()
    changeLayoutStyte=ChangeLayoutStyte.Field()
    changeLayoutItem=ChangeLayoutItem.Field()
    changeLayoutDest=ChangeLayoutDest.Field()
    changeLayoutDestStyle=ChangeLayoutDestStyle.Field()
    changeLayoutImg=ChangeLayoutImg.Field()
    layoutDelete=LayoutDelete.Field()
    addLayout=AddLayout.Field()
    #layoutItem
    changeLayoutItemShow=ChangeLayoutItemShow.Field()
    changeLayoutItemActive=ChangeLayoutItemActive.Field()
    changeLayoutItemName=ChangeLayoutItemName.Field()
    changeLayoutItemTitle=ChangeLayoutItemTitle.Field()
    changeLayoutItemTitleStype=ChangeLayoutItemTitleStype.Field()
    changeLayoutItemPriority=ChangeLayoutItemPriority.Field()
    changeLayoutItemStyte=ChangeLayoutItemStyte.Field()
    changeLayoutItemDest=ChangeLayoutItemDest.Field()
    changeLayoutItemDestStyle=ChangeLayoutItemDestStyle.Field()
    changeLayoutItemImg=ChangeLayoutItemImg.Field()
    layoutItemDelete=LayoutItemDelete.Field()
    addLayoutItem=AddLayoutItem.Field()
    
schema = graphene.Schema(query=Query)

