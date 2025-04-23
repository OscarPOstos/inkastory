from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class StoryNode(models.Model):
    story = models.ForeignKey(Story, related_name='nodes', on_delete=models.CASCADE)
    text = models.TextField()
    option_a_text = models.CharField(max_length=255, blank=True, null=True)
    option_a_target = models.ForeignKey('self', related_name='from_option_a', null=True, blank=True, on_delete=models.SET_NULL)

    option_b_text = models.CharField(max_length=255, blank=True, null=True)
    option_b_target = models.ForeignKey('self', related_name='from_option_b', null=True, blank=True, on_delete=models.SET_NULL)

    is_ending = models.BooleanField(default=False)

    def __str__(self):
        return f'Node {self.id} in Story "{self.story.title}"'