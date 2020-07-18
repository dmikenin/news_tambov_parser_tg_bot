# News Tambov - Telegram bot
Bot with parser, which get news form Tambov newspapers. I used aiogram for async functions and in future, i will optimize load on my bot and increase speed answer.
So, i used library beautifulsoup for parsing sites, where not js or another difficult web-elements, in the next step i will use lib Selenuim.
And i used redis, like storage from last article and always give users unique news (ttl article 1 day, because user see news morning and evening)
For development, i used pattern Facade, because in future i will use many parsers and we have one call for any work.


## Requirements
- aiogram==2.9.2
- requests==2.24.0
- beautifulsoup4==4.9.1
- lxml==4.5.1
- redis==3.5.3

## Installing
```
git clone form GitHub
Create config.py and add setting
python main.py
```
## Next step
Add new parser

Clean static attribute from classes and transfer attribute in init method (early i did static attribute, because was problem with python env in Linux)

## Author
**Denis Mikenin** - *Backend/flutter developer* -
    [my web-site](https://mikenin.com)



