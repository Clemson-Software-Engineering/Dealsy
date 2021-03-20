# Shopping App

## Contents
- [Introduction](#introduction)
- [Main Features](#main-features)
- [Requirements](#requirements)
- [Code Standards](#code-standards)
- [Getting Started](#getting-started)
- [How To Use](#how-to-use)
- [Documentation](#documentation)
- [Testing](#testing)
- [Getting Help](#getting-help)
- [Discussions](#discussions)
- [Contributing](#contributing)

## Introduction
This is a free open source project designed with the intent of creating an easy to use web app to find deals and make shopping online a breeze. We plan to aggregate and scrape data from major marketplaces and online stores to help users find exactly what they are looking for at the best price. The application will sort from best deal to worst deal for the desired product.

*This project is currently in a alpha stage.*

## Main Features
- Easily retrieve information for specific products (Planned)
- Wide range of products (Planned)

## Requirements
This project utilizes Flask and Angular. *Add modules that need to be installed for this project here*

To use this project, you will need to clone this repository. If you have not setup a ssh key for Github or need additional help using Github please refer here [github ssh help](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh) and here [github support](https://support.github.com/) respectively.

```sh
git clone git@github.com:Clemson-Software-Engineering/Dealsy.git
```

*add additional requirements here*

## Code Standards
*add code style here if any*

## Getting Started

To run the backend flask app, you will need to pip install the dependencies and call flask run using the following commands:

```sh
cd backend/
pip install -r requirements.txt
flask run
```

To view the frontend, you will need to nagivate to the frontend and npm install the node modules with the following commands:

```sh
cd frontend/
npm install
ng s -o
```

## How To Use

After you get the frontend up and running you can use the search bar in the upper right corner to search for a product, ex. "microwave" and hit the enter key to view the results!

## Documentation
*add link and info for documentation here*

## Testing
*add info about testing for project*

## Getting Help
Any questions or comments can be sent via email to one of the project admins. When emailing one of the admins please make sure to include the project name in the email subject!
- Ankita Kulkarni: ankitak@g.clemson.edu
- Caroline Kistler: cekistl@g.clemson.edu
- Jack Carroll: jcarro5@g.clemson.edu
- Yash Doiphode: ydoipo@g.clemson.edu

## Discussions
All development discussions take place on Github in this repo by opening an issue as we don't currently have any community chat available for this project.

## Contributing
All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.

A detailed overview on how to contribute can be found in the **[contributing guide](CONTRIBUTING.md)**.

If you are simply looking to start working with the codebase, navigate to the [GitHub "issues" tab](https://github.com/Clemson-Software-Engineering/Dealsy/issues) and start looking through interesting issues. There are a number of issues listed under [Docs](https://github.com/Clemson-Software-Engineering/Dealsy/issues?q=is%3Aopen+sort%3Aupdated-desc+label%3ADocs) and [good first issue](https://github.com/Clemson-Software-Engineering/Dealsy/issues?labels=good+first+issue&sort=updated&state=open) where you could start out.

As contributors and maintainers to this project, you are expected to abide by this projects code of conduct. More information can be found in the **[Contributor Code of Conduct](CODE_OF_CONDUCT.md)**.
