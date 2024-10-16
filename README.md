<p align="center">
  <img src="logo.png" alt="Google-Hacking-Database" />
</p>

# Google-Hacking-Database (GHDB)

  The Google-Hacking-Database (GHDB) is a comprehensive collection of Google search queries, known as "Google Dorks," that help security professionals discover sensitive information exposed online. These queries utilize advanced search operators to locate specific types of data, such as files containing passwords, vulnerabilities on web servers, and other publicly available information that can be leveraged in security assessments. The GHDB is an essential resource for ethical hackers, penetration testers, and anyone interested in cybersecurity.


## Table Of Contents

- [Advanced Search](#advanced-Search)

- [Search Operators](#search-operators)

- [Simple Examples](#simple-examples)

- [Finding Valuable Information](#finding-valuable-information)

- [Further](#further)

- [Meta](#meta)

- [Dork-Exploit-Shellcode](#exploit-database.md)
---

## Advanced Search

Google Dorking describes the process of using advanced search filters that allow to retrieve more efficient results. It is a technique often used by cybersecurity professionals in order to find valuable information about a target. While Google Dorking itself is legal (in most countries), it might quickly lead to actions that aren't, such as visiting sites with illegal content. Hence using [TOR](https://www.torproject.org/) or a [VPN](https://privacyguides.org/vpn/) is recommended. Using a search aggregator like [SearX](https://searx.github.io/searx/) can enhance search privacy and efficiency.

---

## Search Operators

| Operator         | Description                                                                                                              | Syntax                               | Example                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ | --------------------------------- |
| ()               | Group multiple terms or operators. Allows advanced expressions                                                           | (&lt;term> or &lt;operator>)         | inurl:(html \| php)               |
| *                | Wildcard. Matches any word                                                                                               | &lt;text> * &lt;text>                | How to * a computer               |
| ""               | The given keyword has to match exactly. *case-insensitive*                                                               | "&lt;keywords>"                      | "google"                          |
| m..n / m...n     | Search for a range of numbers. *n* should be greater than *m*                                                            | &lt;number>..&lt;number>             | 1..100                            |
| -                | Documents that match the operator are excluded. *NOT*-Operator                                                           | -&lt;operator>                       | -site:youtube.com                 |
| +                | Include documents that match the operator                                                                                | +&lt;operator>                       | +site:youtube.com                 |
| \|               | Logical *OR-Operator*. Only one operator needs to match in order for the overall expression to match                     | &lt;operator> \| &lt;operator>       | "google" \| "yahoo"               |
| ~                | Search for synonyms of the given word. Not supported by Google                                                           | ~&lt;word>                           | ~book                             |
| @                | Perform a search only on the given social media platform. Rather use **site**                                            | @&lt;socialmedia>                    | @instagram                        |
| after            | Search for documents published / indexed after the given date                                                            | after:&lt;yy(-mm-dd)>                | after:2020-06-03                  |
| allintitle       | Same as **intitle** but allows multiple keywords separated by a space                                                    | allintitle:&lt;keywords>             | allintitle:dog cat                |
| allinurl         | Same as **inurl** but allows multiple keywords separated by a space                                                      | allinurl:&lt;keywords>               | allinurl:search com               |
| allintext        | Same as **intext** but allows multiple keywords separated by a space                                                     | allintext:&lt;keywords>              | allintext:math science university |
| AROUND           | Search for documents in which the first word is up to *n* words away from the second word and vice versa                 | &lt;word1> AROUND(&lt;n>) &lt;word2> | google AROUND(10) good            |
| author           | Search for articles written by the given author if applicable                                                            | author:&lt;name>                     | author:Max                        |
| before           | Search for documents published / indexed before the given date                                                           | before:&lt;yy(-mm-dd)>               | before:2020-06-03                 |
| cache            | Search on the cached version of the given website. Use Google's cache to do so                                          | cache:&lt;domain>                    | cache:google.com                  |
| contains         | Search for documents that link to the given filetype. Not supported by Google                                             | contains:&lt;filetype>               | contains:pdf                      |
| date             | Search for documents published within the past *n* months. Not supported by Google                                       | date:&lt;number>                     | date:3                            |
| define           | Search for the definition of the given word                                                                              | define:&lt;word>                     | define:funny                      |
| ext              | Search for a specific filetype                                                                                           | ext:&lt;documenttype>                | ext:pdf                           |
| filetype         | Refer to **ext**                                                                                                         | filetype:&lt;documenttype>           | filetype:pdf                      |
| inanchor         | Search for the given keyword in a website's anchors                                                                      | inanchor:&lt;keyword>                | inanchor:security                 |
| index of         | Search for documents containing direct downloads                                                                         | index of:&lt;term>                   | index of:mp4 videos               |
| info             | Search for information about a website                                                                                   | info:&lt;domain>                     | info:google.com                   |
| intext           | Keyword needs to be in the text of the document                                                                          | intext:&lt;keyword>                  | intext:news                       |
| intitle          | Keyword needs to be in the title of the document                                                                         | intitle:&lt;keyword>                 | intitle:money                     |
| inurl            | Keyword needs to be in the URL of the document                                                                           | inurl:&lt;keyword>                   | inurl:sheet                       |
| link / links     | Search for documents with links containing the given keyword. Useful for finding documents that link to a specific website | link:&lt;keyword>                    | link:google                       |
| location         | Show documents based on the given location                                                                               | location:&lt;location>               | location:USA                      |
| numrange         | Refer to **m..n**                                                                                                        | numrange:&lt;number>-&lt;number>     | numrange:1-100                    |
| OR               | Refer to **\|**                                                                                                          | &lt;operator> OR &lt;operator>       | "google" OR "yahoo"               |
| phonebook        | Search for related phone numbers associated with the given name                                                          | phonebook:&lt;name>                  | phonebook:"william smith"         |
| relate / related | Search for documents that are related to the given website                                                               | relate:&lt;domain>                   | relate:google.com                 |
| safesearch       | Exclude adult content such as pornographic videos                                                                        | safesearch:&lt;keyword>              | safesearch:sex                    |
| source           | Search on a specific news site. Rather use **site**                                                                      | source:&lt;news>                     | source:theguardian                |
| site             | Search on the given site. Given argument might also be just a TLD such as **com, net**, etc                              | site:&lt;domain>                     | site:google.com                   |
| stock            | Search for information about a market stock                                                                              | stock:&lt;stock>                     | stock:dax                         |
| weather          | Search for information about the weather of the given location                                                           | weather:&lt;location>                | weather:Miami                     |

[[Back to top]](#table-of-contents)

---

## Simple Examples

```dork
"google" 1..100
```

> Search for websites that contain the word "google" and a number between 1 and 100

```dork
Videos -site:youtube.*
```

> Search for the term "Videos" but exclude results from YouTube

```dork
How to * a computer after:2022-01-01
```

> Search for websites published after the 1st January 2022 dealing about how to `use/repair/shutdown/...` a computer

```dork
allintext:homework teacher school site:gov before:2020 ext:(html | php | asp)
```

> Search for websites published before 2020 which have the TLD `.gov`, are either html or php documents and contain the words "homework", "teacher" and "school"

```dork
@instagram chr3st5an
```

> Search for the term "chr3st5an" on instagram

---

## Finding Valuable Information

```dork
intitle:"webcamXP 5" | inurl:"lvappl.htm"
```

> Find open/public webcams

```dork
intext:password ext:log
```

> Find log documents that have the string "password" in it

```dork
inurl:/proc/self/cwd
```

> Find vulnerable webservers

```dork
inurl:email.xls ext:xls
```

> Find excel documents that contain email addresses

```dork
index of:mp3 intext:.mp3
```

> Find mp3 (music) documents

---

## Further

You can find more Google Dorks at the [exploit-db](https://www.exploit-db.com/google-hacking-database) - [maltego](https://www.maltego.com/downloads/) 

other [nvd.nist.gov](https://nvd.nist.gov/)/[cxsecurity](https://cxsecurity.com/) or [vulnerability-lab](https://https://vulnerability-lab.com/)

## Resources

Explore the following resources to deepen your understanding of Google Dorking and its applications:

- **[Google Advanced Search Operators](https://support.google.com/websearch/answer/2466433?hl=en)**: Learn about the full range of search operators supported by Google.

- **[Google Dorking Tutorial](https://www.guru99.com/google-dorking.html)**: A beginner's guide to mastering Google Dorking.

- **[OWASP Google Hacking Project](https://owasp.org/www-project-google-hacking/)**: A resource provided by the Open Web Application Security Project for more advanced use cases.

- **[Cybersecurity Blogs](https://krebsonsecurity.com/)**: Follow industry news and insights from leading cybersecurity experts.

[[Back to top]](#table-of-contents)

---

## Meta

### Security Best Practices

While using Google Dorking, it's essential to maintain good security practices to protect your privacy and avoid any potential legal issues. Here are some tips:

- **Use Anonymity Tools**: Always use a VPN or the TOR network to maintain anonymity during your searches.

- **Avoid Malicious Sites**: Be cautious about clicking on suspicious links, especially those leading to potentially illegal or harmful content.

- **Respect Legal Boundaries**: Ensure that your actions remain within legal limits and respect privacy and data protection laws.

- **Secure Your Data**: When conducting searches, avoid using personal or sensitive information that could expose you to risk.

- **Regularly Update Security Tools**: Keep your VPN, antivirus, and other security tools up to date to protect against new threats.

<br>

### Usage Disclaimer

The Google-Hacking-Database (GHDB) is intended for educational and ethical purposes only. Users of this database are advised to operate within the boundaries of the law and to use the information responsibly. The authors and contributors to this project are not liable for any misuse or illegal activity arising from the use of the information contained herein.

By using this database, you agree to abide by all relevant laws and regulations and to refrain from accessing, downloading, or distributing any content obtained through illegal or unethical means.

<br>

### FAQ

**Q: What is Google Dorking?**
- A: Google Dorking refers to using advanced search operators to find information that is not easily accessible through normal search queries.

**Q: Is Google Dorking legal?**
- A: Yes, Google Dorking is legal. However, accessing or using the information discovered in illegal ways is not legal.

**Q: Can I contribute new dorks to this project?**
- A: Absolutely! We encourage contributions. Please follow the Contributing Guidelines to submit new dorks or improvements.

**Q: How can I stay safe while using Google Dorking?**
- A: Use tools like VPNs and TOR for anonymity, avoid illegal content, and follow security best practices.

<br>

### Contributing Guidelines

We welcome contributions to improve and expand the Google-Hacking-Database. To contribute:

1. **Fork the Repository**: Start by forking the project repository to your own GitHub account.

2. **Create a Branch**: Create a new branch for your changes to keep your work separate from the main codebase.

3. **Make Changes**: Implement your changes, whether adding new dorks, improving documentation, or fixing issues.

4. **Test Thoroughly**: Ensure your changes work as expected and do not introduce any new issues.

5. **Submit a Pull Request**: Open a pull request, providing a clear description of your changes, and reference any relevant issues.

6. **Follow the Code of Conduct**: Make sure to adhere to the project's Code of Conduct while contributing.

<br>

## Community Support

If you need help, have questions, or want to discuss Google Dorking with others, join our community:

- **GitHub Discussions**: Participate in discussions, ask questions, and share insights on our [GitHub Discussions page](https://github.com/your-repo/discussions).

- **Issue Tracker**: Report bugs or suggest new features using the [Issue Tracker](https://github.com/your-repo/issues).

- **Social Media**: Follow us on [Twitter](https://twitter.com/your-twitter-handle) for updates and news about the project.

- **Chat Room**: Join our live chat on [Gitter](https://gitter.im/your-repo) for real-time support and collaboration.

---

### License

The information provided here is dedicated to the public domain. Use them as you wish.

[[Back to top]](#table-of-contents)
