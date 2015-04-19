[ComicVineScraper-1.0.86.plugin](http://bit.ly/cvs1086)
  * released November 11, 2014
  * fixed problem where scraper couldn't understand filenames that use hyphens instead of spaces (see issue [399](https://code.google.com/p/comic-vine-scraper/issues/detail?id=399))
  * improved handling of filesnames with leading story arc numbers
    * i.e. this kind of filename, which is quite common: "001 The Zero-Men #132.cbr" (see issue [337](https://code.google.com/p/comic-vine-scraper/issues/detail?id=337))
  * minor improvements when scraper parses very large issue numbers out of filenames
    * these numbers should be confused with years less often (see issues [389](https://code.google.com/p/comic-vine-scraper/issues/detail?id=389) and [395](https://code.google.com/p/comic-vine-scraper/issues/detail?id=395))

---


[ComicVineScraper-1.0.85.plugin](http://bit.ly/cvs1085)
  * released October 24, 2014
  * fixed the obsolete Comic Vine API link on the "Comic Vine" tab in the Settings dialog (see issue [398](https://code.google.com/p/comic-vine-scraper/issues/detail?id=398))
  * minor stability improvements

---


[ComicVineScraper-1.0.84.plugin](http://bit.ly/cvs1084)
  * released August 1, 2014
  * better handling of numbering like "4 of 5" in filenames, when the word 'of' is in non-english languages (see issue [393](https://code.google.com/p/comic-vine-scraper/issues/detail?id=393))
  * the term 'ctc' is now ignored by the scraper when it appears in filenames (see issue [381](https://code.google.com/p/comic-vine-scraper/issues/detail?id=381))
  * also added the [IGNORE\_SEARCHTERM](https://code.google.com/p/comic-vine-scraper/wiki/AdvancedFeatures#IGNORE_SEARCHTERM) advanced setting so users can specify other terms to ignore

---


[ComicVineScraper-1.0.83.plugin](http://bit.ly/cvs1083)
  * released June 29, 2014
  * improved "SCRAPE\_DELAY" implementation (doesn't freeze app now)
  * updated all language packs for latest changes

---


[ComicVineScraper-1.0.82.plugin](http://bit.ly/cvs1082)
  * released June 23, 2014
  * added "SCRAPE\_DELAY" advanced setting

---


[ComicVineScraper-1.0.81.plugin](http://bit.ly/cvs1081)
  * released June 11, 2014
  * fixed bug where your settings got lost when you updated the plugin

---

[ComicVineScraper-1.0.80.plugin](http://bit.ly/cvs1080)
  * released June 11, 2014
  * all text fields now have Copy/Cut/Paste when you right click
  * scraper settings have been moved to windows settings directory so they don't get lost if there's an error updating the plugin
  * fixed plugin to report # of skipped/scraped comics, even when an error occurs while scraping.
  * minor bug fixes

---

[ComicVineScraper-1.0.79.plugin](http://bit.ly/cvs1079)
  * released June 10, 2014
  * all users are now required to provide their own Comic Vine API key
  * added "Comic Vine" tab to settings dialog
  * better error messages when Comic Vine rate limits are reached (see issue [382](https://code.google.com/p/comic-vine-scraper/issues/detail?id=382))
  * better error handling; something goes wrong, don't keep retrying forever
  * minor database query throttling, to ease the load on Comic Vine's database
  * minor efficiency improvements, less accesses to Comic Vine's database

---

ComicVineScraper-1.0.77.plugin
  * released April 6, 2014
  * fixes issue [368](https://code.google.com/p/comic-vine-scraper/issues/detail?id=368)
  * uses new API key to access Comic Vine
  * you can specify your own API key in Advanced Settings

---

ComicVineScraper-1.0.76.plugin
  * released March 23, 2014
  * fixes issue [364](https://code.google.com/p/comic-vine-scraper/issues/detail?id=364)

---

ComicVineScraper-1.0.75.plugin
  * released March 17, 2014
  * fixes issues [363](https://code.google.com/p/comic-vine-scraper/issues/detail?id=363) and [347](https://code.google.com/p/comic-vine-scraper/issues/detail?id=347)

---

ComicVineScraper-1.0.74.plugin
  * released March 11, 2014
  * works with latest changes to ComicVine API

---

ComicVineScraper-1.0.73.plugin
  * checks "comicvine\_volume" field when trying to guess series

---

ComicVineScraper-1.0.72.plugin
  * added new Dutch/Netherlands (nl-NL) language pack

---

ComicVineScraper-1.0.71.plugin
  * fix for issue [349](https://code.google.com/p/comic-vine-scraper/issues/detail?id=349)

---

ComicVineScraper-1.0.70.plugin
  * fix for issue [342](https://code.google.com/p/comic-vine-scraper/issues/detail?id=342)

---

ComicVineScraper-1.0.69.plugin
  * updated missing Polish translations
  * fixes for issue [329](https://code.google.com/p/comic-vine-scraper/issues/detail?id=329) and issue [334](https://code.google.com/p/comic-vine-scraper/issues/detail?id=334)

---

ComicVineScraper-1.0.68.plugin
  * fix for issue [327](https://code.google.com/p/comic-vine-scraper/issues/detail?id=327)

---

ComicVineScraper-1.0.67.plugin
  * added automatic scraping (via issue cover matching)
  * added "confirm each issue before proceeding" option
  * scraper now populates custom comic book fields: comicvine\_issue, and comicvine\_volume
  * scraper no longer adds scraped date when putting CVDB tag into comments
  * updates to all language packs except Polish
  * fixes for issues [322](https://code.google.com/p/comic-vine-scraper/issues/detail?id=322), [323](https://code.google.com/p/comic-vine-scraper/issues/detail?id=323), and [325](https://code.google.com/p/comic-vine-scraper/issues/detail?id=325)