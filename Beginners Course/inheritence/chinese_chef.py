from chef import Chef

#inherite the functions from Chef class
class Chinese_Chef(Chef):
            
    def make_special_dish(self):
        print("The chinese chef makes noodles")
        
    def make_fried_rice(self):
        print("The chinese chef makes a fried rice")