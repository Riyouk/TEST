def register(name,email_id,passwd):
    register_dic = {"name" : name,"email_id" : email_id,"password" : passwd}
    print(f"the entered info are name {name},email_id {email_id},password {passwd}")
if __name__ == "__main__" :
    register("abc","abc@gmail.com","12345")   