telephone_numbers = ['080-1203-4455', '090-9372-9682', '090-3080-4982', '080-3917-5918']
# for i in telephone_numbers:
#     if '090-' == i[:3] in str(i):
#         telephone_numbers.remove(i)
# print(f"080で始まる電話番号 : {telephone_numbers}")

l_new = [i for i in telephone_numbers if "080" == i[:3]]
print(f"080で始まる電話番号 : {l_new}")