from django.db import models


class CSPReport(models.Model):
    document_uri = models.URLField()
    referrer = models.URLField()
    blocked_uri = models.URLField()
    # 其他您希望记录的字段

    def __str__(self):
        return f"CSP Report - {self.document_uri}"
