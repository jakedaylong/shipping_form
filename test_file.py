import os

user_path = os.path.expanduser('~')
user_path_docs = os.path.join(user_path, 'Documents')
user_path_barcodes = os.path.join(user_path_docs, 'Barcodes')

print(user_path)
print(user_path_docs)
print(user_path_barcodes)

recipient_path = '"'+user_path_barcodes + '\\recipients.jpg'+'"'
print(recipient_path)