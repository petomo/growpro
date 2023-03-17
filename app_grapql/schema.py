import graphene
from graphene import relay
from graphql_relay import from_global_id
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_auth.bases import Output,MutationMixin,DynamicArgsMixin

from app_grapql.models import *
  
#Types
class UserType(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )
             
class PageType(DjangoObjectType):
    class Meta:
        model = Page
        fields='__all__'
        filter_fields='__all__'
        interfaces = (relay.Node, )

class MenuType(DjangoObjectType):
    class Meta:
        model = Menu
        fields='__all__'
        filter_fields=("id", "title", "show", "active", "name", "page", "parent", "priority")
        interfaces = (relay.Node, )

class Layout_catergoryType(DjangoObjectType):
    class Meta:
        model = Layout_catergory
        fields='__all__'
        filter_fields='__all__'
        interfaces = (relay.Node, )

class LayoutType(DjangoObjectType):
    class Meta:
        model = Layout
        fields='__all__'
        filter_fields=("id", "title", "show", "active", "name", "parent", "priority","catergory")
        interfaces = (relay.Node, )

class Layout_imgType(DjangoObjectType):
    class Meta:
        model = Layout_img
        fields='__all__'
        filter_fields=("id", "title", "show", "active", "name")
        interfaces = (relay.Node, )

class Page_layoutType(DjangoObjectType):
    class Meta:
        model = Page_layout
        fields='__all__'
        filter_fields='__all__'
        interfaces = (relay.Node, )

class ItemType(DjangoObjectType):
    class Meta:
        model = Item
        fields='__all__'
        filter_fields=("id", "title", "show", "active", "name","supplier","stastus","price")
        interfaces = (relay.Node, )

class Items_sellerType(DjangoObjectType):
    class Meta:
        model = Items_seller
        fields='__all__'
        filter_fields='__all__'
        interfaces = (relay.Node, )

class Item_layoutType(DjangoObjectType):
    class Meta:
        model = Item_layout
        fields='__all__'
        filter_fields='__all__'
        interfaces = (relay.Node, )

class CatergoryType(DjangoObjectType):
    class Meta:
        model = Catergory
        fields='__all__'
        filter_fields=("id", "title", "show", "active", "name", "parent")
        interfaces = (relay.Node, )

class Tag_catergoryType(DjangoObjectType):
    class Meta:
        model = Tag_catergory
        fields='__all__'
        filter_fields='__all__'
        interfaces = (relay.Node, )

class InvoiceType(DjangoObjectType):
    class Meta:
        model = Invoice
        fields='__all__'
        filter_fields='__all__'
        interfaces = (relay.Node, )

class Invoice_historyType(DjangoObjectType):
    class Meta:
        model = Invoice_history
        fields='__all__'
        filter_fields='__all__'
        interfaces = (relay.Node, )

class Invoice_itemType(DjangoObjectType):
    class Meta:
        model = Invoice_item
        fields='__all__'
        filter_fields='__all__'
        interfaces = (relay.Node, )

class Group_joinType(DjangoObjectType):
    class Meta:
        model = Group_join
        fields='__all__'
        filter_fields='__all__'
        interfaces = (relay.Node, )

class Group_user_joinType(DjangoObjectType):
    class Meta:
        model = Group_user_join
        fields='__all__'
        filter_fields='__all__'
        interfaces = (relay.Node, )

class ChatType(DjangoObjectType):
    class Meta:
        model = Chat
        fields='__all__'
        filter_fields='__all__'
        interfaces = (relay.Node, )

class HistoryMutationType(DjangoObjectType):
    class Meta:
        model = HistoryMutation
        fields='__all__'
        filter_fields='__all__'
        interfaces = (relay.Node, )

#action
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
        rom=None
        cls(success=False,errors=[{"message":"User does not exist"}])
        if user.is_authenticated:
            member_name=kwargs.get("member")
            member=User.objects.filter(username__contains=member_name)
            if member:
                rom_dest='&'+user.username+'&'+member_name
                rom=Group_join.objects.get(name__contains=rom_dest)
                if rom:
                    return CreatRomAction(rom,cls)
                rom= Group_join.objects.create(dest=rom_dest,name=rom_dest)
                rom.save()
                cls(success=True,errors=None)             
                return CreatRomAction(rom,cls)
        return  CreatRomAction(rom,cls)

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
        rom=None
        cls(success=False,errors=[{"message":"User does not exist"}])
        if user.is_authenticated:
            romId=kwargs.get("rom")
            _, model_id = from_global_id(romId)
            rom=Group_join.objects.get(id__contains=model_id)
            if rom:
                g=Group_user_join.objects.create(user=user,group_join=rom)
                g.save()
                rom.updateName(str('&'+user.username))               
                return cls(success=True,errors=None)
            return cls(success=False,errors=[{"message":"Rom does not exist"}])
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
        rom=None
        cls(success=False,errors=[{"message":"User does not exist"}])
        if user.is_authenticated:
            romId=kwargs.get("rom")
            dest=kwargs.get("dest")
            _, model_id = from_global_id(romId)
            rom=Group_join.objects.filter(id__contains=model_id)
            if rom:
                chat=Chat.objects.create(user=user,dest=dest,groups=rom,stastus=6)
                chat.save
                g=Group_user_join.objects.filter(user=user,group_join=rom)
                g.last_chat=chat            
                cls(success=True,errors=None)
                return ChatRomAction(chat,cls) 
            cls(success=False,errors=[{"message":"Rom does not exist"}])
            return ChatRomAction(chat,cls)  
        return ChatRomAction(chat,cls) 

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
        invoice=None
        cls(success=False,errors=[{"message":"User does not exist"}])
        if user.is_authenticated:
            invoice=Invoice.objects.get(buyer=user,status_now=1)            
            if invoice:
                invoice.save()               
                cls(success=True,errors=None)
                return get_or_create_CartAction(invoice,cls)
            invoice=user.creat_Invoice_buyer()
            if invoice:              
                cls(success=True,errors=None)
                return get_or_create_CartAction(invoice,cls)
            invoice=user.creat_Invoice_buyer()
            return get_or_create_CartAction(invoice,cls(success=False,errors=[{"message":"Invoice does not exist"}])) 
        return get_or_create_CartAction(invoice,cls)

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
        invoice=None
        item=None
        cls(success=False,errors=[{"message":"User does not exist"}])
        _number=kwargs.get("rom")
        _item=kwargs.get("item")
        _price=kwargs.get("price")
        if user.is_authenticated:
            invoice=Invoice.objects.get(buyer=user,status_now=1)            
            if invoice:
                pass
            else: 
                invoice=user.creat_Invoice_buyer()
            if invoice:
                if _item:
                    _, model_item_id = from_global_id(_item)
                    item=Items_seller.objects.get(id=model_item_id)
                if item and _number and _price:
                    invoice.creat_Invoice_item(item,_number,_price)              
                    cls(success=True,errors=None)
                    return get_or_create_CartAction(invoice,cls)
            return add_item_CartAction(invoice,cls(success=False,errors=[{"message":"Invoice does not exist"}])) 
        return add_item_CartAction(invoice,cls)

#MutationFunction
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

class CreatRom(MutationMixin, DynamicArgsMixin, CreatRomAction, graphene.Mutation):
    __doc__ = CreatRomAction.__doc__
    _required_args = ["member"]

class JoinRom(MutationMixin, DynamicArgsMixin, JoinRomAction, graphene.Mutation):
    __doc__ = JoinRomAction.__doc__
    _required_args = ["rom"]

class ChatRom(MutationMixin, DynamicArgsMixin, ChatRomAction, graphene.Mutation):
    __doc__ = ChatRomAction.__doc__
    _required_args = ["rom","dest"]

class CreateInvoice(MutationMixin, DynamicArgsMixin, get_or_create_CartAction, graphene.Mutation):
    __doc__ = JoinRomAction.__doc__

class Add_item_cart(MutationMixin, DynamicArgsMixin, add_item_CartAction, graphene.Mutation):
    __doc__ = add_item_CartAction.__doc__
    _required_args = ["item","number","price"]

#Query
class Query(graphene.ObjectType):
    all_page = DjangoFilterConnectionField(PageType)
    page = relay.Node.Field(PageType)
    item=relay.Node.Field(ItemType)
    all_Page_layoutType = DjangoFilterConnectionField(Page_layoutType)
    page_layoutType = relay.Node.Field(Page_layoutType)
    all_menu = DjangoFilterConnectionField(MenuType)
    menu = relay.Node.Field(MenuType)
    all_layout=DjangoFilterConnectionField(LayoutType)
    layout=relay.Node.Field(LayoutType)
    all_Catergory=DjangoFilterConnectionField(CatergoryType)
    catergory=relay.Node.Field(CatergoryType)
    all_Invoice=DjangoFilterConnectionField(InvoiceType)
    invoice=relay.Node.Field(InvoiceType)
    all_Item_layoutType=DjangoFilterConnectionField(Item_layoutType)
    item_layoutType=relay.Node.Field(Item_layoutType)
    all_Invoice_item=DjangoFilterConnectionField(LayoutType)
    invoice_item=graphene.relay.Node.Field(Invoice_itemType)
    all_Group_join=DjangoFilterConnectionField(Group_joinType)
    group_join=relay.Node.Field(Group_joinType)
    all_Group_User_join=DjangoFilterConnectionField(Group_user_joinType)
    group_user_join=relay.Node.Field(Group_user_joinType)
    all_Chat=DjangoFilterConnectionField(ChatType)
    chatType=relay.Node.Field(ChatType)

    all_Item=DjangoFilterConnectionField(ItemType,order_by_fields=graphene.String())
    page_by_name = graphene.Field(PageType, name=graphene.String(required=True))
    

    
#Mutation
class Mutation(graphene.ObjectType):
    changeFirtName=ChangeFirtName.Field()
    changeLastName=ChangeLastName.Field()
    changeAddress=ChangeAddressName.Field()
    changePhone=ChangePhone.Field()
    creatRom=CreatRom.Field()
    joinRom=JoinRom.Field()
    chat=ChatRom.Field()
    get_or_createInvoice=CreateInvoice.Field()
    add_item_invoice=Add_item_cart.Field()

schema = graphene.Schema(query=Query)