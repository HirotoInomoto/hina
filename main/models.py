from django.db import models

# Create your models here.
class Log(models.Model):
    start_date = models.DateField("いつから")
    end_date = models.DateField("いつまで")
    comment = models.CharField("コメント", max_length=500, null=True, blank=True)
    pub_date = models.DateTimeField("投稿日時", auto_now_add=True)
    delta = models.IntegerField("日数")
    # start_date_comment = models.CharField("いつから・コメント", max_length=300, null=True, blank=True)
    # end_date_comment = models.CharField("いつまで・コメント", max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.delta} - {self.comment}"