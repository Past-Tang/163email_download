import os
import imapclient
import pyzmail
from email.header import decode_header

# 邮箱配置
email_user = ''  # 替换为您的邮箱地址
email_pass = ''  # 替换为您的邮箱密码
import os
import imapclient
import pyzmail
from email.header import decode_header

# 邮箱配置
# 连接到IMAP服务器
mail = imapclient.IMAPClient('imap.163.com', ssl=True)
mail.login(email_user, email_pass)
mail.id_({'name': 'XXXX', 'version': '1.0.0', 'vendor': 'myclient', 'contact': 'your_email@example.com'})

# 选择邮箱文件夹，这里选择收件箱
mail.select_folder('INBOX', readonly=True)

# 搜索所有邮件
uids = mail.search(['ALL'])

# 保存附件的文件夹
attachment_dir = 'attachments'
if not os.path.isdir(attachment_dir):
    os.mkdir(attachment_dir)

# 遍历每封邮件
for uid in uids:
    # 获取邮件的原始内容
    raw_message = mail.fetch([uid], ['BODY[]', 'FLAGS'])
    message = pyzmail.PyzMessage.factory(raw_message[uid][b'BODY[]'])

    # 遍历邮件中的每个部分
    for mail_part in message.walk():
        # 检查是否为附件
        if mail_part.get_content_maintype() == 'multipart' or mail_part.get('Content-Disposition') is None:
            continue

        filename = mail_part.get_filename()
        if filename:
            # 解码文件名
            dh = decode_header(filename)
            decoded_filename, charset = dh[0]
            if isinstance(decoded_filename, bytes):
                try:
                    decoded_filename = decoded_filename.decode(charset or 'utf-8', 'ignore')
                except LookupError:  # 如果charset不被识别
                    decoded_filename = decoded_filename.decode('gb2312', 'ignore')
            filepath = os.path.join(attachment_dir, decoded_filename)
            # 写入文件
            with open(filepath, 'wb') as f:
                f.write(mail_part.get_payload(decode=True))
            print(f'附件 {decoded_filename} 已保存到 {filepath}')

# 退出登录
mail.logout()