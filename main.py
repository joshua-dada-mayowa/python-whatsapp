# importing the module
import pywhatkit

def send_whatsapp_msg(msg):
    phone_no=input("enter the receiver number: ")
    try:
     # sending message to receiver
        pywhatkit.sendwhatmsg_instantly(phone_no,msg,tab_close=True)

        print("message sent")

    except Exception as e:
  # handling exception
  # and printing error message
        print(str(e))

if __name__=="__main__":
    msg=input("enter your message: ")
    send_whatsapp_msg(msg)
