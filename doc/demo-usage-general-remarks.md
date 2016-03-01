

Most developers use Google Chrome as their main browser during development of a web demo, so that browser is least likely to give you unexpected behavior.

All webdemos require **internet access**. Note that this is true even when you have a local copy of all the demo code&mdash;this is because the webdemos rely on additional JavaScript libraries (e.g. [jQuery](https://jquery.com/), [lodash](https://lodash.com/), [Bootstrap](http://getbootstrap.com/)) that are typically downloaded when you start the webdemo.

If you expect you won't have internet access at the presentation venue, it may be worthwhile to make a local copy or _clone_ of this repository beforehand, including all the video files. That way, you will at least be able to show the screencast video of the demos. [This](./installing-github-desktop-on-windows.md) document describes how to clone a GitHub repository to a Windows system.

Some webdemos have additional requirements. These are explained below.


**IP-whitelisting**

Some demos download data from an external database. It can happen that the database has been configured in such a way that it allows requests for data, as long as that request is made from a certain Internet Protocol or _IP_ address. It is usually possible to add IP addresses to the database's list, but this requires intervention by the database's administrator and therefore may take a few days.

**Credentials**

TODO

**GPU**

TODO


