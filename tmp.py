# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Branches(models.Model):
    outlet = models.OneToOneField('Outlets', models.DO_NOTHING, primary_key=True, db_comment='Привязка к зданию')
    num_workers = models.IntegerField(db_comment='Количество работников')

    class Meta:
        managed = False
        db_table = 'branches'
        db_table_comment = 'Филиалы'


class Clients(models.Model):
    full_name = models.CharField(max_length=50, db_comment='ФИО клиента')
    is_professional = models.BooleanField(db_comment='Проффесионал или Любитель?')
    discount = models.IntegerField(db_comment='Персональная скидка')
    discount_card = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'
        db_table_comment = 'Таблица клиентов различных фотоцентров'


class Deliveries(models.Model):
    storage = models.ForeignKey('Storage', models.DO_NOTHING, db_comment='Связь с главным складом')
    vendor = models.ForeignKey('Vendors', models.DO_NOTHING, db_comment='Связь с поставщиком')
    delivery_date = models.DateField(db_comment='Дата поставки')

    class Meta:
        managed = False
        db_table = 'deliveries'
        db_table_comment = 'Поставки в главный склад'


class DeliveryItems(models.Model):
    delivery = models.ForeignKey(Deliveries, models.DO_NOTHING)
    item = models.ForeignKey('Items', models.DO_NOTHING)
    purchase_price = models.DecimalField(max_digits=15, decimal_places=2, db_comment='Цена закупки товара')
    amount = models.IntegerField(db_comment='Количество поставленных едениц товара')

    class Meta:
        managed = False
        db_table = 'delivery_items'
        unique_together = (('delivery', 'item'),)
        db_table_comment = 'Товары в поставке'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FilmDevelopmentOrders(models.Model):
    code = models.CharField(unique=True, max_length=50, blank=True, null=True, db_comment='Уникальный код пленки')
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True, db_comment='Связь с заказом')

    class Meta:
        managed = False
        db_table = 'film_development_orders'
        db_table_comment = 'Проявка пленок(вложено в чек заказа)'


class Films(models.Model):
    code = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'films'


class Firms(models.Model):
    name = models.CharField(unique=True, max_length=100, db_comment='Название Бренда')

    class Meta:
        managed = False
        db_table = 'firms'
        db_table_comment = 'Бренды товаров'


class Frames(models.Model):
    print_order = models.ForeignKey('PrintOrders', models.DO_NOTHING, db_comment='Связь с заказом')
    amount = models.IntegerField(db_comment='Количество копий')
    film = models.ForeignKey(Films, models.DO_NOTHING, db_comment='Связь с пленкой')
    frame_number = models.IntegerField()
    print_price = models.ForeignKey('PrintPrices', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frames'
        db_table_comment = 'Кадры'


class Items(models.Model):
    firm = models.ForeignKey(Firms, models.DO_NOTHING, db_comment='Связь с брэндом')
    product_name = models.CharField(max_length=100, db_comment='Название товара')
    price = models.DecimalField(max_digits=15, decimal_places=2, db_comment='Цена')

    class Meta:
        managed = False
        db_table = 'items'
        unique_together = (('firm', 'product_name'),)
        db_table_comment = 'Товары'


class Kiosks(models.Model):
    outlet = models.OneToOneField('Outlets', models.DO_NOTHING, primary_key=True, db_comment='Здание где расположен')
    branch_outlet = models.ForeignKey(Branches, models.DO_NOTHING, db_comment='Киоск связан с филиаом')
    num_workers = models.IntegerField(db_comment='Количество работников')

    class Meta:
        managed = False
        db_table = 'kiosks'
        db_table_comment = 'Киоск'


class Orders(models.Model):
    client = models.ForeignKey(Clients, models.DO_NOTHING, db_comment='Клиент, который сделал заказ')
    accept_outlet = models.ForeignKey('Outlets', models.DO_NOTHING, db_comment='Где приняли заказ')
    accept_timestamp = models.DateTimeField(db_comment='Когда заказ поступил')
    total_amount_price = models.IntegerField(
        db_comment='Суммарная цена заказа, которая рассчитывается из купленных товаров, услуг....')
    is_urgent = models.BooleanField(db_comment='Срочность заказа')

    class Meta:
        managed = False
        db_table = 'orders'
        db_table_comment = 'Заказы'


class OutletTypes(models.Model):
    name = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'outlet_types'
        db_table_comment = 'Типы зданий'


class Outlets(models.Model):
    type = models.ForeignKey(OutletTypes, models.DO_NOTHING, db_comment='Тип здания')
    address = models.CharField(max_length=200, db_comment='Адресс')

    class Meta:
        managed = False
        db_table = 'outlets'
        unique_together = (('type', 'address'),)
        db_table_comment = 'Здания'


class PaperSizes(models.Model):
    name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'paper_sizes'
        db_table_comment = 'Формат бумаги'


class PaperTypes(models.Model):
    name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'paper_types'
        db_table_comment = 'Тип бумаги'


class PhotoStores(models.Model):
    outlet = models.OneToOneField(Outlets, models.DO_NOTHING, primary_key=True, db_comment='Привязка к зданию')
    num_workers = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'photo_stores'
        db_table_comment = 'Фотомагазины'


class PrintDiscounts(models.Model):
    photo_amount = models.IntegerField(unique=True, db_comment='Количество фотографий, критерий')
    discount = models.IntegerField(db_comment='Размер скидки в процентах')

    class Meta:
        managed = False
        db_table = 'print_discounts'
        db_table_comment = 'Скидка на печать'


class PrintOrders(models.Model):
    order = models.ForeignKey(Orders, models.DO_NOTHING, db_comment='Связь с заказом')
    discount = models.ForeignKey(PrintDiscounts, models.DO_NOTHING, blank=True, null=True, db_comment='Скидка')

    class Meta:
        managed = False
        db_table = 'print_orders'
        db_table_comment = 'Заказы на печать'


class PrintPrices(models.Model):
    paper_size = models.ForeignKey(PaperSizes, models.DO_NOTHING, db_comment='Формат бумаги')
    paper_type = models.ForeignKey(PaperTypes, models.DO_NOTHING, db_comment='Тип бумаги')
    price = models.DecimalField(max_digits=15, decimal_places=2, db_comment='Цена за (формат, печать)')

    class Meta:
        managed = False
        db_table = 'print_prices'
        unique_together = (('paper_size', 'paper_type'),)
        db_table_comment = 'Расценки на печать'


class SaleFilms(models.Model):
    sale_order = models.ForeignKey('SaleOrders', models.DO_NOTHING, db_comment='Ссылка на продажу товара в заказе')
    film_id = models.IntegerField(db_comment='Ссылка на саму пленку')

    class Meta:
        managed = False
        db_table = 'sale_films'
        db_table_comment = 'Продажа пленок'


class SaleOrders(models.Model):
    order = models.ForeignKey(Orders, models.DO_NOTHING, blank=True, null=True, db_comment='Связь с заказом')
    item = models.ForeignKey(Items, models.DO_NOTHING, db_comment='Связь с товарами')
    amount = models.IntegerField(db_comment='Количество')

    class Meta:
        managed = False
        db_table = 'sale_orders'
        db_table_comment = 'Продажи товаров в заказе'


class ServiceOrders(models.Model):
    order = models.ForeignKey(Orders, models.DO_NOTHING, db_comment='Связь с заказом')
    service_type = models.ForeignKey('ServiceTypesOutlets', models.DO_NOTHING, db_comment='Связь с типом услуги')
    count = models.IntegerField(db_comment='Количество таких услуг заказанных')

    class Meta:
        managed = False
        db_table = 'service_orders'
        db_table_comment = 'Заказ услуг'


class ServiceTypes(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'service_types'


class ServiceTypesNeededItems(models.Model):
    item = models.OneToOneField(Items, models.DO_NOTHING,
                                primary_key=True)  # The composite primary key (item_id, service_type_id) found, that is not supported. The first column is selected.
    service_type = models.ForeignKey(ServiceTypes, models.DO_NOTHING)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_types_needed_items'
        unique_together = (('item', 'service_type'),)


class ServiceTypesOutlets(models.Model):
    service_type = models.ForeignKey(ServiceTypes, models.DO_NOTHING)
    outlet_type = models.ForeignKey(OutletTypes, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'service_types_outlets'
        db_table_comment = 'Типы услуг'


class Storage(models.Model):
    is_main_storage = models.BooleanField(blank=True, null=True, db_comment='Связь с главным складом')
    capacity = models.IntegerField(db_comment='Вместимость')
    outlet = models.ForeignKey(Outlets, models.DO_NOTHING, db_comment='Связь со зданием')

    class Meta:
        managed = False
        db_table = 'storage'
        db_table_comment = 'Склады зданий'


class StorageItems(models.Model):
    storage = models.ForeignKey(Storage, models.DO_NOTHING, db_comment='Связь со складом зданий')
    item = models.ForeignKey(Items, models.DO_NOTHING, db_comment='Связь с товаром')
    quantity = models.IntegerField(db_comment='Количество товаров данного типа на складе')

    class Meta:
        managed = False
        db_table = 'storage_items'
        unique_together = (('storage', 'item'),)
        db_table_comment = 'Товары на складах зданий'


class VendorItems(models.Model):
    vendor = models.ForeignKey('Vendors', models.DO_NOTHING, db_comment='Связь с поставщиком')
    item = models.ForeignKey(Items, models.DO_NOTHING, db_comment='Связь с товаром')
    current_price = models.IntegerField(blank=True, null=True,
                                        db_comment='Текущая цена по которой продает поставщик данный товар')

    class Meta:
        managed = False
        db_table = 'vendor_items'
        unique_together = (('vendor', 'item'),)
        db_table_comment = 'По какой цене продает поставщик товары'


class Vendors(models.Model):
    name = models.CharField(unique=True, max_length=100, db_comment='Название компании(поставщика)')

    class Meta:
        managed = False
        db_table = 'vendors'
        db_table_comment = 'Поставщики'
