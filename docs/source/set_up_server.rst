Getting Started
===============

First, make sure you have:

- **Mention-Python** installed
- your Access token

See the :doc:`installation` page for help if needed.


App
---

Assume your access token is stored in ``access_token`` for all API calls:

App Data
^^^^^^^^
Retrieves useful details about the application.

    Like some other resources, certain properties are translated given the Accept-Language header.

Example:

.. code-block:: python

    >>> from mention import AppDataAPI
    >>> appData = AppDataAPI(access_token)


Alert
-----

Create an Alert
^^^^^^^^^^^^^^^

You can create a new alert for a given ``account_id``.

The minimum requirements for a new alert are the parameters ``name`` as a string, ``queryd`` as a dictionary and ``languages`` as a list of strings.

Example:

.. code-block:: python

    >>> name = "Nandos"
    >>> queryd = {"type": "basic", "included_keywords":
    ...	["Nandos", "Flame-grilled Chicken", "Peri-Peri Sauce"]}
    >>> languages = ["en"]
    >>> newAlert = mention.CreateAnAlertAPI(access_token, account_id, name,
    ...	queryd, languages)
    >>> data = newAlert.query()

If the request was successful, the response will return the full alert data, like if you did a :ref:`Fetch An Alert <Fetch an Alert>`.

Please view the `Create an alert <https://dev.mention.com/current/src/account/alert/PostAlert.html>`_ page to see all the available parameters and :class:`~mention.base.CreateAnAlertAPI` for formatting.


Fetch an Alert
^^^^^^^^^^^^^^

Retrieve details about a single ``alert_id`` for a given ``account_id``.

Example:

.. code-block:: python

    >>> nandosAlert = mention.FetchAnAlertAPI(access_token, account_id,
    ...	alert_id)
    >>> data = nandosAlert.query()
    >>> data['alert']['name']
    'Nandos'

    >>> data['alert']['query']['included_keywords']
    ['Nandos', 'Flame-grilled Chicken', 'Peri-Peri Sauce']


Fetch all alerts of an account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Fetch a list of all alerts for a given ``account_id``.

Example:

.. code-block:: python

    >>> allAlerts = mention.FetchAlertsAPI(access_token, account_id)
    >>> data = nandosAlert.query()
    >>> alertsList = data['alerts']
    >>> alertsList[5]['alert']['name']
    'Nandos'

    >>> data['alert']['query']['included_keywords']
    ['Nandos', 'Flame-grilled Chicken', 'Peri-Peri Sauce']


Update an Alert
^^^^^^^^^^^^^^^

Modifies an existing alert, usually to update the criteria and to improve the search's efficiency for a given ``account_id``.

This API call has all of the same parameters as :ref:`Create An Alert <Create an Alert>`.

Example:

.. code-block:: python

    >>> name = "Nandos"
    >>> queryd = {"type": "basic", "included_keywords":
    ...		["Nandos", "Flame-grilled Chicken", "Peri-Peri Sauce",
    ...		"Garlic Rolls"]}
    >>> languages = ["en", "af"]
    >>> countries = ["US", "ZA", "UK"]
    >>> sources = ["web", "twitter"]

    >>> updateNandosAlert = mention.UpdateAnAlertAPI(access_token, account_id,
    ...	name, queryd, languages, countries, sources)

    >>> data = updateNandosAlert.query()

Again a successful request will return the full alert data as a response.

Please view the `Update an alert <https://dev.mention.com/current/src/account/alert/PutAlert.html>`_ page to see all the available parameters and :class:`~mention.base.UpdateAnAlertAPI` for formatting.


Mention
-------

Fetch a mention
^^^^^^^^^^^^^^^

Retrieve details about a single ``mention_id`` for a given ``alert_id`` from an ``account_id``.

Example:

.. code-block:: python

    >>> nandosMention = mention.FetchAMentionAPI(access_token, account_id,
    ...	alert_id, mention_id)
    >>> data = nandosMention.query()
    >>> data['title']
    "Nando's launches their own food ordering app"

    >>> data['description']
    "Nando's has launched their own app that will allow people to order their favourite meal from the comfort of their own home."

    >>> data['original_url']
    "https:\/\/www.iol.co.za\/business-report\/technology\/nandos-launches-their-own-food-ordering-app-18378360"


Fetch mentions
^^^^^^^^^^^^^^

Fetch a list of all mention for a given ``alert_id`` from an ``account_id``.

There are 16 parameters which can be used to filter the mentions you receive as a response. Please note that some parameters cannot be used in combination with others. For example ``since_id`` cannot be combined with ``before_date``, ``not_before_date`` or ``cursor``.

Please view the `Fetch Mentions <https://dev.mention.com/current/src/account/alert/mention/GetMentions.html>`_ page to see all the available parameters and :class:`~mention.base.FetchAllMentionsAPI` for formatting. For example read and favourite uses the python boolean type instead of a string.

Example:

.. code-block:: python

    >>> nandosMentions = mention.FetchAllMentionsAPI(access_token, account_id,
    ...	alert_id, limit="1000",
    ...	before_date="2018-11-25 12:00",
    ...	not_before_date="2018-10-04 12:00",
    ...	source="twitter",
    ...	read=True)

    >>> data = nandosMentions.query()
    >>> firstMention = data['mentions'][0]
    >>> firstMention['title']
    "Nando's launches their own food ordering app"

    >>> firstMention['description']
    "Nando's has launched their own app that will allow people to order their favourite meal from the comfort of their own home."

    >>> firstMention['original_url']
    "https:\/\/www.iol.co.za\/business-report\/technology\/nandos-launches-their-own-food-ordering-app-18378360"

    >>> if len(data['_links']['more']['href']) == 0:
    >>>		print('No more mentions to receive.')
    "No more mentions to receive."

.. note::

    ``limit`` is capped at 1000. To view more mentions use the ``_links``, ``more`` and ``pull`` urls to receive all of your mentions. To learn more about this, read the bottom of `Fetch Mentions <https://dev.mention.com/current/src/account/alert/mention/GetMentions.html>`_.


Curate a mention
^^^^^^^^^^^^^^^^

Updates an existing ``mention_id`` for a given ``alert_id`` from an ``account_id``. These update concern majorly classification of the mention: indicating the folder, tags, effective tone of the mention, etc... You cannot modify the content of a mention, or its source.

There are 6 parameters which can be used to change how a mention is classified. ``favorite`` and ``trashed`` can only be editted by an admin. Please view the `Curate Mention <https://dev.mention.com/current/src/account/alert/mention/PutMention.html>`_ page to see all the available parameters and :class:`~mention.base.CurateAMentionAPI` for formatting.

Example:

.. code-block:: python

    >>> nandosMention = mention.CurateAMentionAPI(access_token, account_id,
    ...	alert_id,
    ...	mention_id,
    ...	favorite=True,
    ...	tone='-1')

    >>> data = nandosMention.query()
    >>> data['favorite']
    'true'

.. note::

     A mention can only be associated with an existing ``tag``. This means that you have to `create a tag <https://dev.mention.com/current/src/account/alert/tag/PostTag.html>`_ first. Mention-Python does not currently support this feature.


Mark all mentions read
^^^^^^^^^^^^^^^^^^^^^^

Mark all mentions as read for a given ``alert_id`` from an ``account_id``.

Example:

.. code-block:: python

    >>> nandos = mention.MarkAllMentionsReadAPI(access_token, account_id,
    ...	alert_id)

    >>> data = nandos.query()