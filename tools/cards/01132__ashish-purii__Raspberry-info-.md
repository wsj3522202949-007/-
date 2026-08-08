---
id: tool-01132
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Raspberry-info-
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/ashish-purii/raspberry-info-
created: 2026-07-18
updated: 2026-07-18
no: 1132
category: 二、网文 / 长篇 AI 写作系统 库
repo: ashish-purii/Raspberry-info-
stars: 1
url: https://github.com/ashish-purii/raspberry-info-
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 404359995248d7ff
  - methods/最强写作方法论_全球最强综合版.md
---

# ashish-purii/Raspberry-info-

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ashish-purii/raspberry-info-
- **Stars**：1
- **语言**：Python
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：This is the source code for the Raspberry IO site. Raspberry IO is a place to share knowledge about using the Python programming language to control Raspberry Pi computers.  This is an open source project. We welcome contributions. You can help by fixing bugs, planning new features, writing documentation, writing tests, etc
- **本地描述**：This is the source code for the Raspberry IO site. Raspberry IO is a place to share knowledge about using the Python programming language to control Raspberry Pi computers.  This is an open source project. We welcome contributions. You can help by fixing bugs, planning new features, writing documentation, writing tests, etc
- **拉取时间**：2026-07-23 23:12:02

---



Raspberry IO

========================



This is the source code for the `Raspberry IO <http://raspberry.io/>`_

site. Raspberry IO is a place to share knowledge about using the

Python programming language to control Raspberry Pi computers.



This is an open source project. We welcome contributions. You can help

by fixing bugs, planning new features, writing documentation, writing

tests, or even managing the project. Ready to contribute? Read our

`Getting Started <https://raspberry-io.readthedocs.org/>`_ document.





Submit an issue

------------------------



Found an issue? Have a question? We appreciate any and all feedback!

Issues are managed on `Github

<https://github.com/python/raspberryio/issues>`_. Please include

details about the browser, operating system, and/or device being used.



If you have a feature you'd like us to consider adding, please add the

"Proposal" label to your issue.



Dependencies

------------------------



Raspberry IO is a Django project using Postgres as our database. To

get started, you will need the following programs installed. These

should be installed using your operating system's standard package

management system:



- Python >= 2.6 (2.7 recommended)

- `pip >= 1.1 <http://www.pip-installer.org/>`_

- `virtualenv >= 1.7 <http://www.virtualenv.org/>`_

- `virtualenvwrapper >= 3.0 <http://pypi.python.org/pypi/virtualenvwrapper>`_

- Postgres >= 8.4 (9.1 recommended)

- git >= 1.7



Running the project

------------------------



Download the code::



    git clone git@github.com:python/raspberryio.git

    cd raspberryio



Create a virtualenv and install the necessary requirements::



    mkvirtualenv --distribute raspberryio

    $VIRTUAL_ENV/bin/pip install -r $PWD/requirements/dev.txt



Create a local settings file and set your ``DJANGO_SETTINGS_MODULE``

to use it::



    cp raspberryio/settings/local.example.py raspberryio/settings/local.py

    echo "export DJANGO_SETTINGS_MODULE=raspberryio.settings.local" >> $VIRTUAL_ENV/bin/postactivate

    echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate



Add the project directory to the virtualenv, deactivate and reactivate

it to setup the environment variables above::



    add2virtualenv .

    deactivate

    workon raspberryio



Create the Postgres database::



    createdb -E UTF-8 raspberryio



Run the initial syncdb/migrate. When asked to create a superuser,

answer ``no``. ::



    django-admin.py syncdb

    django-admin.py migrate



NOTE:

   Creating a superuser in the syncdb step will trigger the error

   ``django.db.utils.DatabaseError: relation "userprofile_profile"

   does not exist`` because of a required one-to-one relation with a

   user profile model that doesn't exist in the database yet.



**Now**, create a superuser (This will also create the profile correctly)::



    django-admin.py createsuperuser



Run the test suite with::



    django-admin.py test



You should now be able to run the development server::



    django-admin.py runserver





License

---------------------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---



This code is licensed under the `Apache 2.0 License

<http://www.apache.org/licenses/LICENSE-2.0.html>`_.

