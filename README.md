![Zyte logo](zyte.png)

# Trial Project: Product spider #

### Goal ###

The goal of this trial project is to create a spider with Scrapy to scrape artistic work information from a museum website. The specs are detailed below.

**Note:** The museum website was created for this trial and both it and the spider have no commercial value.

### Product spider ###

Create a Python 3.8+ spider to scrape all works in the "In Sunsh" and "Summertime" categories on [the Scrapinghub Maybe Modern Art Collection website](http://pstrial-2019-12-16.toscrape.com).
It should navigate down the work browse tree (e.g.: Summertime / Wrapper From / Barn Owl) to the lowest level and parse on a per-work basis.

If a work does not have information for a specific field, please omit the field.

Fields:

* url: (string) URL of the work being scraped
* artist: (list of strings) List of artists for the work (we assume photographer, sculptor, designer etc are all artists)
* title: (string) Title of the work
* image: (string) URL of the image
* height: (float) Physical height in cm, only if available in cm
* width: (float) Physical width in cm, only if available in cm
* description: (string) Description of the work
* categories: (list of strings) Names of the categories visited to reach the item via the browse tree. Ex: ["Summertime", "Wrapper From", "Ao Shu"]

### Getting started

Scrapy is an application framework for crawling web sites and extracting structured data.
It is the primary library used for data extraction at Zyte, which is the main reason why this trial is focused on Scrapy.

Using a [basic spider](https://doc.scrapy.org/en/latest/intro/tutorial.html#our-first-spider) should be enough to complete the task
(we include a Spider template at `artworks/spiders/trial.py`).
However, we also have a comprehensive [tutorial](https://doc.scrapy.org/en/latest/intro/tutorial.html) which provides deeper insight into Scrapy.

In addition, please see the `assumptions.txt`, `feedback.txt` and `hours.txt` files. The "Deliverable" section contains further information about them.


#### Running locally

1. Scrapy allows to [run](https://doc.scrapy.org/en/latest/intro/tutorial.html#how-to-run-our-spider) any spider locally.
   > scrapy crawl trial

2. More than that you can also [debug](https://doc.scrapy.org/en/latest/topics/commands.html#shell) with Scrapy.
   It can be really useful if you are getting responses different to the ones you see in the browser or would like to check selectors quickly:
   > $ scrapy shell <url_to_explore>
   >
   > \>>> # experiment with response


#### Running at Scrapy Cloud (AKA "SC")

This trial requires a crawling job at Scrapy Cloud as deliverable.

Zyte has its own [command line tool](https://shub.readthedocs.io/en/stable/quickstart.html) to make Scrapy Cloud deployments, called `shub`.

Important steps to make deployments the right way:

1. [Login to Scrapy Cloud](https://shub.readthedocs.io/en/stable/quickstart.html#basic-usage) by executing `shub login`

    You'll need to provide your Zyte API key on this step. It can be found at https://app.zyte.com/account/apikey

2. [Set the project id](https://shub.readthedocs.io/en/stable/configuration.html#where-to-configure-shub) so _shub_ would know the target for deployment.

    `scrapinghub.yml` file needs to be updated with the correct project id. You can take it from the end of the URL you received with the invitation to the trial:
    `https://app.zyte.com/p/<project_id>/`

    **Attention**: This project is configured to use `scrapy == 2.5`,
    so if you are using a different version you'll need to update `scrapinghub.yml` and `requirements.txt` accordingly. For more information about the available `scrapy` versions in SC, please refer to [Changing the Deploy Environment With Scrapy Cloud Stacks](https://support.zyte.com/support/solutions/articles/22000200402)

3. Run `shub deploy` to load code into Scrapy Cloud.
4. Run `shub schedule trial` to start a spider job on SC. It is also possible to run the spider in the UI by hitting `Run` button.
5. Check your project page at `https://app.zyte.com/p/<project_id>/` to see the collected data.


### Deliverable ###

* The spider, committed and pushed to this repository

    The spider should be written in Python 3.8+ and follow the PEP8 style guidelines. Please also commit shub's `scrapinghub.yml` file (with any sensitive information removed).

    Please keep the followings points in mind when delivering your code:

    1. Commit History. Do not worry about delivering a clean commit history, do as many commits as you would do while working normally. Please do not squash everything into a single commit, we use the commit history to review the evolution of your work.
    2. Code quality. The final version of your code will be considered finished and production-ready - please make sure the spider results are complete and look correct upon inspection. You can check the [online documentation](https://doc.scrapy.org) to learn about Scrapy's features and best practices.

* A complete run of your finished spider in Scrapy Cloud
   You will receive an email with an invitation to a Scrapy Cloud project for this purpose 
   (if you do not, please let us know). [Instructions for deploying can be found here](https://support.zyte.com/support/solutions/articles/22000204081-deploying-your-spiders-to-scrapy-cloud)

* Spent time report

    Please include a file called "hours.txt" with a list of tasks you worked on and the amounts of time you worked on them. You can be as detailed as you want, but a summary of high-level points is often enough (learning Scrapy, spider design, implementation, testing, etc). Keep in mind that this is not a time competition, a clean implementation is preferable over a quick one.

* Assumptions and decisions report

    Please document assumptions you made and reasons for decisions you made in a file called "assumptions.txt" in your repository. We will refer to this if your code contains things we did not expect.

* Feedback

    We would appreciate any feedback as per this trial. Please put it into "feedback.txt". Some specific questions are provided, but if you only have one thing to say, we're eager to receive any feedback at all. Please share!

### Time limit ###

We expect this project to take around 8-10 hours depending on your level of experience. We do not want you to over-invest yourself in this project, so if you're still working after spending 16 hours please stop and submit what you've completed.

### Deadlines ###

This project does not have a deadline. Just submit the results as soon as you have them ready (but no sooner) including the spent time report. The sooner you submit, the sooner we will move to the next step.

### Confidentiality ###

Please do not share code or specifications about this project with anyone outside Zyte.
