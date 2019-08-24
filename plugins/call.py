from slackbot.bot import *

from . import options
from . import emoji


@respond_to('^create\s--text\s\S+(\s*--\S+\s\S+)*$')
def create(message, *args, **kwargs):
    opt = options.parse(message.body['text'])
    emoji.register(opt)

    message.reply('スタンプを作ったよ :' + opt['name'] + ':' + r'(`:' + opt['name'] +
                  r':`)')


@respond_to('^help$')
def help(message):
    message.reply(
        r'ヘルプだよ :point_right: `create --text 文字列 [--color 文字色 [--back_color 背景色] [--font フォント]]`'
    )


@respond_to('^help --color$')
def help_color(message):
    message.reply(r'色一覧だよ :point_right: `' + str(list(options.COLORS.keys())) +
                  r'`')


@respond_to('^help --font$')
def help_font(message):
    message.reply(r'フォント一覧だよ :point_right: `' + str(options.FONTS) + r'`')
