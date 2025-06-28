from django.db import models
from django.conf import settings


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título")
    description = models.TextField(blank=True, verbose_name="Descrição")
    completed = models.BooleanField(default=False, verbose_name="Concluída")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name="Usuário"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.user.name}"
    