import scrapy


class PokemonItem(scrapy.Item):
    ID=scrapy.Field()
    Name = scrapy.Field()
    Image = scrapy.Field()
    Type = scrapy.Field()
    Total = scrapy.Field()
    HP = scrapy.Field()
    Attack = scrapy.Field()
    Defense = scrapy.Field()
    Sp_Atk = scrapy.Field()
    Sp_Def = scrapy.Field()
    Speed = scrapy.Field()


class PokemonDbSpider(scrapy.Spider):
    name = "pokemon_db"
    allowed_domains = ["pokemondb.net"]
    start_urls = ["https://pokemondb.net/pokedex/all"]

    def parse(self, response):
        pokemon_id=response.xpath("//span[@class='infocard-cell-data']/text()").getall()
        image_src=response.xpath("//img[@class='img-fixed icon-pkmn']/@src").getall()
        names = response.xpath('//a[@class="ent-name"]/text()').getall()
        types = response.xpath("//td[@class='cell-icon']//a/text()").getall()
        totals = response.xpath('//td[@class="cell-num cell-total"]/text()').getall()
        hps = response.xpath("//tr/td[@class='cell-num'][1]/text()").getall()
        attacks = response.xpath("//tr/td[@class='cell-num'][2]/text()").getall()
        defenses = response.xpath("//tr/td[@class='cell-num'][3]/text()").getall()
        sp_atks = response.xpath("//tr/td[@class='cell-num'][4]/text()").getall()
        sp_defs = response.xpath("//tr/td[@class='cell-num'][5]/text()").getall()
        speeds = response.xpath("//tr/td[@class='cell-num'][6]/text()").getall()

        # Create PokemonItem objects and populate them with data
        for pokemon_id, image_src, name, type, total, hp, attack, defense, sp_atk, sp_def, speed in zip(
         pokemon_id, image_src, names, types, totals, hps, attacks, defenses, sp_atks, sp_defs, speeds
        ):
            item = PokemonItem()
            item['ID']=pokemon_id
            item["Image"]=image_src
            item["Name"] = name
            item["Type"] = type
            item["Total"] = total
            item["HP"] = hp
            item["Attack"] = attack
            item["Defense"] = defense
            item["Sp_Atk"] = sp_atk
            item["Sp_Def"] = sp_def
            item["Speed"] = speed

            yield item

        print('executed Successfuly!')
.