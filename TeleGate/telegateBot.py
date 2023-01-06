from telegram.ext import Updater, CommandHandler, MessageHandler, ChatJoinRequestHandler
import contractWrapper as contract

# Your bot's token
bot_token = 'Bot token goes here'

# send user list of commands 
def menu(update, context):
    commands = "/myID - Get your user ID\n\n"\
               "/chatID - Get the current chatID\n\n"\
               "/join <Chat Tag> - Get invite link\n\n"\
               "/check <Chat Tag> - Check chat tag availability\n\n"\
               "/price <Chat Tag> - Check a group's join price"      
    update.message.reply_text(commands)

# send user an invite link when /join command is used
def invite(update, context):
    # case for missing chat tag
    if(not context.args):
        errorMessege = "Missing chat tag!\nCorrect usage: /join <Chat Tag>"
        update.message.reply_text(errorMessege)
    else:
        # fetch private chat link from smart contract
        link = contract.getLink(context.args[0])
        # if chat tag is invalid notify user
        if(not link):
            link = "Invalid chat tag!"
        # send reply message
        update.message.reply_text(link)

# send user price of specified chat
def priceCheck(update, context):
    # case for missing chat tag
    if(not context.args):
        errorMessege = "Missing chat tag!\nCorrect usage: /price <Chat Tag>"
        update.message.reply_text(errorMessege)
    else:
        # check if chat exists
        if(contract.isChatTagActive(context.args[0])):
            update.message.reply_text(contract.getPrice(context.args[0]))
        else:
            update.message.reply_text("Chat not found!")

# send user the availability status of a chat tag
def tagCheck(update, context):
    # case for missing chat tag
    if(not context.args):
        errorMessege = "Missing chat tag!\nCorrect usage: /check <Chat Tag>"
        update.message.reply_text(errorMessege)
    else:
        # fetch status from smart contract
        status = contract.isChatTagActive(context.args[0])
        # case for unavailable tag
        if(status):
            message = "Tag unavailable \U0000274C"
        # case for available tag
        else:
            message = "Tag available \U00002705"
        # send reply message
        update.message.reply_text(message)

def userID(update, context):
    # send user their telegram user ID when /myID is called
    update.message.reply_text(update.effective_user.id)

def chatID(update, context):
    # send user the current telegram chat ID when /chatID is called
    update.message.reply_text(update.effective_chat.id)
    
def handleRequest(update, context):
    # check if group is registered
    if(contract.isChatIdActive(str(update.effective_chat.id))):
            # accept user request if subscribed
            if(contract.getSubStatus(str(update.effective_chat.id), str(update.effective_user.id))):
                context.bot.approve_chat_join_request(
                    chat_id=update.effective_chat.id, user_id=update.effective_user.id)
            # decline user request if user not subscribed
            else:
                context.bot.decline_chat_join_request(
                chat_id=update.effective_chat.id, user_id=update.effective_user.id)

def main():
    # Pass your bot token to the updater
    updater = Updater(bot_token, use_context=True)
    # on command '/start' or '/help' call menu()
    updater.dispatcher.add_handler(CommandHandler("start", menu))
    updater.dispatcher.add_handler(CommandHandler("help", menu))
    # on command '/join' call join()
    updater.dispatcher.add_handler(CommandHandler("join", invite))
    # on command '/check' call tagCheck()
    updater.dispatcher.add_handler(CommandHandler("check", tagCheck))
    # on command '/price' call priceCheck()
    updater.dispatcher.add_handler(CommandHandler("price", priceCheck))
    # on command '/myID' call userID()
    updater.dispatcher.add_handler(CommandHandler("myid", userID))
    # on command '/chatID' call userID()
    updater.dispatcher.add_handler(CommandHandler("chatid", chatID))
    # on new join request, call handleRequest()
    updater.dispatcher.add_handler(ChatJoinRequestHandler(handleRequest))
    # Start the Bot
    updater.start_polling()
    # Keep the bot in idle state
    updater.idle()

if __name__ == '__main__':
    main()