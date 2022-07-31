from django.contrib import admin

from market.models import NewsMarket


class NewsMarketAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'author')


admin.site.register(NewsMarket, NewsMarketAdmin)
