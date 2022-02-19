
from django.db import models


class MovieTitle (models.Model):
   title = models.CharField(max_length=200, null=True)

   def __str__(self):
       return self.title


class Category (models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    category = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.id}'



class Contestants(models.Model):
    class Meta:
        verbose_name_plural = "Contestants"

    name = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name



class Nominations(models.Model):
    class Meta:
        verbose_name_plural = "Nominations"

    parent_category = models.ForeignKey(MovieTitle, on_delete=models.CASCADE) 
    contestant = models.ForeignKey(Contestants, on_delete=models.CASCADE) 
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    nomination_code = models.CharField(max_length=100, null=True)
    vote_amount = models.DecimalField(max_digits=9, decimal_places=2, default=0)



    def __str__(self):
        return f"{self.contestant} | {self.nomination_code} | {self.parent_category} | {self.category} | {self.vote_amount}" 




# class Votes(models.Model):
#     class Meta:
#         verbose_name_plural = "Votes"

#     parent_category = models.ForeignKey(Nominations, related_name="parent_category_title", on_delete=models.CASCADE)
#     contestant = models.ForeignKey(Nominations, related_name="contestant_name", on_delete=models.CASCADE)
#     nomination_code = models.ForeignKey(Nominations, related_name="nominations", on_delete=models.CASCADE)
#     category = models.ForeignKey(Nominations, related_name="sub_category", on_delete=models.CASCADE)
#     vote_amount = models.DecimalField(max_digits=9, decimal_places=2, default=0)


#     def __str__(self):
#         return f"{self.contestant_code} | {self.vote_amount}" 

    


