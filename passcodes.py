#! /usr/bin/env python

import re

inf = """
Delivered-To: zc@nianticlabs.com			
Received from: 216.7.55.16 with SMTP id hc23711iw55;			
Received from: 7.11.55.16 with SMTP id bwm167119c237;			
Received from: nlan3.nianticlabs.com (nlan3.nianticlabs.com [237.11.55.16])			
        by nlan3.nianticlabs.com with ESMTPS id cxbi.s23789c.10.17.12.48.46			
        (version=TLSv1/SSLv3 cipher=OTHER);			
        by nlan3.nianticlabs.com with ESMTPS id cxbi.s23789c.10.17.12.48.46			
Received-SPF: neutral (nianticlabs.com: 55.11.55.16 client-ip=55.11.55.16;)			
Authentication-Results: nlan3.nianticlabs.com; spf=neutral ; dkim=pass (test mode) header.i=@nianticlabs.com			
Message-ID:<icwm23716711b104.109216@nianticlabs.com>			
Received from: 184.237.55.16 with SMTP id z9v5qgnirut6hz6;			
From: 'Dr. Lynton-Wolfe' <wolfe@nianticlabs.com>			
Reply-to: <wolfe@nianticlabs.com>			
Subject: New Numbers			
To: Dr. Ezekiel Calvin <zc@nianticlabs.com>			
MIME-Version: 1.0 Content-Type: multipart/alternative; boundary='752727816-478887812-6809307=:105712'--752727816-478887812-6809307=:105712			
Content-Type: text/plain; charset=us-ascii			
			
			
Dr. Calvin,

An update to our conversation on Wednesday.

The XM fabric has evolved slightly since the shifts that occurred at that time.

Item synthesis rates are recovering, portal keys seem to be generating slightly 
more often, and in particular, when harvesting a portal in direct alignment with
the scanner (i.e. a friendly portal), item production seems to always yield a
positive net result.

I will be continuing to monitor the data and will provide an update as soon as
we have learned more.

olw
 			
 		

"""

passgex = r".*([0-9][a-z][a-z][0-9]([a-z]+)[a-z][0-9][a-z][0-9][a-z]).*"

for i in inf.split ():
    m = re.match (passgex, i)
    if m:
        print m.group (1)
    m = re.match (passgex, i[::-1])
    if m:
        print m.group (1)
