import tkinter
import tkinter.messagebox
import customtkinter
import contractWrapper as contract

# setting interface appearance and theme
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("TeleGate")
        self.geometry(f"{1100}x{680}")
        self.resizable(width=False, height=False)

        # configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # create sidebar frame with navigation widgets
        self.telegate = customtkinter.CTkLabel(self, text="TeleGate", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.telegate.grid(row=0, column=0, padx=20, pady=(20, 20))
        self.subscribe = customtkinter.CTkButton(self, height=70, text="Subscribe", 
            font=customtkinter.CTkFont(size=20), command=self.subscribeTab)
        self.subscribe.grid(row=1, column=0, padx=20, pady=10, sticky=customtkinter.N)
        self.groupSetup = customtkinter.CTkButton(self, height=70, text="Group Setup", 
            font=customtkinter.CTkFont(size=20), command=self.setupTab)
        self.groupSetup.grid(row=2, column=0, padx=20, pady=10, sticky=customtkinter.N)
        self.groupSettings = customtkinter.CTkButton(self, height=70, text="Group Settings", 
            font=customtkinter.CTkFont(size=20), command=self.settingsTab)
        self.groupSettings.grid(row=3, column=0, padx=20, pady=10, sticky=customtkinter.N)
        self.groupLookup = customtkinter.CTkButton(self, height=70, text="Group Lookup", 
            font=customtkinter.CTkFont(size=20), command=self.lookupTab)
        self.groupLookup.grid(row=4, column=0, padx=20, pady=10, sticky=customtkinter.N)

        # frame for subscribe tab
        self.subscribeFrame = customtkinter.CTkFrame(self, width=880, corner_radius=0)
        self.subscribeFrame.grid(row=0, column=1, rowspan=6, sticky="nsew")

        # subscribe tab layout
        self.subTitle = customtkinter.CTkLabel(self.subscribeFrame, text="Subscribe to a group", font=customtkinter.CTkFont(size=30))
        self.subTitle.grid(row=0, column=1, padx=(90,0), pady=(40, 0), sticky=customtkinter.NW)
        self.subInfo = customtkinter.CTkLabel(self.subscribeFrame, 
            text="Wallet Address - Wallet address to complete transaction with\n\n"\
                 "Wallet Key - Private key corresponding to wallet address\n\n"\
                 "Chat Tag - Chat tag of group to subscribe to\n\n"\
                 "User ID - User ID of member to be added to group (retrieved from @TeleGateBot)", 
            justify=customtkinter.LEFT, font=customtkinter.CTkFont(size=18))
        self.subInfo.grid(row=1, column=1, padx=(90,0), pady=(50, 50), sticky=customtkinter.SW)
        self.walletEntry_s = customtkinter.CTkEntry(self.subscribeFrame, height=40, width=350, placeholder_text="Wallet Address")
        self.walletEntry_s.grid(row=2, column=1, columnspan=1, padx=(90,0), pady=10, sticky=customtkinter.NW)
        self.keyEntry_s = customtkinter.CTkEntry(self.subscribeFrame, height=40, width=350, placeholder_text="Wallet Key")
        self.keyEntry_s.grid(row=2, column=1, columnspan=1, padx=(460,0), pady=10, sticky=customtkinter.NE)
        self.chatTag_s = customtkinter.CTkEntry(self.subscribeFrame, height=40, width=350, placeholder_text="Chat Tag")
        self.chatTag_s.grid(row=3, column=1, columnspan=1, padx=(90,0), pady=(20, 0), sticky=customtkinter.SW)
        self.userID_s = customtkinter.CTkEntry(self.subscribeFrame, height=40, width=350, placeholder_text="User ID")
        self.userID_s.grid(row=3, column=1, columnspan=1, padx=(460,0), pady=(20, 0), sticky=customtkinter.SE)
        self.subscribeButton = customtkinter.CTkButton(self.subscribeFrame, text="Subscribe", width=150, height=60,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callSubscribe)
        self.subscribeButton.grid(row=4, column=1, padx=(90, 20), pady=(55, 10), sticky=customtkinter.NW)

        # frame for group setup/initialization tab
        self.setupFrame = customtkinter.CTkFrame(self, width=880, corner_radius=0)

        # group setup tab layout
        self.setupTitle = customtkinter.CTkLabel(self.setupFrame, text="Setup TeleGate for a Telegram group", font=customtkinter.CTkFont(size=30))
        self.setupTitle.grid(row=0, column=1, padx=(90,0), pady=(40, 0), sticky=customtkinter.NW)
        self.setupInfo = customtkinter.CTkLabel(self.setupFrame, 
            text="Wallet Address - Wallet address to complete transaction with\n\n"\
                 "Wallet Key - Private key corresponding to wallet address\n\n"\
                 "Chat Tag - A custom chat tag for your group\n\n"\
                 "Chat ID -  Chat ID of your group (retrieved from @TeleGateBot)\n\n"\
                 "Link - Telegram invite link for your group\n\n"\
                 "Price - Group entry price (BNB)", 
            justify=customtkinter.LEFT, font=customtkinter.CTkFont(size=18))
        self.setupInfo.grid(row=1, column=1, padx=(90,0), pady=(30, 30), sticky=customtkinter.SW)
        self.walletEntry_i = customtkinter.CTkEntry(self.setupFrame, height=40, width=350, placeholder_text="Wallet Address")
        self.walletEntry_i.grid(row=2, column=1, columnspan=1, padx=(90,0), pady=10, sticky=customtkinter.NW)
        self.keyEntry_i = customtkinter.CTkEntry(self.setupFrame, height=40, width=350, placeholder_text="Wallet Key")
        self.keyEntry_i.grid(row=2, column=1, columnspan=1, padx=(460,0), pady=10, sticky=customtkinter.NE)
        self.chatTag_i = customtkinter.CTkEntry(self.setupFrame, height=40, width=350, placeholder_text="Chat Tag")
        self.chatTag_i.grid(row=3, column=1, columnspan=1, padx=(90,0), pady=10, sticky=customtkinter.SW)
        self.chatID_i = customtkinter.CTkEntry(self.setupFrame, height=40, width=350, placeholder_text="Chat ID")
        self.chatID_i.grid(row=3, column=1, columnspan=1, padx=(460,0), pady=10, sticky=customtkinter.SE)
        self.link_i = customtkinter.CTkEntry(self.setupFrame, height=40, width=350, placeholder_text="Link")
        self.link_i.grid(row=4, column=1, columnspan=1, padx=(90,0), pady=10, sticky=customtkinter.SW)
        self.price_i = customtkinter.CTkEntry(self.setupFrame, height=40, width=350, placeholder_text="Price")
        self.price_i.grid(row=4, column=1, columnspan=1, padx=(460,0), pady=10, sticky=customtkinter.SE)
        self.setupButton = customtkinter.CTkButton(self.setupFrame, text="Setup", width=150, height=60,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callInitialize)
        self.setupButton.grid(row=5, column=1, padx=(90, 20), pady=(25, 10), sticky=customtkinter.NW)

        # frame for group settings/configurations tab
        self.settingsFrame = customtkinter.CTkFrame(self, width=880, corner_radius=0)

        # group settings tab layout
        self.settingsTitle = customtkinter.CTkLabel(self.settingsFrame, text="Manage your TeleGate group", 
            font=customtkinter.CTkFont(size=30))
        self.settingsTitle.grid(row=0, column=1, padx=(90,0), pady=40, sticky=customtkinter.NW)
        self.walletEntry_c = customtkinter.CTkEntry(self.settingsFrame, height=40, width=350, placeholder_text="Wallet Address")
        self.walletEntry_c.grid(row=1, column=1, columnspan=1, padx=(90,0), pady=(10, 25), sticky=customtkinter.NW)
        self.keyEntry_c = customtkinter.CTkEntry(self.settingsFrame, height=40, width=350, placeholder_text="Wallet Key")
        self.keyEntry_c.grid(row=1, column=1, columnspan=1, padx=(460,0), pady=(10, 25), sticky=customtkinter.NE)
        self.chatTag_c = customtkinter.CTkEntry(self.settingsFrame, height=40, width=720, placeholder_text="Chat Tag")
        self.chatTag_c.grid(row=1, column=1, columnspan=1, padx=(90,0), pady=(90, 10), sticky=customtkinter.SW)
        self.changeLink = customtkinter.CTkLabel(self.settingsFrame, text="Change group invite link", 
            font=customtkinter.CTkFont(size=26))
        self.changeLink.grid(row=2, column=1, padx=(90,0), pady=(40, 25), sticky=customtkinter.NW)
        self.link_c = customtkinter.CTkEntry(self.settingsFrame, height=40, width=550, placeholder_text="Link")
        self.link_c.grid(row=3, column=1, columnspan=1, padx=(90, 10), pady=10, sticky=customtkinter.NW)
        self.changeLinkButton = customtkinter.CTkButton(self.settingsFrame, text="Change Link", width=150, height=40,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callChangeLink)
        self.changeLinkButton.grid(row=3, column=1, padx=(10, 0), pady=(10, 25), sticky=customtkinter.NE)
        self.changePrice = customtkinter.CTkLabel(self.settingsFrame, text="Change group entry price", 
            font=customtkinter.CTkFont(size=26))
        self.changePrice.grid(row=4, column=1, padx=(90,0), pady=25, sticky=customtkinter.NW)
        self.price_c = customtkinter.CTkEntry(self.settingsFrame, height=40, width=550, placeholder_text="Price")
        self.price_c.grid(row=5, column=1, columnspan=1, padx=(90, 10), pady=10, sticky=customtkinter.NW)
        self.changePriceButton = customtkinter.CTkButton(self.settingsFrame, text="Change Price", width=150, height=40,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callChangePrice)
        self.changePriceButton.grid(row=5, column=1, padx=(10, 0), pady=(10, 25), sticky=customtkinter.NE)

        # frame for group lookup tab
        self.lookupFrame = customtkinter.CTkFrame(self, width=880, corner_radius=0)

        # group lookup tab layout
        self.lookupTitle = customtkinter.CTkLabel(self.lookupFrame, text="TeleGate Group Lookup", 
            font=customtkinter.CTkFont(size=30))
        self.lookupTitle.grid(row=0, column=1, padx=(90,0), pady=(40, 20), sticky=customtkinter.NW)
        self.getLink = customtkinter.CTkLabel(self.lookupFrame, text="Get group invite link", 
            font=customtkinter.CTkFont(size=22))
        self.getLink.grid(row=1, column=1, padx=(90,0), pady=20, sticky=customtkinter.NW)
        self.chatTag_l = customtkinter.CTkEntry(self.lookupFrame, height=40, width=550, placeholder_text="Chat Tag")
        self.chatTag_l.grid(row=1, column=1, columnspan=1, padx=(90, 10), pady=(70, 10), sticky=customtkinter.W)
        self.getLinkButton = customtkinter.CTkButton(self.lookupFrame, text="Get Link", width=150, height=40,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callGetLink)
        self.getLinkButton.grid(row=1, column=1, padx=(660, 0), pady=(70, 10), sticky=customtkinter.E)
        self.getPrice = customtkinter.CTkLabel(self.lookupFrame, text="Get group entry price", 
            font=customtkinter.CTkFont(size=22))
        self.getPrice.grid(row=2, column=1, padx=(90,0), pady=20, sticky=customtkinter.NW)
        self.chatTag_l1 = customtkinter.CTkEntry(self.lookupFrame, height=40, width=550, placeholder_text="Chat Tag")
        self.chatTag_l1.grid(row=2, column=1, columnspan=1, padx=(90, 10), pady=(70, 10), sticky=customtkinter.W)
        self.getPriceButton = customtkinter.CTkButton(self.lookupFrame, text="Get Price", width=150, height=40,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callGetPrice)
        self.getPriceButton.grid(row=2, column=1, padx=(660, 0), pady=(70, 10), sticky=customtkinter.E)
        self.getTag = customtkinter.CTkLabel(self.lookupFrame, text="Get chat tag availability", 
            font=customtkinter.CTkFont(size=22))
        self.getTag.grid(row=3, column=1, padx=(90,0), pady=20, sticky=customtkinter.NW)
        self.chatTag_l2 = customtkinter.CTkEntry(self.lookupFrame, height=40, width=550, placeholder_text="Chat Tag")
        self.chatTag_l2.grid(row=3, column=1, columnspan=1, padx=(90, 10), pady=(70, 10), sticky=customtkinter.W)
        self.getTagButton = customtkinter.CTkButton(self.lookupFrame, text="Check Tag", width=150, height=40,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callCheckChatTag)
        self.getTagButton.grid(row=3, column=1, padx=(660, 0), pady=(70, 10), sticky=customtkinter.E)
        self.getSubStatus = customtkinter.CTkLabel(self.lookupFrame, text="Get user subscription status", 
            font=customtkinter.CTkFont(size=22))
        self.getSubStatus.grid(row=4, column=1, padx=(90,0), pady=20, sticky=customtkinter.NW)
        self.chatID_l = customtkinter.CTkEntry(self.lookupFrame, height=40, width=270, placeholder_text="Chat ID")
        self.chatID_l.grid(row=4, column=1, columnspan=1, padx=(90, 10), pady=(70, 10), sticky=customtkinter.W)
        self.userID_l = customtkinter.CTkEntry(self.lookupFrame, height=40, width=270, placeholder_text="User ID")
        self.userID_l.grid(row=4, column=1, columnspan=1, padx=(210, 10), pady=(70, 10))
        self.getStatusButton = customtkinter.CTkButton(self.lookupFrame, text="Check Status", width=150, height=40,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callSubStatus)
        self.getStatusButton.grid(row=4, column=1, padx=(660, 0), pady=(70, 10), sticky=customtkinter.E)
        self.result = customtkinter.CTkLabel(self.lookupFrame, text="", height=50, corner_radius=10,
            font=customtkinter.CTkFont(size=26), fg_color="grey20")
    
    # closes existing tabs and activates the subscribe tab
    def subscribeTab(self):
        self.lookupFrame.grid_forget()
        self.setupFrame.grid_forget()
        self.settingsFrame.grid_forget()
        self.subscribeFrame.grid(row=0, column=1, rowspan=6, sticky="nsew")

    # closes existing tabs and activates the group setup tab
    def setupTab(self):
        self.lookupFrame.grid_forget()
        self.subscribeFrame.grid_forget()
        self.settingsFrame.grid_forget()
        self.setupFrame.grid(row=0, column=1, rowspan=6, sticky="nsew")

    # closes existing tabs and activates the group settings tab
    def settingsTab(self):
        self.lookupFrame.grid_forget()
        self.subscribeFrame.grid_forget()
        self.setupFrame.grid_forget()
        self.settingsFrame.grid(row=0, column=1, rowspan=6, sticky="nsew")

    # closes existing tabs and activates the group lookup tab
    def lookupTab(self):
        self.subscribeFrame.grid_forget()
        self.setupFrame.grid_forget()
        self.settingsFrame.grid_forget()
        self.lookupFrame.grid(row=0, column=1, rowspan=6, sticky="nsew")
    
    # retrieve and use entry inputs to call subscribe() from smart contract wrapper
    def callSubscribe(self):
        wallet = self.walletEntry_s.get() 
        key = self.keyEntry_s.get()
        chatTag = self.chatTag_s.get()
        userID = self.userID_s.get()
        # announce transaction status
        if(contract.subscribe(wallet, key, chatTag, userID) == 1):
            self.subscribeButton.configure(text="Failed", fg_color="red")
        else:
            self.subscribeButton.configure(text="Subscribed!", fg_color="green")

    # retrieve and use entry inputs to call initializeGroup() from smart contract wrapper
    def callInitialize(self):
        wallet = self.walletEntry_i.get() 
        key = self.keyEntry_i.get()
        chatTag = self.chatTag_i.get()
        chatID = self.chatID_i.get()
        link = self.link_i.get()
        price = self.price_i.get()
        # announce transaction status
        if(contract.initializeGroup(wallet, key, chatTag, chatID, link, price) == 1):
            self.setupButton.configure(text="Failed", fg_color="red")
        else:
            self.setupButton.configure(text="Success!", fg_color="green")

    # retrieve and use entry inputs to call changeLink() from smart contract wrapper
    def callChangeLink(self):
        wallet = self.walletEntry_c.get() 
        key = self.keyEntry_c.get()
        chatTag = self.chatTag_c.get()
        link = self.link_c.get()
        # announce transaction status
        if(contract.changeLink(wallet, key, chatTag, link) == 1):
            self.changeLinkButton.configure(text="Failed", fg_color="red")
        else:
            self.changeLinkButton.configure(text="Success!", fg_color="green")

    # retrieve and use entry inputs to call changePrice() from smart contract wrapper
    def callChangePrice(self):
        wallet = self.walletEntry_c.get() 
        key = self.keyEntry_c.get()
        chatTag = self.chatTag_c.get()
        price = self.price_c.get()
        # announce transaction status
        if(contract.changePrice(wallet, key, chatTag, price) == 1):
            self.changePriceButton.configure(text="Failed", fg_color="red")
        else:
            self.changePriceButton.configure(text="Success!", fg_color="green")

    # retrieve and use entry inputs to call getLink() from smart contract wrapper
    def callGetLink(self):
        chatTag = self.chatTag_l.get()
        self.result.configure(text=contract.getLink(chatTag), fg_color="grey20")
        self.result.grid(row=5, column=1, sticky="nsew", padx=(90, 0), pady=(25, 0))

    # retrieve and use entry inputs to call getPrice() from smart contract wrapper
    def callGetPrice(self):
        chatTag = self.chatTag_l1.get()
        self.result.configure(text=str(contract.getPrice(chatTag))+" BNB", fg_color="grey20")
        self.result.grid(row=5, column=1, sticky="nsew", padx=(90, 0), pady=(25, 0))

    # retrieve and use entry inputs to call isChatTagActive() from smart contract wrapper
    def callCheckChatTag(self):
        chatTag = self.chatTag_l2.get()
        # announce tag availability
        if(contract.isChatTagActive(chatTag)):
            self.result.configure(text="Unavailable", fg_color="red")
        else:
            self.result.configure(text="Available", fg_color="green")

        self.result.grid(row=5, column=1, sticky="nsew", padx=(90, 0), pady=(25, 0))

    # retrieve and use entry inputs to call getSubStatus() from smart contract wrapper
    def callSubStatus(self):
        chatID = self.chatID_l.get()
        userID = self.userID_l.get()
        # announce user subscription status
        if(contract.getSubStatus(chatID, userID)):
            self.result.configure(text="Subscribed", fg_color="green")
        else:
            self.result.configure(text="Not Subscribed", fg_color="red")

        self.result.grid(row=5, column=1, sticky="nsew", padx=(90, 0), pady=(25, 0))

if __name__ == "__main__":
    app = App()
    app.mainloop()