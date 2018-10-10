from django.db import models


# programming_languages table
class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


# languages table
class Language(models.Model):
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ["code"]


# developers table
class Developer(models.Model):
    email = models.CharField(max_length=40)
    programming_languages = models.ManyToManyField(ProgrammingLanguage)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.email

    def get_programming_languages(self):
        return ', '.join([p.name for p in self.programming_languages.all()])

    def get_languages(self):
        return ', '.join([l.code for l in self.languages.all()])

    class Meta:
        ordering = ["pk"]


class SearchDeveloper(models.Model):

    @staticmethod
    def get_selected_developers_with_programming_languages(p_languages):

        developers = Developer.objects

        for i in p_languages:
            developers = developers.filter(programming_languages=ProgrammingLanguage.objects.filter(name__iexact=i).get().id)

        return developers.distinct()

    @staticmethod
    def get_selected_developers_with_languages(languages):

        lang_ids = list()
        for i in languages:
            lang_ids.append(Language.objects.filter(code__icontains=i).get().id)

        return Developer.objects.filter(languages__in=lang_ids).distinct()

    @staticmethod
    def get_selected_developers(programming_languages, languages):

        if len(programming_languages) > 0 and len(languages) > 0:
            return SearchDeveloper.get_selected_developers_with_programming_languages(
                programming_languages).filter(
                id__in=[dev.id for dev in SearchDeveloper.get_selected_developers_with_languages(languages)])

        elif len(programming_languages) > 0 :
            return SearchDeveloper.get_selected_developers_with_programming_languages(
                programming_languages)

        elif len(languages) > 0:
            return SearchDeveloper.get_selected_developers_with_languages(
                languages)

        return list()
