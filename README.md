Intro
=======
Taken from (1) and reduced to very limited set of icon's to have my most used emojis on my cell phone in sync. This doesn't fit at all but ok for me :) Enjoy!

Testing your own on the fly (tested on linux): 
  1. move selected file from image_src/ to images/ 
  2. Gajim -> settings:  toggle ones the emoji settings
  3. Test sending to your cell phone

(1): [jplitza/gajim-emojione](https://github.com/jplitza/gajim-emojione)



Unicode Emojis for Gajim
========================

This is a set of unicode emojis (or emoticons) for [Gajim], an XMPP client.
It makes Gajim display emojis sent by Android or Apple devices nicely and enables Gajim users to themselves send Unicode emojis.

It is based on [EmojiOne] with an automatically generated and only slightly modified index file attached to it so that Gajim can handle the icons correctly.
I manually added all ASCII codes the original “static“ emoticon pack that comes with Gajim supports (and a few more), but will gladly accept patches with more such additions.

[Gajim]: https://gajim.org/
[EmojiOne]: http://emojione.com/

Installation
------------
Either [download the ZIP][ZIP] or use git to clone the repository to the correct location (see below), go to the preferences of Gajim and select the newly appeared emoticon pack. The correct folders are:

* Linux: `$HOME/.local/share/gajim/emoticons/`
* Windows Vista/7/8/10: `%USERPROFILE%\AppData\Roaming\Gajim\Emoticons\`

[ZIP]: https://github.com/jplitza/gajim-emojione/archive/master.zip

License
-------
The emoji art itself is licensed by [EmojiOne] under [CC-BY 4.0].
The index file and generation script hardly count as an intellectual creation, but if needed, they are licensed under [CC0].

[CC-BY 4.0]: https://creativecommons.org/licenses/by/4.0/
[CC0]: https://creativecommons.org/publicdomain/zero/1.0/
