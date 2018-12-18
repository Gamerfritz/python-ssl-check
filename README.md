# python-ssl-check
Simple python script to check multiple SSL certificate expiration dates.

Add all webservices you need to check in a text file like:<br>
<code>adress,port</code><br>
<code>www.github.com,443
</code>
<br><br>
Then you must paste the path in the <code>file</code> variable.<br>
The output will be the amount of days until expiration.

It is possible to use this script in combination with Zabbix for certificate monitoring.
