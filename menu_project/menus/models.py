from django.db import models


class Node(models.Model):
    '''Node model'''
    text = models.CharField(max_length=250, verbose_name='Текст пункта')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True,
        verbose_name='Родитель'
    )

    def __str__(self):
        return self.text

    @property
    def level(self):
        if not self.parent:
            return 0
        return self.parent.level + 1

    def get_ancestors(self, node):
        current_parent = node.parent
        ancestors = []
        while current_parent:
            ancestors = self.get_ancestors(current_parent)
            ancestors.append(current_parent)
            return ancestors
        return ancestors

    def get_root(self, node):
        root = ''
        while node.parent:
            root = node.parent
            return root
        return root

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункт'
