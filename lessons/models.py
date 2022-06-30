from django.db import models
from django.utils.text import slugify

class Base(models.Model):
    create = models.DateTimeField(auto_now_add=True, verbose_name='Data da criação')
    update = models.DateTimeField(auto_now=True, verbose_name='Data da atualizção')
    isActive = models.BooleanField(default=True, verbose_name='Ativo?')

    class Meta:
        abstract = True


class Teacher(Base):
    teacher = models.CharField(max_length=255, unique=True, verbose_name='Professor(a)')
    image_url = models.URLField(verbose_name='Image URL')
    
    class Meta:
        verbose_name = 'Professor(a)'
        verbose_name_plural = 'Professores(a)'

    def __str__(self):
        return self.teacher

class Lesson(Base):
    type = (
        ('AO VIVO', 'AO VIVO'),
        ('AULA PRÁTICA', 'AULA PRÁTICA')
    )

    title = models.CharField(max_length=255, verbose_name='Titulo', unique=True)
    date = models.DateTimeField()
    description = models.TextField(verbose_name='Descrição')
    slug = models.SlugField(max_length=255, verbose_name='Slug', unique=True, blank=True, null=True)
    #video_id = models.CharField(max_length=255, verbose_name='Video ID')
    lesson_type = models.CharField(choices=type, max_length=20, verbose_name='Tipo da aula')
    teacher = models.ForeignKey(Teacher, verbose_name='teacher_info', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
            
    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'

    def __str__(self):
        return self.title


