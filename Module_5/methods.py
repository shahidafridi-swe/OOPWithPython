class Phone:
    brand = "Redmi"
    features = ["camera", "speaker", "NFC"]
    
    def call(self): #methods
        print("Calling Ruma...")
        
    def send_sms(self, number, messege): #methods
        text = f"{messege} \nsent to {number}"
        return text

myPhone = Phone()

myPhone.call()
result = myPhone.send_sms("01704805887", "Hello Ruma")
print(result)