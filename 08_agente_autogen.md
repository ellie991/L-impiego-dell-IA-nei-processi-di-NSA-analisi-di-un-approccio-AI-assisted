# Trascrizione sessione agente AutoGen

Data: 2026-09-09T15:41:44

## user

Analizza i seguenti output raccolti nel laboratorio e procedi con le 4 fasi.

=== OUTPUT NMAP ===
# Nmap 7.94 scan initiated Tue Sep  8 06:41:53 2026 as: nmap -sS -sV -O -p- -oN output/02_nmap_full.txt 192.168.64.3
Nmap scan report for 192.168.64.3
Host is up (0.00081s latency).
Not shown: 65505 closed tcp ports (reset)
PORT      STATE SERVICE     VERSION
21/tcp    open  ftp         vsftpd 2.3.4
22/tcp    open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
23/tcp    open  telnet      Linux telnetd
25/tcp    open  smtp        Postfix smtpd
53/tcp    open  domain      ISC BIND 9.4.2
80/tcp    open  http        Apache httpd 2.2.8 ((Ubuntu) DAV/2)
111/tcp   open  rpcbind     2 (RPC #100000)
139/tcp   open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp   open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
512/tcp   open  exec        netkit-rsh rexecd
513/tcp   open  login
514/tcp   open  tcpwrapped
1099/tcp  open  java-rmi    GNU Classpath grmiregistry
1524/tcp  open  bindshell   Metasploitable root shell
2049/tcp  open  nfs         2-4 (RPC #100003)
2121/tcp  open  ftp         ProFTPD 1.3.1
3306/tcp  open  mysql       MySQL 5.0.51a-3ubuntu5
3632/tcp  open  distccd     distccd v1 ((GNU) 4.2.4 (Ubuntu 4.2.4-1ubuntu4))
5432/tcp  open  postgresql  PostgreSQL DB 8.3.0 - 8.3.7
5900/tcp  open  vnc         VNC (protocol 3.3)
6000/tcp  open  X11         (access denied)
6667/tcp  open  irc         UnrealIRCd
6697/tcp  open  irc         UnrealIRCd
8009/tcp  open  ajp13?
8180/tcp  open  http        Apache Tomcat/Coyote JSP engine 1.1
8787/tcp  open  drb         Ruby DRb RMI (Ruby 1.8; path /usr/lib/ruby/1.8/drb)
40536/tcp open  mountd      1-3 (RPC #100005)
47876/tcp open  nlockmgr    1-4 (RPC #100021)
55681/tcp open  status      1 (RPC #100024)
58639/tcp open  java-rmi    GNU Classpath grmiregistry
MAC Address: 72:A2:1C:AB:FE:2F (Unknown)
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6
OS details: Linux 2.6.9 - 2.6.33
Network Distance: 1 hop
Service Info: Hosts:  metasploitable.localdomain, irc.Metasploitable.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Sep  8 06:44:35 2026 -- 1 IP address (1 host up) scanned in 162.24 seconds

=== OUTPUT NIKTO ===
- Nikto v2.5.0/
+ Target Host: 192.168.64.3
+ Target Port: 80
+ GET /: Retrieved x-powered-by header: PHP/5.2.4-2ubuntu5.10.
+ GET /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options: 
+ GET /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/: 
+ GET /index: Uncommon header 'tcn' found, with contents: list.
+ GET /index: Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. The following alternatives for 'index' were found: index.php. See: http://www.wisec.it/sectou.php?id=4698ebdc59d15,https://exchange.xforce.ibmcloud.com/vulnerabilities/8275: 
+ HEAD Apache/2.2.8 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ ODNFBFYA /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ TRACE /: HTTP TRACE method is active which suggests the host is vulnerable to XST. See: https://owasp.org/www-community/attacks/Cross_Site_Tracing: 
+ GET /phpinfo.php: Output from the phpinfo() function was found.
+ GET /doc/: Directory indexing found.
+ GET /doc/: The /doc/ directory is browsable. This may be /usr/doc. See: CVE-1999-0678: 
+ GET /?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings. See: OSVDB-12184: 
+ GET /?=PHPE9568F36-D428-11d2-A769-00AA001ACF42: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings. See: OSVDB-12184: 
+ GET /?=PHPE9568F34-D428-11d2-A769-00AA001ACF42: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings. See: OSVDB-12184: 
+ GET /?=PHPE9568F35-D428-11d2-A769-00AA001ACF42: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings. See: OSVDB-12184: 
+ GET /phpMyAdmin/changelog.php: phpMyAdmin is for managing MySQL databases, and should be protected or limited to authorized hosts.
+ GET /phpMyAdmin/ChangeLog: Server may leak inodes via ETags, header found with file /phpMyAdmin/ChangeLog, inode: 92462, size: 40540, mtime: Tue Dec  9 09:24:00 2008. See: CVE-2003-1418: 
+ GET /phpMyAdmin/ChangeLog: phpMyAdmin is for managing MySQL databases, and should be protected or limited to authorized hosts.
+ GET /test/: Directory indexing found.
+ GET /test/: This might be interesting.
+ GET /phpinfo.php: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information. See: CWE-552: 
+ GET /icons/: Directory indexing found.
+ GET /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/: 
+ GET /phpMyAdmin/: phpMyAdmin directory found.
+ GET /phpMyAdmin/Documentation.html: phpMyAdmin is for managing MySQL databases, and should be protected or limited to authorized hosts.
+ GET /phpMyAdmin/README: phpMyAdmin is for managing MySQL databases, and should be protected or limited to authorized hosts. See: https://typo3.org/: 
+ GET /#wp-config.php#: #wp-config.php# file found. This file contains the credentials.

=== REPORT GVM (CSV) ===
IP,Hostname,Port,Port Protocol,CVSS,Severity,QoD,Solution Type,NVT Name,Summary,Specific Result,NVT OID,CVEs,Task ID,Task Name,Timestamp,Result ID,Impact,Solution,Affected Software/OS,Vulnerability Insight,Vulnerability Detection Method,Product Detection Result,BIDs,CERTs,Other References
192.168.64.3,,,,10.0,Critical,80,"Mitigation","Operating System (OS) End of Life (EOL) Detection","The Operating System (OS) on the remote host has reached the end
  of life (EOL) and should not be used anymore.","The ""Ubuntu"" Operating System on the remote host has reached the end of life.

CPE:               cpe:/o:canonical:ubuntu_linux:8.04
Installed version,
build or SP:       8.04
EOL date:          2013-05-09
EOL info:          https://documentation.ubuntu.com/project/release-team/list-of-releases/
",1.3.6.1.4.1.25623.1.0.103674,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,bfdf4ab2-99c8-4f14-a7c9-44d4cb992dda,"An EOL version of an OS is not receiving any security updates
  from the vendor. Unfixed security vulnerabilities might be leveraged by an attacker to compromise
  the security of this host.","Update the OS on the remote host to a version which is still
  supported and receiving security updates by the vendor.

  Note / Important: Please create an override for this result if the target host is a:

  - Windows system with Extended Security Updates (ESU)

  - System with additional 3rd-party / non-vendor security updates like e.g. from 'TuxCare',
  'Freexian Extended LTS' or similar","","","Checks if an EOL version of an OS is present on the target
  host.
Details:
Operating System (OS) End of Life (EOL) Detection
(OID: 1.3.6.1.4.1.25623.1.0.103674)
Version used: 2025-05-21T05:40:19Z
","Product: cpe:/o:canonical:ubuntu_linux:8.04
Method: OS Detection Consolidation and Reporting
(OID: 1.3.6.1.4.1.25623.1.0.105937)
","","",""
192.168.64.3,,1524,tcp,10.0,Critical,99,"Workaround","Possible Backdoor: Ingreslock","A backdoor is installed on the remote host.","The service is answering to an 'id;' command with the following response: uid=0(root) gid=0(root)
",1.3.6.1.4.1.25623.1.0.103549,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,665a4870-ab16-46f1-9304-47c78870962d,"Attackers can exploit this issue to execute arbitrary commands in the
  context of the application. Successful attacks will compromise the affected isystem.","A whole cleanup of the infected system is recommended.","","","
Details:
Possible Backdoor: Ingreslock
(OID: 1.3.6.1.4.1.25623.1.0.103549)
Version used: 2023-07-25T05:05:58Z
","","","",""
192.168.64.3,,8787,tcp,10.0,Critical,99,"Mitigation","Distributed Ruby (dRuby/DRb) Multiple RCE Vulnerabilities","Systems using Distributed Ruby (dRuby/DRb), which is available in Ruby versions 1.6
  and later, may permit unauthorized systems to execute distributed commands.","The service is running in $SAFE >= 1 mode. However it is still possible to run arbitrary syscall commands on the remote host. Sending an invalid syscall the service returned the following response:

Flo:Errno::ENOSYS:bt[""3/usr/lib/ruby/1.8/drb/drb.rb:1555:in `syscall'""0/usr/lib/ruby/1.8/drb/drb.rb:1555:in `send'""4/usr/lib/ruby/1.8/drb/drb.rb:1555:in `__send__'""A/usr/lib/ruby/1.8/drb/drb.rb:1555:in `perform_without_block'""3/usr/lib/ruby/1.8/drb/drb.rb:1515:in `perform'""5/usr/lib/ruby/1.8/drb/drb.rb:1589:in `main_loop'""0/usr/lib/ruby/1.8/drb/drb.rb:1585:in `loop'""5/usr/lib/ruby/1.8/drb/drb.rb:1585:in `main_loop'""1/usr/lib/ruby/1.8/drb/drb.rb:1581:in `start'""5/usr/lib/ruby/1.8/drb/drb.rb:1581:in `main_loop'""//usr/lib/ruby/1.8/drb/drb.rb:1430:in `run'""1/usr/lib/ruby/1.8/drb/drb.rb:1427:in `start'""//usr/lib/ruby/1.8/drb/drb.rb:1427:in `run'""6/usr/lib/ruby/1.8/drb/drb.rb:1347:in `initialize'""//usr/lib/ruby/1.8/drb/drb.rb:1627:in `new'""9/usr/lib/ruby/1.8/drb/drb.rb:1627:in `start_service'""%/usr/sbin/druby_timeserver.rb:12:errnoi+:mesg""Function not implemented
",1.3.6.1.4.1.25623.1.0.108010,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,27a75eff-0a81-4043-8730-91173416cc7f,"By default, Distributed Ruby does not impose restrictions on allowed hosts or set the
  $SAFE environment variable to prevent privileged activities. If other controls are not in place, especially if the
  Distributed Ruby process runs with elevated privileges, an attacker could execute arbitrary system commands or Ruby
  scripts on the Distributed Ruby server. An attacker may need to know only the URI of the listening Distributed Ruby
  server to submit Ruby commands.","Administrators of environments that rely on Distributed Ruby should ensure that
  appropriate controls are in place. Code-level controls may include:

  - Implementing taint on untrusted input

  - Setting $SAFE levels appropriately (>=2 is recommended if untrusted hosts are allowed to submit Ruby commands, and >=3 may be appropriate)

  - Including drb/acl.rb to set ACLEntry to restrict access to trusted hosts","","","Send a crafted command to the service and check for a remote command execution
  via the instance_eval or syscall requests.
Details:
Distributed Ruby (dRuby/DRb) Multiple RCE Vulnerabilities
(OID: 1.3.6.1.4.1.25623.1.0.108010)
Version used: 2024-06-28T05:05:33Z
","","","",""
192.168.64.3,,80,tcp,10.0,Critical,80,"VendorFix","TWiki < 4.2.4 Multiple XSS / Command Execution Vulnerabilities","TWiki is prone to multiple cross-site scripting (XSS) and
  command execution vulnerabilities.","Installed version: 01.Feb.2003
Fixed version:     4.2.4

",1.3.6.1.4.1.25623.1.0.800320,"CVE-2008-5304,CVE-2008-5305",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,58015738-2597-4398-9c19-51e09a110b8f,"Successful exploitation could allow execution of arbitrary script code or
  commands. This could let attackers steal cookie-based authentication credentials or compromise the affected
  application.","Update to version 4.2.4 or later.","TWiki versions prior to 4.2.4.","The flaws are due to:

  - %URLPARAM{}% variable is not properly sanitized which lets attackers
    conduct cross-site scripting attack.

  - %SEARCH{}% variable is not properly sanitised before being used in an
    eval() call which lets the attackers execute perl code through eval
    injection attack.","
Details:
TWiki < 4.2.4 Multiple XSS / Command Execution Vulnerabilities
(OID: 1.3.6.1.4.1.25623.1.0.800320)
Version used: 2025-12-11T05:46:19Z
","","","",""
192.168.64.3,,512,tcp,10.0,Critical,80,"Mitigation","The rexec service is running","This remote host is running a rexec service.","The rexec service was detected on the target system.
",1.3.6.1.4.1.25623.1.0.100111,"CVE-1999-0618",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,fcb0b481-43f7-4cb2-87f2-57273241ea58,"","Disable the rexec service and use alternatives like SSH
  instead.","","rexec (remote execution client for an exec server) has the same
  kind of functionality that rsh has: you can execute shell commands on a remote computer.

  The main difference is that rexec authenticate by reading the username and password *unencrypted*
  from the socket.","Checks whether an rexec service is exposed on the target
  host.
Details:
The rexec service is running
(OID: 1.3.6.1.4.1.25623.1.0.100111)
Version used: 2023-09-12T05:05:19Z
","","","",""
192.168.64.3,,8009,tcp,9.8,Critical,99,"VendorFix","Apache Tomcat AJP RCE Vulnerability (Ghostcat) - Active Check","Apache Tomcat is prone to a remote code execution (RCE)
  vulnerability in the AJP connector dubbed 'Ghostcat'.","It was possible to read the file ""/WEB-INF/web.xml"" through the AJP connector.

Result:

AB 8\x0004 Ã\x0088 \x0002OK  \x0001 \x000CContent-Type  \x001Ctext/html;charset=ISO-8859-1 AB\x001FÃ¼\x0003\x001FÃ¸<!--
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the ""License""); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an ""AS IS"" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<?xml version=""1.0"" encoding=""ISO-8859-1""?>
<!DOCTYPE html PUBLIC ""-//W3C//DTD XHTML 1.0 Strict//EN""
   ""http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"">

<html xmlns=""http://www.w3.org/1999/xhtml"" xml:lang=""en"" lang=""en"">
    <head>
    <title>Apache Tomcat/5.5</title>
    <style type=""text/css"">
    /*<![CDATA[*/
      body {
          color: #000000;
          background-color: #FFFFFF;
	  font-family: Arial, ""Times New Roman"", Times, serif;
          margin: 10px 0px;
      }

    img {
       border: none;
    }
    
    a:link, a:visited {
        color: blue
    }

    th {
        font-family: Verdana, ""Times New Roman"", Times, serif;
        font-size: 110%;
        font-weight: normal;
        font-style: italic;
        background: #D2A41C;
        text-align: left;
    }

    td {
        color: #000000;
	font-family: Arial, Helvetica, sans-serif;
    }
    
    td.menu {
        background: #FFDC75;
    }

    .center {
        text-align: center;
    }

    .code {
        color: #000000;
        font-family: ""Courier New"", Courier, monospace;
        font-size: 110%;
        margin-left: 2.5em;
    }
    
     #banner {
        margin-bottom: 12px;
     }

     p#congrats {
         margin-top: 0;
         font-weight: bold;
         text-align: center;
     }

     p#footer {
         text-align: right;
         font-size: 80%;
     }
     /*]]>*/
   </style>
</head>

<body>

<!-- Header -->
<table id=""banner"" width=""100%"">
    <tr>
      <td align=""left"" style=""width:130px"">
        <a href=""http://tomcat.apache.org/"">
	  <img src=""tomcat.gif"" height=""92"" width=""130"" alt=""The Mighty Tomcat - MEOW!""/>
	</a>
      </td>
      <td align=""left"" valign=""top""><b>Apache Tomcat/5.5</b></td>
      <td align=""right"">
        <a href=""http://www.apache.org/"">
	  <img src=""asf-logo-wide.gif"" height=""51"" width=""537"" alt=""The Apache Software Foundation""/>
	</a>
       </td>
     </tr>
</table>

<table>
    <tr>

        <!-- Table of Contents -->
        <td valign=""top"">
            <table width=""100%"" border=""1"" cellspacing=""0"" cellpadding=""3"">
                <tr>
		  <th>Administration</th>
                </tr>
                <tr>
		  <td class=""menu"">
		    <a href=""manager/status"">Status</a><br/>
                    <a href=""admin"">Tomcat&nbsp;Administration</a><br/>
                    <a href=""manager/html"">Tomcat&nbsp;Manager</a><br/>
                    &nbsp;
                  </td>
                </tr>
            </table>

	    <br />
            <table width=""100%"" border=""1"" cellspacing=""0"" cellpadding=""3"">
                <tr>
		  <th>Documentation</th>
                </tr>
                <tr>
                  <td class=""menu"">
                    <a href=""RELEASE-NOTES.txt"">Release&nbsp;Notes</a><br/>
                    <a href=""tomcat-docs/changelog.html"">Change&nbsp;Log</a><br/>
                    <a href=""tomcat-docs"">Tomcat&nbsp;Documentation</a><br/>                        &nbsp;
                    &nbsp;
		    </td>
                </tr>
            </table>
	    
            <br/>
            <table width=""100%"" border=""1"" cellspacing=""0"" cellpadding=""3"">
                <tr>
                  <th>Tomcat Online</th>
                </tr>
                <tr>
                  <td class=""menu"">
                    <a href=""http://tomcat.apache.org/"">Home&nbsp;Page</a><br/>
		    <a href=""http://tomcat.apache.org/faq/"">FAQ</a><br/>
                    <a href=""http://tomcat.apache.org/bugreport.html"">Bug&nbsp;Database</a><br/>
                    <a href=""http://issues.apache.org/bugzilla/buglist.cgi?bug_status=UNCONFIRMED&amp;bug_status=NEW&amp;bug_status=ASSIGNED&amp;bug_status=REOPENED&amp;bug_status=RESOLVED&amp;resolution=LATER&amp;resolution=REMIND&amp;resolution=---&amp;bugidtype=include&amp;product=Tomcat+5&amp;cmdtype=doit&amp;order=Importance"">Open Bugs</a><br/>
                    <a href=""http://mail-archives.apache.org/mod_mbox/tomcat-users/"">Users&nbsp;Mailing&nbsp;List</a><br/>
                    <a href=""http://mail-archives.apache.org/mod_mbox/tomcat-dev/"">Developers&nbsp;Mailing&nbsp;List</a><br/>
                    <a href=""irc://irc.freenode.net/#tomcat"">IRC</a><br/>
		    &nbsp;
                  </td>
                </tr>
            </table>
	    
            <br/>
            <table width=""100%"" border=""1"" cellspacing=""0"" cellpadding=""3"">
                <tr>
                  <th>Examples</th>
                </tr>
                <tr>
                  <td class=""menu"">
                    <a href=""jsp-examples/"">JSP&nbsp;Examples</a><br/>
                    <a href=""servlets-examples/"">Servlet&nbsp;Examples</a><br/>
                    <a href=""webdav/"">WebDAV&nbsp;capabilities</a><br/>
     		    &nbsp;
                  </td>
                </tr>
            </table>
	    
            <br/>
            <table width=""100%"" border=""1"" cellspacing=""0"" cellpadding=""3"">
                <tr>
		  <th>Miscellaneous</th>
                </tr>
                <tr>
                  <td class=""menu"">
                    <a href=""http://java.sun.com/products/jsp"">Sun's&nbsp;Java&nbsp;Server&nbsp;Pages&nbsp;Site</a><br/>
                    <a href=""http://java.sun.com/products/servlet"">Sun's&nbsp;Servlet&nbsp;Site</a><br/>
    		    &nbsp;
                  </td>
                </tr>
            </table>
        </td>

        <td style=""width:20px"">&nbsp;</td>
	
        <!-- Body -->
        <td align=""left"" valign=""top"">
          <p id=""congrats"">If you're seeing this page via a web browser, it means you've setup Tomcat successfully. Congratulations!</p>
 
          <p>As you may have guessed by now, this is the default Tomcat home page. It can be found on the local filesystem at:</p>
          <p class=""code"">$CATALINA_HOME/webapps/ROOT/index.jsp</p>
	  
          <p>where ""$CATALINA_HOME"" is the root of the Tomcat installation directory. If you're seeing this page, and you don't think you should be, then either you're either a user who has arrived at new installation of Tomcat, or you're an administrator who hasn't got his/her setup quite right. Providing the latter is the case, please refer to the <a href=""tomcat-docs"">Tomcat Documentation</a> for more detailed setup and administration information than is found in the INSTALL file.</p>

            <p><b>NOTE:</b> This page is precompiled. If you change it, this page will not change since
                  it was compiled into a servlet at build time.
                  (See <tt>$CATALINA_HOME/webapps/ROOT/WEB-INF/web.xml</tt> as to how it was mapped.)
            </p>

            <p><b>NOTE: For security reasons, using the administration webapp
            is restricted to users with role ""admin"". The manager webapp
            is restricted to users with role ""manager"".</b>
            Users are defined in <code>$CATALINA_HOME/conf/tomcat-users.xml</code>.</p>

            <p>Included with this release are a host of sample Servlets and JSPs (with associated source code), extensive documentation (including the Servlet 2.4 and JSP 2.0 API JavaDoc), and an introductory guide to developing web applications.</p>

            <p>Tomcat mailing lists are available at the Tomcat project web site:</p>

           <ul>
               <li><b><a href=""mailto:users@tomcat.apache.org"">users@tomc
",1.3.6.1.4.1.25623.1.0.143545,"CVE-2020-1938",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,b56fe007-c630-44f6-a8ab-efbcc0dbab40,"","'- Update Apache Tomcat to version 7.0.100, 8.5.51, 9.0.31 or
  later

  - For other products using Tomcat please contact the vendor for more information on fixed
  versions","Apache Tomcat versions prior 7.0.100, 8.5.51 or 9.0.31 when the
  AJP connector is enabled.

  Other products like JBoss or Wildfly which are using Tomcat might be affected as well.","Apache Tomcat server has a file containing vulnerability, which
  can be used by an attacker to read or include any files in all webapp directories on Tomcat, such
  as webapp configuration files or source code.","Sends a crafted AJP request and checks the response.
Details:
Apache Tomcat AJP RCE Vulnerability (Ghostcat) - Active Check
(OID: 1.3.6.1.4.1.25623.1.0.143545)
Version used: 2026-03-18T05:59:10Z
","","","DFN-CERT-2021-1736,DFN-CERT-2020-1508,DFN-CERT-2020-1413,DFN-CERT-2020-1276,DFN-CERT-2020-1134,DFN-CERT-2020-0850,DFN-CERT-2020-0835,DFN-CERT-2020-0821,DFN-CERT-2020-0569,DFN-CERT-2020-0557,DFN-CERT-2020-0501,DFN-CERT-2020-0381,WID-SEC-2024-0528,WID-SEC-2023-2480,CB-K20/0711,CB-K20/0705,CB-K20/0693,CB-K20/0555,CB-K20/0543,CB-K20/0154",""
192.168.64.3,,3306,tcp,9.8,Critical,95,"Mitigation","MySQL / MariaDB Default Credentials (MySQL Protocol)","It was possible to login into the remote MySQL using default
  credentials.","It was possible to login as user ""root"" with an empty password.
",1.3.6.1.4.1.25623.1.0.103551,"CVE-2001-0645,CVE-2002-1809,CVE-2004-1532,CVE-2004-2357,CVE-2006-1451,CVE-2007-2554,CVE-2007-6081,CVE-2009-0919,CVE-2014-3419,CVE-2015-4669,CVE-2016-6531,CVE-2018-15719,CVE-2024-22901,CVE-2026-47847",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,39ed6bf9-f365-4c78-ae59-5f90613471fc,"","'- Change the password as soon as possible

  - Contact the vendor for other possible fixes / updates","The following products are know to use such weak credentials:

  - CVE-2001-0645: Symantec/AXENT NetProwler 3.5.x

  - CVE-2002-1809: Windows binary release of MySQL 3.23.2 through 3.23.52

  - CVE-2004-1532: AppServ 2.5.x and earlier

  - CVE-2004-2357: Proofpoint Protection Server

  - CVE-2006-1451: MySQL Manager in Apple Mac OS X 10.3.9 and 10.4.6

  - CVE-2007-2554: Associated Press (AP) Newspower 4.0.1 and earlier

  - CVE-2007-6081: AdventNet EventLog Analyzer build 4030

  - CVE-2009-0919: XAMPP

  - CVE-2014-3419: Infoblox NetMRI before 6.8.5

  - CVE-2015-4669: Xsuite 2.x

  - CVE-2016-6531, CVE-2018-15719: Open Dental before version 18.4

  - CVE-2024-22901: Vinchin Backup & Recovery 7.2 and prior

  - CVE-2026-47847: Bitnami MariaDB Galera container images and Helm chart

  - No CVE / GHSA-g38h-mr9p-fjmf: Vvveb CMS 1.0.8 and prior

  Other products might be affected as well.","","
Details:
MySQL / MariaDB Default Credentials (MySQL Protocol)
(OID: 1.3.6.1.4.1.25623.1.0.103551)
Version used: 2026-07-22T06:26:54Z
","Product: cpe:/a:mysql:mysql:5.0.51a
Method: MariaDB / Oracle MySQL Detection (MySQL Protocol)
(OID: 1.3.6.1.4.1.25623.1.0.100152)
","","",""
192.168.64.3,,21,tcp,9.8,Critical,99,"VendorFix","vsftpd Compromised Source Packages Backdoor Vulnerability - Active Check","vsftpd is prone to a backdoor vulnerability.","Vulnerability was detected according to the Vulnerability Detection Method.",1.3.6.1.4.1.25623.1.0.103185,"CVE-2011-2523",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,6915574d-975e-43da-be03-b4ac720c3fea,"Attackers can exploit this issue to execute arbitrary commands
  in the context of the application. Successful attacks will compromise the affected
  application.","The repaired package can be downloaded from the referenced
  vendor homepage. Please validate the package with its signature.","vsftpd 2.3.4 source packages downloaded between 20110630
  and 20110703 are affected.","The tainted source package contains a backdoor which opens a
  shell on port 6200/tcp.","
Details:
vsftpd Compromised Source Packages Backdoor Vulnerability - Active Check
(OID: 1.3.6.1.4.1.25623.1.0.103185)
Version used: 2026-02-18T05:57:21Z
","","","",""
192.168.64.3,,6200,tcp,9.8,Critical,99,"VendorFix","vsftpd Compromised Source Packages Backdoor Vulnerability - Active Check","vsftpd is prone to a backdoor vulnerability.","Vulnerability was detected according to the Vulnerability Detection Method.",1.3.6.1.4.1.25623.1.0.103185,"CVE-2011-2523",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,57a4822f-fb69-4a99-a726-10ec3baba2b7,"Attackers can exploit this issue to execute arbitrary commands
  in the context of the application. Successful attacks will compromise the affected
  application.","The repaired package can be downloaded from the referenced
  vendor homepage. Please validate the package with its signature.","vsftpd 2.3.4 source packages downloaded between 20110630
  and 20110703 are affected.","The tainted source package contains a backdoor which opens a
  shell on port 6200/tcp.","
Details:
vsftpd Compromised Source Packages Backdoor Vulnerability - Active Check
(OID: 1.3.6.1.4.1.25623.1.0.103185)
Version used: 2026-02-18T05:57:21Z
","","","",""
192.168.64.3,,3632,tcp,9.3,Critical,99,"VendorFix","DistCC RCE Vulnerability (CVE-2004-2687)","DistCC is prone to a remote code execution (RCE)
  vulnerability.","It was possible to execute the ""id"" command.

Result: uid=1(daemon) gid=1(daemon)
",1.3.6.1.4.1.25623.1.0.103553,"CVE-2004-2687",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,59a73fc9-bcb8-4fc7-89cc-b92935acf84a,"DistCC by default trusts its clients completely that in turn
  could allow a malicious client to execute arbitrary commands on the server.","Vendor updates are available. Please see the references for
  more information.

  For more information about DistCC's security see the references.","","DistCC 2.x, as used in XCode 1.5 and others, when not configured
  to restrict access to the server port, allows remote attackers to execute arbitrary commands via
  compilation jobs, which are executed by the server without authorization checks.","
Details:
DistCC RCE Vulnerability (CVE-2004-2687)
(OID: 1.3.6.1.4.1.25623.1.0.103553)
Version used: 2022-07-07T10:16:06Z
","","","DFN-CERT-2019-0381",""
192.168.64.3,,5900,tcp,9.0,Critical,70,"Mitigation","VNC Brute Force Login","The VNC service is prone to default credentials.","It was possible to connect to the VNC server with the password: password
",1.3.6.1.4.1.25623.1.0.106056,"CVE-2026-65313",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,9af34829-85b1-4ed4-9fd8-9c1b56f4c6db,"","Change the password to something hard to guess or enable
  password protection at all.","Various products (e.g. HIPASE-250) and misconfigurations.","This script tries to authenticate to a VNC server with the
  passwords set in the password preference. It will also test and report if no authentication /
  password is required at all.

  Note: Some VNC servers have a blacklisting scheme that blocks IP addresses after five unsuccessful
  connection attempts for a period of time. The script will abort the brute force attack if it
  encounters that it gets blocked.

  Note as well that passwords can be max. 8 characters long.","Tries to log in with given passwords via VNC protocol.
Details:
VNC Brute Force Login
(OID: 1.3.6.1.4.1.25623.1.0.106056)
Version used: 2026-08-18T05:48:51Z
","","","",""
192.168.64.3,,5432,tcp,9.0,Critical,99,"Mitigation","PostgreSQL Default Credentials (PostgreSQL Protocol)","It was possible to login into the remote PostgreSQL as user
  postgres using weak credentials.","It was possible to login as user postgres with password ""postgres"".


",1.3.6.1.4.1.25623.1.0.103552,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,4effc97f-472b-4e91-9afc-b7e85d18da58,"","Change the password as soon as possible.","","","
Details:
PostgreSQL Default Credentials (PostgreSQL Protocol)
(OID: 1.3.6.1.4.1.25623.1.0.103552)
Version used: 2024-07-19T15:39:06Z
","Product: cpe:/a:postgresql:postgresql:8.3.1
Method: PostgreSQL Detection Consolidation
(OID: 1.3.6.1.4.1.25623.1.0.128025)
","","",""
192.168.64.3,,6697,tcp,8.1,High,80,"VendorFix","UnrealIRCd Authentication Spoofing Vulnerability","UnrealIRCd is prone to authentication spoofing vulnerability.","Installed version: 3.2.8.1
Fixed version:     3.2.10.7

",1.3.6.1.4.1.25623.1.0.809883,"CVE-2016-7144",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,87ef1c3b-3a22-4e59-8457-b28cddbfdea5,"Successful exploitation of this vulnerability
  will allow remote attackers to spoof certificate fingerprints and consequently
  log in as another user.","Update to version 3.2.10.7, 4.0.6 or later.","UnrealIRCd before 3.2.10.7 and
  4.x before 4.0.6.","The flaw exists due to an error in
  the 'm_authenticate' function in 'modules/m_sasl.c' script.","Checks if a vulnerable version is present on the target host.
Details:
UnrealIRCd Authentication Spoofing Vulnerability
(OID: 1.3.6.1.4.1.25623.1.0.809883)
Version used: 2025-12-17T05:46:28Z
","Product: cpe:/a:unrealircd:unrealircd:3.2.8.1
Method: UnrealIRCd Detection
(OID: 1.3.6.1.4.1.25623.1.0.809884)
","","",""
192.168.64.3,,80,tcp,7.5,High,95,"VendorFix","PHP < 5.3.13, 5.4.x < 5.4.3 Multiple Vulnerabilities - Active Check","PHP is prone to multiple vulnerabilities.","By doing the following HTTP POST request:

""HTTP POST"" body : <?php phpinfo();?>
URL              : http://192.168.64.3/cgi-bin/php?%2D%64+%61%6C%6C%6F%77%5F%75%72%6C%5F%69%6E%63%6C%75%64%65%3D%6F%6E+%2D%64+%73%61%66%65%5F%6D%6F%64%65%3D%6F%66%66+%2D%64+%73%75%68%6F%73%69%6E%2E%73%69%6D%75%6C%61%74%69%6F%6E%3D%6F%6E+%2D%64+%64%69%73%61%62%6C%65%5F%66%75%6E%63%74%69%6F%6E%73%3D%22%22+%2D%64+%6F%70%65%6E%5F%62%61%73%65%64%69%72%3D%6E%6F%6E%65+%2D%64+%61%75%74%6F%5F%70%72%65%70%65%6E%64%5F%66%69%6C%65%3D%70%68%70%3A%2F%2F%69%6E%70%75%74+%2D%64+%63%67%69%2E%66%6F%72%63%65%5F%72%65%64%69%72%65%63%74%3D%30+%2D%64+%63%67%69%2E%72%65%64%69%72%65%63%74%5F%73%74%61%74%75%73%5F%65%6E%76%3D%30+%2D%6E

it was possible to execute the ""<?php phpinfo();?>"" command.

Result:
  <title>phpinfo()</title><meta name=""ROBOTS"" content=""NOINDEX,NOFOLLOW,NOARCHIVE"" /></head>
  <tr><td class=""e"">Configuration File (php.ini) Path </td><td class=""v"">/etc/php5/cgi </td></tr>
  <h2>PHP Core</h2>
  <h2>PHP Variables</h2>
",1.3.6.1.4.1.25623.1.0.103482,"CVE-2012-1823,CVE-2012-2311,CVE-2012-2336,CVE-2012-2335",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,f563927c-53c9-44b8-8c17-726aa370d5c1,"Exploiting this issue allows remote attackers to view the source
  code of files in the context of the server process. This may allow the attacker to obtain
  sensitive information and to run arbitrary PHP code on the affected computer. Other attacks are
  also possible.","PHP: Update to version 5.3.13, 5.4.3 or later

  - Other products / applications: Please contact the vendor for a solution","PHP versions prior to 5.3.13 and 5.4.x prior to 5.4.3.

  Other products / applications might be affected by the tested CVE-2012-1823 as well.","When PHP is used in a CGI-based setup (such as Apache's
  mod_cgid), the php-cgi receives a processed query string parameter as command line arguments which
  allows command-line switches, such as -s, -d or -c to be passed to the php-cgi binary, which can
  be exploited to disclose source code and obtain arbitrary code execution.

  An example of the -s command, allowing an attacker to view the source code of index.php is below:

  http://example.com/index.php?-s","Send multiple a crafted HTTP POST requests and checks the
  responses.

  Notes:

  - This script checks for the presence of CVE-2012-1823 which indicates that the system is also
  affected by the other included CVEs.

  - It is currently expected that a result of this VT is reported if the system is generally
  exposing a phpinfo() output on the relevant URL / endpoint (independent from the running product).
  Exposing such sensitive information is generally seen as a security misconfiguration and should be
  avoided.
Details:
PHP < 5.3.13, 5.4.x < 5.4.3 Multiple Vulnerabilities - Active Check
(OID: 1.3.6.1.4.1.25623.1.0.103482)
Version used: 2026-04-23T06:21:05Z
","","","DFN-CERT-2013-1494,DFN-CERT-2012-1316,DFN-CERT-2012-1276,DFN-CERT-2012-1268,DFN-CERT-2012-1267,DFN-CERT-2012-1266,DFN-CERT-2012-1173,DFN-CERT-2012-1101,DFN-CERT-2012-0994,DFN-CERT-2012-0993,DFN-CERT-2012-0992,DFN-CERT-2012-0920,DFN-CERT-2012-0915,DFN-CERT-2012-0914,DFN-CERT-2012-0913,DFN-CERT-2012-0907,DFN-CERT-2012-0906,DFN-CERT-2012-0900,DFN-CERT-2012-0880,DFN-CERT-2012-0878",""
192.168.64.3,,6697,tcp,7.5,High,70,"VendorFix","UnrealIRCd Backdoor","Detection of backdoor in UnrealIRCd.","Vulnerability was detected according to the Vulnerability Detection Method.",1.3.6.1.4.1.25623.1.0.80111,"CVE-2010-2075",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,b491273e-8faf-4cec-ac09-7162b5d08708,"","Install latest version of unrealircd and check signatures of
  software you're installing.","The issue affects Unreal 3.2.8.1 for Linux. Reportedly package
  Unreal3.2.8.1.tar.gz downloaded in November 2009 and later is affected. The MD5 sum of the
  affected file is 752e46f2d873c1679fa99de3f52a274d. Files with MD5 sum of
  7b741e94e867c0a7370553fd01506c66 are not affected.","Remote attackers can exploit this issue to execute arbitrary
  system commands within the context of the affected application.","
Details:
UnrealIRCd Backdoor
(OID: 1.3.6.1.4.1.25623.1.0.80111)
Version used: 2025-03-21T05:38:29Z
","Product: cpe:/a:unrealircd:unrealircd:3.2.8.1
Method: UnrealIRCd Detection
(OID: 1.3.6.1.4.1.25623.1.0.809884)
","","",""
192.168.64.3,,2121,tcp,7.5,High,95,"Mitigation","FTP Brute Force Logins With Default Credentials Reporting","It was possible to login into the remote FTP server using
  weak/known credentials.","It was possible to login with the following credentials <User>:<Password>

msfadmin:msfadmin
postgres:postgres
service:service
user:user
",1.3.6.1.4.1.25623.1.0.108718,"CVE-1999-0501,CVE-1999-0502,CVE-1999-0507,CVE-1999-0508,CVE-2001-1594,CVE-2013-7404,CVE-2014-9198,CVE-2015-7261,CVE-2016-8731,CVE-2017-8218,CVE-2018-9068,CVE-2018-17771,CVE-2018-19063,CVE-2018-19064,CVE-2018-25147,CVE-2020-36915",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,fed6b041-e2f7-4e7d-8eb3-1a56c67be6b3,"This issue may be exploited by a remote attacker to e.g. gain
  access to sensitive information or modify system configuration.","Change the password as soon as possible.","","The following devices are / software is known to be affected:

  - CVE-2001-1594: Codonics printer FTP service as used in GE Healthcare eNTEGRA P&R

  - CVE-2013-7404: GE Healthcare Discovery NM 750b

  - CVE-2014-9198: Schneider Electric ETG3000 FactoryCast HMI gateways

  - CVE-2015-7261: QNAP iArtist Lite distributed with QNAP Signage Station

  - CVE-2016-8731: Foscam C1 devices

  - CVE-2017-8218: vsftpd on TP-Link C2 and C20i devices

  - CVE-2018-9068: IMM2 for IBM and Lenovo System x

  - CVE-2018-17771: Ingenico Telium 2 PoS terminals

  - CVE-2018-19063, CVE-2018-19064: Foscam C2 and Opticam i5 devices

  - CVE-2018-25147: Microhard Systems IPn4G

  - CVE-2020-36915: Adtec Digital SignEdje Digital Signage Player

  Note: As the VT 'FTP Brute Force Logins With Default Credentials' (OID:
  1.3.6.1.4.1.25623.1.0.108717) might run into a timeout the actual reporting of this vulnerability
  takes place in this VT instead.","Reports weak/known credentials detected by the VT
  'FTP Brute Force Logins With Default Credentials' (OID: 1.3.6.1.4.1.25623.1.0.108717).
Details:
FTP Brute Force Logins With Default Credentials Reporting
(OID: 1.3.6.1.4.1.25623.1.0.108718)
Version used: 2026-01-16T15:42:49Z
","","","",""
192.168.64.3,,21,tcp,7.5,High,95,"Mitigation","FTP Brute Force Logins With Default Credentials Reporting","It was possible to login into the remote FTP server using
  weak/known credentials.","It was possible to login with the following credentials <User>:<Password>

msfadmin:msfadmin
postgres:postgres
service:service
user:user
",1.3.6.1.4.1.25623.1.0.108718,"CVE-1999-0501,CVE-1999-0502,CVE-1999-0507,CVE-1999-0508,CVE-2001-1594,CVE-2013-7404,CVE-2014-9198,CVE-2015-7261,CVE-2016-8731,CVE-2017-8218,CVE-2018-9068,CVE-2018-17771,CVE-2018-19063,CVE-2018-19064,CVE-2018-25147,CVE-2020-36915",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,f3d091f0-465b-4af5-87b1-1e2711b2d903,"This issue may be exploited by a remote attacker to e.g. gain
  access to sensitive information or modify system configuration.","Change the password as soon as possible.","","The following devices are / software is known to be affected:

  - CVE-2001-1594: Codonics printer FTP service as used in GE Healthcare eNTEGRA P&R

  - CVE-2013-7404: GE Healthcare Discovery NM 750b

  - CVE-2014-9198: Schneider Electric ETG3000 FactoryCast HMI gateways

  - CVE-2015-7261: QNAP iArtist Lite distributed with QNAP Signage Station

  - CVE-2016-8731: Foscam C1 devices

  - CVE-2017-8218: vsftpd on TP-Link C2 and C20i devices

  - CVE-2018-9068: IMM2 for IBM and Lenovo System x

  - CVE-2018-17771: Ingenico Telium 2 PoS terminals

  - CVE-2018-19063, CVE-2018-19064: Foscam C2 and Opticam i5 devices

  - CVE-2018-25147: Microhard Systems IPn4G

  - CVE-2020-36915: Adtec Digital SignEdje Digital Signage Player

  Note: As the VT 'FTP Brute Force Logins With Default Credentials' (OID:
  1.3.6.1.4.1.25623.1.0.108717) might run into a timeout the actual reporting of this vulnerability
  takes place in this VT instead.","Reports weak/known credentials detected by the VT
  'FTP Brute Force Logins With Default Credentials' (OID: 1.3.6.1.4.1.25623.1.0.108717).
Details:
FTP Brute Force Logins With Default Credentials Reporting
(OID: 1.3.6.1.4.1.25623.1.0.108718)
Version used: 2026-01-16T15:42:49Z
","","","",""
192.168.64.3,,514,tcp,7.5,High,80,"Mitigation","rsh Unencrypted Cleartext Login","This remote host is running a rsh service.","The rsh service is misconfigured so it is allowing connections without a password or with default root:root credentials.
",1.3.6.1.4.1.25623.1.0.100080,"CVE-1999-0651",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,63d84037-0d65-4180-bb6d-45ba9d78ea1b,"","Disable the rsh service and use alternatives like SSH
  instead.","","rsh (remote shell) is a command line computer program which can
  execute shell commands as another user, and on another computer across a computer network.

  Remark: NIST don't see 'configuration issues' as software flaws so the referenced CVE has a
  severity of 0.0. The severity of this VT has been raised by Greenbone to still report a
  configuration issue on the target.","
Details:
rsh Unencrypted Cleartext Login
(OID: 1.3.6.1.4.1.25623.1.0.100080)
Version used: 2021-10-20T09:03:29Z
","","","",""
192.168.64.3,,80,tcp,7.5,High,99,"Mitigation","Test HTTP dangerous methods","Misconfigured web servers allows remote clients to perform
  dangerous HTTP methods such as PUT and DELETE.","We could upload the following files via the PUT method at this web server:

http://192.168.64.3/dav/puttest1679092686.html

We could delete the following files via the DELETE method at this web server:

http://192.168.64.3/dav/puttest1679092686.html


",1.3.6.1.4.1.25623.1.0.10498,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,6c04693c-140c-442b-ab24-5a2296f5c459,"'- Enabled PUT method: This might allow an attacker to upload
  and run arbitrary code on this web server.

  - Enabled DELETE method: This might allow an attacker to delete additional files on this web
  server.","Use access restrictions to these dangerous HTTP methods
  or disable them completely.","Web servers with enabled PUT and/or DELETE methods.","","Checks if dangerous HTTP methods such as PUT and DELETE are
  enabled and can be misused to upload or delete files.
Details:
Test HTTP dangerous methods
(OID: 1.3.6.1.4.1.25623.1.0.10498)
Version used: 2023-08-01T13:29:10Z
","","","",""
192.168.64.3,,80,tcp,7.5,High,99,"WillNotFix","EasyPHP Webserver <= 12.1 Multiple Vulnerabilities - Active Check","EasyPHP Webserver is prone to multiple vulnerabilities.","Vulnerable URL: http://192.168.64.3/phpinfo.php
Concluded from:
  <title>phpinfo()</title><meta name=""ROBOTS"" content=""NOINDEX,NOFOLLOW,NOARCHIVE"" /></head>
  <tr><td class=""e"">Configuration File (php.ini) Path </td><td class=""v"">/etc/php5/cgi </td></tr>
  <h2>PHP Core</h2>
  <h2>PHP Variables</h2>
",1.3.6.1.4.1.25623.1.0.803189,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,ab260634-a2a1-4213-9005-8780f62fea9d,"Successful exploitation will allow attackers to gain
  administrative access, disclose the information, inject PHP code/shell and execute a remote PHP
  Code.","No known solution was made available for at least one year
  since the disclosure of this vulnerability. Likely none will be provided anymore. General solution
  options are to upgrade to a newer release, disable respective features, remove the product or
  replace the product by another one.","EasyPHP version 12.1 and prior.","The bug in EasyPHP WebServer Manager, its skipping
  authentication for certain requests. Which allows to bypass the authentication, disclose the
  information or execute a remote PHP code.","Sends a crafted HTTP GET request and checks the response.

  Note: It is currently expected that a result of this VT is reported if the system is generally
  exposing a phpinfo() output on the relevant URL / endpoint (independent from the running product).
  Exposing such sensitive information is generally seen as a security misconfiguration and should be
  avoided.
Details:
EasyPHP Webserver <= 12.1 Multiple Vulnerabilities - Active Check
(OID: 1.3.6.1.4.1.25623.1.0.803189)
Version used: 2025-11-11T05:40:18Z
","","","",""
192.168.64.3,,5432,tcp,7.4,High,70,"VendorFix","SSL/TLS: OpenSSL CCS Man in the Middle Security Bypass Vulnerability","OpenSSL is prone to a security bypass vulnerability.","Vulnerability was detected according to the Vulnerability Detection Method.",1.3.6.1.4.1.25623.1.0.105042,"CVE-2014-0224",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,65f68c3d-cb15-4817-ae52-9b013dc3792e,"Successfully exploiting this issue may allow attackers to obtain
  sensitive information by conducting a man-in-the-middle attack. This may lead to other attacks.","Updates are available. Please see the references for more information.","OpenSSL before 0.9.8za, 1.0.0 before 1.0.0m and 1.0.1 before 1.0.1h.","OpenSSL does not properly restrict processing of ChangeCipherSpec
  messages, which allows man-in-the-middle attackers to trigger use of a zero-length master key in
  certain OpenSSL-to-OpenSSL communications, and consequently hijack sessions or obtain sensitive
  information, via a crafted TLS handshake, aka the 'CCS Injection' vulnerability.","Send two SSL ChangeCipherSpec request and check the response.
Details:
SSL/TLS: OpenSSL CCS Man in the Middle Security Bypass Vulnerability
(OID: 1.3.6.1.4.1.25623.1.0.105042)
Version used: 2025-01-17T15:39:18Z
","","","DFN-CERT-2016-0388,DFN-CERT-2015-0593,DFN-CERT-2015-0427,DFN-CERT-2015-0396,DFN-CERT-2015-0082,DFN-CERT-2015-0079,DFN-CERT-2015-0078,DFN-CERT-2014-1717,DFN-CERT-2014-1632,DFN-CERT-2014-1364,DFN-CERT-2014-1357,DFN-CERT-2014-1350,DFN-CERT-2014-1265,DFN-CERT-2014-1209,DFN-CERT-2014-0917,DFN-CERT-2014-0789,DFN-CERT-2014-0778,DFN-CERT-2014-0768,DFN-CERT-2014-0752,DFN-CERT-2014-0747,DFN-CERT-2014-0738,DFN-CERT-2014-0715,DFN-CERT-2014-0714,DFN-CERT-2014-0709,WID-SEC-2026-0180,WID-SEC-2023-0500,CB-K15/0567,CB-K15/0415,CB-K15/0384,CB-K15/0080,CB-K15/0079,CB-K15/0074,CB-K14/1617,CB-K14/1537,CB-K14/1299,CB-K14/1297,CB-K14/1294,CB-K14/1202,CB-K14/1174,CB-K14/1153,CB-K14/0876,CB-K14/0756,CB-K14/0746,CB-K14/0736,CB-K14/0722,CB-K14/0716,CB-K14/0708,CB-K14/0684,CB-K14/0683,CB-K14/0680",""
192.168.64.3,,25,tcp,6.8,Medium,99,"VendorFix","Multiple Vendors STARTTLS Implementation Plaintext Arbitrary Command Injection Vulnerability","Multiple vendors' implementations of 'STARTTLS' are prone to a
  vulnerability that lets attackers inject arbitrary commands.","Vulnerability was detected according to the Vulnerability Detection Method.",1.3.6.1.4.1.25623.1.0.103935,"CVE-2011-0411,CVE-2011-1430,CVE-2011-1431,CVE-2011-1432,CVE-2011-1506,CVE-2011-1575,CVE-2011-1926,CVE-2011-2165",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,d05c4f12-e6dd-488e-a234-1cc73ea7387d,"An attacker can exploit this issue to execute arbitrary commands
  in the context of the user running the application. Successful exploits can allow attackers to
  obtain email usernames and passwords.","Updates are available. Please see the references for more
  information.","The following vendors are known to be affected:

  Ipswitch

  Kerio

  Postfix

  Qmail-TLS

  Oracle

  SCO Group

  spamdyke

  ISC","","Send a special crafted 'STARTTLS' request and check the
  response.
Details:
Multiple Vendors STARTTLS Implementation Plaintext Arbitrary Command Injecti...
(OID: 1.3.6.1.4.1.25623.1.0.103935)
Version used: 2023-10-31T05:06:37Z
","","","DFN-CERT-2011-0917,DFN-CERT-2011-0912,DFN-CERT-2011-0897,DFN-CERT-2011-0844,DFN-CERT-2011-0818,DFN-CERT-2011-0808,DFN-CERT-2011-0771,DFN-CERT-2011-0741,DFN-CERT-2011-0712,DFN-CERT-2011-0673,DFN-CERT-2011-0597,DFN-CERT-2011-0596,DFN-CERT-2011-0519,DFN-CERT-2011-0516,DFN-CERT-2011-0483,DFN-CERT-2011-0434,DFN-CERT-2011-0393,DFN-CERT-2011-0381,CB-K15/1514",""
192.168.64.3,,80,tcp,6.8,Medium,80,"VendorFix","TWiki Cross-Site Request Forgery Vulnerability (Sep 2010)","TWiki is prone to a cross-site request forgery (CSRF) vulnerability.","Installed version: 01.Feb.2003
Fixed version:     4.3.2

",1.3.6.1.4.1.25623.1.0.801281,"CVE-2009-4898",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,68aa1b7f-6a12-44c1-b45b-6db3ad8165c8,"Successful exploitation will allow attacker to gain administrative
  privileges on the target application and can cause CSRF attack.","Upgrade to TWiki version 4.3.2 or later.","TWiki version prior to 4.3.2","Attack can be done by tricking an authenticated TWiki user into visiting
  a static HTML page on another side, where a Javascript enabled browser will send an HTTP POST request
  to TWiki, which in turn will process the request as the TWiki user.","
Details:
TWiki Cross-Site Request Forgery Vulnerability (Sep 2010)
(OID: 1.3.6.1.4.1.25623.1.0.801281)
Version used: 2024-03-01T14:37:10Z
","","","",""
192.168.64.3,,21,tcp,6.4,Medium,80,"Mitigation","Anonymous FTP Login Reporting","Reports if the remote FTP Server allows anonymous logins.","It was possible to login to the remote FTP service with the following anonymous account(s):

anonymous:anonymous@example.com
ftp:anonymous@example.com

",1.3.6.1.4.1.25623.1.0.900600,"CVE-1999-0497",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,35b0b5f0-30fe-4e07-98cc-814f5e4f88ae,"Based on the files accessible via this anonymous FTP login and
  the permissions of this account an attacker might be able to:

  - gain access to sensitive files

  - upload or delete files.","If you do not want to share files, you should disable anonymous
  logins.","","A host that provides an FTP service may additionally provide
  Anonymous FTP access as well. Under this arrangement, users do not strictly need an account on the
  host. Instead the user typically enters 'anonymous' or 'ftp' when prompted for username. Although
  users are commonly asked to send their email address as their password, little to no verification
  is actually performed on the supplied data.

  Remark: NIST don't see 'configuration issues' as software flaws so the referenced CVE has a
  severity of 0.0. The severity of this VT has been raised by Greenbone to still report a
  configuration issue on the target.","
Details:
Anonymous FTP Login Reporting
(OID: 1.3.6.1.4.1.25623.1.0.900600)
Version used: 2021-10-20T09:03:29Z
","","","",""
192.168.64.3,,80,tcp,6.1,Medium,80,"VendorFix","jQuery < 1.9.0 XSS Vulnerability","jQuery is prone to a cross-site scripting (XSS)
  vulnerability.","Installed version: 1.3.2
Fixed version:     1.9.0
Installation
path / port:       /mutillidae/javascript/ddsmoothmenu/jquery.min.js

Detection info (see OID: 1.3.6.1.4.1.25623.1.0.150658 for more info):
- Identified file: http://192.168.64.3/mutillidae/javascript/ddsmoothmenu/jquery.min.js
- Referenced at:   http://192.168.64.3/mutillidae/
",1.3.6.1.4.1.25623.1.0.141636,"CVE-2012-6708",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,94e9b7e2-27fe-49cb-bdf9-05218dfcd3bc,"","Update to version 1.9.0 or later.","jQuery prior to version 1.9.0.","The jQuery(strInput) function does not differentiate selectors
  from HTML in a reliable fashion. In vulnerable versions, jQuery determined whether the input was
  HTML by looking for the '<' character anywhere in the string, giving attackers more flexibility
  when attempting to construct a malicious payload. In fixed versions, jQuery only deems the input
  to be HTML if it explicitly starts with the '<' character, limiting exploitability only to
  attackers who can control the beginning of a string, which is far less common.","Checks if a vulnerable version is present on the target host.
Details:
jQuery < 1.9.0 XSS Vulnerability
(OID: 1.3.6.1.4.1.25623.1.0.141636)
Version used: 2023-07-14T05:06:08Z
","","","DFN-CERT-2025-1803,DFN-CERT-2023-1197,DFN-CERT-2020-0590,WID-SEC-2026-1752,WID-SEC-2022-0673,CB-K22/0045,CB-K18/1131",""
192.168.64.3,,80,tcp,6.1,Medium,80,"VendorFix","TWiki < 6.1.0 XSS Vulnerability","bin/statistics in TWiki 6.0.2 allows XSS via the webs parameter.","Installed version: 01.Feb.2003
Fixed version:     6.1.0

",1.3.6.1.4.1.25623.1.0.141830,"CVE-2018-20212",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,11e3101d-6e01-4925-a9c3-2d50adac22d2,"","Update to version 6.1.0 or later.","TWiki version 6.0.2 and probably prior.","","Checks if a vulnerable version is present on the target host.
Details:
TWiki < 6.1.0 XSS Vulnerability
(OID: 1.3.6.1.4.1.25623.1.0.141830)
Version used: 2023-07-14T16:09:27Z
","","","",""
192.168.64.3,,80,tcp,6.0,Medium,80,"VendorFix","TWiki CSRF Vulnerability","TWiki is prone to a cross-site request forgery (CSRF) vulnerability.","Installed version: 01.Feb.2003
Fixed version:     4.3.1

",1.3.6.1.4.1.25623.1.0.800400,"CVE-2009-1339",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,86ca4f00-0104-4f21-8408-8bee254438ec,"Successful exploitation will allow attacker to gain administrative
  privileges on the target application and can cause CSRF attack.","Upgrade to version 4.3.1 or later.","TWiki version prior to 4.3.1","Remote authenticated user can create a specially crafted image tag that,
  when viewed by the target user, will update pages on the target system with the privileges of the target user
  via HTTP requests.","
Details:
TWiki CSRF Vulnerability
(OID: 1.3.6.1.4.1.25623.1.0.800400)
Version used: 2024-06-28T05:05:33Z
","","","",""
192.168.64.3,,5432,tcp,5.9,Medium,98,"Mitigation","SSL/TLS: Deprecated SSLv2 and SSLv3 Protocol Detection","It was possible to detect the usage of the deprecated SSLv2
  and/or SSLv3 protocol on this system.","In addition to TLSv1.0+ the service is also providing the deprecated SSLv3 protocol and supports one or more ciphers. Those supported ciphers can be found in the 'SSL/TLS: Report Supported Cipher Suites' (OID: 1.3.6.1.4.1.25623.1.0.802067) VT.
",1.3.6.1.4.1.25623.1.0.111012,"CVE-2016-0800,CVE-2014-3566",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,3911f7c0-02a9-44b6-9646-092820f62055,"An attacker might be able to use the known cryptographic flaws to
  eavesdrop the connection between clients and the service to get access to sensitive data
  transferred within the secured connection.

  Furthermore newly uncovered vulnerabilities in this protocols won't receive security updates
  anymore.","It is recommended to disable the deprecated SSLv2 and/or SSLv3
  protocols in favor of the TLSv1.2+ protocols.

  Please see the references for more resources supporting you with this task.","All services providing an encrypted communication using the
  SSLv2 and/or SSLv3 protocols.","The SSLv2 and SSLv3 protocols contain known cryptographic flaws
  like:

  - CVE-2014-3566: Padding Oracle On Downgraded Legacy Encryption (POODLE)

  - CVE-2016-0800: Decrypting RSA with Obsolete and Weakened eNcryption (DROWN)","Checks the used SSL protocols of the services provided by this
  system.
Details:
SSL/TLS: Deprecated SSLv2 and SSLv3 Protocol Detection
(OID: 1.3.6.1.4.1.25623.1.0.111012)
Version used: 2026-06-03T07:18:10Z
","Product: cpe:/a:ietf:transport_layer_security:1.0
Method: SSL/TLS: Version Detection
(OID: 1.3.6.1.4.1.25623.1.0.105782)
","","DFN-CERT-2018-0096,DFN-CERT-2017-1238,DFN-CERT-2017-1236,DFN-CERT-2016-1929,DFN-CERT-2016-1527,DFN-CERT-2016-1468,DFN-CERT-2016-1216,DFN-CERT-2016-1174,DFN-CERT-2016-1168,DFN-CERT-2016-0884,DFN-CERT-2016-0841,DFN-CERT-2016-0644,DFN-CERT-2016-0642,DFN-CERT-2016-0496,DFN-CERT-2016-0495,DFN-CERT-2016-0465,DFN-CERT-2016-0459,DFN-CERT-2016-0453,DFN-CERT-2016-0451,DFN-CERT-2016-0415,DFN-CERT-2016-0403,DFN-CERT-2016-0388,DFN-CERT-2016-0360,DFN-CERT-2016-0359,DFN-CERT-2016-0357,DFN-CERT-2016-0171,DFN-CERT-2015-1431,DFN-CERT-2015-1075,DFN-CERT-2015-1026,DFN-CERT-2015-0664,DFN-CERT-2015-0548,DFN-CERT-2015-0404,DFN-CERT-2015-0396,DFN-CERT-2015-0259,DFN-CERT-2015-0254,DFN-CERT-2015-0245,DFN-CERT-2015-0118,DFN-CERT-2015-0114,DFN-CERT-2015-0083,DFN-CERT-2015-0082,DFN-CERT-2015-0081,DFN-CERT-2015-0076,DFN-CERT-2014-1717,DFN-CERT-2014-1680,DFN-CERT-2014-1632,DFN-CERT-2014-1564,DFN-CERT-2014-1542,DFN-CERT-2014-1414,DFN-CERT-2014-1366,DFN-CERT-2014-1354,WID-SEC-2026-0180,WID-SEC-2025-1658,WID-SEC-2023-0431,WID-SEC-2023-0427,CB-K18/0094,CB-K17/1198,CB-K17/1196,CB-K16/1828,CB-K16/1438,CB-K16/1384,CB-K16/1141,CB-K16/1107,CB-K16/1102,CB-K16/0792,CB-K16/0599,CB-K16/0597,CB-K16/0459,CB-K16/0456,CB-K16/0433,CB-K16/0424,CB-K16/0415,CB-K16/0413,CB-K16/0374,CB-K16/0367,CB-K16/0331,CB-K16/0329,CB-K16/0328,CB-K16/0156,CB-K15/1514,CB-K15/1358,CB-K15/1021,CB-K15/0972,CB-K15/0637,CB-K15/0590,CB-K15/0525,CB-K15/0393,CB-K15/0384,CB-K15/0287,CB-K15/0252,CB-K15/0246,CB-K15/0237,CB-K15/0118,CB-K15/0110,CB-K15/0108,CB-K15/0080,CB-K15/0078,CB-K15/0077,CB-K15/0075,CB-K14/1617,CB-K14/1581,CB-K14/1537,CB-K14/1479,CB-K14/1458,CB-K14/1342,CB-K14/1314,CB-K14/1313,CB-K14/1311,CB-K14/1304,CB-K14/1296",""
192.168.64.3,,5432,tcp,5.9,Medium,98,"Mitigation","SSL/TLS: Report Weak Cipher Suites","This routine reports all weak SSL/TLS cipher suites accepted by
  a service.","'Weak' cipher suites accepted by this service via the SSLv3 protocol:

TLS_RSA_WITH_RC4_128_SHA

'Weak' cipher suites accepted by this service via the TLSv1.0 protocol:

TLS_RSA_WITH_RC4_128_SHA


",1.3.6.1.4.1.25623.1.0.103440,"CVE-2013-2566,CVE-2015-2808,CVE-2015-4000",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,949f3573-1e54-4118-bacd-f2fac08e3734,"This could allow remote attackers to obtain sensitive information
  or have other, unspecified impacts.","The configuration of this services should be changed so that it
  does not accept the listed weak cipher suites anymore.

  Please see the references for more resources supporting you with this task.","All services providing an encrypted communication using weak
  SSL/TLS cipher suites.","These rules are applied for the evaluation of the cryptographic
  strength:

  - RC4 is considered to be weak (CVE-2013-2566, CVE-2015-2808)

  - Ciphers using 64 bit or less are considered to be vulnerable to brute force methods and
  therefore considered as weak (CVE-2015-4000)

  - 1024 bit RSA authentication is considered to be insecure and therefore as weak

  - Any cipher considered to be secure for only the next 10 years is considered as medium

  - Any other cipher is considered as strong","Checks previous collected cipher suites.

  NOTE: No severity for SMTP services with 'Opportunistic TLS' and weak cipher suites on port 25/tcp
  is reported. If too strong cipher suites are configured for this service the alternative would be
  to fall back to an even more insecure cleartext communication.
Details:
SSL/TLS: Report Weak Cipher Suites
(OID: 1.3.6.1.4.1.25623.1.0.103440)
Version used: 2026-06-03T07:18:10Z
","Product: cpe:/a:ietf:transport_layer_security
Method: SSL/TLS: Report Supported Cipher Suites
(OID: 1.3.6.1.4.1.25623.1.0.802067)
","","DFN-CERT-2023-2939,DFN-CERT-2021-0775,DFN-CERT-2020-1561,DFN-CERT-2020-1276,DFN-CERT-2017-1821,DFN-CERT-2016-1692,DFN-CERT-2016-1648,DFN-CERT-2016-1168,DFN-CERT-2016-0665,DFN-CERT-2016-0642,DFN-CERT-2016-0184,DFN-CERT-2016-0135,DFN-CERT-2016-0101,DFN-CERT-2016-0035,DFN-CERT-2015-1853,DFN-CERT-2015-1679,DFN-CERT-2015-1632,DFN-CERT-2015-1608,DFN-CERT-2015-1542,DFN-CERT-2015-1518,DFN-CERT-2015-1406,DFN-CERT-2015-1341,DFN-CERT-2015-1194,DFN-CERT-2015-1144,DFN-CERT-2015-1113,DFN-CERT-2015-1078,DFN-CERT-2015-1067,DFN-CERT-2015-1038,DFN-CERT-2015-1016,DFN-CERT-2015-1012,DFN-CERT-2015-0980,DFN-CERT-2015-0977,DFN-CERT-2015-0976,DFN-CERT-2015-0960,DFN-CERT-2015-0956,DFN-CERT-2015-0944,DFN-CERT-2015-0937,DFN-CERT-2015-0925,DFN-CERT-2015-0884,DFN-CERT-2015-0881,DFN-CERT-2015-0879,DFN-CERT-2015-0866,DFN-CERT-2015-0844,DFN-CERT-2015-0800,DFN-CERT-2015-0737,DFN-CERT-2015-0696,DFN-CERT-2014-0977,WID-SEC-2026-0180,CB-K21/0067,CB-K19/0812,CB-K17/1750,CB-K16/1593,CB-K16/1552,CB-K16/1102,CB-K16/0617,CB-K16/0599,CB-K16/0168,CB-K16/0121,CB-K16/0090,CB-K16/0030,CB-K15/1751,CB-K15/1591,CB-K15/1550,CB-K15/1517,CB-K15/1514,CB-K15/1464,CB-K15/1442,CB-K15/1334,CB-K15/1269,CB-K15/1136,CB-K15/1090,CB-K15/1059,CB-K15/1022,CB-K15/1015,CB-K15/0986,CB-K15/0964,CB-K15/0962,CB-K15/0932,CB-K15/0927,CB-K15/0926,CB-K15/0907,CB-K15/0901,CB-K15/0896,CB-K15/0889,CB-K15/0877,CB-K15/0850,CB-K15/0849,CB-K15/0834,CB-K15/0827,CB-K15/0802,CB-K15/0764,CB-K15/0733,CB-K15/0667,CB-K14/0935,CB-K13/0942",""
192.168.64.3,,25,tcp,5.9,Medium,98,"Mitigation","SSL/TLS: Deprecated SSLv2 and SSLv3 Protocol Detection","It was possible to detect the usage of the deprecated SSLv2
  and/or SSLv3 protocol on this system.","In addition to TLSv1.0+ the service is also providing the deprecated SSLv2 and SSLv3 protocols and supports one or more ciphers. Those supported ciphers can be found in the 'SSL/TLS: Report Supported Cipher Suites' (OID: 1.3.6.1.4.1.25623.1.0.802067) VT.
",1.3.6.1.4.1.25623.1.0.111012,"CVE-2016-0800,CVE-2014-3566",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,2d4f0ea6-4417-4176-96ee-82cdeb25943c,"An attacker might be able to use the known cryptographic flaws to
  eavesdrop the connection between clients and the service to get access to sensitive data
  transferred within the secured connection.

  Furthermore newly uncovered vulnerabilities in this protocols won't receive security updates
  anymore.","It is recommended to disable the deprecated SSLv2 and/or SSLv3
  protocols in favor of the TLSv1.2+ protocols.

  Please see the references for more resources supporting you with this task.","All services providing an encrypted communication using the
  SSLv2 and/or SSLv3 protocols.","The SSLv2 and SSLv3 protocols contain known cryptographic flaws
  like:

  - CVE-2014-3566: Padding Oracle On Downgraded Legacy Encryption (POODLE)

  - CVE-2016-0800: Decrypting RSA with Obsolete and Weakened eNcryption (DROWN)","Checks the used SSL protocols of the services provided by this
  system.
Details:
SSL/TLS: Deprecated SSLv2 and SSLv3 Protocol Detection
(OID: 1.3.6.1.4.1.25623.1.0.111012)
Version used: 2026-06-03T07:18:10Z
","Product: cpe:/a:ietf:transport_layer_security:1.0
Method: SSL/TLS: Version Detection
(OID: 1.3.6.1.4.1.25623.1.0.105782)
","","DFN-CERT-2018-0096,DFN-CERT-2017-1238,DFN-CERT-2017-1236,DFN-CERT-2016-1929,DFN-CERT-2016-1527,DFN-CERT-2016-1468,DFN-CERT-2016-1216,DFN-CERT-2016-1174,DFN-CERT-2016-1168,DFN-CERT-2016-0884,DFN-CERT-2016-0841,DFN-CERT-2016-0644,DFN-CERT-2016-0642,DFN-CERT-2016-0496,DFN-CERT-2016-0495,DFN-CERT-2016-0465,DFN-CERT-2016-0459,DFN-CERT-2016-0453,DFN-CERT-2016-0451,DFN-CERT-2016-0415,DFN-CERT-2016-0403,DFN-CERT-2016-0388,DFN-CERT-2016-0360,DFN-CERT-2016-0359,DFN-CERT-2016-0357,DFN-CERT-2016-0171,DFN-CERT-2015-1431,DFN-CERT-2015-1075,DFN-CERT-2015-1026,DFN-CERT-2015-0664,DFN-CERT-2015-0548,DFN-CERT-2015-0404,DFN-CERT-2015-0396,DFN-CERT-2015-0259,DFN-CERT-2015-0254,DFN-CERT-2015-0245,DFN-CERT-2015-0118,DFN-CERT-2015-0114,DFN-CERT-2015-0083,DFN-CERT-2015-0082,DFN-CERT-2015-0081,DFN-CERT-2015-0076,DFN-CERT-2014-1717,DFN-CERT-2014-1680,DFN-CERT-2014-1632,DFN-CERT-2014-1564,DFN-CERT-2014-1542,DFN-CERT-2014-1414,DFN-CERT-2014-1366,DFN-CERT-2014-1354,WID-SEC-2026-0180,WID-SEC-2025-1658,WID-SEC-2023-0431,WID-SEC-2023-0427,CB-K18/0094,CB-K17/1198,CB-K17/1196,CB-K16/1828,CB-K16/1438,CB-K16/1384,CB-K16/1141,CB-K16/1107,CB-K16/1102,CB-K16/0792,CB-K16/0599,CB-K16/0597,CB-K16/0459,CB-K16/0456,CB-K16/0433,CB-K16/0424,CB-K16/0415,CB-K16/0413,CB-K16/0374,CB-K16/0367,CB-K16/0331,CB-K16/0329,CB-K16/0328,CB-K16/0156,CB-K15/1514,CB-K15/1358,CB-K15/1021,CB-K15/0972,CB-K15/0637,CB-K15/0590,CB-K15/0525,CB-K15/0393,CB-K15/0384,CB-K15/0287,CB-K15/0252,CB-K15/0246,CB-K15/0237,CB-K15/0118,CB-K15/0110,CB-K15/0108,CB-K15/0080,CB-K15/0078,CB-K15/0077,CB-K15/0075,CB-K14/1617,CB-K14/1581,CB-K14/1537,CB-K14/1479,CB-K14/1458,CB-K14/1342,CB-K14/1314,CB-K14/1313,CB-K14/1311,CB-K14/1304,CB-K14/1296",""
192.168.64.3,,80,tcp,5.8,Medium,99,"Mitigation","HTTP Debugging Methods (TRACE/TRACK) Enabled","The remote web server supports the TRACE and/or TRACK
  methods. TRACE and TRACK are HTTP methods which are used to debug web server connections.","The web server has the following HTTP methods enabled: TRACE
",1.3.6.1.4.1.25623.1.0.11213,"CVE-2003-1567,CVE-2004-2320,CVE-2004-2763,CVE-2005-3398,CVE-2006-4683,CVE-2007-3008,CVE-2008-7253,CVE-2009-2823,CVE-2010-0386,CVE-2012-2223,CVE-2014-7883",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,f8db9b25-75df-4228-9e9d-3979f2fb31b8,"An attacker may use this flaw to trick your legitimate web
  users to give him their credentials.","Disable the TRACE and TRACK methods in your web server
  configuration.

  Please see the manual of your web server or the references for more information.","Web servers with enabled TRACE and/or TRACK methods.","It has been shown that web servers supporting this methods
  are subject to cross-site-scripting attacks, dubbed XST for Cross-Site-Tracing, when used in
  conjunction with various weaknesses in browsers.","Checks if HTTP methods such as TRACE and TRACK are
  enabled and can be used.
Details:
HTTP Debugging Methods (TRACE/TRACK) Enabled
(OID: 1.3.6.1.4.1.25623.1.0.11213)
Version used: 2023-08-01T13:29:10Z
","","","DFN-CERT-2021-1825,DFN-CERT-2014-1018,DFN-CERT-2010-0020,CB-K14/0981",""
192.168.64.3,,22,tcp,5.3,Medium,80,"Mitigation","Weak Host Key Algorithm(s) (SSH)","The remote SSH server is configured to allow / support weak host
  key algorithm(s).","The remote SSH server supports the following weak host key algorithm(s):

host key algorithm | Description
-----------------------------------------------------------------------------------------
ssh-dss            | Digital Signature Algorithm (DSA) / Digital Signature Standard (DSS)
",1.3.6.1.4.1.25623.1.0.117687,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,f5d7791f-c5d6-40a1-a40e-20de5733ae67,"","Disable the reported weak host key algorithm(s).","","","Checks the supported host key algorithms of the remote SSH
  server.

  Currently weak host key algorithms are defined as the following:

  - ssh-dss: Digital Signature Algorithm (DSA) / Digital Signature Standard (DSS)
Details:
Weak Host Key Algorithm(s) (SSH)
(OID: 1.3.6.1.4.1.25623.1.0.117687)
Version used: 2024-06-14T05:05:48Z
","Product: cpe:/a:ietf:secure_shell_protocol
Method: SSH Protocol Algorithms Supported
(OID: 1.3.6.1.4.1.25623.1.0.105565)
","","",""
192.168.64.3,,5432,tcp,5.3,Medium,80,"Mitigation","SSL/TLS: Server Certificate / Certificate in Chain with RSA keys less than 2048 bits","The remote SSL/TLS server certificate and/or any of the
  certificates in the certificate chain is using a RSA key with less than 2048 bits.","The remote SSL/TLS server is using the following certificate(s) with a RSA key with less than 2048 bits (public-key-size:public-key-algorithm:serial:issuer):

1024:RSA:00FAF93A4C7FB6B9CC:1.2.840.113549.1.9.1=#726F6F74407562756E74753830342D626173652E6C6F63616C646F6D61696E,CN=ubuntu804-base.localdomain,OU=Office for Complication of Otherwise Simple Affairs,O=OCOSA,L=Everywhere,ST=There is no such thing outside US,C=XX (Server certificate)
",1.3.6.1.4.1.25623.1.0.150710,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,736cd489-7860-4fdb-9072-5db563d46a08,"Using certificates with weak RSA key size can lead to
  unauthorized exposure of sensitive information.","Replace the certificate with a stronger key and reissue the
  certificates it signed.","","SSL/TLS certificates using RSA keys with less than 2048 bits are
  considered unsafe.","Checks the RSA keys size of the server certificate and all
  certificates in chain for a size < 2048 bit.
Details:
SSL/TLS: Server Certificate / Certificate in Chain with RSA keys less than 2...
(OID: 1.3.6.1.4.1.25623.1.0.150710)
Version used: 2021-12-10T12:48:00Z
","","","",""
192.168.64.3,,25,tcp,5.3,Medium,80,"Mitigation","SSL/TLS: Server Certificate / Certificate in Chain with RSA keys less than 2048 bits","The remote SSL/TLS server certificate and/or any of the
  certificates in the certificate chain is using a RSA key with less than 2048 bits.","The remote SSL/TLS server is using the following certificate(s) with a RSA key with less than 2048 bits (public-key-size:public-key-algorithm:serial:issuer):

1024:RSA:00FAF93A4C7FB6B9CC:1.2.840.113549.1.9.1=#726F6F74407562756E74753830342D626173652E6C6F63616C646F6D61696E,CN=ubuntu804-base.localdomain,OU=Office for Complication of Otherwise Simple Affairs,O=OCOSA,L=Everywhere,ST=There is no such thing outside US,C=XX (Server certificate)
",1.3.6.1.4.1.25623.1.0.150710,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,63628f1b-0bcc-4443-b7b2-3d532b685f2a,"Using certificates with weak RSA key size can lead to
  unauthorized exposure of sensitive information.","Replace the certificate with a stronger key and reissue the
  certificates it signed.","","SSL/TLS certificates using RSA keys with less than 2048 bits are
  considered unsafe.","Checks the RSA keys size of the server certificate and all
  certificates in chain for a size < 2048 bit.
Details:
SSL/TLS: Server Certificate / Certificate in Chain with RSA keys less than 2...
(OID: 1.3.6.1.4.1.25623.1.0.150710)
Version used: 2021-12-10T12:48:00Z
","","","",""
192.168.64.3,,80,tcp,5.3,Medium,80,"Workaround","phpinfo() Output Reporting (HTTP)","Reporting of files containing the output of the phpinfo() PHP
  function previously detected via HTTP.","The following files are calling the function phpinfo() which disclose potentially sensitive information:

http://192.168.64.3/mutillidae/phpinfo.php
Concluded from:
  <title>phpinfo()</title><meta name=""ROBOTS"" content=""NOINDEX,NOFOLLOW,NOARCHIVE"" /></head>
  <tr><td class=""e"">Configuration File (php.ini) Path </td><td class=""v"">/etc/php5/cgi </td></tr>
  <h2>PHP Core</h2>
  <h2>PHP Variables</h2>

http://192.168.64.3/phpinfo.php
Concluded from:
  <title>phpinfo()</title><meta name=""ROBOTS"" content=""NOINDEX,NOFOLLOW,NOARCHIVE"" /></head>
  <tr><td class=""e"">Configuration File (php.ini) Path </td><td class=""v"">/etc/php5/cgi </td></tr>
  <h2>PHP Core</h2>
  <h2>PHP Variables</h2>
",1.3.6.1.4.1.25623.1.0.11229,"CVE-2008-0149,CVE-2023-49282,CVE-2023-49283,CVE-2024-10486",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,82c08947-7e19-47f1-bec9-0866adf2c874,"Some of the information that can be gathered from this file
  includes:

  The username of the user running the PHP process, if it is a sudo user, the IP address of the
  host, the web server version, the system version (Unix, Linux, Windows, ...), and the root
  directory of the web server.","Delete the listed files or restrict access to them.","All systems exposing a file containing the output of the
  phpinfo() PHP function.

  This VT is also reporting if an affected endpoint for the following products have been identified:

  - CVE-2008-0149: TUTOS

  - CVE-2023-49282, CVE-2023-49283: Microsoft Graph PHP SDK

  - CVE-2024-10486: Google for WooCommerce plugin for WordPress","Many PHP installation tutorials instruct the user to create a
  file called phpinfo.php or similar containing the phpinfo() statement. Such a file is often left
  back in the webserver directory.","This script reports files identified by the following separate
  VT: 'phpinfo() Output Detection (HTTP)' (OID: 1.3.6.1.4.1.25623.1.0.108474).
Details:
phpinfo() Output Reporting (HTTP)
(OID: 1.3.6.1.4.1.25623.1.0.11229)
Version used: 2025-07-09T05:43:50Z
","","","",""
192.168.64.3,,22,tcp,5.3,Medium,80,"Mitigation","Weak Key Exchange (KEX) Algorithm(s) Supported (SSH)","The remote SSH server is configured to allow / support weak key
  exchange (KEX) algorithm(s).","The remote SSH server supports the following weak KEX algorithm(s):

KEX algorithm                      | Reason
-------------------------------------------------------------------------------------------
diffie-hellman-group-exchange-sha1 | Using SHA-1
diffie-hellman-group1-sha1         | Using Oakley Group 2 (a 1024-bit MODP group) and SHA-1
",1.3.6.1.4.1.25623.1.0.150713,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,b4a8e983-10cd-4e63-93a1-acd535d41b39,"An attacker can quickly break individual connections.","Disable the reported weak KEX algorithm(s)

  - 1024-bit MODP group / prime KEX algorithms:

  Alternatively use elliptic-curve Diffie-Hellmann in general, e.g. Curve 25519.","","'- 1024-bit MODP group / prime KEX algorithms:

  Millions of HTTPS, SSH, and VPN servers all use the same prime numbers for Diffie-Hellman key
  exchange. Practitioners believed this was safe as long as new key exchange messages were generated
  for every connection. However, the first step in the number field sieve-the most efficient
  algorithm for breaking a Diffie-Hellman connection-is dependent only on this prime.

  A nation-state can break a 1024-bit prime.","Checks the supported KEX algorithms of the remote SSH server.

  Currently weak KEX algorithms are defined as the following:

  - non-elliptic-curve Diffie-Hellmann (DH) KEX algorithms with 1024-bit MODP group / prime

  - ephemerally generated key exchange groups uses SHA-1

  - using RSA 1024-bit modulus key
Details:
Weak Key Exchange (KEX) Algorithm(s) Supported (SSH)
(OID: 1.3.6.1.4.1.25623.1.0.150713)
Version used: 2024-06-14T05:05:48Z
","Product: cpe:/a:ietf:secure_shell_protocol
Method: SSH Protocol Algorithms Supported
(OID: 1.3.6.1.4.1.25623.1.0.105565)
","","",""
192.168.64.3,,25,tcp,5.0,Medium,99,"Workaround","Check if Mailserver answer to VRFY and EXPN requests","The Mailserver on this host answers to VRFY and/or EXPN requests.","'VRFY root' produces the following answer: 252 2.0.0 root


",1.3.6.1.4.1.25623.1.0.100072,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,ddadb95d-295a-4bd2-bcdb-eda5d730759c,"","Disable VRFY and/or EXPN on your Mailserver.

  For postfix add 'disable_vrfy_command=yes' in 'main.cf'.

  For Sendmail add the option 'O PrivacyOptions=goaway'.

  It is suggested that, if you really want to publish this type of information, you use a mechanism
  that legitimate users actually know about, such as Finger or HTTP.","","VRFY and EXPN ask the server for information about an address. They are
  inherently unusable through firewalls, gateways, mail exchangers for part-time hosts, etc.","
Details:
Check if Mailserver answer to VRFY and EXPN requests
(OID: 1.3.6.1.4.1.25623.1.0.100072)
Version used: 2023-10-31T05:06:37Z
","","","",""
192.168.64.3,,80,tcp,5.0,Medium,99,"WillNotFix","QWikiwiki directory traversal vulnerability","The remote host is running QWikiwiki, a Wiki application written in PHP.

  The remote version of this software contains a validation input flaw which may allow an attacker
  to use it to read arbitrary files on the remote host with the privileges of the web server.","Vulnerable URL: http://192.168.64.3/mutillidae/index.php?page=../../../../../../../../../../../etc/passwd%00
",1.3.6.1.4.1.25623.1.0.16100,"CVE-2005-0283",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,aee51dcc-5bf6-4731-9dd0-c2743fc7531f,"","No known solution was made available for at least one year since the disclosure
  of this vulnerability. Likely none will be provided anymore. General solution options are to upgrade to a newer
  release, disable respective features, remove the product or replace the product by another one.","","","
Details:
QWikiwiki directory traversal vulnerability
(OID: 1.3.6.1.4.1.25623.1.0.16100)
Version used: 2025-04-15T05:54:49Z
","","","",""
192.168.64.3,,80,tcp,5.0,Medium,80,"Mitigation","/doc directory browsable","The /doc directory is browsable.
  /doc shows the content of the /usr/doc directory and therefore it shows which programs and - important! - the version of the installed programs.","Vulnerable URL: http://192.168.64.3/doc/
",1.3.6.1.4.1.25623.1.0.10056,"CVE-1999-0678",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,64ed0f24-01b5-4a31-8763-d8f47472792a,"","Use access restrictions for the /doc directory.
  If you use Apache you might use this in your access.conf:

  <Directory /usr/doc>
  AllowOverride None
  order deny, allow
  deny from all
  allow from localhost
  </Directory>","","","
Details:
/doc directory browsable
(OID: 1.3.6.1.4.1.25623.1.0.10056)
Version used: 2023-08-01T13:29:10Z
","","","",""
192.168.64.3,,5432,tcp,5.0,Medium,70,"VendorFix","SSL/TLS: Renegotiation DoS Vulnerability (CVE-2011-1473, CVE-2011-5094)","The remote SSL/TLS service is prone to a denial of service (DoS)
  vulnerability.","The following indicates that the remote SSL/TLS service is affected:

Protocol Version | Successful re-done SSL/TLS handshakes (Renegotiation) over an existing / already established SSL/TLS connection
----------------------------------------------------------------------------------------------------------------------------------
TLSv1.0          | 10
",1.3.6.1.4.1.25623.1.0.117761,"CVE-2011-1473,CVE-2011-5094",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,e56e6683-becb-4e8f-b4e5-676684953bee,"The flaw might make it easier for remote attackers to cause a
  DoS (CPU consumption) by performing many renegotiations within a single connection.","Users should contact their vendors for specific patch
  information.

  A general solution is to remove/disable renegotiation capabilities altogether from/in the affected
  SSL/TLS service.","Every SSL/TLS service which does not properly restrict
  client-initiated renegotiation.","The flaw exists because the remote SSL/TLS service does not
  properly restrict client-initiated renegotiation within the SSL and TLS protocols.

  Note: The referenced CVEs are affecting OpenSSL and Mozilla Network Security Services (NSS) but
  both are in a DISPUTED state with the following rationale:

  > It can also be argued that it is the responsibility of server deployments, not a security
  library, to prevent or limit renegotiation when it is inappropriate within a specific environment.

  Both CVEs are still kept in this VT as a reference to the origin of this flaw.","Checks if the remote service allows to re-do the same SSL/TLS
  handshake (Renegotiation) over an existing / already established SSL/TLS connection.
Details:
SSL/TLS: Renegotiation DoS Vulnerability (CVE-2011-1473, CVE-2011-5094)
(OID: 1.3.6.1.4.1.25623.1.0.117761)
Version used: 2026-03-13T05:54:58Z
","","","DFN-CERT-2025-0933,DFN-CERT-2017-1013,DFN-CERT-2017-1012,DFN-CERT-2014-0809,DFN-CERT-2013-1928,DFN-CERT-2012-1112,WID-SEC-2026-2904,WID-SEC-2026-0180,WID-SEC-2024-1591,WID-SEC-2024-0796,WID-SEC-2023-1435,CB-K17/0980,CB-K17/0979,CB-K14/0772,CB-K13/0915,CB-K13/0462",""
192.168.64.3,,25,tcp,5.0,Medium,70,"VendorFix","SSL/TLS: Renegotiation DoS Vulnerability (CVE-2011-1473, CVE-2011-5094)","The remote SSL/TLS service is prone to a denial of service (DoS)
  vulnerability.","The following indicates that the remote SSL/TLS service is affected:

Protocol Version | Successful re-done SSL/TLS handshakes (Renegotiation) over an existing / already established SSL/TLS connection
----------------------------------------------------------------------------------------------------------------------------------
TLSv1.0          | 10
",1.3.6.1.4.1.25623.1.0.117761,"CVE-2011-1473,CVE-2011-5094",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,7d56789a-ece0-4c63-a0da-0b4ea41dca3b,"The flaw might make it easier for remote attackers to cause a
  DoS (CPU consumption) by performing many renegotiations within a single connection.","Users should contact their vendors for specific patch
  information.

  A general solution is to remove/disable renegotiation capabilities altogether from/in the affected
  SSL/TLS service.","Every SSL/TLS service which does not properly restrict
  client-initiated renegotiation.","The flaw exists because the remote SSL/TLS service does not
  properly restrict client-initiated renegotiation within the SSL and TLS protocols.

  Note: The referenced CVEs are affecting OpenSSL and Mozilla Network Security Services (NSS) but
  both are in a DISPUTED state with the following rationale:

  > It can also be argued that it is the responsibility of server deployments, not a security
  library, to prevent or limit renegotiation when it is inappropriate within a specific environment.

  Both CVEs are still kept in this VT as a reference to the origin of this flaw.","Checks if the remote service allows to re-do the same SSL/TLS
  handshake (Renegotiation) over an existing / already established SSL/TLS connection.
Details:
SSL/TLS: Renegotiation DoS Vulnerability (CVE-2011-1473, CVE-2011-5094)
(OID: 1.3.6.1.4.1.25623.1.0.117761)
Version used: 2026-03-13T05:54:58Z
","","","DFN-CERT-2025-0933,DFN-CERT-2017-1013,DFN-CERT-2017-1012,DFN-CERT-2014-0809,DFN-CERT-2013-1928,DFN-CERT-2012-1112,WID-SEC-2026-2904,WID-SEC-2026-0180,WID-SEC-2024-1591,WID-SEC-2024-0796,WID-SEC-2023-1435,CB-K17/0980,CB-K17/0979,CB-K14/0772,CB-K13/0915,CB-K13/0462",""
192.168.64.3,,80,tcp,5.0,Medium,99,"WillNotFix","awiki <= 20100125 Multiple LFI Vulnerabilities - Active Check","awiki is prone to multiple local file include (LFI)
  vulnerabilities because it fails to properly sanitize user-supplied input.","Vulnerable URL: http://192.168.64.3/mutillidae/index.php?page=/etc/passwd
",1.3.6.1.4.1.25623.1.0.103210,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,5ecc17d5-6498-4309-b0e7-439e9a5dc469,"An attacker can exploit this vulnerability to obtain potentially
  sensitive information and execute arbitrary local scripts in the context of the webserver
  process. This may allow the attacker to compromise the application and the host.","No known solution was made available for at least one year
  since the disclosure of this vulnerability. Likely none will be provided anymore. General
  solution options are to upgrade to a newer release, disable respective features, remove the
  product or replace the product by another one.","awiki version 20100125 and prior.","","Sends a crafted HTTP GET request and checks the response.
Details:
awiki <= 20100125 Multiple LFI Vulnerabilities - Active Check
(OID: 1.3.6.1.4.1.25623.1.0.103210)
Version used: 2025-04-15T05:54:49Z
","","","",""
192.168.64.3,,25,tcp,5.0,Medium,99,"Mitigation","SSL/TLS: Certificate Expired","The remote server's SSL/TLS certificate has already expired.","The certificate of the remote service expired on 2010-04-16 14:07:45.

Certificate details:
fingerprint (SHA-1)             | ED093088706603BFD5DC237399B498DA2D4D31C6
fingerprint (SHA-256)           | E7A7FA0D63E457C7C4A59B38B70849C6A70BDA6F830C7AF1E32DEE436DE813CC
issued by                       | 1.2.840.113549.1.9.1=#726F6F74407562756E74753830342D626173652E6C6F63616C646F6D61696E,CN=ubuntu804-base.localdomain,OU=Office for Complication of Otherwise Simple Affairs,O=OCOSA,L=Everywhere,ST=There is no such thing outside US,C=XX
public key algorithm            | RSA
public key size (bits)          | 1024
serial                          | 00FAF93A4C7FB6B9CC
signature algorithm             | sha1WithRSAEncryption
subject                         | 1.2.840.113549.1.9.1=#726F6F74407562756E74753830342D626173652E6C6F63616C646F6D61696E,CN=ubuntu804-base.localdomain,OU=Office for Complication of Otherwise Simple Affairs,O=OCOSA,L=Everywhere,ST=There is no such thing outside US,C=XX
subject alternative names (SAN) | None
valid from                      | 2010-03-17 14:07:45 UTC
valid until                     | 2010-04-16 14:07:45 UTC
",1.3.6.1.4.1.25623.1.0.103955,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,d95486ef-0c2c-4771-9315-6bd0c83b17be,"","Replace the SSL/TLS certificate by a new one.","","This script checks expiry dates of certificates associated with
  SSL/TLS-enabled services on the target and reports whether any have already expired.","
Details:
SSL/TLS: Certificate Expired
(OID: 1.3.6.1.4.1.25623.1.0.103955)
Version used: 2026-03-13T05:54:58Z
","Product: cpe:/a:ietf:transport_layer_security
Method: SSL/TLS: Collect and Report Certificate Details
(OID: 1.3.6.1.4.1.25623.1.0.103692)
","","",""
192.168.64.3,,5432,tcp,5.0,Medium,99,"Mitigation","SSL/TLS: Certificate Expired","The remote server's SSL/TLS certificate has already expired.","The certificate of the remote service expired on 2010-04-16 14:07:45.

Certificate details:
fingerprint (SHA-1)             | ED093088706603BFD5DC237399B498DA2D4D31C6
fingerprint (SHA-256)           | E7A7FA0D63E457C7C4A59B38B70849C6A70BDA6F830C7AF1E32DEE436DE813CC
issued by                       | 1.2.840.113549.1.9.1=#726F6F74407562756E74753830342D626173652E6C6F63616C646F6D61696E,CN=ubuntu804-base.localdomain,OU=Office for Complication of Otherwise Simple Affairs,O=OCOSA,L=Everywhere,ST=There is no such thing outside US,C=XX
public key algorithm            | RSA
public key size (bits)          | 1024
serial                          | 00FAF93A4C7FB6B9CC
signature algorithm             | sha1WithRSAEncryption
subject                         | 1.2.840.113549.1.9.1=#726F6F74407562756E74753830342D626173652E6C6F63616C646F6D61696E,CN=ubuntu804-base.localdomain,OU=Office for Complication of Otherwise Simple Affairs,O=OCOSA,L=Everywhere,ST=There is no such thing outside US,C=XX
subject alternative names (SAN) | None
valid from                      | 2010-03-17 14:07:45 UTC
valid until                     | 2010-04-16 14:07:45 UTC
",1.3.6.1.4.1.25623.1.0.103955,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,b94442de-3308-4f04-aa91-914d1c5b0b67,"","Replace the SSL/TLS certificate by a new one.","","This script checks expiry dates of certificates associated with
  SSL/TLS-enabled services on the target and reports whether any have already expired.","
Details:
SSL/TLS: Certificate Expired
(OID: 1.3.6.1.4.1.25623.1.0.103955)
Version used: 2026-03-13T05:54:58Z
","Product: cpe:/a:ietf:transport_layer_security
Method: SSL/TLS: Collect and Report Certificate Details
(OID: 1.3.6.1.4.1.25623.1.0.103692)
","","",""
192.168.64.3,,5900,tcp,4.8,Medium,70,"Mitigation","VNC Server Unencrypted Data Transmission","The remote host is running a VNC server providing one or more insecure or
  cryptographically weak Security Type(s) not intended for use on untrusted networks.","The VNC server provides the following insecure or cryptographically weak Security Type(s):

2 (VNC authentication)
",1.3.6.1.4.1.25623.1.0.108529,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,b6d33ac5-5760-437b-a834-6c4939957935,"An attacker can uncover sensitive data by sniffing traffic to the
  VNC server.","Run the session over an encrypted channel provided by IPsec [RFC4301] or SSH [RFC4254].
  Some VNC server vendors are also providing more secure Security Types within their products.","","","
Details:
VNC Server Unencrypted Data Transmission
(OID: 1.3.6.1.4.1.25623.1.0.108529)
Version used: 2023-07-12T05:05:04Z
","","","",""
192.168.64.3,,23,tcp,4.8,Medium,70,"Mitigation","Telnet Unencrypted Cleartext Login","The remote host is running a Telnet service that allows cleartext logins over
  unencrypted connections.","Vulnerability was detected according to the Vulnerability Detection Method.",1.3.6.1.4.1.25623.1.0.108522,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,7fde73d7-87f2-4545-8c31-c65db78d82f7,"An attacker can uncover login names and passwords by sniffing traffic to the
  Telnet service.","Replace Telnet with a protocol like SSH which supports encrypted connections.","","","
Details:
Telnet Unencrypted Cleartext Login
(OID: 1.3.6.1.4.1.25623.1.0.108522)
Version used: 2023-10-13T05:06:09Z
","","","",""
192.168.64.3,,2121,tcp,4.8,Medium,70,"Mitigation","FTP Unencrypted Cleartext Login","The remote host is running a FTP service that allows cleartext logins over
  unencrypted connections.","The remote FTP service accepts logins without a previous sent 'AUTH TLS' command. Response(s):

Non-anonymous sessions: 331 Password required for openvasvt
Anonymous sessions:     331 Password required for anonymous
",1.3.6.1.4.1.25623.1.0.108528,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,0da5a3fe-b84a-4e22-978c-265ff330c672,"An attacker can uncover login names and passwords by sniffing traffic to the
  FTP service.","Enable FTPS or enforce the connection via the 'AUTH TLS' command. Please see
  the manual of the FTP service for more information.","","","Tries to login to a non FTPS enabled FTP service without sending a
  'AUTH TLS' command first and checks if the service is accepting the login without enforcing the use of
  the 'AUTH TLS' command.
Details:
FTP Unencrypted Cleartext Login
(OID: 1.3.6.1.4.1.25623.1.0.108528)
Version used: 2023-12-20T05:05:58Z
","","","",""
192.168.64.3,,21,tcp,4.8,Medium,70,"Mitigation","FTP Unencrypted Cleartext Login","The remote host is running a FTP service that allows cleartext logins over
  unencrypted connections.","The remote FTP service accepts logins without a previous sent 'AUTH TLS' command. Response(s):

Non-anonymous sessions: 331 Please specify the password.
Anonymous sessions:     331 Please specify the password.
",1.3.6.1.4.1.25623.1.0.108528,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,f367de12-9bc8-4000-8e85-9a5a437d6013,"An attacker can uncover login names and passwords by sniffing traffic to the
  FTP service.","Enable FTPS or enforce the connection via the 'AUTH TLS' command. Please see
  the manual of the FTP service for more information.","","","Tries to login to a non FTPS enabled FTP service without sending a
  'AUTH TLS' command first and checks if the service is accepting the login without enforcing the use of
  the 'AUTH TLS' command.
Details:
FTP Unencrypted Cleartext Login
(OID: 1.3.6.1.4.1.25623.1.0.108528)
Version used: 2023-12-20T05:05:58Z
","","","",""
192.168.64.3,,80,tcp,4.8,Medium,80,"Workaround","Cleartext Transmission of Sensitive Information via HTTP","The host / application transmits sensitive information (username, passwords) in
  cleartext via HTTP.","The following input fields were identified (URL:input name):

http://192.168.64.3/dvwa/login.php:password
http://192.168.64.3/phpMyAdmin/:pma_password
http://192.168.64.3/phpMyAdmin/?D=A:pma_password
http://192.168.64.3/tikiwiki/tiki-install.php:pass
",1.3.6.1.4.1.25623.1.0.108440,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,3ffb6e2c-d44a-4e31-8fee-eaa65a7a4c75,"An attacker could use this situation to compromise or eavesdrop on the
  HTTP communication between the client and the server using a man-in-the-middle attack to get access to
  sensitive data like usernames or passwords.","Enforce the transmission of sensitive data via an encrypted SSL/TLS connection.
  Additionally make sure the host / application is redirecting all users to the secured SSL/TLS connection before
  allowing to input sensitive data into the mentioned functions.","Hosts / applications which doesn't enforce the transmission of sensitive data via an
  encrypted SSL/TLS connection.","","Evaluate previous collected information and check if the host / application is not
  enforcing the transmission of sensitive data via an encrypted SSL/TLS connection.

  The script is currently checking the following:

  - HTTP Basic Authentication (Basic Auth)

  - HTTP Forms (e.g. Login) with input field of type 'password'
Details:
Cleartext Transmission of Sensitive Information via HTTP
(OID: 1.3.6.1.4.1.25623.1.0.108440)
Version used: 2023-09-07T05:05:21Z
","","","",""
192.168.64.3,,22,tcp,4.3,Medium,80,"Mitigation","Weak Encryption Algorithm(s) Supported (SSH)","The remote SSH server is configured to allow / support weak
  encryption algorithm(s).","The remote SSH server supports the following weak client-to-server encryption algorithm(s):

3des-cbc
aes128-cbc
aes192-cbc
aes256-cbc
arcfour
arcfour128
arcfour256
blowfish-cbc
cast128-cbc
rijndael-cbc@lysator.liu.se


The remote SSH server supports the following weak server-to-client encryption algorithm(s):

3des-cbc
aes128-cbc
aes192-cbc
aes256-cbc
arcfour
arcfour128
arcfour256
blowfish-cbc
cast128-cbc
rijndael-cbc@lysator.liu.se
",1.3.6.1.4.1.25623.1.0.105611,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,e0447b54-840c-47d8-a3a7-0f2b3ee977b2,"","Disable the reported weak encryption algorithm(s).","","'- The 'arcfour' cipher is the Arcfour stream cipher with 128-bit
  keys. The Arcfour cipher is believed to be compatible with the RC4 cipher [SCHNEIER]. Arcfour
  (and RC4) has problems with weak keys, and should not be used anymore.

  - The 'none' algorithm specifies that no encryption is to be done. Note that this method provides
  no confidentiality protection, and it is NOT RECOMMENDED to use it.

  - A vulnerability exists in SSH messages that employ CBC mode that may allow an attacker to
  recover plaintext from a block of ciphertext.","Checks the supported encryption algorithms (client-to-server
  and server-to-client) of the remote SSH server.

  Currently weak encryption algorithms are defined as the following:

  - Arcfour (RC4) cipher based algorithms

  - 'none' algorithm

  - CBC mode cipher based algorithms
Details:
Weak Encryption Algorithm(s) Supported (SSH)
(OID: 1.3.6.1.4.1.25623.1.0.105611)
Version used: 2024-06-14T05:05:48Z
","Product: cpe:/a:ietf:secure_shell_protocol
Method: SSH Protocol Algorithms Supported
(OID: 1.3.6.1.4.1.25623.1.0.105565)
","","",""
192.168.64.3,,80,tcp,4.3,Medium,99,"WillNotFix","phpMyAdmin error.php Cross Site Scripting Vulnerability","phpMyAdmin is prone to a cross-site scripting (XSS) vulnerability.","Vulnerability was detected according to the Vulnerability Detection Method.",1.3.6.1.4.1.25623.1.0.801660,"CVE-2010-4480",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,baf53782-759a-4008-b51f-9b952331f9cc,"Successful exploitation will allow attackers to inject arbitrary
HTML code within the error page and conduct phishing attacks.","No known solution was made available for at least one year since the disclosure
  of this vulnerability. Likely none will be provided anymore. General solution options are to upgrade to a newer
  release, disable respective features, remove the product or replace the product by another one.","phpMyAdmin version 3.3.8.1 and prior.","The flaw is caused by input validation errors in the 'error.php'
script when processing crafted BBcode tags containing '@' characters, which
could allow attackers to inject arbitrary HTML code within the error page
and conduct phishing attacks.","
Details:
phpMyAdmin 'error.php' Cross Site Scripting Vulnerability
(OID: 1.3.6.1.4.1.25623.1.0.801660)
Version used: 2023-10-17T05:05:34Z
","","","DFN-CERT-2011-0467,DFN-CERT-2011-0451,DFN-CERT-2011-0016,DFN-CERT-2011-0002",""
192.168.64.3,,25,tcp,4.3,Medium,80,"VendorFix","SSL/TLS: RSA Temporary Key Handling RSA_EXPORT Downgrade Issue (FREAK)","This host is accepting 'RSA_EXPORT' cipher suites and is prone
  to a man-in-the-middle (MITM) vulnerability.","'RSA_EXPORT' cipher suites accepted by this service via the SSLv3 protocol:

TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA
TLS_RSA_EXPORT_WITH_DES40_CBC_SHA
TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5
TLS_RSA_EXPORT_WITH_RC4_40_MD5

'RSA_EXPORT' cipher suites accepted by this service via the TLSv1.0 protocol:

TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA
TLS_RSA_EXPORT_WITH_DES40_CBC_SHA
TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5
TLS_RSA_EXPORT_WITH_RC4_40_MD5


",1.3.6.1.4.1.25623.1.0.805142,"CVE-2015-0204",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,f9cefb7c-52c9-4e63-8112-143e3807dbf7,"Successful exploitation will allow remote attacker to downgrade
  the security of a session to use 'RSA_EXPORT' cipher suites, which are significantly weaker than
  non-export cipher suites. This may allow a man-in-the-middle attacker to more easily break the
  encryption and monitor or tamper with the encrypted stream.","'- Remove support for 'RSA_EXPORT' cipher suites from the
  service. Please see the references for more resources supporting you with this task.

  - If the service is using OpenSSL: Update to version 0.9.8zd, 1.0.0p, 1.0.1k or later.","'- Hosts accepting 'RSA_EXPORT' cipher suites.

  - OpenSSL versions prior to 0.9.8zd, 1.0.0 prior to 1.0.0p and 1.0.1 prior to 1.0.1k.","Flaw is due to improper handling RSA temporary keys in a
  non-export RSA key exchange cipher suite.","Checks previous collected cipher suites.
Details:
SSL/TLS: RSA Temporary Key Handling 'RSA_EXPORT' Downgrade Issue (FREAK)
(OID: 1.3.6.1.4.1.25623.1.0.805142)
Version used: 2026-06-03T07:18:10Z
","Product: cpe:/a:ietf:transport_layer_security
Method: SSL/TLS: Report Supported Cipher Suites
(OID: 1.3.6.1.4.1.25623.1.0.802067)
","","DFN-CERT-2018-1408,DFN-CERT-2016-1372,DFN-CERT-2016-1164,DFN-CERT-2016-0388,DFN-CERT-2015-1853,DFN-CERT-2015-1332,DFN-CERT-2015-0884,DFN-CERT-2015-0800,DFN-CERT-2015-0758,DFN-CERT-2015-0567,DFN-CERT-2015-0544,DFN-CERT-2015-0530,DFN-CERT-2015-0396,DFN-CERT-2015-0375,DFN-CERT-2015-0374,DFN-CERT-2015-0305,DFN-CERT-2015-0199,DFN-CERT-2015-0021,WID-SEC-2026-0180,CB-K18/0799,CB-K16/1289,CB-K16/1096,CB-K15/1751,CB-K15/1266,CB-K15/0850,CB-K15/0764,CB-K15/0720,CB-K15/0548,CB-K15/0526,CB-K15/0509,CB-K15/0493,CB-K15/0384,CB-K15/0365,CB-K15/0364,CB-K15/0302,CB-K15/0192,CB-K15/0016",""
192.168.64.3,,80,tcp,4.3,Medium,80,"VendorFix","jQuery < 1.6.3 XSS Vulnerability","jQuery is prone to a cross-site scripting (XSS)
  vulnerability.","Installed version: 1.3.2
Fixed version:     1.6.3
Installation
path / port:       /mutillidae/javascript/ddsmoothmenu/jquery.min.js

Detection info (see OID: 1.3.6.1.4.1.25623.1.0.150658 for more info):
- Identified file: http://192.168.64.3/mutillidae/javascript/ddsmoothmenu/jquery.min.js
- Referenced at:   http://192.168.64.3/mutillidae/
",1.3.6.1.4.1.25623.1.0.141637,"CVE-2011-4969",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,101ec697-2e85-4fdd-8f6f-fe34df5565d8,"","Update to version 1.6.3 or later.","jQuery prior to version 1.6.3.","Cross-site scripting (XSS) vulnerability in jQuery before 1.6.3,
  when using location.hash to select elements, allows remote attackers to inject arbitrary web
  script or HTML via a crafted tag.","Checks if a vulnerable version is present on the target host.
Details:
jQuery < 1.6.3 XSS Vulnerability
(OID: 1.3.6.1.4.1.25623.1.0.141637)
Version used: 2023-07-14T05:06:08Z
","","","DFN-CERT-2017-0199,DFN-CERT-2016-0890,WID-SEC-2026-1752,CB-K17/0195",""
192.168.64.3,,80,tcp,4.3,Medium,99,"VendorFix","Apache HTTP Server httpOnly Cookie Information Disclosure Vulnerability","Apache HTTP Server is prone to a cookie information disclosure vulnerability.","Vulnerability was detected according to the Vulnerability Detection Method.",1.3.6.1.4.1.25623.1.0.902830,"CVE-2012-0053",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,1892524c-8c88-48bf-8b97-53050ebcdbcf,"Successful exploitation will allow attackers to obtain sensitive information
  that may aid in further attacks.","Update to Apache HTTP Server version 2.2.22 or later.","Apache HTTP Server versions 2.2.0 through 2.2.21.","The flaw is due to an error within the default error response for
  status code 400 when no custom ErrorDocument is configured, which can be
  exploited to expose 'httpOnly' cookies.","
Details:
Apache HTTP Server 'httpOnly' Cookie Information Disclosure Vulnerability
(OID: 1.3.6.1.4.1.25623.1.0.902830)
Version used: 2026-02-24T05:57:09Z
","Product: cpe:/a:apache:http_server:2.2.8
Method: Apache HTTP Server Detection Consolidation
(OID: 1.3.6.1.4.1.25623.1.0.117232)
","","DFN-CERT-2015-0082,DFN-CERT-2014-1592,DFN-CERT-2014-0635,DFN-CERT-2013-1307,DFN-CERT-2012-1276,DFN-CERT-2012-1112,DFN-CERT-2012-0928,DFN-CERT-2012-0758,DFN-CERT-2012-0744,DFN-CERT-2012-0568,DFN-CERT-2012-0425,DFN-CERT-2012-0424,DFN-CERT-2012-0387,DFN-CERT-2012-0343,DFN-CERT-2012-0332,DFN-CERT-2012-0306,DFN-CERT-2012-0264,DFN-CERT-2012-0203,DFN-CERT-2012-0188,CB-K15/0080,CB-K14/1505,CB-K14/0608",""
192.168.64.3,,25,tcp,4.3,Medium,98,"Mitigation","SSL/TLS: Deprecated TLSv1.0 and TLSv1.1 Protocol Detection","It was possible to detect the usage of the deprecated TLSv1.0
  and/or TLSv1.1 protocol on this system.","The service is only providing the deprecated TLSv1.0 protocol and supports one or more ciphers. Those supported ciphers can be found in the 'SSL/TLS: Report Supported Cipher Suites' (OID: 1.3.6.1.4.1.25623.1.0.802067) VT.
",1.3.6.1.4.1.25623.1.0.117274,"CVE-2011-3389,CVE-2015-0204,CVE-2023-41928,CVE-2024-41270,CVE-2025-3200",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,471e20bf-0123-497c-8599-8cdd43cadac4,"An attacker might be able to use the known cryptographic flaws to
  eavesdrop the connection between clients and the service to get access to sensitive data
  transferred within the secured connection.

  Furthermore newly uncovered vulnerabilities in this protocols won't receive security updates
  anymore.","It is recommended to disable the deprecated TLSv1.0 and/or
  TLSv1.1 protocols in favor of the TLSv1.2+ protocols.

  Please see the references for more resources supporting you with this task.","'- All services providing an encrypted communication using the
  TLSv1.0 and/or TLSv1.1 protocols

  - CVE-2023-41928: Kiloview P1 4G and P2 4G Video Encoder

  - CVE-2024-41270: Gorush v1.18.4

  - CVE-2025-3200: Multiple products from Wiesemann & Theis","The TLSv1.0 and TLSv1.1 protocols contain known cryptographic
  flaws like:

  - CVE-2011-3389: Browser Exploit Against SSL/TLS (BEAST)

  - CVE-2015-0204: Factoring Attack on RSA-EXPORT Keys Padding Oracle On Downgraded Legacy
  Encryption (FREAK)","Checks the used TLS protocols of the services provided by this
  system.
Details:
SSL/TLS: Deprecated TLSv1.0 and TLSv1.1 Protocol Detection
(OID: 1.3.6.1.4.1.25623.1.0.117274)
Version used: 2026-06-03T07:18:10Z
","Product: cpe:/a:ietf:transport_layer_security:1.0
Method: SSL/TLS: Version Detection
(OID: 1.3.6.1.4.1.25623.1.0.105782)
","","DFN-CERT-2020-0177,DFN-CERT-2020-0111,DFN-CERT-2019-0068,DFN-CERT-2018-1441,DFN-CERT-2018-1408,DFN-CERT-2016-1372,DFN-CERT-2016-1164,DFN-CERT-2016-0388,DFN-CERT-2015-1853,DFN-CERT-2015-1332,DFN-CERT-2015-0884,DFN-CERT-2015-0800,DFN-CERT-2015-0758,DFN-CERT-2015-0567,DFN-CERT-2015-0544,DFN-CERT-2015-0530,DFN-CERT-2015-0396,DFN-CERT-2015-0375,DFN-CERT-2015-0374,DFN-CERT-2015-0305,DFN-CERT-2015-0199,DFN-CERT-2015-0079,DFN-CERT-2015-0021,DFN-CERT-2014-1414,DFN-CERT-2013-1847,DFN-CERT-2013-1792,DFN-CERT-2012-1979,DFN-CERT-2012-1829,DFN-CERT-2012-1530,DFN-CERT-2012-1380,DFN-CERT-2012-1377,DFN-CERT-2012-1292,DFN-CERT-2012-1214,DFN-CERT-2012-1213,DFN-CERT-2012-1180,DFN-CERT-2012-1156,DFN-CERT-2012-1155,DFN-CERT-2012-1039,DFN-CERT-2012-0956,DFN-CERT-2012-0908,DFN-CERT-2012-0868,DFN-CERT-2012-0867,DFN-CERT-2012-0848,DFN-CERT-2012-0838,DFN-CERT-2012-0776,DFN-CERT-2012-0722,DFN-CERT-2012-0638,DFN-CERT-2012-0627,DFN-CERT-2012-0451,DFN-CERT-2012-0418,DFN-CERT-2012-0354,DFN-CERT-2012-0234,DFN-CERT-2012-0221,DFN-CERT-2012-0177,DFN-CERT-2012-0170,DFN-CERT-2012-0146,DFN-CERT-2012-0142,DFN-CERT-2012-0126,DFN-CERT-2012-0123,DFN-CERT-2012-0095,DFN-CERT-2012-0051,DFN-CERT-2012-0047,DFN-CERT-2012-0021,DFN-CERT-2011-1953,DFN-CERT-2011-1946,DFN-CERT-2011-1844,DFN-CERT-2011-1826,DFN-CERT-2011-1774,DFN-CERT-2011-1743,DFN-CERT-2011-1738,DFN-CERT-2011-1706,DFN-CERT-2011-1628,DFN-CERT-2011-1627,DFN-CERT-2011-1619,DFN-CERT-2011-1482,WID-SEC-2026-0180,WID-SEC-2023-1435,CB-K18/0799,CB-K16/1289,CB-K16/1096,CB-K15/1751,CB-K15/1266,CB-K15/0850,CB-K15/0764,CB-K15/0720,CB-K15/0548,CB-K15/0526,CB-K15/0509,CB-K15/0493,CB-K15/0384,CB-K15/0365,CB-K15/0364,CB-K15/0302,CB-K15/0192,CB-K15/0079,CB-K15/0016,CB-K14/1342,CB-K14/0231,CB-K13/0845,CB-K13/0796,CB-K13/0790",""
192.168.64.3,,5432,tcp,4.3,Medium,98,"Mitigation","SSL/TLS: Deprecated TLSv1.0 and TLSv1.1 Protocol Detection","It was possible to detect the usage of the deprecated TLSv1.0
  and/or TLSv1.1 protocol on this system.","The service is only providing the deprecated TLSv1.0 protocol and supports one or more ciphers. Those supported ciphers can be found in the 'SSL/TLS: Report Supported Cipher Suites' (OID: 1.3.6.1.4.1.25623.1.0.802067) VT.
",1.3.6.1.4.1.25623.1.0.117274,"CVE-2011-3389,CVE-2015-0204,CVE-2023-41928,CVE-2024-41270,CVE-2025-3200",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,511f32c6-2fdb-4e2a-b96a-2e6a09bc0c0a,"An attacker might be able to use the known cryptographic flaws to
  eavesdrop the connection between clients and the service to get access to sensitive data
  transferred within the secured connection.

  Furthermore newly uncovered vulnerabilities in this protocols won't receive security updates
  anymore.","It is recommended to disable the deprecated TLSv1.0 and/or
  TLSv1.1 protocols in favor of the TLSv1.2+ protocols.

  Please see the references for more resources supporting you with this task.","'- All services providing an encrypted communication using the
  TLSv1.0 and/or TLSv1.1 protocols

  - CVE-2023-41928: Kiloview P1 4G and P2 4G Video Encoder

  - CVE-2024-41270: Gorush v1.18.4

  - CVE-2025-3200: Multiple products from Wiesemann & Theis","The TLSv1.0 and TLSv1.1 protocols contain known cryptographic
  flaws like:

  - CVE-2011-3389: Browser Exploit Against SSL/TLS (BEAST)

  - CVE-2015-0204: Factoring Attack on RSA-EXPORT Keys Padding Oracle On Downgraded Legacy
  Encryption (FREAK)","Checks the used TLS protocols of the services provided by this
  system.
Details:
SSL/TLS: Deprecated TLSv1.0 and TLSv1.1 Protocol Detection
(OID: 1.3.6.1.4.1.25623.1.0.117274)
Version used: 2026-06-03T07:18:10Z
","Product: cpe:/a:ietf:transport_layer_security:1.0
Method: SSL/TLS: Version Detection
(OID: 1.3.6.1.4.1.25623.1.0.105782)
","","DFN-CERT-2020-0177,DFN-CERT-2020-0111,DFN-CERT-2019-0068,DFN-CERT-2018-1441,DFN-CERT-2018-1408,DFN-CERT-2016-1372,DFN-CERT-2016-1164,DFN-CERT-2016-0388,DFN-CERT-2015-1853,DFN-CERT-2015-1332,DFN-CERT-2015-0884,DFN-CERT-2015-0800,DFN-CERT-2015-0758,DFN-CERT-2015-0567,DFN-CERT-2015-0544,DFN-CERT-2015-0530,DFN-CERT-2015-0396,DFN-CERT-2015-0375,DFN-CERT-2015-0374,DFN-CERT-2015-0305,DFN-CERT-2015-0199,DFN-CERT-2015-0079,DFN-CERT-2015-0021,DFN-CERT-2014-1414,DFN-CERT-2013-1847,DFN-CERT-2013-1792,DFN-CERT-2012-1979,DFN-CERT-2012-1829,DFN-CERT-2012-1530,DFN-CERT-2012-1380,DFN-CERT-2012-1377,DFN-CERT-2012-1292,DFN-CERT-2012-1214,DFN-CERT-2012-1213,DFN-CERT-2012-1180,DFN-CERT-2012-1156,DFN-CERT-2012-1155,DFN-CERT-2012-1039,DFN-CERT-2012-0956,DFN-CERT-2012-0908,DFN-CERT-2012-0868,DFN-CERT-2012-0867,DFN-CERT-2012-0848,DFN-CERT-2012-0838,DFN-CERT-2012-0776,DFN-CERT-2012-0722,DFN-CERT-2012-0638,DFN-CERT-2012-0627,DFN-CERT-2012-0451,DFN-CERT-2012-0418,DFN-CERT-2012-0354,DFN-CERT-2012-0234,DFN-CERT-2012-0221,DFN-CERT-2012-0177,DFN-CERT-2012-0170,DFN-CERT-2012-0146,DFN-CERT-2012-0142,DFN-CERT-2012-0126,DFN-CERT-2012-0123,DFN-CERT-2012-0095,DFN-CERT-2012-0051,DFN-CERT-2012-0047,DFN-CERT-2012-0021,DFN-CERT-2011-1953,DFN-CERT-2011-1946,DFN-CERT-2011-1844,DFN-CERT-2011-1826,DFN-CERT-2011-1774,DFN-CERT-2011-1743,DFN-CERT-2011-1738,DFN-CERT-2011-1706,DFN-CERT-2011-1628,DFN-CERT-2011-1627,DFN-CERT-2011-1619,DFN-CERT-2011-1482,WID-SEC-2026-0180,WID-SEC-2023-1435,CB-K18/0799,CB-K16/1289,CB-K16/1096,CB-K15/1751,CB-K15/1266,CB-K15/0850,CB-K15/0764,CB-K15/0720,CB-K15/0548,CB-K15/0526,CB-K15/0509,CB-K15/0493,CB-K15/0384,CB-K15/0365,CB-K15/0364,CB-K15/0302,CB-K15/0192,CB-K15/0079,CB-K15/0016,CB-K14/1342,CB-K14/0231,CB-K13/0845,CB-K13/0796,CB-K13/0790",""
192.168.64.3,,25,tcp,4.0,Medium,80,"Mitigation","SSL/TLS: Certificate Signed Using A Weak Signature Algorithm","The remote service is using a SSL/TLS certificate in the certificate chain that has been signed using a
  cryptographically weak hashing algorithm.","The following certificates are part of the certificate chain but using insecure signature algorithms:

Subject:              1.2.840.113549.1.9.1=#726F6F74407562756E74753830342D626173652E6C6F63616C646F6D61696E,CN=ubuntu804-base.localdomain,OU=Office for Complication of Otherwise Simple Affairs,O=OCOSA,L=Everywhere,ST=There is no such thing outside US,C=XX
Signature Algorithm:  sha1WithRSAEncryption


",1.3.6.1.4.1.25623.1.0.105880,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,4c2f9ecd-d9a7-489b-8db3-5bac27f722b8,"","Servers that use SSL/TLS certificates signed with a weak SHA-1, MD5, MD4 or MD2 hashing algorithm will need to obtain new
  SHA-2 signed SSL/TLS certificates to avoid web browser SSL/TLS certificate warnings.","","The following hashing algorithms used for signing SSL/TLS certificates are considered cryptographically weak
  and not secure enough for ongoing use:

  - Secure Hash Algorithm 1 (SHA-1)

  - Message Digest 5 (MD5)

  - Message Digest 4 (MD4)

  - Message Digest 2 (MD2)

  Beginning as late as January 2017 and as early as June 2016, browser developers such as Microsoft and Google will begin warning users when visiting
  web sites that use SHA-1 signed Secure Socket Layer (SSL) certificates.

  NOTE: The script preference allows to set one or more custom SHA-1 fingerprints of CA certificates which are trusted by this routine. The fingerprints
  needs to be passed comma-separated and case-insensitive:

  Fingerprint1

  or

  fingerprint1, Fingerprint2","Check which hashing algorithm was used to sign the remote SSL/TLS certificate.
Details:
SSL/TLS: Certificate Signed Using A Weak Signature Algorithm
(OID: 1.3.6.1.4.1.25623.1.0.105880)
Version used: 2021-10-15T11:13:32Z
","","","",""
192.168.64.3,,5432,tcp,4.0,Medium,80,"Workaround","SSL/TLS: Diffie-Hellman Key Exchange Insufficient DH Group Strength Vulnerability","The SSL/TLS service uses Diffie-Hellman groups with insufficient
  strength (key size < 2048).","Server Temporary Key Size: 1024 bits

",1.3.6.1.4.1.25623.1.0.106223,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,3f67a982-83ab-4ca7-834e-c529d319b205,"An attacker might be able to decrypt the SSL/TLS communication
  offline.","'- Deploy (Ephemeral) Elliptic-Curve Diffie-Hellman (ECDHE) or use
  a 2048-bit or stronger Diffie-Hellman group. Please see the references for more resources
  supporting you with this task.

  - For Apache Web Servers: Beginning with version 2.4.7, mod_ssl will use DH parameters which
  include primes with lengths of more than 1024 bits.","All services providing an encrypted communication using
  Diffie-Hellman groups with insufficient strength.","The Diffie-Hellman group are some big numbers that are used as
  base for the DH computations. They can be, and often are, fixed. The security of the final secret
  depends on the size of these parameters. It was found that 512 and 768 bits to be weak, 1024 bits
  to be breakable by really powerful attackers like governments.","Checks the DHE temporary public key size.
Details:
SSL/TLS: Diffie-Hellman Key Exchange Insufficient DH Group Strength Vulnerab...
(OID: 1.3.6.1.4.1.25623.1.0.106223)
Version used: 2026-06-03T07:18:10Z
","","","",""
192.168.64.3,,5432,tcp,4.0,Medium,80,"Mitigation","SSL/TLS: Certificate Signed Using A Weak Signature Algorithm","The remote service is using a SSL/TLS certificate in the certificate chain that has been signed using a
  cryptographically weak hashing algorithm.","The following certificates are part of the certificate chain but using insecure signature algorithms:

Subject:              1.2.840.113549.1.9.1=#726F6F74407562756E74753830342D626173652E6C6F63616C646F6D61696E,CN=ubuntu804-base.localdomain,OU=Office for Complication of Otherwise Simple Affairs,O=OCOSA,L=Everywhere,ST=There is no such thing outside US,C=XX
Signature Algorithm:  sha1WithRSAEncryption


",1.3.6.1.4.1.25623.1.0.105880,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,ad2ba59e-34c2-47c2-ae6e-c6af7c7aee07,"","Servers that use SSL/TLS certificates signed with a weak SHA-1, MD5, MD4 or MD2 hashing algorithm will need to obtain new
  SHA-2 signed SSL/TLS certificates to avoid web browser SSL/TLS certificate warnings.","","The following hashing algorithms used for signing SSL/TLS certificates are considered cryptographically weak
  and not secure enough for ongoing use:

  - Secure Hash Algorithm 1 (SHA-1)

  - Message Digest 5 (MD5)

  - Message Digest 4 (MD4)

  - Message Digest 2 (MD2)

  Beginning as late as January 2017 and as early as June 2016, browser developers such as Microsoft and Google will begin warning users when visiting
  web sites that use SHA-1 signed Secure Socket Layer (SSL) certificates.

  NOTE: The script preference allows to set one or more custom SHA-1 fingerprints of CA certificates which are trusted by this routine. The fingerprints
  needs to be passed comma-separated and case-insensitive:

  Fingerprint1

  or

  fingerprint1, Fingerprint2","Check which hashing algorithm was used to sign the remote SSL/TLS certificate.
Details:
SSL/TLS: Certificate Signed Using A Weak Signature Algorithm
(OID: 1.3.6.1.4.1.25623.1.0.105880)
Version used: 2021-10-15T11:13:32Z
","","","",""
192.168.64.3,,25,tcp,4.0,Medium,80,"Workaround","SSL/TLS: Diffie-Hellman Key Exchange Insufficient DH Group Strength Vulnerability","The SSL/TLS service uses Diffie-Hellman groups with insufficient
  strength (key size < 2048).","Server Temporary Key Size: 1024 bits

",1.3.6.1.4.1.25623.1.0.106223,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,c2526527-4ab1-4824-993f-1618c77977d9,"An attacker might be able to decrypt the SSL/TLS communication
  offline.","'- Deploy (Ephemeral) Elliptic-Curve Diffie-Hellman (ECDHE) or use
  a 2048-bit or stronger Diffie-Hellman group. Please see the references for more resources
  supporting you with this task.

  - For Apache Web Servers: Beginning with version 2.4.7, mod_ssl will use DH parameters which
  include primes with lengths of more than 1024 bits.","All services providing an encrypted communication using
  Diffie-Hellman groups with insufficient strength.","The Diffie-Hellman group are some big numbers that are used as
  base for the DH computations. They can be, and often are, fixed. The security of the final secret
  depends on the size of these parameters. It was found that 512 and 768 bits to be weak, 1024 bits
  to be breakable by really powerful attackers like governments.","Checks the DHE temporary public key size.
Details:
SSL/TLS: Diffie-Hellman Key Exchange Insufficient DH Group Strength Vulnerab...
(OID: 1.3.6.1.4.1.25623.1.0.106223)
Version used: 2026-06-03T07:18:10Z
","","","",""
192.168.64.3,,25,tcp,3.7,Low,80,"VendorFix","SSL/TLS: DHE_EXPORT MITM Security Bypass Vulnerability (LogJam)","This host is accepting 'DHE_EXPORT' cipher suites and is prone
  to a man-in-the-middle (MITM) vulnerability.","'DHE_EXPORT' cipher suites accepted by this service via the SSLv3 protocol:

TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA
TLS_DH_anon_EXPORT_WITH_DES40_CBC_SHA
TLS_DH_anon_EXPORT_WITH_RC4_40_MD5

'DHE_EXPORT' cipher suites accepted by this service via the TLSv1.0 protocol:

TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA
TLS_DH_anon_EXPORT_WITH_DES40_CBC_SHA
TLS_DH_anon_EXPORT_WITH_RC4_40_MD5


",1.3.6.1.4.1.25623.1.0.805188,"CVE-2015-4000",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,03248ca9-ff3a-4afe-a00f-cb0d7c42fd25,"Successful exploitation will allow a man-in-the-middle attacker
  to downgrade the security of a TLS session to 512-bit export-grade cryptography, which is
  significantly weaker, allowing the attacker to more easily break the encryption and monitor or
  tamper with the encrypted stream.","'- Remove support for 'DHE_EXPORT' cipher
  suites from the service. Please see the references for more resources supporting you with this
  task.

  - If the service is using OpenSSL: Update to version 1.0.1n, 1.0.2b or later.","'- Hosts accepting 'DHE_EXPORT' cipher suites.

  - OpenSSL versions prior to 1.0.1n and 1.0.2 prior to 1.0.2b.","Flaw is triggered when handling Diffie-Hellman key exchanges
  defined in the 'DHE_EXPORT' cipher suites.","Checks previous collected cipher suites.
Details:
SSL/TLS: 'DHE_EXPORT' MITM Security Bypass Vulnerability (LogJam)
(OID: 1.3.6.1.4.1.25623.1.0.805188)
Version used: 2026-06-03T07:18:10Z
","Product: cpe:/a:ietf:transport_layer_security
Method: SSL/TLS: Report Supported Cipher Suites
(OID: 1.3.6.1.4.1.25623.1.0.802067)
","","DFN-CERT-2023-2939,DFN-CERT-2021-0775,DFN-CERT-2020-1561,DFN-CERT-2020-1276,DFN-CERT-2016-1692,DFN-CERT-2016-1648,DFN-CERT-2016-0665,DFN-CERT-2016-0642,DFN-CERT-2016-0184,DFN-CERT-2016-0135,DFN-CERT-2016-0101,DFN-CERT-2016-0035,DFN-CERT-2015-1679,DFN-CERT-2015-1632,DFN-CERT-2015-1608,DFN-CERT-2015-1542,DFN-CERT-2015-1518,DFN-CERT-2015-1406,DFN-CERT-2015-1341,DFN-CERT-2015-1194,DFN-CERT-2015-1144,DFN-CERT-2015-1113,DFN-CERT-2015-1078,DFN-CERT-2015-1067,DFN-CERT-2015-1016,DFN-CERT-2015-0980,DFN-CERT-2015-0977,DFN-CERT-2015-0976,DFN-CERT-2015-0960,DFN-CERT-2015-0956,DFN-CERT-2015-0944,DFN-CERT-2015-0925,DFN-CERT-2015-0879,DFN-CERT-2015-0844,DFN-CERT-2015-0737,WID-SEC-2026-0180,CB-K21/0067,CB-K19/0812,CB-K16/1593,CB-K16/1552,CB-K16/0617,CB-K16/0599,CB-K16/0168,CB-K16/0121,CB-K16/0090,CB-K16/0030,CB-K15/1591,CB-K15/1550,CB-K15/1517,CB-K15/1464,CB-K15/1442,CB-K15/1334,CB-K15/1269,CB-K15/1136,CB-K15/1090,CB-K15/1059,CB-K15/1022,CB-K15/1015,CB-K15/0964,CB-K15/0932,CB-K15/0927,CB-K15/0926,CB-K15/0907,CB-K15/0901,CB-K15/0896,CB-K15/0877,CB-K15/0834,CB-K15/0802,CB-K15/0733",""
192.168.64.3,,25,tcp,3.4,Low,80,"Mitigation","SSL/TLS: SSLv3 Protocol CBC Cipher Suites Information Disclosure Vulnerability (POODLE)","This host is prone to an information disclosure vulnerability.","Vulnerability was detected according to the Vulnerability Detection Method.",1.3.6.1.4.1.25623.1.0.802087,"CVE-2014-3566",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,223ec2cf-49f8-4c58-a97a-25f5a2cd5216,"Successful exploitation will allow a  man-in-the-middle attackers gain access to the plain text data stream.","Possible Mitigations are:

  - Disable SSLv3

  - Disable cipher suites supporting CBC cipher modes

  - Enable TLS_FALLBACK_SCSV if the service is providing TLSv1.0+","","The flaw is due to the block cipher padding not being deterministic and not covered by the Message Authentication Code","Evaluate previous collected information about this service.
Details:
SSL/TLS: SSLv3 Protocol CBC Cipher Suites Information Disclosure Vulnerabili...
(OID: 1.3.6.1.4.1.25623.1.0.802087)
Version used: 2026-03-13T05:54:58Z
","Product: cpe:/a:ietf:transport_layer_security
Method: SSL/TLS: Report Supported Cipher Suites
(OID: 1.3.6.1.4.1.25623.1.0.802067)
","","DFN-CERT-2017-1238,DFN-CERT-2017-1236,DFN-CERT-2016-1929,DFN-CERT-2016-1527,DFN-CERT-2016-1468,DFN-CERT-2016-1168,DFN-CERT-2016-0884,DFN-CERT-2016-0642,DFN-CERT-2016-0388,DFN-CERT-2016-0171,DFN-CERT-2015-1431,DFN-CERT-2015-1075,DFN-CERT-2015-1026,DFN-CERT-2015-0664,DFN-CERT-2015-0548,DFN-CERT-2015-0404,DFN-CERT-2015-0396,DFN-CERT-2015-0259,DFN-CERT-2015-0254,DFN-CERT-2015-0245,DFN-CERT-2015-0118,DFN-CERT-2015-0114,DFN-CERT-2015-0083,DFN-CERT-2015-0082,DFN-CERT-2015-0081,DFN-CERT-2015-0076,DFN-CERT-2014-1717,DFN-CERT-2014-1680,DFN-CERT-2014-1632,DFN-CERT-2014-1564,DFN-CERT-2014-1542,DFN-CERT-2014-1414,DFN-CERT-2014-1366,DFN-CERT-2014-1354,WID-SEC-2026-0180,WID-SEC-2025-1658,WID-SEC-2023-0431,CB-K17/1198,CB-K17/1196,CB-K16/1828,CB-K16/1438,CB-K16/1384,CB-K16/1102,CB-K16/0599,CB-K16/0156,CB-K15/1514,CB-K15/1358,CB-K15/1021,CB-K15/0972,CB-K15/0637,CB-K15/0590,CB-K15/0525,CB-K15/0393,CB-K15/0384,CB-K15/0287,CB-K15/0252,CB-K15/0246,CB-K15/0237,CB-K15/0118,CB-K15/0110,CB-K15/0108,CB-K15/0080,CB-K15/0078,CB-K15/0077,CB-K15/0075,CB-K14/1617,CB-K14/1581,CB-K14/1537,CB-K14/1479,CB-K14/1458,CB-K14/1342,CB-K14/1314,CB-K14/1313,CB-K14/1311,CB-K14/1304,CB-K14/1296",""
192.168.64.3,,5432,tcp,3.4,Low,80,"Mitigation","SSL/TLS: SSLv3 Protocol CBC Cipher Suites Information Disclosure Vulnerability (POODLE)","This host is prone to an information disclosure vulnerability.","Vulnerability was detected according to the Vulnerability Detection Method.",1.3.6.1.4.1.25623.1.0.802087,"CVE-2014-3566",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,1614e068-1d8d-44bd-8b11-4ba6ec1541ed,"Successful exploitation will allow a  man-in-the-middle attackers gain access to the plain text data stream.","Possible Mitigations are:

  - Disable SSLv3

  - Disable cipher suites supporting CBC cipher modes

  - Enable TLS_FALLBACK_SCSV if the service is providing TLSv1.0+","","The flaw is due to the block cipher padding not being deterministic and not covered by the Message Authentication Code","Evaluate previous collected information about this service.
Details:
SSL/TLS: SSLv3 Protocol CBC Cipher Suites Information Disclosure Vulnerabili...
(OID: 1.3.6.1.4.1.25623.1.0.802087)
Version used: 2026-03-13T05:54:58Z
","Product: cpe:/a:ietf:transport_layer_security
Method: SSL/TLS: Report Supported Cipher Suites
(OID: 1.3.6.1.4.1.25623.1.0.802067)
","","DFN-CERT-2017-1238,DFN-CERT-2017-1236,DFN-CERT-2016-1929,DFN-CERT-2016-1527,DFN-CERT-2016-1468,DFN-CERT-2016-1168,DFN-CERT-2016-0884,DFN-CERT-2016-0642,DFN-CERT-2016-0388,DFN-CERT-2016-0171,DFN-CERT-2015-1431,DFN-CERT-2015-1075,DFN-CERT-2015-1026,DFN-CERT-2015-0664,DFN-CERT-2015-0548,DFN-CERT-2015-0404,DFN-CERT-2015-0396,DFN-CERT-2015-0259,DFN-CERT-2015-0254,DFN-CERT-2015-0245,DFN-CERT-2015-0118,DFN-CERT-2015-0114,DFN-CERT-2015-0083,DFN-CERT-2015-0082,DFN-CERT-2015-0081,DFN-CERT-2015-0076,DFN-CERT-2014-1717,DFN-CERT-2014-1680,DFN-CERT-2014-1632,DFN-CERT-2014-1564,DFN-CERT-2014-1542,DFN-CERT-2014-1414,DFN-CERT-2014-1366,DFN-CERT-2014-1354,WID-SEC-2026-0180,WID-SEC-2025-1658,WID-SEC-2023-0431,CB-K17/1198,CB-K17/1196,CB-K16/1828,CB-K16/1438,CB-K16/1384,CB-K16/1102,CB-K16/0599,CB-K16/0156,CB-K15/1514,CB-K15/1358,CB-K15/1021,CB-K15/0972,CB-K15/0637,CB-K15/0590,CB-K15/0525,CB-K15/0393,CB-K15/0384,CB-K15/0287,CB-K15/0252,CB-K15/0246,CB-K15/0237,CB-K15/0118,CB-K15/0110,CB-K15/0108,CB-K15/0080,CB-K15/0078,CB-K15/0077,CB-K15/0075,CB-K14/1617,CB-K14/1581,CB-K14/1537,CB-K14/1479,CB-K14/1458,CB-K14/1342,CB-K14/1314,CB-K14/1313,CB-K14/1311,CB-K14/1304,CB-K14/1296",""
192.168.64.3,,22,tcp,2.6,Low,80,"Mitigation","Weak MAC Algorithm(s) Supported (SSH)","The remote SSH server is configured to allow / support weak MAC
  algorithm(s).","The remote SSH server supports the following weak client-to-server MAC algorithm(s):

hmac-md5
hmac-md5-96
hmac-sha1-96
umac-64@openssh.com


The remote SSH server supports the following weak server-to-client MAC algorithm(s):

hmac-md5
hmac-md5-96
hmac-sha1-96
umac-64@openssh.com
",1.3.6.1.4.1.25623.1.0.105610,"",fe544882-fff8-4082-8221-6de099fdbba9,"Scan Metasploitable2",2026-08-28T18:52:02Z,6de037df-8801-4bae-8f07-696554b4319b,"","Disable the reported weak MAC algorithm(s).","","","Checks the supported MAC algorithms (client-to-server and
  server-to-client) of the remote SSH server.

  Currently weak MAC algorithms are defined as the following:

  - MD5 based algorithms

  - 96-bit based algorithms

  - 64-bit based algorithms

  - 'none' algorithm
Details:
Weak MAC Algorithm(s) Supported (SSH)
(OID: 1.3.6.1.4.1.25623.1.0.105610)
Version used: 2024-06-14T05:05:48Z
","Product: cpe:/a:ietf:secure_shell_protocol
Method: SSH Protocol Algorithms Supported
(OID: 1.3.6.1.4.1.25623.1.0.105565)
","","",""


---

## security_analyst

**Fase 1: INTERPRETAZIONE**

Analisi dei servizi rilevati sulle porte TCP aperte della macchina Metasploitable 2 tramite gli output Nmap, Nikto e GVM/OpenVAS.

| Porta  | Servizio           | Versione/Dettagli                                                                                                   |
|--------|--------------------|--------------------------------------------------------------------------------------------------------------------|
| 21     | FTP                | vsftpd 2.3.4                                                                                                       |
| 22     | SSH                | OpenSSH 4.7p1 Debian 8ubuntu1                                                                                      |
| 23     | Telnet             | Linux telnetd                                                                                                      |
| 25     | SMTP               | Postfix smtpd                                                                                                      |
| 53     | DNS                | ISC BIND 9.4.2                                                                                                     |
| 80     | HTTP               | Apache httpd 2.2.8 (Ubuntu) + PHP/5.2.4-2ubuntu5.10 + vari webapp vulnerabili (PhpMyAdmin, Mutillidae, TWiki, etc) |
| 111    | RPC                | rpcbind 2                                                                                                          |
| 139    | Samba              | Samba smbd 3.X - 4.X                                                                                                |
| 445    | Samba              | Samba smbd 3.X - 4.X                                                                                                |
| 512    | exec (rexecd)      | netkit-rsh rexecd                                                                                                  |
| 513    | login              | (versione non determinata; rlogin/misconfigured rsh)                                                               |
| 514    | tcpwrapped         | Presenza di rsh/rcp                                                                                                 |
| 1099   | Java RMI           | GNU Classpath grmiregistry                                                                                         |
| 1524   | bindshell          | Backdoor shell root (attenzione: shell remota)                                                                     |
| 2049   | NFS                | nfsd 2-4                                                                                                |
| 2121   | FTP                | ProFTPD 1.3.1                                                                                                      |
| 3306   | MySQL              | MySQL 5.0.51a-3ubuntu5                                                                                             |
| 3632   | distccd            | distccd v1 ((GNU) 4.2.4 (Ubuntu 4.2.4-1ubuntu4))                                                                   |
| 5432   | PostgreSQL         | PostgreSQL DB 8.3.0 - 8.3.7                                                                                        |
| 5900   | VNC                | VNC protocol 3.3                                                                                                   |
| 6000   | X11                | (access denied)                                                                                                    |
| 6667   | IRC                | UnrealIRCd                                                                                                         |
| 6697   | IRC                | UnrealIRCd                                                                                                         |
| 8009   | AJP13              | Apache JServ Protocol (Tomcat/5.5 rilevato da GVM su questa porta)                                                 |
| 8180   | HTTP (Tomcat)      | Apache Tomcat/Coyote JSP engine 1.1                                                                                |
| 8787   | Ruby DRb RMI       | Ruby 1.8 DRb (Distributed Ruby)                                                                                    |
| 40536  | mountd             | mountd 1-3 (RPC)                                                                                                   |
| 47876  | nlockmgr           | Network Lock Manager (RPC)                                                                                         |
| 55681  | status             | status 1 (RPC)                                                                                                     |
| 58639  | Java RMI           | GNU Classpath grmiregistry                                                                                         |
| 6200   | shell backdoor     | vsftpd 2.3.4 backdoor port (rilevata dalla scansione GVM/OpenVAS)                                                  |

**Note aggiuntive dal report Nikto e GVM**:

- Apache/2.2.8 espone PHP 5.2.4 (fortemente obsoleti e “End of Life”).
- Directory browsing abilitato (es: /doc/, /icons/, /test/).
- mod_negotiation attivo: enumerate files brute-force.
- Metodi HTTP PUT/DELETE/TRACE abilitati.
- Diverse webapp con versioni vulnerabili (TWiki, PhpMyAdmin, jQuery, EasyPHP, QWikiwiki, Mutillidae, awiki, etc.)
- Phpinfo accessibile pubblicamente (/phpinfo.php).
- Oltre ai servizi standard, sono esposti varie backdoor (ad es. shell root su porta 1524 e backdoor vsftpd su 6200).
- Diverse credenziali predefinite/weak su MySQL, PostgreSQL, entrambi i servizi FTP, VNC, UnrealIRCd.
- Servizi critici come distccd, Samba, NFS a configurazione debole/potenzialmente vulnerabili.
- Servizi SSH, FTP, Telnet, VNC, SMTP, PostgreSQL accettano protocolli e cifrature deboli, chiavi corte, algoritmi legacy/mal configurati.

La lista dei servizi è molto lunga ed esaustiva. Se hai bisogno della specifica di una particolare porta/servizio, chiedi ora.

**Attendi conferma per procedere alla fase 2 (correlazione CVE).**

---

## analista_umano



---

## analista_umano



---

## security_analyst

**Fase 2: CORRELAZIONE**

Per ogni servizio/versione identificato e vulnerabilità segnalata dagli scanner, riporto il mapping con le CVE reali e i relativi punteggi CVSS (dove documentati), con eventuali note di incertezza sull'attribuzione.

---

### **FTP - vsftpd 2.3.4 (porta 21)**
- **Vulnerabilità**: Backdoor remota, credenziali deboli/di default, login anonimo, supporto cleartext.
- **CVE associate**:
  - **CVE-2011-2523** — vsftpd 2.3.4 backdoor (CVSS: 9.8 [AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H])
  - **CVE-1999-0497** — FTP Anonymous Login (configurazione insicura; CVSS 0.0 in NVD)
  - **CVE-1999-0501/0502/0507/0508** — Credenziali deboli/standard su FTP (CVSS 0.0 in NVD)
- **Vulnerabilità supplementari**: Supporto plaintext (nessuna CVE specifica); FTP crittografia assente.

---

### **FTP - ProFTPD 1.3.1 (porta 2121)**
- **Vulnerabilità**: Credenziali di default deboli, chiavi non cifrate.
- **CVE associate**:
  - Stesse delle varianti su vsftpd (vedi sopra).

---

### **SSH - OpenSSH 4.7p1 (porta 22)**
- **Vulnerabilità**: Algoritmi deboli (DSA, SHA-1, arcfour, 3DES, CBC, MAC MD5), chiavi corte.
- **CVE associate**:
  - Nessuna CVE strettamente associata agli algoritmi weak-by-design, ma è prassi considerare queste debolezze “known issues” crittografiche (vedi POODLE, DROWN, etc.).  
- **Note**: Le debolezze algoritmiche in SSH non sono generalmente censite con una CVE a meno di implementazioni particolari.

---

### **Telnet (porta 23)**
- **Vulnerabilità**: Cleartext login (nessuna cifratura).
- **CVE**: Nessuna specifica (configurazione insicura nota).

---

### **SMTP - Postfix (porta 25)**
- **Vulnerabilità**: 
  - STARTTLS Plaintext Injection:  
    - **CVE-2011-0411**, **CVE-2011-1430**, **CVE-2011-1431**, ... (multiple vendor, CVSS intorno a 6.8)
  - Algoritmi deboli/obsolete, chiave corta, Cert scaduto:
    - **CVE-2014-3566** (POODLE, CVSS 3.4), **CVE-2015-0204** (FREAK, CVSS 4.3), **CVE-2016-0800** (DROWN, CVSS 5.9)
  - Diffie-Hellman debole, SHA-1, TLSv1.0, VRFY/EXPN abilitato.
- **Note**: Più debolezze in TLS riportano vari CVE (vedi dettagli report sopra).

---

### **HTTP - Apache 2.2.8/PHP 5.2.4 (porta 80)**
- **Vulnerabilità critiche**:
  - Apache EoL/outdated (nessuna CVE, ma **EOL: CVSS 10.0**)
  - Directory browsing: **CVE-1999-0678** (severity 0, ma censita)
  - Phpinfo accessibile: **CVE-2008-0149**, **CVE-2023-49282** (CVSS 5.3)
  - PUT/DELETE/TRACE attivi (Cross Site Tracing): **CVE-2004-2320**, **CVE-2012-2223**, etc.
  - Webapp vulnerabili:
    - **TWiki < 4.2.4**: **CVE-2008-5304**, **CVE-2008-5305** (CVSS da 6 a 10)
    - **TWiki < 6.1.0**: **CVE-2018-20212**
    - **TWiki CSRF**: **CVE-2009-1339**, **CVE-2009-4898**
    - **PhpMyAdmin**: **CVE-2010-4480** (XSS), **CVE-2003-1418** (ETag leaks)
    - **EasyPHP**: Nessuna CVE (EOL, vulnerabilità multiple note)
    - **Mutillidae**: Diverse vulnerabilità by design.
    - **awiki**: Nessuna CVE riportata
    - **QWikiwiki**: **CVE-2005-0283** (directory traversal)
    - **jQuery < 1.9.0**: **CVE-2012-6708** (XSS); **CVE-2011-4969**
    - **PHP <= 5.4.3**: **CVE-2012-1823**, **CVE-2012-2311**, **CVE-2012-2335**, **CVE-2012-2336** (RCE exploit su CGI; CVSS 7.5+)
  - Settaggi HTTP insicuri: Cookies, Metodi, header mancanti.
  - Chiarezza trasmissione form/password (HTTP semplice)

---

### **Samba (porta 139/445)**
- **Vulnerabilità**: Versione obsoleta. Smb 3.x e 4.x storicamente soggetto a RCE/misconfig/directory traversal. Nessuna CVE specifica fornita da output.
- **Note**: Metasploitable 2 di solito usa configurazioni intentionatamente insicure (ad es. condivisioni aperte).

---

### **exec/login/tcpwrapped (porte 512/513/514)**
- **Vulnerabilità**: Rexec e servizi r- (rlogin, rsh) trasmettono credenziali in chiaro; accesso root/deboli.
- **CVE**: **CVE-1999-0618** (rexec), **CVE-1999-0651** (rsh cleartext root login); severity 0, GVM la riporta a livello più alto.

---

### **Backdoor shell root (porta 1524)**
- **Vulnerabilità**: Shell remota come root, backdoor.
- **CVE**: Nessuna; questa specifica implementazione è una “misconfiguration/intentional vulnerability” tipica di Metasploitable. Catalogata come Critica (CVSS 10.0).

---

### **Distributed Ruby DRb RMI (porta 8787)**
- **Vulnerabilità**: RCE remota by design. 
- **CVE**: Nessuna ufficiale, vulnerabilità tipica della configurazione Ruby DRb insicura, valutata CVSS 10.0.

---

### **MySQL 5.0.51a (porta 3306)**
- **Vulnerabilità**: Credenziali di default (root/nopass), versione obsoleta, RCE molteplici, encryption debole.
- **CVE**: Vedi lista estesa fornita da output (ad esempio: **CVE-2016-6531**, **CVE-2014-3419**, **CVE-2009-0919**, **CVE-2018-15719**, **CVE-2024-22901**, molti altri), diverse Severe (CVSS > 7).

---

### **PostgreSQL 8.3.0-8.3.7 (porta 5432)**
- **Vulnerabilità**: Credenziali weak (postgres:postgres); Outdated/EOL; TLS debole; Cert scaduto.
- **CVE**: Nessuna CVE su credenziali di default nelle versioni classiche, ma più note debolezze TLS: **CVE-2014-0224**, **CVE-2011-1473**, **CVE-2011-5094**, **CVE-2013-2566**, **CVE-2015-4000**, **CVE-2015-2808**, **CVE-2014-3566**, **CVE-2015-0204**, **CVE-2011-3389**, ecc.

---

### **distccd (porta 3632)**
- **Vulnerabilità**: RCE da client non autenticati.
- **CVE**: **CVE-2004-2687** (CVSS 9.3)

---

### **VNC (porta 5900)**
- **Vulnerabilità**: password “password”, traffico non cifrato.
- **CVE**: Default credentials (nessuna per protocollo, **CVE-2026-65313** è presente come riferimento GVM), crittografia debole.

---

### **UnrealIRCd (6667, 6697)**
- **Vulnerabilità**: Credenziali/sessi spoofabili, backdoor.
- **CVE**: **CVE-2016-7144** (spoofing, CVSS 8.1), **CVE-2010-2075** (backdoor in UnrealIRCd 3.2.8.1, CVSS 7.5)

---

### **Apache Tomcat/5.5 su 8009 (AJP) e 8180**
- **Vulnerabilità**: AJP Ghostcat RCE.
- **CVE**: **CVE-2020-1938** (Ghostcat, CVSS 9.8)

---

### **NFS & RPC services (111, 2049, 40536, 47876, 55681)**
- **Vulnerabilità note**: Spesso usabili per escalating/enum. Nessuna CVE specifica nei report, configurazioni by default giudicate rischiose.

---

### **Sistema operativo Ubuntu 8.04 EOL**
- **Evidenza**: Non più aggiornato, nessuna CVE particolare ma rappresenta criticità massima (CVSS 10.0 “End of Life”).

---

Se hai bisogno del dettaglio di una specifica CVE/vulnerabilità, oppure vuoi la lista completa dei CVE con corrispondenza CVSS, chiedi ora.

**Attendere la richiesta di proseguire alla fase 3 (PRIORITIZZAZIONE)**.

---

## analista_umano



---

## analista_umano

svolgi entrambe per favore

---

## security_analyst

**Fase 3: PRIORITIZZAZIONE**

Classifichiamo le vulnerabilità individuate in base al loro rischio (Critica, Alta, Media, Bassa) valutando l'impatto, la facilità di sfruttamento e la presenza di exploit noti. La motivazione segue ogni categoria.

---

### PRIORITÀ CRITICA

**Criterio:** Vulnerabilità che consentono esecuzione di codice remoto, accesso privilegiato, backdoor con exploit pubblici, credenziali root note o esposizione totale del sistema. Quasi sempre con CVSS ≥ 9.

1. **Sistema Operativo EOL (Ubuntu 8.04)**  
   *Motivazione*: Sistema senza supporto, nessuna patch per vulnerabilità note/future; esposto a exploit “forever day”.  
   CVSS: 10.0  
   - (Nessuna CVE specifica, criticità massima)

2. **Backdoor vsftpd 2.3.4 (porta 21/6200)**  
   *Motivazione*: Permette connessione shell remota come root.  
   CVE-2011-2523, CVSS 9.8

3. **Ingreslock/BindShell root (porta 1524)**  
   *Motivazione*: Shell remota in ascolto, non autorizzata, come root.  
   CVSS: 10.0

4. **Distccd RCE (porta 3632)**  
   *Motivazione*: RCE completamente non autenticata, exploit pubblici.  
   CVE-2004-2687, CVSS 9.3

5. **Ghostcat Tomcat AJP (porta 8009)**  
   *Motivazione*: File read/RCE su tutte le webapp Tomcat, facile da sfruttare anche da internet.  
   CVE-2020-1938, CVSS 9.8

6. **Webapp & PHP CGI RCE (HTTP/80)**  
   - **PHP < 5.3.13/5.4.3 CGI RCE:**  
     CVE-2012-1823, CVSS 7.5+  
   - **TWiki < 4.2.4:**  
     XSS/Command Execution, CVE-2008-5304/5305, CVSS 10.0

7. **Credenziali di Default/Weak (critiche)**  
   - MySQL root senza password (**CVE-2001-0645**, CVSS 9.8 e altri)
   - PostgreSQL postgres:postgres  
   - FTP (vsftpd/ProFTPD): msfadmin/msfadmin, postgres/postgres, etc.  
   - VNC password “password”  
   *Motivazione*: Accesso instantaneo a sistema/applicazione con privilegi massimi e possibilità di pivoting.

8. **Distributed Ruby DRb (8787)**  
   *Motivazione*: RCE remota senza autenticazione; exploit pubblici; spesso come utente privilegiato.  
   CVSS: 10.0

---

### PRIORITÀ ALTA

**Criterio:** Impatto elevato (account compromise, escalation), ma non necessariamente root da remoto o RCE diretta; exploit spesso pubblici; CVSS 7.0-8.9.

1. **UnrealIRCd Authentication Spoofing/Backdoor (6667/6697)**  
   - Spoofing: CVE-2016-7144, CVSS 8.1  
   - Backdoor: CVE-2010-2075, CVSS 7.5

2. **Command Injection su webapp**  
   - EasyPHP, QWikiwiki (CVE-2005-0283, directory traversal su /etc/passwd), Mutillidae, awiki (LFI)  
   *Motivazione*: Possibilità di accesso a file di sistema/arbitrary code via file inclusion/etc.

3. **Dangerous HTTP Methods (PUT/DELETE/TRACE)**  
   *Motivazione*: Possibilità di upload o rimozione arbitraria di file da remoto.

4. **Infoleak by phpinfo() pubblico**  
   - CVE-2008-0149, CVSS ~5-7; ma impatto pratico spesso maggiore in combinazione (pivot).

5. **Cifrature/Protocolli Weak su SSH/SMTP/Postgres**  
   - Facilita downgrade attack/sniﬃng/attacchi MITM; impatto maggiore su reti insicure.

---

### PRIORITÀ MEDIA

**Criterio:** Infoleak, XSS, software/configurazioni insicuri sfruttabili con prerequisiti/bassi impatti localizzati; CVSS 4.0-6.9.

1. **Apache httpOnly Cookie Infoleak**  
   - CVE-2012-0053

2. **CSRF e XSS su webapp (TWiki, PhpMyAdmin, jQuery, etc)**  
   - CVE-2018-20212, CVE-2009-4898, CVE-2010-4480, CVE-2012-6708, CVE-2011-4969

3. **Anonymous FTP login**  
   - CVE-1999-0497  
   *Motivazione*: Dipende dai permessi effettivi, può essere basso rischio se ben segregato.

4. **Directory Browsing abilitato (/doc, /icons, /test)**  
   - CVE-1999-0678  
   *Motivazione*: Espone info e file, ma non dà accesso diretto privilegiato.

5. **Configurazioni TLS deboli, chiavi RSA <2048, cert scaduti, hashing SHA1**  
   - FREAK (**CVE-2015-0204**), DROWN (**CVE-2016-0800**), POODLE (**CVE-2014-3566**)
   - In vari servizi: Postfix, PostgreSQL, etc.

---

### PRIORITÀ BASSA

**Criterio:** Solo se combinata ad altro porta impatti seri, vulnerabilità legacy (rsh, rexec, telnet) in ambienti dove la rete è fidata; debolezze passive; CVSS ≤ 4.

1. **Servizi legacy (rsh/rexec/telnet/FTP/HTTP in chiaro)**  
   - CVE-1999-0618, CVE-1999-0651  
   *Motivazione*: Da soli usati solo in LAN fidate o laboratori, ma pericolosi “in the wild”.

2. **Misconfigurazioni webserver (headers mancanti, MIME, mod_negotiation)**  
   - Nessuna CVE, rischio escalation solo in casi particolari o con altri bug.

3. **Variazioni debolezze crittografiche in ambienti chiusi**  
   - TLSv1.0/TLSv1.1: CVE-2011-3389/2015-0204

---

#### NOTE

- Nella realtà, la priorità può mutare secondo contesto/contromisure/layer di segregazione.
- Molte di queste vulnerabilità sono Critical/High solo perché l’ambiente laboratoriale è completamente privo di hardening/isolation.
- Alcune CVE indicate (es. per brute force o config deboli) hanno CVSS bassi su NVD perché “config issues”; tuttavia GVM/Greenbone (e best practice security) le segnala come rischio alto.

---

**Se vuoi la tabella dettagliata per ogni vulnerabilità/porta, o la vuoi già inclusa nel report tecnico, dimmelo ora – altrimenti proseguo con la BOZZA DI REPORT.**

---

## analista_umano



---

## analista_umano

prosegui includendola nel report tecnico

---

## security_analyst

**Fase 4: REPORT TECNICO**

---

# **Report Tecnico di Sicurezza**
## Host Analizzato: 192.168.64.3 (Metasploitable 2)
**Data scansione:** 2026-09-08  
**Strumenti utilizzati:** Nmap 7.94, Nikto 2.5.0, GVM/OpenVAS (2026)

---

## 1. **Sommario dei Servizi Identificati**

| Porta   | Servizio                        | Versione/Dettagli                                                                                 |
|---------|---------------------------------|--------------------------------------------------------------------------------------------------|
| 21      | FTP (vsftpd)                    | vsftpd 2.3.4                                                                                     |
| 22      | SSH                             | OpenSSH 4.7p1 Debian 8ubuntu1 (algoritmi e chiavi deboli)                                        |
| 23      | Telnet                          | Linux telnetd (login cleartext)                                                                  |
| 25      | SMTP (Postfix)                  | Postfix smtpd (TLS/SSL weak config, cert debole/scaduto)                                         |
| 53      | DNS                             | ISC BIND 9.4.2                                                                                   |
| 80      | HTTP                            | Apache 2.2.8 + PHP 5.2.4 (Ubuntu) + vari webapp obsolete/vulnerabili                             |
| 111     | RPC                             | rpcbind 2                                                                                        |
| 139/445 | Samba                           | smbd 3.X - 4.X                                                                                   |
| 512/513/514 | exec/login/tcpwrapped/rsh  | netkit-rsh, rsh, rcp legacy                                                                      |
| 1099/58639 | Java RMI                     | GNU Classpath grmiregistry                                                                       |
| 1524    | Shell (backdoor)                | Shell root remota (bindshell Ingreslock/manuale)                                                 |
| 2049    | NFS                             | nfsd 2-4                                                                                         |
| 2121    | FTP (ProFTPD)                   | ProFTPD 1.3.1                                                                                    |
| 3306    | MySQL                           | MySQL 5.0.51a (default root, auth debole)                                                        |
| 3632    | distccd                         | distccd v1 RCE                                                                                   |
| 5432    | PostgreSQL                      | 8.3.0 - 8.3.7 (default user, TLS debole)                                                         |
| 5900    | VNC                             | VNC protocol 3.3 (default password, cleartext)                                                   |
| 6000    | X11                             | (access denied)                                                                                  |
| 6667/6697 | IRC (UnrealIRCd)              | UnrealIRCd (backdoor e spoofing)                                                                 |
| 8009    | Tomcat AJP                      | Tomcat 5.5 (Ghostcat)                                                                            |
| 8180    | Tomcat HTTP                     | Tomcat/Coyote JSP engine 1.1                                                                     |
| 8787    | Ruby DRb RMI                    | Distributed Ruby 1.8                                                                             |
| 6200    | Shell (vsftpd backdoor)         | vsftpd 2.3.4 shell backdoor                                                                      |
| altre   | RPC e servizi NFS (mountd, nlockmgr, status)                                            |

---

## 2. **Tabella delle Vulnerabilità, CVE e Priorità**

| Porta | Servizio                  | Vulnerabilità (riassunto)                                 | CVE/ID principali              | CVSS/NVD        | PRIORITÀ  | Note/Motivazione                                              |
|-------|---------------------------|----------------------------------------------------------|-------------------------------|-----------------|-----------|---------------------------------------------------------------|
| *All* | Ubuntu 8.04 (OS)          | EOL, no patch                                            | - (EOL)                       | 10.0            | Critica   | Esposto a qualsiasi exploit, assenza patch future             |
| 21    | vsftpd 2.3.4              | Backdoor remota, default/anon credentials, plaintext     | CVE-2011-2523, CVE-1999-0497  | 9.8, 0          | Critica   | Shell root, accesso anonimo/weak                              |
| 6200  | vsftpd shell backdoor     | Shell root remota                                        | CVE-2011-2523                 | 9.8             | Critica   | --                                                            |
| 1524  | Shell root bind           | Shell root remota                                        | -                             | 10.0 (best prac)| Critica   | Intentional “lab” backdoor                                    |
| 3632  | distccd                   | Remote Code Execution                                    | CVE-2004-2687                 | 9.3             | Critica   | RCE senza autenticazione                                      |
| 8009  | Tomcat AJP                | Ghostcat (file read/RCE)                                 | CVE-2020-1938                 | 9.8             | Critica   | Facilmente sfruttabile                                        |
| 80    | Apache 2.2.8/PHP 5.2.4    | PHP/CGI RCE, info leak, PUT/TRACE, XSS, webapp old/vuln  | V.ampia lista (vedi dettaglio)| 6.0–10.0        | Critica/Alta | Diverse vulnerabilità letali via HTTP                         |
| 3306  | MySQL                     | Default root/no pass, vari bug noti                      | CVE-2016-6531, altri          | 9.8++           | Critica   | Accesso admin remoto facile                                   |
| 5432  | PostgreSQL                | Default postgres:postgres, SSL debole                    | -                             | 9.0/6.9         | Critica/Alta | Facile accesso, attaccabile via password debole               |
| 23    | Telnet                    | Cleartext login                                          | -                             | -               | Alta      | Sniffable, facilità brute                                    |
| 512/513/514 | rsh/rexec           | Weak/cleartext, login root                               | CVE-1999-0618/0651            | 0 (NVD)         | Alta      | Praticamente accesso root da remoto                           |
| 8787  | Ruby DRb RMI              | RCE remota                                               | -                             | 10.0             | Critica   | Nessuna protezione tipica, pivot su altri servizi             |
| 5900  | VNC                       | Password “password”, cleartext                           | CVE-2026-65313 (GVM interna)  | 9.0             | Critica   | Accesso desktop diretto                                       |
| 6667/6697 | UnrealIRCd            | Auth spoofing, backdoor                                  | CVE-2016-7144, CVE-2010-2075  | 8.1, 7.5         | Alta      | Sistema IRC completamente compromesso                         |
| 2121  | ProFTPD 1.3.1             | Default creds, cleartext                                 | vedi FTP                      | 7.5             | Alta      | Stessi problemi di vsftpd                                     |
| 80    | TWiki (webapp)            | RCE/XSS/CSRF via CGI                                     | CVE-2008-5304/5305/2009-1339  | 9–10             | Critica/Alta| Arbitrary code/web defacement                                 |
| 80    | QWikiWiki/Mutillidae/awiki| LFI, XSS, traversal, brute-force                         | CVE-2005-0283, altri          | 7.5/mix         | Alta/Media | Dipende da file accessibili                                   |
| 80    | PhpMyAdmin                | XSS, etag leak, setup esposto                            | CVE-2010-4480, CVE-2003-1418  | 4–6              | Media      | Può portare a escalation                                      |
| 80    | jQuery                    | XSS, input vuln                                          | CVE-2012-6708, CVE-2011-4969  | 6.1, 4.3         | Media      | Re-usable per phishing/pivot                                  |
| 25/5432 | SSL/TLS (vari servizi)  | Weak cipher, key<2048, TLS v1.0/SSLv3/POODLE/FREAK/DROWN | CVE-2014-3566, CVE-2015-0204  | 3-6               | Media      | Facilmente downgradabili a cleartext, eavesdropping           |
| 80    | Directory listing         | Infoleak                                                 | CVE-1999-0678                 | 0 HR*            | Media/Bassa | HR*: Human-rated rischio alto solo se contenuto critico        |
| 21/23/22/2121 | Plaintext login   | Brute-force/sniffing credenziali                         | -                             | -                | Media      | Sfruttabili se esposti su WAN                                 |
| 80    | Infoleak phpinfo          | Disclosure informazioni sensitive                        | CVE-2008-0149, CVE-2023-49282 | ~5.3             | Alta       | Per pivoting e recon                                          |
| *varie* | Samba, NFS, RPC         | Config insicura, escalation                              | -                             | -                | Media      | Sfruttabili per lateral movement                              |

---

## 3. **Approfondimento: Criticità di Rischio**

- **Massima urgenza** ai servizi che permettono accesso root diretto o esecuzione di codice remoto senza autenticazione (backdoor, RCE su distccd, Ghostcat, DRb, credenziali root note).
- Servizi di database con password di default rappresentano immediate possibilità di furto/modifica dati o pivot verso OS.
- Webapp obsolete e non patchate (TWiki, PhpMyAdmin, Mutillidae, jQuery old, directory traversal) favoriscono escalation e attacchi XSS/RCE, con potenziale impatto combinato.
- Weak crypto/config (SSL/TLS/SSH) costituisce minaccia grave in presenza di attaccante “on the wire”, ma in ambiente laboratorio l’impatto può essere considerato inferiore, pur restando una best practice correggere.
- Scoperta di molteplici servizî in “cleartext” (FTP, Telnet, rsh, VNC), configurazioni out-of-the-box, eccessivo numero di servizi superflui e permessi eccessivi nei demoni di sistema.

---

## 4. **Raccomandazioni Prioritarie**

1. **Isolare/Spegnere immediatamente la macchina dalla rete pubblico/internet.**
2. **Eliminare le backdoor (vsftpd 2.3.4, Ingreslock) e aggiornare tutte le componenti ai rami supportati e patchare dove possibile.**
3. **Disabilitare/rimuovere servizi legacy non necessari (rsh/rexec/telnet, distccd, DRb, samba non autenticata).**
4. **Aggiornare tutte le webapp (TWiki, PhpMyAdmin, etc.) e rimuovere o proteggere file/informazioni sensibili (phpinfo, setup vari, directory pubbliche e configurazioni di default).**
5. **Cambiare tutte le password di default e configurare strong authentication; disabilitare login anonimi.**
6. **Rivedere la configurazione di SSL/TLS/SSH, aggiornare certificati, disabilitare cipher/key/protocolli weak, abilitare solo algoritmi e chiavi moderni.**
7. **Duro hardening alla superficie HTTP: chiudere directory/listing, limitare metodi HTTP, abilitare headers sicurezza, rimuovere file test/directory di esempio.**
8. **Eseguire uno scan nuovo dopo ogni ciclo di correzione.**

---

## 5. **Appendice: Immagine di Rischio Combinato**

La presenza di (1) sistema EOL non patchato, (2) servizi con backdoor note e (3) credenziali di default non modificate, unita alle decine di vulnerabilità note e sfruttabili, rappresenta uno scenario di rischio totale. Su un host esposto a Internet o anche solo accessibile da una LAN non strettamente controllata, la compromissione completa della macchina è da considerarsi **certa e immediata**.

---

**FINE REPORT**  
**Nota**: Questa analisi è stata svolta in ambiente di laboratorio e NON deve considerarsi “buona prassi” l’esposizione di simile superficie vulnerabile neppure in test/dev.

TERMINATO

---

