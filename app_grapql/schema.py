import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_auth.bases import Output,MutationMixin,DynamicArgsMixin
from graphene.utils.str_converters import to_snake_case

from app_grapql.models import *
#custum
class OrderedDjangoFilterConnectionField(DjangoFilterConnectionField):
    @classmethod
    def resolve_queryset(
        cls, connection, iterable, info, args, filtering_args, filterset_class
    ):
        qs = super(DjangoFilterConnectionField, cls).resolve_queryset(
            connection, iterable, info, args
        )
        filter_kwargs = {k: v for k, v in args.items() if k in filtering_args}
        qs = filterset_class(data=filter_kwargs, queryset=qs, request=info.context).qs

        order = args.get('orderBy', None)
        if order:
            if type(order) is str:
                snake_order = to_snake_case(order)
            else:
                snake_order = [to_snake_case(o) for o in order]
            qs = qs.order_by(*snake_order)
        return qs
    
#Types
class UserType(DjangoObjectType):
    class Meta:
        model = User
             
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
    class Arguments:
        firtName=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        if user.is_authenticated:
            user.first_name=kwargs.get("firtName")
            user.save()
            return cls(success=True,errors=None)
        return cls(success=False,errors="User does not exist")

class ChangeFirtName(MutationMixin, DynamicArgsMixin, ChangeFirtNameAction, graphene.Mutation):
    __doc__ = ChangeFirtNameAction.__doc__
    _required_args = ["firtName"]

class ChangeLastNameAction(Output):
    class Arguments:
        lastName=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        if user.is_authenticated:
            user.last_name=kwargs.get("lastName")
            user.save()
            return cls(success=True,errors=None)
        return cls(success=False,errors="User does not exist")

class ChangeLastName(MutationMixin, DynamicArgsMixin, ChangeLastNameAction, graphene.Mutation):
    __doc__ = ChangeLastNameAction.__doc__
    _required_args = ["lastName"]

class ChangeAddressAction(Output):
    class Arguments:
        address=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        if user.is_authenticated:
            user.address=kwargs.get("address")
            user.save()
            return cls(success=True,errors=None)
        return cls(success=False,errors="User does not exist")

class ChangeAddressName(MutationMixin, DynamicArgsMixin, ChangeAddressAction, graphene.Mutation):
    __doc__ = ChangeAddressAction.__doc__
    _required_args = ["address"]

class ChangePhoneAction(Output):
    class Arguments:
        phone=graphene.String(required=True)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user=info.context.user
        if user.is_authenticated:
            user.phone=kwargs.get("phone")
            user.save()
            return cls(success=True,errors=None)
        return cls(success=False,errors="User does not exist")

class ChangePhone(MutationMixin, DynamicArgsMixin, ChangePhoneAction, graphene.Mutation):
    __doc__ = ChangePhoneAction.__doc__
    _required_args = ["phone"]


#Query
class Query(graphene.ObjectType):
    all_page = DjangoFilterConnectionField(PageType)
    page = graphene.relay.Node.Field(PageType)
    item=graphene.relay.Node.Field(ItemType)
    all_Page_layoutType = DjangoFilterConnectionField(Page_layoutType)
    page_layoutType = graphene.relay.Node.Field(Page_layoutType)
    all_menu = DjangoFilterConnectionField(MenuType)
    menu = graphene.relay.Node.Field(MenuType)
    all_layout=DjangoFilterConnectionField(LayoutType)
    layout=graphene.relay.Node.Field(LayoutType)
    all_Catergory=DjangoFilterConnectionField(CatergoryType)
    catergory=graphene.relay.Node.Field(CatergoryType)
    all_Invoice=DjangoFilterConnectionField(InvoiceType)
    invoice=graphene.relay.Node.Field(InvoiceType)
    all_Item_layoutType=DjangoFilterConnectionField(Item_layoutType)
    item_layoutType=graphene.relay.Node.Field(Item_layoutType)
    all_Invoice_item=DjangoFilterConnectionField(LayoutType)
    invoice_item=graphene.relay.Node.Field(Invoice_itemType)
    all_Group_join=DjangoFilterConnectionField(Group_joinType)
    group_join=graphene.relay.Node.Field(Group_joinType)
    all_Group_User_join=DjangoFilterConnectionField(Group_user_joinType)
    group_user_join=graphene.relay.Node.Field(Group_user_joinType)
    all_Chat=DjangoFilterConnectionField(ChatType)
    chatType=graphene.relay.Node.Field(ChatType)

    all_Item=DjangoFilterConnectionField(ItemType,order_by_fields=graphene.String())
    page_by_name = graphene.Field(PageType, name=graphene.String(required=True))
    

    

#Mutation
class Mutation(graphene.ObjectType):
    changeFirtName=ChangeFirtName.Field()
    changeLastName=ChangeLastName.Field()
    changeAddress=ChangeAddressName.Field()
    changePhone=ChangePhone.Field()
    

schema = graphene.Schema(query=Query)