# Python-WhatsApp

This is a Python project that allows you to send WhatsApp messages instantly and remotely control your PC using your phone (Windows only). The project utilizes the `pywhatkit` library for WhatsApp functionalities.

## Project Repository

[python-whatsapp on GitHub](https://github.com/joshua-dada-mayowa/python-whatsapp)

## Instructions

### Sending WhatsApp Messages

1. Clone the repository:

   ```bash
   git clone https://github.com/joshua-dada-mayowa/python-whatsapp.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-whatsapp
   ```

3. Open the `main.py` file and run the script:

   ```bash
   python main.py
   ```

4. Enter your message when prompted and the recipient's phone number.

   Note: Make sure to have the `pywhatkit` library installed. You can install it using:

   ```bash
   pip install pywhatkit
   ```

### Remotely Controlling PC (Windows only)

1. Open the `remote.py` file:

   ```bash
   python remote.py
   ```

   This method can be used to remotely control your PC using your phone.

### Message Log

The `PyWhatKit_DB.txt` file contains a log of sent messages with details such as date, time, phone number, group ID, and message content.

```plaintext
Date: 16/12/2022
Time: 0:25
Phone Number: +2347087503522
Message: omo you ugly oo
--------------------
... (other log entries)
--------------------
Date: 16/12/2022
Time: 1:52
Phone Number: +2348103364059
Message: you saying pain is what i need?
--------------------
```

Feel free to explore and customize the project for your needs! If you encounter any issues, refer to the documentation or raise an issue on the [GitHub repository](https://github.com/joshua-dada-mayowa/python-whatsapp/issues).
