import scrapy

# Get all stats players in NBA season 2019-20
class NBATest(scrapy.Spider):
    name = 'Miranha'

    # If you want see more stats in previous season and the current you can put the link like that
    #  start_urls = ['https://www.basketball-reference.com/leagues/NBA_2019_per_game.html','https://www.basketball-reference.com/leagues/NBA_2020_per_game.html']

    # Where the data can found
    start_urls = ['https://www.basketball-reference.com/leagues/NBA_2019_per_game.html']

    def parse(self, response):
        all_players = response.xpath('//*[@id="per_game_stats"]/tbody/tr')

        for player in all_players:
            player_name = player.xpath('td[@data-stat="player"]/a/text()').get()
            player_team = player.xpath('td[@data-stat="team_id"]/a/text()').get()
            player_stats = player.xpath('td/text()').getall()

            yield{
                'Player Name': player_name,
                'Player Team': player_team,
                'Player Stats': player_stats
            }