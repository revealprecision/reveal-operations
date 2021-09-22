# Reveal Operations

## Purpose of this repository

This repository is to help with the operational deployment and running of a basic reveal instance.  It will provide basic tooling that will assist an organisation in deploying a Reveal instance using a docker platform.

Further documentation can found at <https://www.revealprecision.com> and <https://revealplatform.atlassian.net/wiki>

## Deploying a Reveal instance

### Preparing DNS names

This docker-compose assumes that you are operating DNS and SSL see the README_certs.md for ideas around using SSL and DNS connected to Azure and LetsEncrypt.

The nginx configuration expects certs for Keycloak, OpenSRP, Reveal Web and Superset.

Alternatively you can put the following names in your `/etc/hosts`

```bash
127.0.0.1   opensrp-dev.akros.online
127.0.0.1   reveal-dev.akros.online
127.0.0.1   data-dev.akros.online
127.0.0.1   sso-dev.akros.online
```

## Containers

You will need to bring in docker containers from the following repositories.

* reveal-web <https://github.com/revealprecision/reveal-web>
* reveal-etl <https://github.com/revealprecision/reveal-etl>

### Starting

Running Reveal using docker-compose please read the configuration README_config.md

## Contributions

This repository is maintained by the Operations team at Akros <https://www.akros.com> as implementers of Reveal.

## Support

For support please contact Stefanus Heath at Akros <sheath@akros.com>

## Repository

This repository is shared under the Apache License v2.0 <https://www.apache.org/licenses/LICENSE-2.0>
