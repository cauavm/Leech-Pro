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
/{RCLONE_COMMAND} : Mudar configurações do Drive (**BLOQUEADO**)
 
/{CLONE_COMMAND_G}: Este comando é usadado para clonear os arquivos ou pasta do Google Drive utilizando o Gclone
Sintaxe:- `[ID do arquivo ou da pasta][espaço][nome da sua pasta(se o ID é do arquivo, não coloque nada)]` e então responda /gclone.
 
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
 
Funciona apenas com links diretos e links do YouTube agora. É como você poder adicionar um prefixo customizado para o nome do arquivo original. Por exemplo, se eu arquivo é gk.txt, será o que você adicionar em CUSTOM_FILE_NAME + gk.txt

Funciona apenas com link direto/YouTube. Não funciona com Magnet Link ou Arquivo Torrent.

E também adicinou nomes personalizados, como...
 
Você deve passar o link como www.download.me/gk.txt | novo.txt

o arquivo será upado como novo.txt
 
/{SAVE_THUMBNAIL}: Utilize em resposta a uma Foto para salvar como uma Thumbnail Personalizada.

/{CLEAR_THUMBNAIL}: Limpar Thumbnails Personalizadas salvas.

/{TOGGLE_VID}: Fazer o upload do arquivo como Streamável

/{TOGGLE_DOC}: Fazer o upload do arquivo como Documento

**Como utilizar....?**
__Envie qualquer um dos comandos disponíveis como resposta para um link/magnet/torrent. 👊__

**Modo de Upload atual:** `{utxt}`

""",
        disable_web_page_preview=True,
    )
