# CREATE CERTS

use acme.sh from this repository

```bash
git clone git@github.com:acmesh-official/acme.sh.git
```

## POWERSHELL TO CREATE A RBAC USER FOR DNS MANAGEMENT

<https://docs.certifytheweb.com/docs/dns/providers/azuredns/>

```powershell
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Import-Module Az.Accounts
PS C:\Users\Tony> Connect-AzAccount
```

then

```powershell
$azurePassword = ConvertTo-SecureString "SOME_PASSWORD" -AsPlainText -Force
$credentials = New-Object Microsoft.Azure.Commands.ActiveDirectory.PSADPasswordCredential -Property @{ StartDate=Get-Date; EndDate=Get-Date -Year 2024; Password=$azurePassword}
$MyServicePrincipal = New-AzADServicePrincipal -DisplayName "LetsEncrypt" -PasswordCredential $credentials
```

to see the account run

```powershell
Get-AzADApplication | Select-Object displayname, objectid, applicationid
```

### Grant the Application rights to update DNS

* Login to portal.azure.com from a web browser
* Click on your DNS Zone
* Click on Access Control (IAM)
* Click on (+) Add
* Select:
  * Role: DNS Zone Contributor
  * Assign access to: Azure AD user, group or application
  * Select: Type in LetsEncrypt
  * Click Save

### Create Service Principal Secret

From the Azure portal, click Azure Active Directory:

* Click App Registrations
* Click LetsEncrypt
* Click Certificates & secrets
* Click Client secrets
* Click New client secret
* Type a key description, choose when it will expire (or never – your choice) and click save.

## CREATE SSL CERTS

for acme.sh in order to run we need to have

```bash
export AZUREDNS_SUBSCRIPTIONID="YOUR_SUBSRIPTIONID"
export AZUREDNS_TENANTID="YOUR_TENANTID"
export AZUREDNS_APPID="YOUR_APPID"
export AZUREDNS_CLIENTSECRET="YOUR_CLIENTSECRET"

SUFFIX=mcp-zm;
PREFIX=data; 
./acme.sh --debug --force --issue --server letsencrypt --dns dns_azure -d DOMAIN_NAME_FOR_SUPERSET  # e.g. data-dev.akros.online
./acme.sh --debug --force --issue --server letsencrypt --dns dns_azure -d DOMAIN_NAME_FOR_OPENSRP  # e.g. opensrp-dev.akros.online
./acme.sh --debug --force --issue --server letsencrypt --dns dns_azure -d DOMAIN_NAME_FOR_WEB  # e.g. reveal-dev.akros.online
./acme.sh --debug --force --issue --server letsencrypt --dns dns_azure -d DOMAIN_NAME_FOR_KEYCLOAK  # e.g. sso-dev.akros.online
```
