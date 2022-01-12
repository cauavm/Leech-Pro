import logging

import pyrogram
from tobrot import *

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(
            f"""<b>🙋🏻‍♂️ Olá!\n\n Esse é um bot de downloads do @animezey. O uso do bot é permitido apenas no grupo.</b>\n\n<b>Current CHAT ID: <code>{message.chat.id}</code>""",
            parse_mode="html",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Channel', url='https://t.me/animezey')
                    ]
                ]
               )
            )
        # leave chat
        await client.leave_chat(chat_id=message.chat.id, delete=True)
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    if UPLOAD_AS_DOC:
        utxt = "Document"
    else:
        utxt = "Streamable"
    await message.reply_text(
        f"""Comandos disponíveis
/{RCLONE_COMMAND} : This will change your drive config on fly.(First one will be default)
 
/{CLONE_COMMAND_G}: This command is used to clone gdrive files or folder using gclone.
Syntax:- `[ID of the file or folder][one space][name of your folder only(If the id is of file, don't put anything)]` and then reply /gclone to it.
 
/{LOG_COMMAND}: Gerar logs.
 
/{YTDL_COMMAND}: Este comando deve ser usado em resposta a um link suportado.
 
/{PYTDL_COMMAND}: Baixar vídeos de uma playlist do YouTube e fazer o upload para o Telegram.
 
/{GYTDL_COMMAND}: Baixar e fazer o upload para o Google Drive.
 
/{GPYTDL_COMMAND}: Baixar playlist do YouTube e fazer o upload para o Google Drive.
 
/{LEECH_COMMAND}: Este comando deve ser usado em resposta a um Magnet Link, link de Torrent, ou link direto. [Irá gerar SPAM no chat e enviar os downloads como arquivos separados, se houver mais de um arquivo.].
 
/{LEECH_ZIP_COMMAND}: Este comando deve ser usaddo em resposta a um Magnet Link, link de Torrent, ou link direto. [Irá criar um arquivo .tar.gz na saída do diretório e enviar os arquivos no chat, dividido em partes de 1024MiB cada, devido a limitações do Telegram]
 
/{GLEECH_COMMAND}: Este comando deve ser usado em resposta a um Magnet Link, link de Torrent, ou link direto. Irá baixar os arquivos do link ou torrent enviado e irá fazer o upload para o Google Drive usando o Rclone.
 
/{GLEECH_ZIP_COMMAND} Este comando irá comprimir a pasta/arquivo e fazer o upload para o Google Drive.
 
/{LEECH_UNZIP_COMMAND}: Descompactar o arquivo e fazer o upload para o Telegram.
 
/{GLEECH_UNZIP_COMMAND}: Descompactar o arquivo e fazer o upload para o Google Drive.
 
/{TELEGRAM_LEECH_COMMAND}: Fazer um Mirror do arquivo do Telegram para o Google Drive.
 
/{TELEGRAM_LEECH_UNZIP_COMMAND}: Descompactar arquivo do Telegram e fazer o upload para o Google Drive.
 
/{GET_SIZE_G}: Mostrar o tamanho total da pasta no Google Drive.
 
/{RENEWME_COMMAND}: Deletar os downloads restantes que não estão sendo deletados após o arquivo ser uplado ou após o comando /cancel
 
/{CANCEL_COMMAND_G} [GID]: para cancelar o seu download.

/{RENAME_COMMAND}: Renomear arquivos do Telegram.
 
Only work with direct link and youtube link for nowIt is like u can add custom name as prefix of the original file name. Like if your file name is gk.txt uploaded will be what u add in CUSTOM_FILE_NAME + gk.txt
 
Only works with direct link/youtube link.No magnet or torrent.
 
And also added custom name like...
 
You have to pass link as www.download.me/gk.txt | new.txt
 
the file will be uploaded as new.txt.
 
/{SAVE_THUMBNAIL}: Utilize em resposta a uma Foto para salvar como uma Thumbnail Personalizada.

/{CLEAR_THUMBNAIL}: Limpar Thumbnails Personalizadas salvas.

/{TOGGLE_VID}: Fazer o upload do arquivo como Streamável

/{TOGGLE_DOC}: Fazer o upload do arquivo como Documento

**How to Use....?**
__Send any one of the available command, as a reply to a valid link/magnet/torrent. 👊__

**Current Custom Upload Mode:** `{utxt}`

""",
        disable_web_page_preview=True,
    )
