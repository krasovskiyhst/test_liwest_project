from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class CategoriesOfProduct(models.Model):
    name = models.CharField(max_length=200)
    seq = models.IntegerField(default=0)

    class Meta:
        ordering = ['seq']

    def save(self, *args, **kwargs):
        try:
            last_group = CategoriesOfProduct.objects.latest('seq')
            last_big_value_seq = last_group.seq
            if self.seq <= last_big_value_seq and self.seq != 0:
                # Если новое значение seq меньше или равно самому большому seq в БД,
                # и не является default, то у всех объектов, где seq >= прибавляем 1 к полю seq
                groups_with_field_seq_greater_than_new_seq = CategoriesOfProduct.objects.filter(seq__gte=self.seq)
                for group in groups_with_field_seq_greater_than_new_seq:
                    group.seq += 1
                CategoriesOfProduct.objects.bulk_update(groups_with_field_seq_greater_than_new_seq, fields=['seq'])

            if self.seq == 0:
                # Если seq не выбран (default), то ставим значение на 1 больше, чем у самого большего seq в БД
                self.seq = last_big_value_seq + 1
        except ObjectDoesNotExist:
            # Если пока нет ни одного объекта, то просто сохраняем
            pass

        super(CategoriesOfProduct, self).save(*args, **kwargs)


class GroupsOfProduct(models.Model):
    category_id = models.ForeignKey(CategoriesOfProduct, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    seq = models.IntegerField(default=0)

    class Meta:
        ordering = ['seq']

    def save(self, *args, **kwargs):
        try:
            last_group = GroupsOfProduct.objects.latest('seq')
            last_big_value_seq = last_group.seq
            if self.seq <= last_big_value_seq and self.seq != 0:
                # Если новое значение seq меньше или равно самому большому seq в БД,
                # и не является default, то у всех объектов, где seq >= прибавляем 1 к полю seq
                groups_with_field_seq_greater_than_new_seq = GroupsOfProduct.objects.filter(seq__gte=self.seq)
                for group in groups_with_field_seq_greater_than_new_seq:
                    group.seq += 1
                GroupsOfProduct.objects.bulk_update(groups_with_field_seq_greater_than_new_seq, fields=['seq'])

            if self.seq == 0:
                # Если seq не выбран (default), то ставим значение на 1 больше, чем у самого большего seq в БД
                self.seq = last_big_value_seq + 1
        except ObjectDoesNotExist:
            # Если пока нет ни одного объекта, то просто сохраняем
            pass

        super(GroupsOfProduct, self).save(*args, **kwargs)


class Product(models.Model):
    group_id = models.ForeignKey(GroupsOfProduct, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    hidden = models.BooleanField()
