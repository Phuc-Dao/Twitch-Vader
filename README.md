<p align="center">
  <a href="client/img/dotino.png">
    <img src="/static/Blue_Robot.png" height="200" />
  </a>

</p>

&nbsp;
# Twitch-Vader
>Measures sentiment from twitch viewers using Vaders sentiment analysis \


Basic Lexicon contains following values:

    '<3': 0.4,
    '4head': 1,
    'babyrage': -0.7,
    'biblethump': -0.7,
    'blessrng': 0.3,
    'bloodtrail': 0.7,
    'coolstorybob': -1,
    'residentsleeper': -1,
    'kappa': -0.3,
    'lul': -0.3,
    'pogchamp': 1.5,
    'heyguys': 1,
    'wutface': -1.5,
    'kreygasm': 1,
    'seemsgood': 0.7,
    'kappapride': 0.7,
    'feelsgoodman': 1,
    'notlikethis': -1
    
Chat messages are logged to chat_log.log, along with a sentiment rating for each message in the format "#channel [sentiment] user: message" eg:\
`[DEBUG] twitch: #beyondthesummit: [-0.6037] hayashidayuki: RIGGED GAME BibleThump` 

## Installation
Requires python3 and python3-pip. Instructions are written for Ubuntu 16.04 command line
- Install requirements `sudo pip3 install -r /path/to/project/requirements.txt`
- Run migrations `python3 /path/to/project/manage.py migrate`
- Runserver `python3 /path/to/project/manage.py runserver --noreload`

## Commands

All commands that can be called from chat via different calls. Note that some commands can only be called by Moderators, Trusted-Moderators or Bot-Admins. Chat games can also be started by regular users, if they have spam points to pay for it.

### All-User commands:

| Command               | Description           | Examples  |
| --------------------- | --------------------- | --------- |
| `!active`             | Returns the amount of active viewers in chat. | - |
| `!smorc`              | Returns a random SMOrc quote. | - |
| `!quote [<number>]`   | Returns a random quote. Optional a number can be given to call a specific quote. | `!quote` , `!quote 2` |
| `!slap <user>`        | Sends a slap to another user. | `!slap Monkalot` |
| `!hug <user>`         | Sends a hug to another user. | `!hug Monkalot` |
| `!pjsalt`             | Sends a pjsalt pyramid in chat.      | - |
| `!call <emote> <text>`| Sends a call interlaced by an emote. All Twitch- and BTTV-emotes and emojis are supported. | `!call Kappa a nice stream` |
| `!any <emote> <text>` | Sends out any sentence interlaced by an emote. All Twitch- and BTTV-emotes and emojis are supported. | `!any Jebaited Long have we waited, now we Jebaited` |
| `!word <emote> <text>`| Sends a word with an emote interlaced between letters. All Twitch- and BTTV-emotes and emojis are supported. | `!word monkaS dragons` |
| `!rank [<username>]`  | Returns the current spam-rank and -points for the chatter or optional for a specific <username>. | `!rank` , `!rank monkalot` |
| `!topspammers`        | Returns the five highest ranked spammers. | - |
| `!kpm`                | Returns the amount of Kappas per minute in channel. | - |
| `!tkp`                | Returns the total amount of Kappas in channel. | - |
| `!minute <emote>`     | Returns the amount of a specific emote per minute in channel. All Twitch- and BTTV-emotes and emojis are supported. | `!minute BabyRage` |
| `!total <emote>`      | Returns the total amount of a specific emote in channel. All Twitch- and BTTV-emotes and emojis are supported. | `!total EleGiggle` |
| `!oralpleasure on/off`  | Turns oralpleasure on or off. | - |
| `!calc <formula>`       | A chat calculator that can do some pretty advanced stuff like sqrt and trigonometry. | `!calc (5+7)/2` , <br>`!calc log(5^2) + sin(pi/4)` |
| `<botname> <text>`      | Talk to the bot. Questions can be asked or a conversation can be started with the native speech engine. | `Hey Monkalot, how are you doing?`, `What's 2Head + 2Head? @Monkalot` |
| `[<hearthstone card>]` | Get some information about a hearthstone card. Allows up to two spelling mistakes. | `[Malganis]` |

### Moderator commands:

| Command               | Description           | Examples  |
| --------------------- | --------------------- | --------- |
| `!addquote <quote>`   | Adds a quote to the *quotelist*. | `!addquote "Priest in 2k17 LUL"` |
| `!delquote <quote>`   | Deletes a quote from the *quotelist*. | `!delquote "Priest in 2k17 LUL"` |
| <nobr>`!block on/off`</nobr>     | Turns pyramidblock on or off. If on, pyramids will be interupted by the bot. | - |
| <nobr>`!games on/off`</nobr>     | Turns automatic games on or off. If on, *chatgames* will start automaticly after a certain amount of time. | - |

### Trusted-Moderator commands:

| Command               | Description           | Examples  |
| --------------------- | --------------------- | --------- |
| `!sleep`    			| Puts the bot in *sleepmode*. All games will be disabled and the bot only responses to admins | - |
| `!wakeup`    			| Puts the in normal mode again. | - |
| `!addcommand <command> <response>` | Adds a command to the *simplereply*-list. | `!addcommand !ping pong` |
| `!delcommand <command>`| Deletes a command from the *simplereply*-list. | `!delcommand !ping` |
| `!replylist`          | Returns all available commands from the *simplereply*-list. | - |

### Admin commands:

| Command               | Description           | Examples  |
| --------------------- | --------------------- | --------- |
| `!addmod <username>`  | Adds a mod to the list of *trusted mods*. | `!addmod Monkalot` |
| `!delmod <username>`  | Deletes a mod from the list of *trusted mods*. | `!delmod Monkalot` |
| `!g <username> <pronouns>` | Allows changing gender pronouns for a user. Three pronouns have to be given. | `!g monkalot she her hers` |

## How to "Run" 

Twitch Disposition is not compiled into an executable. The best way to run the program is to open the "src" folder in your Python IDE of choice. From here there are three steps to get the program running. 

1. Edit the "CHANNEL" variable "Settings.py" file to match the twitch streamer whose chat room you would like to analyze. NOTE the channel name needs to be in all lowercase. 
2. Ensure you have all the dependent packages for your Python Interpreter (PyQt5, nltk, numpy).
3. Run the "Run.py" file. 

When you are finished stop the script through your Python IDE. 

### VADER

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. It is fully open-sourced under the [MIT License](http://choosealicense.com/).

### Natural Language Toolkit (NLTK)

[NLTK](http://www.nltk.org/) is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.

Thanks to a hands-on guide introducing programming fundamentals alongside topics in computational linguistics, plus comprehensive API documentation, NLTK is suitable for linguists, engineers, students, educators, researchers, and industry users alike. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project.

#### Contributing

Anyone is welcome to re-use the code used in this project.

#### References

* [Python](https://www.python.org/)
* [Twitch API](https://dev.twitch.tv/)
* [NLTK](http://www.nltk.org/)
* [VADER](https://github.com/cjhutto/vaderSentiment)
* [PyQtGraph](http://www.pyqtgraph.org/)
