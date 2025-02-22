import requests
from bs4 import BeautifulSoup

# Example function to fetch player count from MMO Populations
def fetch_mmo_population():
    url = 'https://mmo-population.com/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Locate the section containing the top MMORPGs
        top_mmos_section = soup.find('div', class_='top-mmos')
        if top_mmos_section:
            games = top_mmos_section.find_all('div', class_='game')
            for game in games[:30]:  # Limit to top 30 games
                name = game.find('div', class_='game-name').text.strip()
                player_count = game.find('div', class_='player-count').text.strip()
                print(f'{name}: {player_count}')
        else:
            print('Top MMOs section not found.')
    else:
        print(f'Failed to retrieve data. Status code: {response.status_code}')

# Example function to fetch player count using BattleMetrics API
def fetch_battlemetrics_data():
    url = 'https://api.battlemetrics.com/games'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for game in data['data'][:30]:  # Limit to top 30 games
            name = game['attributes']['name']
            player_count = game['attributes']['players']
            print(f'{name}: {player_count} players online')
    else:
        print(f'Failed to retrieve data. Status code: {response.status_code}')

# Main function to execute the data fetching
def main():
    print('Fetching data from MMO Populations...')
    fetch_mmo_population()
    print('\nFetching data from BattleMetrics...')
    fetch_battlemetrics_data()

if __name__ == '__main__':
    main()
