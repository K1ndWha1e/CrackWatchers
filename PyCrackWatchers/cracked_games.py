import requests
from calculations import cracked_date_after

main_url = 'https://api.crackwatch.com/api/games?'


class Cracked_games:
    def __init__(self, page=0, count=0, sort_by='release_date', is_aaa='false'):

        url = f'{main_url}page={page}&sort_by={sort_by}&is_aaa={is_aaa}' \
            f'&is_cracked=true&is_released=true'
        print(url)
        result = requests.get(url).json()
        self.game_info = result[count]
        print(self.game_info)
        self.status = 'CRACKED'

    def get_title(self):
        return self.game_info['title']

    def get_slug(self):
        #doesnt matter
        pass

    def get_release_date(self):
        return self.game_info['releaseDate'][:10]

    def get_protection(self):
        return ''.join(self.game_info['protections'])

    def get_version(self):
        return self.game_info['versions']

    def get_image(self):
        return self.game_info['image']

    def get_poster(self):
        return self.game_info['imagePoster']

    def get_crack_date(self):
        return self.game_info['crackDate'][:10]

    def is_aaa(self):
        return self.game_info['isAAA']

    def get_comments_count(self):
        return self.game_info['commentsCount']

    def get_followers_count(self):
        return self.game_info['followersCount']

    @property
    def get_scene_group(self):
        return ''.join(self.game_info['groups'])

    def get_url(self):
        return self.game_info['url']

    def get_status(self):
        return self.status

    def get_cracked_after(self):
        return cracked_date_after(Cracked_games.get_crack_date(self), Cracked_games.get_release_date(self))

    def get_price(self):
        try:
            return f"${self.game_info['steamPrice']}"
        except KeyError:
            return 'N/A'

    def get_id(self):
        return self.game_info['_id']


info = Cracked_games(count=4, is_aaa='true')
print(info.get_title())
print(info.get_release_date())
print(info.get_protection())
print(info.get_version())
print(info.get_image())
print(info.get_poster())
print(info.get_crack_date())
print(info.is_aaa())
print(info.get_comments_count())
print(info.get_followers_count())
print(info.get_scene_group)
print(info.get_url())
print(info.get_status())
print(info.get_cracked_after())
print(info.get_id())