## Creating SSL Certificates

To enable HTTPS on your website, you need to get a certificate (a type of file) from a Certificate Authority (CA). [Let’s Encrypt](https://letsencrypt.org/getting-started/)is a CA.
In order to get a certificate for your website’s domain from Let’s Encrypt, you have to demonstrate control over the domain.

### Use Certbot to generate your Certificate

People with shell access use the [Certbot ACME client](https://certbot.eff.org/instructions?ws=webproduct&os=ubuntubionic). 
It can automate certificate issuance and installation with no downtime. It also has expert modes for people who don’t want autoconfiguration.

The first step is to choose the correct System and Software your HTTP website is running on. In our case this is Ngnix and Ubuntu 18.

![Choosing correct settings for SSL certificate](/documentation/images/Certbot_chooseSystem.png)

You have to follow 9 steps to make your HTTP website into an HTTPS website.

#### 1. SSH into the server
SSH into the server running your HTTP website as a user with sudo privileges.

#### 2. Install snapd
You'll need to install snapd and make sure you follow any instructions to enable classic snap support.

Follow [these instructions](https://snapcraft.io/docs/installing-snapd) on snapcraft's site to install snapd.
For our system (Ubuntu 18) Snap is pre-installed.

#### 3. Ensure that your version of snapd is up to date
Execute the following instructions on the command line on the machine to ensure that you have the latest version of snapd.

```/> sudo snap install core; sudo snap refresh core```

#### 4. Remove certbot-auto and any Certbot OS packages
If you have any Certbot packages installed using an OS package manager like ```apt```, ```dnf```, or ```yum```, you should remove them before
installing the Certbot snap to ensure that when you run the command ```certbot``` the snap is used rather than the installation from your
OS package manager. The exact command to do this depends on your OS, but common examples ```are sudo apt-get remove certbot```,
```sudo dnf remove certbot```, or ```sudo yum remove certbot```.

#### 5. Install Certbot
Run this command on the command line on the machine to install Certbot.

```/> sudo snap install --classic certbot```

#### 6. Prepare the Certbot command

Execute the following instruction on the command line on the machine to ensure that the ```certbot``` command can be run.

```/> sudo ln -s /snap/bin/certbot /usr/bin/certbot```

#### 7. Choose how you'd like to run Certbot

*Either get and install your certificates...*
Run this command to get a certificate and have Certbot edit your nginx configuration automatically to serve it, turning on HTTPS access in a single step.

```/> sudo certbot --nginx```

*Or, just get a certificate*

If you're feeling more conservative and would like to make the changes to your nginx configuration by hand, run this command.

``` /> sudo certbot certonly --nginx```

#### 8. Test automatic renewal
The Certbot packages on your system come with a cron job or systemd timer that will renew your certificates automatically before they expire.
You will not need to run Certbot again, unless you change your configuration.
You can test automatic renewal for your certificates by running this command:

``` /> sudo certbot renew --dry-run```

The command to renew certbot is installed in one of the following locations:

```/etc/crontab/```
```/etc/cron.*/*```
```systemctl list-timers```

#### 9. Confirm that Certbot worked

To confirm that your site is set up properly, ```visit https://yourwebsite.com/``` in your browser and look for the lock icon in the URL bar.

