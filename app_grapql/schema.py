from graphql_auth.bases import Output,MutationMixin,DynamicArgsMixin,graphene
from graphql_relay import from_global_id
from graphene_django import DjangoObjectType,filter
from django.core.files.base import ContentFile,File
from django.core.files.uploadedfile import UploadedFile
from graphene_file_upload.scalars import Upload

from app_grapql.models import *

#Types
class UserType(DjangoObjectType):
    class Meta:
        model = User
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

#file    
class UploadFileAction(Output):
    fileUpload=graphene.Field(HistoryUploadfileType)
    class Arguments:
        file = Upload(required=True)
        fileType=graphene.String(required=True)
    
    def resolve_mutation(cls, root, info, **kwargs):
        cls.success=False
        cls.errors=[{"message":"user does not exist"}]
        # Xử lý tệp tin ở đây
        user=info.context.user
        cls.fileUpload=None
        file=None

        if user.is_authenticated:
            file=kwargs.get("file")
            fileType=kwargs.get("fileType")
        else: return cls

        if file:
            content_file = ContentFile(file.read())
            uploaded_file = UploadedFile(file=content_file, name=file.name)
            fileUpload=HistoryFileUp.create(user=user,file=uploaded_file,filetype=fileType)
            fileUpload.size=uploaded_file.size
            fileUpload.title=file.name
        else: 
            cls.errors=[{"message":"file does not exist"}]
            return cls
        
        if fileUpload:
            fileUpload.save()
            cls.success=True
            cls.errors=None
            cls.fileUpload=fileUpload
            return cls
        cls.errors=[{"message":"file does not save"}]
        return cls
    
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

#file
class UploadFile_mutation(MutationMixin, DynamicArgsMixin, UploadFileAction, graphene.Mutation):
    __doc__ = UploadFileAction.__doc__
    _required_args = ["file","fileType"]

#Query
class Query(graphene.ObjectType):
    all_page = filter.DjangoFilterConnectionField(PageType)
    page = graphene.relay.Node.Field(PageType)
    item=graphene.relay.Node.Field(ItemType)
    items_seller=graphene.relay.Node.Field(Items_sellerType)
    all_Page_layoutType = filter.DjangoFilterConnectionField(Page_layoutType)
    page_layoutType = graphene.relay.Node.Field(Page_layoutType)
    all_menu = filter.DjangoFilterConnectionField(MenuType)
    menu = graphene.relay.Node.Field(MenuType)
    all_layout=filter.DjangoFilterConnectionField(LayoutType)
    layout=graphene.relay.Node.Field(LayoutType)
    all_Catergory=filter.DjangoFilterConnectionField(CatergoryType)
    catergory=graphene.relay.Node.Field(CatergoryType)
    all_Invoice=filter.DjangoFilterConnectionField(InvoiceType)
    invoice=graphene.relay.Node.Field(InvoiceType)
    all_Item_layoutType=filter.DjangoFilterConnectionField(Item_layoutType)
    invoice_info=graphene.relay.Node.Field(InvoiceInfoType)
    all_invoiceinfo=filter.DjangoFilterConnectionField(InvoiceInfoType)
    item_layoutType=graphene.relay.Node.Field(Item_layoutType)
    all_Invoice_item=filter.DjangoFilterConnectionField(LayoutType)
    invoice_item=graphene.relay.Node.Field(Invoice_itemType)
    all_Group_join=filter.DjangoFilterConnectionField(Group_joinType)
    group_join=graphene.relay.Node.Field(Group_joinType)
    all_Group_User_join=filter.DjangoFilterConnectionField(Group_user_joinType)
    group_user_join=graphene.relay.Node.Field(Group_user_joinType)
    all_Chat=filter.DjangoFilterConnectionField(ChatType)
    chat=graphene.relay.Node.Field(ChatType)
    allBuyer=filter.DjangoFilterConnectionField(BuyerType)
    buyer=graphene.relay.Node.Field(BuyerType)
    allSeller=filter.DjangoFilterConnectionField(SellerType)
    seller=graphene.relay.Node.Field(SellerType)
    allSupplier=filter.DjangoFilterConnectionField(SupplierType)
    supplier=graphene.relay.Node.Field(SupplierType)
    allLikeItemSeller=filter.DjangoFilterConnectionField(LikeItemSellerType)
    likeItemSeller=graphene.relay.Node.Field(LikeItemSellerType)
    
    
    filterItemSeller=graphene.List(Items_sellerType,title=graphene.String(required=True),stastus=graphene.String(required=True))
    filterItemSellerCt=graphene.List(Items_sellerType,catergory=graphene.String(required=True),stastus=graphene.String(required=True),number=graphene.String(required=True),page=graphene.String(required=True))
    all_ItemSeller_order=filter.DjangoFilterConnectionField(Items_sellerType,order_by_fields=graphene.String())
    all_Items_seller=filter.DjangoFilterConnectionField(Items_sellerType,order_by_fields=graphene.String())
    page_by_name = graphene.Field(PageType, name=graphene.String(required=True))

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
    changeFirtName=ChangeFirtName.Field()
    changeLastName=ChangeLastName.Field()
    changeAddress=ChangeAddressName.Field()
    changePhone=ChangePhone.Field()
    creatRom=CreatRom.Field()
    joinRom=JoinRom.Field()
    chat=ChatRom.Field()
    get_or_createInvoice=Get_or_createInvoice.Field()
    add_item_invoice=Add_item_cart.Field()
    likeItem=Add_item_Like.Field()
    disLikeItem=Add_item_disLike.Field()
    removeItemCart=Remove_item_cart.Field()
    orderCart=Ordercart.Field()
    cancelCart=Cancelcart.Field()

    uploadFile=UploadFile_mutation.Field()
    
schema = graphene.Schema(query=Query)


'''tham khảo
#from django.core.files.storage import FileSystemStorage
class UploadFileAction(Output):
    file_url = graphene.String()
    class Arguments:
        file = Upload(required=True)
    
    def resolve_mutation(cls, root, info, **kwargs):
        cls(success=False,errors=[{"message":"file does not exist"}])
        # Xử lý tệp tin ở đây
        file=kwargs.get("file")
        content_file = ContentFile(file.read())
        uploaded_file = UploadedFile(file=content_file, name=file.name)
        
        # Lưu trữ uploaded_file vào thư mục media/upload
        fs = FileSystemStorage(location='app_grapql/static/upload/fileupload/%Y/%m')
        #if uploaded_file.size>1024*1024*10:
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        if file_url:
            cls(success=True,errors=None)
        return UploadFileAction(file_url,cls)
'''
