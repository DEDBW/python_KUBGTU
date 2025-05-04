from django.db import models

class Zhanr(models.Model):
    nomer_zhanra = models.AutoField(primary_key=True, db_column='Номер_жанра')
    nazvanie = models.CharField(max_length=255, db_column='Название')
    podzhanr = models.CharField(max_length=255, db_column='Поджанр', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Жанр'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.nazvanie if self.nazvanie else f'Жанр #{self.nomer_zhanra}'


class Izdatel(models.Model):
    nomer_izdatelya = models.AutoField(primary_key=True, db_column='Номер_издателя')
    nomer_strany = models.ForeignKey('Strana', on_delete=models.SET_NULL, db_column='Номер_страны', blank=True, null=True)
    nazvanie_kompanii = models.CharField(max_length=255, db_column='Название_компании', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Издатель'
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'

    def __str__(self):
        return self.nazvanie_kompanii if self.nazvanie_kompanii else f'Издатель #{self.nomer_izdatelya}'


class Platforma(models.Model):
    nomer_platformy = models.AutoField(primary_key=True, db_column='Номер_платформы')
    nazvanie = models.CharField(max_length=255, db_column='Название', blank=True, null=True)
    proizvoditel = models.CharField(max_length=255, db_column='Производитель', blank=True, null=True)
    tip_platformy = models.CharField(max_length=255, db_column='Тип_платформы', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Платформа'
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'

    def __str__(self):
        return self.nazvanie if self.nazvanie else f'Платформа #{self.nomer_platformy}'


class Razrabotchik(models.Model):
    nomer_razrabotchika = models.AutoField(primary_key=True, db_column='Номер_разработчика')
    nomer_strany = models.ForeignKey('Strana', on_delete=models.SET_NULL, db_column='Номер_страны', blank=True, null=True)
    nazvanie_kompanii = models.CharField(max_length=255, db_column='Название_компании', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Разработчик'
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'

    def __str__(self):
        return self.nazvanie_kompanii if self.nazvanie_kompanii else f'Разработчик #{self.nomer_razrabotchika}'


class Strana(models.Model):
    nomer_strany = models.AutoField(primary_key=True, db_column='Номер_страны')
    nazvanie = models.CharField(max_length=255, db_column='Название', blank=True, null=True)
    ofitsialnyy_yazyk = models.ForeignKey('Yazyk', on_delete=models.SET_NULL, db_column='Официальный_язык', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Страна'
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.nazvanie if self.nazvanie else f'Страна #{self.nomer_strany}'


class Yazyk(models.Model):
    nomer_yazyka = models.AutoField(primary_key=True, db_column='Номер_языка')
    iso_kod = models.CharField(unique=True, max_length=2, db_column='iso_код')
    nazvanie = models.CharField(max_length=255, db_column='Название', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Язык'
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.nazvanie if self.nazvanie else f'Язык #{self.nomer_yazyka}'


class Igra(models.Model):
    nomer_igry = models.AutoField(primary_key=True, db_column='Номер_игры')
    nomer_zhanra = models.ForeignKey(Zhanr, on_delete=models.SET_NULL, db_column='Номер_жанра', blank=True, null=True)
    nomer_izdatelya = models.ForeignKey(Izdatel, on_delete=models.SET_NULL, db_column='Номер_издателя', blank=True, null=True)
    nomer_razrabotchika = models.ForeignKey(Razrabotchik, on_delete=models.SET_NULL, db_column='Номер_разработчика', blank=True, null=True)
    oblozhka = models.ImageField(db_column='Путь_к_обложке', upload_to='game_covers/', blank=True, null=True)
    nazvanie = models.CharField(max_length=255, db_column='Название', blank=True, null=True)
    data_vyhoda = models.DateField(db_column='Дата_выхода', blank=True, null=True)
    tsena = models.DecimalField(max_digits=10, decimal_places=2, db_column='Цена', blank=True, null=True)
    vozrastnoy_reyting = models.CharField(max_length=50, db_column='Возрастной_рейтинг', blank=True, null=True)
    razmer_igry = models.CharField(max_length=50, db_column='Размер_игры', blank=True, null=True)

    platformy = models.ManyToManyField(
        Platforma,
        through='IgryPoPlatformam',
        related_name='igry_na_platforme'
    )
    yazyki = models.ManyToManyField(
        Yazyk,
        through='IgryPoYazykam',
        related_name='igry_na_yazyke'
    )

    class Meta:
        managed = False
        db_table = 'Игра'
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return self.nazvanie if self.nazvanie else f'Игра #{self.nomer_igry}'


class ObnovlenieIgry(models.Model):
    nomer_obnovleniya = models.AutoField(primary_key=True, db_column='Номер_обновления')
    nomer_igry = models.ForeignKey(Igra, on_delete=models.SET_NULL, db_column='Номер_игры', blank=True, null=True)
    nomer_versii = models.CharField(max_length=50, db_column='Номер_версии', blank=True, null=True)
    data_obnovleniya = models.DateTimeField(db_column='Дата_обновления', blank=True, null=True)
    razmer_obnovleniya = models.CharField(max_length=50, db_column='Размер_обновления', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Обновление_игры'
        verbose_name = 'Обновление игры'
        verbose_name_plural = 'Обновления игры'

    def __str__(self):
        if self.nomer_igry and self.nomer_versii:
            return f'Обновление {self.nomer_versii} для {self.nomer_igry.nazvanie}'
        return f'Обновление #{self.nomer_obnovleniya}'


class Polzovatel(models.Model):
    nomer_polzovatelya = models.AutoField(primary_key=True, db_column='Номер_пользователя')
    imya = models.CharField(max_length=255, db_column='Имя', blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    parol = models.CharField(max_length=255, db_column='Пароль', blank=True, null=True)
    data_registratsii = models.DateTimeField(db_column='Дата_регистрации', blank=True, null=True)
    nomer_telefona = models.CharField(max_length=20, db_column='Номер_телефона', blank=True, null=True)
    data_rozhdeniya = models.DateField(db_column='Дата_рождения', blank=True, null=True)

    druzya = models.ManyToManyField(
        'self',
        through='SpisokDruzey',
        symmetrical=False,
        related_name='chleny_spiska_druzey'
    )

    class Meta:
        managed = False
        db_table = 'Пользователь'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.imya if self.imya else (self.email if self.email else f'Пользователь #{self.nomer_polzovatelya}')


class IgryPoPlatformam(models.Model):
    nomer_igry = models.ForeignKey(Igra, on_delete=models.DO_NOTHING, db_column='Номер_игры')
    nomer_platformy = models.ForeignKey(Platforma, on_delete=models.DO_NOTHING, db_column='Номер_платформы')

    class Meta:
        managed = False
        db_table = 'Игры_по_платформам'
        unique_together = (('nomer_igry', 'nomer_platformy'),)
        verbose_name = 'Игра на платформе'
        verbose_name_plural = 'Игры по платформам'

    def __str__(self):
        if self.nomer_igry and self.nomer_platformy:
            return f'Игра "{self.nomer_igry.nazvanie}" на "{self.nomer_platformy.nazvanie}"'
        return f'Связь Игры/Платформы (неопределена)'


class IgryPoYazykam(models.Model):
    nomer_igry = models.ForeignKey(Igra, on_delete=models.DO_NOTHING, db_column='Номер_игры')
    nomer_yazyka = models.ForeignKey(Yazyk, on_delete=models.DO_NOTHING, db_column='Номер_языка')

    class Meta:
        managed = False
        db_table = 'Игры_по_языкам'
        unique_together = (('nomer_igry', 'nomer_yazyka'),)
        verbose_name = 'Язык игры'
        verbose_name_plural = 'Игры по языкам'

    def __str__(self):
        if self.nomer_igry and self.nomer_yazyka:
            return f'Игра "{self.nomer_igry.nazvanie}" на языке "{self.nomer_yazyka.nazvanie}"'
        return f'Связь Игры/Языка (неопределена)'


class SpisokDruzey(models.Model):
    polzovatel_1 = models.ForeignKey(Polzovatel, on_delete=models.DO_NOTHING, db_column='Пользователь_1', related_name='friends_as_user1')
    polzovatel_2 = models.ForeignKey(Polzovatel, on_delete=models.DO_NOTHING, db_column='Пользователь_2', related_name='friends_as_user2')

    class Meta:
        managed = False
        db_table = 'Список_друзей'
        unique_together = (('polzovatel_1', 'polzovatel_2'),)
        verbose_name = 'Друг пользователя'
        verbose_name_plural = 'Список друзей'

    def __str__(self):
        if self.polzovatel_1 and self.polzovatel_2:
            return f'Дружба между {self.polzovatel_1.imya} и {self.polzovatel_2.imya}'
        return f'Дружба (неопределена)'