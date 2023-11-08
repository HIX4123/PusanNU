import re

txt="sniperdata@pusan.ac.kr ( [164.125.7.132])\
	by pusan.ac.kr (psmtpd 5.30.0122)\
	with ESMTP id 5748966592189830097	for hgcho@pusan.ac.kr; Fri, 1 Jun 2012 16:26:35 +0900\
Received: from unknown (HELO uranus.scholarone.com) (170.107.183.89)\
	by 10.10.1.12 with SMTP; 1 Jun 2012 16:26:25 +0900\
    X-Original-SENDERIP: 170.107.183.89\
    X-Original-MAILFROM: onbehalfof+\
    k.jackson+ieee.org@manuscriptcentral.com\
Received: from tss1be0073 (tss1be0073.tshhosting.com\
From: k.jackson@ieee.org\
Sender: onbehalfof+k.jackson+ieee.org@manuscriptcentral.com\
To: hgcho@pusan.ac.kr\
Cc: adrian.bors@york.ac.uk\
nuscriptcentral.com"


stx = txt.replace('\n',' ')  #1개만 바꿈
#stx = txt.substitue('\n',' ')  #1개만 바꿈
print( len(txt), len(stx) )
p1= r"(\w+@\w+\.)"


out = re.match( p1, stx )
print(out)

out = re.search( p1, stx)
print(out)