from django.db import models



# Класс для создания размеры пиццы
class Size(models.Model):
    size=models.IntegerField(verbose_name="Размеры")
    def __str__(self):
        return str(self.size)
    class Meta:
        ordering = ['id']
        verbose_name='Размеры пиццы'
        verbose_name_plural='Размеры пиццы'

# Класс для создания Типа пиццы
class Type(models.Model):
    type_of_pizza=models.CharField(max_length=50,verbose_name="Тип пиццы")
    def __str__(self):
        return "{}".format(self.type_of_pizza)
    class Meta:
        ordering = ['id']
        verbose_name='Тип пиццы'
        verbose_name_plural='Тип пиццы'



# Класс для создания самой Пиццы
class Pizza(models.Model):
    imageUrl=models.ImageField(verbose_name='Изображения')
    name=models.CharField(max_length=255,verbose_name='Название')
    types=models.ManyToManyField(Type,verbose_name='Тип',related_name="typesOfpizzas")
    sizes=models.ManyToManyField(Size,verbose_name='Размеры',related_name="sizeOfpizza")
    price=models.IntegerField(verbose_name='Цена')
    category=models.IntegerField(verbose_name='Категория') 
    rating=models.IntegerField(verbose_name='рейтинг')


    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['id']
        verbose_name='Пиццы'
        verbose_name_plural='Пиццы'

