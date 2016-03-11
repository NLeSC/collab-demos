# General remarks for usage of the demos

Most developers use Google Chrome as their main browser during development of a web demo, so that browser is least likely to give you unexpected behavior.

All webdemos require **internet access**. Note that this is true even when you have a local copy of all the demo code&mdash;this is because the webdemos rely on additional JavaScript libraries (e.g. [jQuery](https://jquery.com/), [lodash](https://lodash.com/), [Bootstrap](http://getbootstrap.com/), [D3](https://d3js.org/)) that are typically downloaded when you start the webdemo.

If you expect you won't have internet access at the presentation venue, it may be worthwhile to make a local copy or _clone_ of this repository beforehand, including all the video files. That way, you will at least be able to show the screencast video of the demos. [This](./getting-a-full-repo-copy.md) document describes how to clone a GitHub repository to a Windows system.

Some webdemos have additional requirements. These are explained below.


**IP-whitelisting**

Some demos download data from an external database. It can happen that the database has been configured in such a way that it will allow a request for data as long as that request is made from a known (or _whitelisted_) Internet Protocol or _IP_ address. Typically, the Collab's IP address is on the whitelist, so the demo will work as long as you are using wired internet in the Collab. Note, however, that this does not automatically mean it also works via wireless internet (in the Collab), since that has its own IP address which may or may not be on the whitelist. The IP address for venues other than the Collab are typically unknown to the database, so the demo will not work there. It is usually possible to add IP addresses to the database's whitelist, but since this requires intervention by both the administrator of the wireless network at the venue, and the administrator of the database, it usually takes a few days to arrange.

**Credentials**

Some demos may require a login and password. What they are varies per demo. In any case, it's useful to keep your credentials for sharepoint handy, you may need it for showing the pitch presentations for example.

**GPU**

Some webdemos use hardware acceleration using GPUs. If your laptop doesn't have a (decent) GPU, it will still work, but the demo may get prohibitively slow. If you plan on showing the demo in the Collab, it may be worthwile to use the Collab Windows machine instead of your own laptop, since the Collab machine has good GPU capabilities (dual Quadro K5000's; [specs](http://www.nvidia.com/object/quadro-k5000.html#pdpContent=2)), in particular with respect to memory.

**Database**

Some demos get their data from a database. It can happen that the connection to that database is slow, even when the internet connection is good.


**Network**

TODO network speed, interference of other nearby wireless devices


