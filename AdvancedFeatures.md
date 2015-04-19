## Advanced Settings ##

There are a number of advanced settings that you can use to control Comic Vine Scraper.  You use them by adding special instructions into the "Advanced" section of the Settings window.

For example, if you don't want the scraper to load cover art from the Comic Vine website, you can type the following line into the Settings window:

```
SHOW_COVERS=FALSE
```

There are many other advanced settings that you can add.  There can only be one instruction per line, but the order of the instruction lines doesn't matter.  Capitalization and whitespace don't matter either.

Here's a list of the advanced settings instructions that you can use:


&lt;BR&gt;




&lt;BR&gt;




&lt;BR&gt;




&lt;BR&gt;


### ALT\_SEARCH\_REGEX ###

If you know how to write [regular expressions](http://www.google.ca/search?q=regular+expressions+tutorial), you can use this setting to improve how Comic Vine Scraper searches for your comic books based on their filenames.

Your custom regular expression will be matched against the filename of each comic as it is being scraped.  It must contain a _named group_ called **'series'** that matches the name of the comic book series.  If possible, it should also contain a named group called **'num'** that matches the issue number of that comic, and optionally a third one called **'year'** that matches the year that the comic was published.

So if your comic book files were named something like:

```
0001, Batman Beyond, DC Comics (2009).cbz
0002, Batman Beyond, DC Comics (2009).cbr
```

you could provide a regular expression like:

```
ALT_SEARCH_REGEX=(?P<num>\d+),(?P<series>.+),.+\((?P<year>\d{4})\)\.(cbz|cbr)
```



&lt;BR&gt;




&lt;BR&gt;


### IGNORE\_AFTER\_YEAR ###

Use this to cause the scraper to hide all comic book series that were first published **after** a certain year.   For example, if you don't want your searches to show any series that started after 1994:
```
IGNORE_AFTER_YEAR=1994
```



&lt;BR&gt;




&lt;BR&gt;



### IGNORE\_BEFORE\_YEAR ###

Use this to cause the scraper to hide all comic book series that were first published **before** a certain year.   For example, if you don't want your searches to show any series that started before 1980:
```
IGNORE_BEFORE_YEAR=1980
```



&lt;BR&gt;




&lt;BR&gt;



### IGNORE\_FOLDERS ###

Normally, Comic Vine Scraper will only decide that two comics are part of the same series if their files are in the same folder on your hard drive (and even then, they must also have the same series names.)  If you don't want the scraper to consider the location of each comic when deciding whether or not two comics are part of the same series, just add the following line:
```
IGNORE_FOLDERS=TRUE
```
Once you've done this, the scraper will only compare two comic books' file names when deciding if they belong to the same series.  Their file locations will be ignored.



&lt;BR&gt;




&lt;BR&gt;



### IGNORE\_PUBLISHER ###

Use this to cause the scraper to hide all comic book series that are published by a specific publisher.  You can also use the IGNORE\_PUBLISHER instruction more than once to cause the scraper to ignore multiple publishers.

For example, if you don't want your searches to show any series published by 'Panini' OR 'Panini Comics', add the following two lines:
```
IGNORE_PUBLISHER=panini
IGNORE_PUBLISHER=panini comics
```



&lt;BR&gt;




&lt;BR&gt;



### IGNORE\_SEARCHTERM ###

This setting causes the scraper to ignore a search term when trying to find a comic on Comic Vine.

When the scraper searches for your comic, it does so based on your comic's filename.  If that filename contains certain terms like 'c2c' or 'noads', those terms will not be used as part of the search.  You can use IGNORE\_SEARCHTERM to specify additional terms that should never be used for searching.

You may only specify one search term per line, and it must contain ONLY alphanumeric characters (a-z and 0-9).  Search terms may NOT contain spaces or other punctuation characters.

For example, if you want the scraper to ignore the words 'digital' and 'covers' when searching for comics, add the following two lines:
```
IGNORE_SEARCHTERM=digital
IGNORE_SEARCHTERM=covers
```



&lt;BR&gt;




&lt;BR&gt;



### IMPRINT ###

Use this to define your own imprint publishers in cases where the default Comic Vine Scraper imprints are not to your liking.  This instruction allows you to define a new imprint or override an existing one.  You can also use the IMPRINT instruction more than once if you want to create multiple imprints.

For example, if your want the scraper to treat 'Panini' as an imprint of 'Marvel', you can add the line:
```
IMPRINT=Panini => Marvel
```

You can also remove any of the default Comic Vine Scraper imprints by redefining them as imprints of themselves.  For example, if you want Comic Vine Scraper to stop treating 'Maverick' as an imprint of 'Dark Horse Comics', simply add the line:
```
IMPRINT=Maverick => Maverick
```



&lt;BR&gt;




&lt;BR&gt;



### NEVER\_IGNORE\_THRESHOLD ###

This stops the scraper from ignoring comic series that have a large number of issues.  For example, if you want to ignore all the comics that came out before 1980, EXCEPT for ones that have 100 issues or more:
```
IGNORE_BEFORE_YEAR=1980
NEVER_IGNORE_THRESHOLD=100
```



&lt;BR&gt;




&lt;BR&gt;



### NOTE\_SCRAPE\_DATE ###

Use this to cause the scraper to include the current date and time whenever it writes out CVDB info into the "Notes" field of your comic books. But be careful; doing this will force the scraper to update all of your comic books every time they are re-scraped, even if their other metadata has not changed:
```
NOTE_SCRAPE_DATE=TRUE
```



&lt;BR&gt;




&lt;BR&gt;



### PUBLISHER\_ALIAS ###

Use this to change the name that Comic Vine Scraper will scrape for a publisher.  You can use this instruction more than once to change the name of multiple publishers.

For example, if you want comics from the publisher 'Dynamite Entertainment' to be scraped with the publisher name 'Dynamite', just add the following line:
```
PUBLISHER_ALIAS=Dynamite Entertainment => Dynamite
```

Or if you want to rename 'Marvel', you could add something like:
```
PUBLISHER_ALIAS=Marvel => Stan Lee and Friends
```



&lt;BR&gt;




&lt;BR&gt;



### SCRAPE\_DELAY ###

You can force Comic Vine Scraper to pause for a certain number of seconds between each comic that it scrapes.  This makes scraping take longer, of course, but it can be a useful if Comic Vine bans you from scraping because you are accessing their database too frequently:
```
SCRAPE_DELAY=30
```
WARNING: setting this value will make Comic Vine Scraper seem very slow and unresponsive.  Use this feature are your own risk!



&lt;BR&gt;




&lt;BR&gt;



### SCRAPE\_RATING ###

Older versions of Comic Vine Scraper used to scrape a piece of metadata called the "Rating" from the Comic Vine website.  If you still want to scrape the Rating, you can re-enable this feature:
```
SCRAPE_RATING=TRUE
```
WARNING: scraping the Rating causes Comic Vine Scraper connect to the Comic Vine website more often, which can make it run very slowly and use up your Comic Vine access limit more quickly.  Enable this feature at your own risk!



&lt;BR&gt;




&lt;BR&gt;



### SHOW\_COVERS ###

Use this to turn off issue cover art while scraping.  For slower internet connections, this may speed up scraping.
```
SHOW_COVERS=FALSE
```



&lt;BR&gt;




&lt;BR&gt;



### WELCOME\_DIALOG ###

Use this to turn off the initial 'Welcome' window that appears when you first start scraping.   BUT BE CAREFUL!  That Welcome window is the easiest way to get into the Settings window--once you turn it off, you may have trouble finding your way back into Settings to turn it back on again!
```
WELCOME_DIALOG=FALSE
```



&lt;BR&gt;




&lt;BR&gt;




---




&lt;BR&gt;




&lt;BR&gt;



## The CVINFO file ##

You can create a special file called **cvinfo** in any folder where you keep your comic book scans.  Whenever you scrape a new comic that's stored in the same folder as a **cvinfo** file, the scraper will use **cvinfo** to automatically determine which series your comic belongs to.

The **cvinfo** file must be a plain text file, like you would create with Notepad, or some other simple text editor.  It should contain exactly one line, and that line should be the web address (URL) for a comic book series at the ComicVine website.

For example, if you have a folder that contains ONLY issues from "Detective Comics", you could add a **cvinfo** file with the following:

```
http://www.comicvine.com/detective-comics/4050-18058/
```

See that number "4050-18058" at the end?  That's the important part.  If that number doesn't start with "4050-", you've got the wrong Comic Vine page, and your **cvinfo** file isn't going to work!



&lt;BR&gt;




&lt;BR&gt;




---



&lt;BR&gt;



## CVDB Tags ##

Comic Vine Scraper (or you!) can add a special marker called a "CVDB Tag" into the _Tags_ and _Notes_ sections of each of your scraped comics.  If you look in the _Tags_ or _Notes_ of any comic that you've already scraped, you'll find an example of a CVDB tag.  It will look something like "CVDB123456".

The scraper can use these CVDB tags to figure out which Comic Vine entry you chose the last time you scraped each comic.  As long as your comics have their CVDB tags, you won't have to choose Comic Vine entries again when you re-scrape them; the scraper will automatically remember which entry to use.

There is also a special tag called "CVDBSKIP", which causes the scraper to ignore comics.  There are two ways you can add a CVDBSKIP tag to a comic scan:

  1. Using ComicRack, type the word "CVDBSKIP" into the _Tags_ and _Notes_ for that comic. (Replace any previous CVDB tag that might already be there.)
  1. When you are scraping your comics, hold down the "Control" key and click the "Skip" button when the comic you want to CVDBSKIP comes up

If you do this, Comic Vine Scraper will COMPLETELY IGNORE your comic from now on.  In other words, it will never try to scrape that comic ever again, even if you tell it to.  Of course, if you change your mind and decide you don't want this, all you need to do is remove the CVDBSKIP tag.



&lt;BR&gt;




&lt;BR&gt;

