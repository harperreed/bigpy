big.py
=====

After [wondering on twitter what the best HTML5 presentation system was](https://twitter.com/harper/status/272538510349717506), I had a [few](https://twitter.com/maxogden/status/272539403287666689) [people](https://twitter.com/mattdennewitz/status/272543105071337473) mention that [big]() was a solid presentation generator. 

However, I wanted to use markdown to curate and handle my presentations and [big](https://github.com/tmcw/big) didn't handle markdown. There was a [fork](https://github.com/mdznr/big) that use markdown. I wanted to keep my content separate for curation purposes, so it didn't work for me. 

Instead, I wrote a helper: [big.py](https://github.com/harperreed/bigpy). 

#Usage

`$ python big.py --help`

	Usage: big.py [options]

	Options:
	  -h, --help            show this help message and exit
	  -s SLIDES.md, --slides=SLIDES.md
                        markdown file holding your slides!
	  -c big.css, --css=big.css
                        big stylesheet
	  -j big.js, --js=big.js
                        big javascript
	  -m MODE, --mode=MODE  mode: remote, local[default: remote]
	  -t TEMPLATE_MODE, --template_mode=TEMPLATE_MODE
                        template mode: allinone, light [default: allinone]

###Generate all in one `slide.html` from `slide.md`:

`$ python big.py -s slides.md`

	Attempting to open slide file: slides.md
	Remote css/js selected
	Pulling css from: https://raw.github.com/tmcw/big/gh-pages/big.css
	Pulling js from: https://raw.github.com/tmcw/big/gh-pages/big.js
	Parsing markdown file
		Title: Example Slides
		Author: Harper Reed
		Date: November 24, 2012
		Number of slides: 15
	Allinone template mode 
	Writing HTML: slides.html

This will output a `slides.html` that pulls the latest `big.css` and `big.js` from [tmcw/big]() embedded in it.  

###Generate all in one `slides.html` from local js/css

`$ python big.py -s slides.md --mode local`

	Attempting to open slide file: slides.md
	Local css/js selected
	Parsing markdown file
		Title: Example Slides
		Author: Harper Reed
		Date: November 24, 2012
		Number of slides: 15
	Allinone template mode 
	Writing HTML: slides.html
	
This will output `slides.html` with a local copy of `big.css` and `big.js` embeded in it. 

###Generate `slides.html` calling remote js/css

`$ python big.py -s slides.md --template_mode light`

###Generate allinone `slides.html`

`$ python big.py -s slides.md --template_mode allinone`

**Mix and match to your delight!**


#Examples slides.md

	% Example Slides
	% Harper Reed
	% November 24, 2012
	
	# use &harr; to navigate
	# Big.py
	# Big+Python+Markdown
	# Big
	# *Presentation software* for busy busy hackers
	# +text
	# +markdown formatting
	# as *big* as it can be
	# no config
	# *1.5k*
	# ![Images](http://farm3.static.flickr.com/2506/5757000880_509440308e_z.jpg) images too
	# JS+CSS [github.com/ tmcw/ big](https://github.com/tmcw/big)
	# Big.py
	# Helper script to generate slides from markdown
	# PY+MD [github.com/ harperreed/ bigpy](https://github.com/harperreed/bigpy)
	
#Next

No idea. I don't know if i will use this. I just wanted a way to generate big html with a script. It seemed like it should be easy. It was. Only one movie of hacking.

Feel free to fix things as you need them.  

#Thanks

* Obviously thanks goes to [Tom MacWright](https://github.com/tmcw) for [Big](https://github.com/tmcw/big).
* [@maxogden](https://twitter.com/maxogden) for his insane presentation on [JS for cats](http://t.co/90zq8ux6). It was what convinced me to check out [Big](https://github.com/tmcw/big). 
