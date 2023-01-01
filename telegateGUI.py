import tkinter
import tkinter.messagebox
import customtkinter
import contractWrapper as contract

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
        # create sidebar frame with widgets
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
        # Frame for subscribe tab
        self.subscribeFrame = customtkinter.CTkFrame(self, width=880, corner_radius=0)
        self.subscribeFrame.grid(row=0, column=1, rowspan=6, sticky="nsew")
        # Subscribe tab
        self.subTitle = customtkinter.CTkLabel(self.subscribeFrame, text="Subscribe to a group", font=customtkinter.CTkFont(size=30))
        self.subTitle.grid(row=0, column=1, padx=(90,0), pady=(40, 0), sticky=customtkinter.NW)
        self.subInfo = customtkinter.CTkLabel(self.subscribeFrame, 
            text="Wallet Address - Wallet address to complete transaction with\n\n"\
                 "Wallet Key - Private key corresponding to wallet address\n\n"\
                 "Chat Tag - Chat tag of group to subscribe to\n\n"\
                 "User ID - User ID of member to be added to group", 
            justify=customtkinter.LEFT, font=customtkinter.CTkFont(size=18))
        self.subInfo.grid(row=1, column=1, padx=(90,0), pady=(50, 50), sticky=customtkinter.SW)
        self.walletEntry = customtkinter.CTkEntry(self.subscribeFrame, height=40, width=350, placeholder_text="Wallet Address")
        self.walletEntry.grid(row=2, column=1, columnspan=1, padx=(90,0), pady=10, sticky=customtkinter.NW)
        self.keyEntry = customtkinter.CTkEntry(self.subscribeFrame, height=40, width=350, placeholder_text="Wallet Key")
        self.keyEntry.grid(row=2, column=1, columnspan=1, padx=(460,0), pady=10, sticky=customtkinter.NE)
        self.chatTag = customtkinter.CTkEntry(self.subscribeFrame, height=40, width=350, placeholder_text="Chat Tag")
        self.chatTag.grid(row=3, column=1, columnspan=1, padx=(90,0), pady=(20, 0), sticky=customtkinter.SW)
        self.userID = customtkinter.CTkEntry(self.subscribeFrame, height=40, width=350, placeholder_text="User ID")
        self.userID.grid(row=3, column=1, columnspan=1, padx=(460,0), pady=(20, 0), sticky=customtkinter.SE)
        self.subscribeButton = customtkinter.CTkButton(self.subscribeFrame, text="Subscribe", width=150, height=60,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callSubscribe)
        self.subscribeButton.grid(row=4, column=1, padx=(90, 20), pady=(55, 10), sticky=customtkinter.NW)
        # Frame for group setup tab
        self.setupFrame = customtkinter.CTkFrame(self, width=880, corner_radius=0)
        # Group setup tab
        self.setupTitle = customtkinter.CTkLabel(self.setupFrame, text="Setup TeleGate for a Telegram group", font=customtkinter.CTkFont(size=30))
        self.setupTitle.grid(row=0, column=1, padx=(90,0), pady=(40, 0), sticky=customtkinter.NW)
        self.setupInfo = customtkinter.CTkLabel(self.setupFrame, 
            text="Wallet Address - Wallet address to complete transaction with\n\n"\
                 "Wallet Key - Private key corresponding to wallet address\n\n"\
                 "Chat Tag - Chat tag of group to subscribe to\n\n"\
                 "Chat ID - \n\n"\
                 "Link - \n\n"\
                 "Price - ", 
            justify=customtkinter.LEFT, font=customtkinter.CTkFont(size=18))
        self.setupInfo.grid(row=1, column=1, padx=(90,0), pady=(30, 30), sticky=customtkinter.SW)
        self.walletEntry = customtkinter.CTkEntry(self.setupFrame, height=40, width=350, placeholder_text="Wallet Address")
        self.walletEntry.grid(row=2, column=1, columnspan=1, padx=(90,0), pady=10, sticky=customtkinter.NW)
        self.keyEntry = customtkinter.CTkEntry(self.setupFrame, height=40, width=350, placeholder_text="Wallet Key")
        self.keyEntry.grid(row=2, column=1, columnspan=1, padx=(460,0), pady=10, sticky=customtkinter.NE)
        self.chatTag = customtkinter.CTkEntry(self.setupFrame, height=40, width=350, placeholder_text="Chat Tag")
        self.chatTag.grid(row=3, column=1, columnspan=1, padx=(90,0), pady=10, sticky=customtkinter.SW)
        self.chatID = customtkinter.CTkEntry(self.setupFrame, height=40, width=350, placeholder_text="Chat ID")
        self.chatID.grid(row=3, column=1, columnspan=1, padx=(460,0), pady=10, sticky=customtkinter.SE)
        self.link = customtkinter.CTkEntry(self.setupFrame, height=40, width=350, placeholder_text="Link")
        self.link.grid(row=4, column=1, columnspan=1, padx=(90,0), pady=10, sticky=customtkinter.SW)
        self.price = customtkinter.CTkEntry(self.setupFrame, height=40, width=350, placeholder_text="Price")
        self.price.grid(row=4, column=1, columnspan=1, padx=(460,0), pady=10, sticky=customtkinter.SE)
        self.setupButton = customtkinter.CTkButton(self.setupFrame, text="Setup", width=150, height=60,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callInitialize)
        self.setupButton.grid(row=5, column=1, padx=(90, 20), pady=(25, 10), sticky=customtkinter.NW)
        # Frame for group settings tab
        self.settingsFrame = customtkinter.CTkFrame(self, width=880, corner_radius=0)
        # Group settings tab
        self.settingsTitle = customtkinter.CTkLabel(self.settingsFrame, text="Manage your TeleGate group", 
            font=customtkinter.CTkFont(size=30))
        self.settingsTitle.grid(row=0, column=1, padx=(90,0), pady=40, sticky=customtkinter.NW)
        self.walletEntry = customtkinter.CTkEntry(self.settingsFrame, height=40, width=350, placeholder_text="Wallet Address")
        self.walletEntry.grid(row=1, column=1, columnspan=1, padx=(90,0), pady=(10, 25), sticky=customtkinter.NW)
        self.keyEntry = customtkinter.CTkEntry(self.settingsFrame, height=40, width=350, placeholder_text="Wallet Key")
        self.keyEntry.grid(row=1, column=1, columnspan=1, padx=(460,0), pady=(10, 25), sticky=customtkinter.NE)
        self.chatTag = customtkinter.CTkEntry(self.settingsFrame, height=40, width=720, placeholder_text="Chat Tag")
        self.chatTag.grid(row=1, column=1, columnspan=1, padx=(90,0), pady=(90, 10), sticky=customtkinter.SW)
        self.changeLink = customtkinter.CTkLabel(self.settingsFrame, text="Change group invite link", 
            font=customtkinter.CTkFont(size=26))
        self.changeLink.grid(row=2, column=1, padx=(90,0), pady=(40, 25), sticky=customtkinter.NW)
        self.link = customtkinter.CTkEntry(self.settingsFrame, height=40, width=550, placeholder_text="Link")
        self.link.grid(row=3, column=1, columnspan=1, padx=(90, 10), pady=10, sticky=customtkinter.NW)
        self.changeLinkButton = customtkinter.CTkButton(self.settingsFrame, text="Change Link", width=150, height=40,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callChangeLink)
        self.changeLinkButton.grid(row=3, column=1, padx=(10, 0), pady=(10, 25), sticky=customtkinter.NE)
        self.changePrice = customtkinter.CTkLabel(self.settingsFrame, text="Change group entry price", 
            font=customtkinter.CTkFont(size=26))
        self.changePrice.grid(row=4, column=1, padx=(90,0), pady=25, sticky=customtkinter.NW)
        self.price = customtkinter.CTkEntry(self.settingsFrame, height=40, width=550, placeholder_text="Price")
        self.price.grid(row=5, column=1, columnspan=1, padx=(90, 10), pady=10, sticky=customtkinter.NW)
        self.changePriceButton = customtkinter.CTkButton(self.settingsFrame, text="Change Price", width=150, height=40,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callChangePrice)
        self.changePriceButton.grid(row=5, column=1, padx=(10, 0), pady=(10, 25), sticky=customtkinter.NE)
        # Frame for group lookup tab
        self.lookupFrame = customtkinter.CTkFrame(self, width=880, corner_radius=0)
        # Group lookup tab
        self.lookupTitle = customtkinter.CTkLabel(self.lookupFrame, text="TeleGate Group Lookup", 
            font=customtkinter.CTkFont(size=30))
        self.lookupTitle.grid(row=0, column=1, padx=(90,0), pady=(40, 20), sticky=customtkinter.NW)
        self.getLink = customtkinter.CTkLabel(self.lookupFrame, text="Get group invite link", 
            font=customtkinter.CTkFont(size=22))
        self.getLink.grid(row=1, column=1, padx=(90,0), pady=20, sticky=customtkinter.NW)
        self.chatTag = customtkinter.CTkEntry(self.lookupFrame, height=40, width=550, placeholder_text="Chat Tag")
        self.chatTag.grid(row=1, column=1, columnspan=1, padx=(90, 10), pady=(70, 10), sticky=customtkinter.W)
        self.getLinkButton = customtkinter.CTkButton(self.lookupFrame, text="Get Link", width=150, height=40,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callGetLink)
        self.getLinkButton.grid(row=1, column=1, padx=(660, 0), pady=(70, 10), sticky=customtkinter.E)
        self.getPrice = customtkinter.CTkLabel(self.lookupFrame, text="Get group entry price", 
            font=customtkinter.CTkFont(size=22))
        self.getPrice.grid(row=2, column=1, padx=(90,0), pady=20, sticky=customtkinter.NW)
        self.chatTag1 = customtkinter.CTkEntry(self.lookupFrame, height=40, width=550, placeholder_text="Chat Tag")
        self.chatTag1.grid(row=2, column=1, columnspan=1, padx=(90, 10), pady=(70, 10), sticky=customtkinter.W)
        self.getPriceButton = customtkinter.CTkButton(self.lookupFrame, text="Get Price", width=150, height=40,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callGetPrice)
        self.getPriceButton.grid(row=2, column=1, padx=(660, 0), pady=(70, 10), sticky=customtkinter.E)
        self.getTag = customtkinter.CTkLabel(self.lookupFrame, text="Get chat tag availability", 
            font=customtkinter.CTkFont(size=22))
        self.getTag.grid(row=3, column=1, padx=(90,0), pady=20, sticky=customtkinter.NW)
        self.chatTag2 = customtkinter.CTkEntry(self.lookupFrame, height=40, width=550, placeholder_text="Chat Tag")
        self.chatTag2.grid(row=3, column=1, columnspan=1, padx=(90, 10), pady=(70, 10), sticky=customtkinter.W)
        self.getTagButton = customtkinter.CTkButton(self.lookupFrame, text="Check Tag", width=150, height=40,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callCheckChatTag)
        self.getTagButton.grid(row=3, column=1, padx=(660, 0), pady=(70, 10), sticky=customtkinter.E)
        self.getSubStatus = customtkinter.CTkLabel(self.lookupFrame, text="Get user subscription status", 
            font=customtkinter.CTkFont(size=22))
        self.getSubStatus.grid(row=4, column=1, padx=(90,0), pady=20, sticky=customtkinter.NW)
        self.chatTag3 = customtkinter.CTkEntry(self.lookupFrame, height=40, width=270, placeholder_text="Chat Tag")
        self.chatTag3.grid(row=4, column=1, columnspan=1, padx=(90, 10), pady=(70, 10), sticky=customtkinter.W)
        self.userID = customtkinter.CTkEntry(self.lookupFrame, height=40, width=270, placeholder_text="User ID")
        self.userID.grid(row=4, column=1, columnspan=1, padx=(210, 10), pady=(70, 10))
        self.getStatusButton = customtkinter.CTkButton(self.lookupFrame, text="Check Status", width=150, height=40,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            font=customtkinter.CTkFont(size=18), command=self.callSubStatus)
        self.getStatusButton.grid(row=4, column=1, padx=(660, 0), pady=(70, 10), sticky=customtkinter.E)
        self.result = customtkinter.CTkLabel(self.lookupFrame, text="", height=50, corner_radius=10,
            font=customtkinter.CTkFont(size=26), fg_color="grey20")
        
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def subscribeTab(self):
        self.lookupFrame.grid_forget()
        self.setupFrame.grid_forget()
        self.settingsFrame.grid_forget()
        self.subscribeFrame.grid(row=0, column=1, rowspan=6, sticky="nsew")

    def setupTab(self):
        self.lookupFrame.grid_forget()
        self.subscribeFrame.grid_forget()
        self.settingsFrame.grid_forget()
        self.setupFrame.grid(row=0, column=1, rowspan=6, sticky="nsew")

    def settingsTab(self):
        self.lookupFrame.grid_forget()
        self.subscribeFrame.grid_forget()
        self.setupFrame.grid_forget()
        self.settingsFrame.grid(row=0, column=1, rowspan=6, sticky="nsew")

    def lookupTab(self):
        self.subscribeFrame.grid_forget()
        self.setupFrame.grid_forget()
        self.settingsFrame.grid_forget()
        self.lookupFrame.grid(row=0, column=1, rowspan=6, sticky="nsew")
  
    def callSubscribe(self):
        wallet = self.walletEntry.get() 
        key = self.keyEntry.get()
        chatTag = self.chatTag.get()
        userID = self.userID.get()
        
        if(contract.subscribe(wallet, key, chatTag, userID) == 1):
            self.subscribeButton.configure(text="Failed", fg_color="red")
        else:
            self.subscribeButton.configure(text="Subscribed!", fg_color="green")

    def callInitialize(self):
        wallet = self.walletEntry.get() 
        key = self.keyEntry.get()
        chatTag = self.chatTag.get()
        chatID = self.chatID.get()
        link = self.link.get()
        price = self.price.get()
        
        if(contract.initializeGroup(wallet, key, chatTag, chatID, link, price) == 1):
            self.setupButton.configure(text="Failed", fg_color="red")
        else:
            self.setupButton.configure(text="Success!", fg_color="green")

    def callChangeLink(self):
        wallet = self.walletEntry.get() 
        key = self.keyEntry.get()
        chatTag = self.chatTag.get()
        link = self.link.get()

        if(contract.changeLink(wallet, key, chatTag, link) == 1):
            self.changeLinkButton.configure(text="Failed", fg_color="red")
        else:
            self.changeLinkButton.configure(text="Success!", fg_color="green")

    def callChangePrice(self):
        wallet = self.walletEntry.get() 
        key = self.keyEntry.get()
        chatTag = self.chatTag.get()
        price = self.price.get()

        if(contract.changePrice(wallet, key, chatTag, price) == 1):
            self.changePriceButton.configure(text="Failed", fg_color="red")
        else:
            self.changePriceButton.configure(text="Success!", fg_color="green")

    def callGetLink(self):
        chatTag = self.chatTag.get()
        self.result.configure(text=contract.getLink(chatTag), fg_color="grey20")
        self.result.grid(row=5, column=1, sticky="nsew", padx=(90, 0), pady=(25, 0))

    def callGetPrice(self):
        chatTag = self.chatTag1.get()
        self.result.configure(text=contract.getPrice(chatTag), fg_color="grey20")
        self.result.grid(row=5, column=1, sticky="nsew", padx=(90, 0), pady=(25, 0))

    def callCheckChatTag(self):
        chatTag = self.chatTag2.get()
        if(contract.isChatTagActive(chatTag)):
            self.result.configure(text="Unavailable", fg_color="red")
        else:
            self.result.configure(text="Available", fg_color="green")

        self.result.grid(row=5, column=1, sticky="nsew", padx=(90, 0), pady=(25, 0))

    def callSubStatus(self):
        chatTag = self.chatTag3.get()
        userID = self.userID.get()
        if(contract.getSubStatus(chatTag, userID)):
            self.result.configure(text="Subscribed", fg_color="green")
        else:
            self.result.configure(text="Not Subscribed", fg_color="red")

        self.result.grid(row=5, column=1, sticky="nsew", padx=(90, 0), pady=(25, 0))

if __name__ == "__main__":
    app = App()
    app.mainloop()