CSS Layouts
Because CSS was never meant to be to do complex layouts, but was meant for “flat” documents, CSS layout went through a bit of history.

Tables and images
Initially, web designers and brands wanted websites to offer “pixel-perfect” like on print. However, this was very difficult to achieve as CSS did not render similarly across browsers, and fonts rendered very differently depending on the OS (which is still the case today, actually). Therefore, the very first “visual” websites were mostly images ordered together in border-less tables. This was obviously a nightmare in performance (huge images + very verbose HTML did not fare well with slow web connections) and in accessibility/SEO (tables are meant for tabular data and are recognized as such semantically, and texts in images were not recognized at text; for instance, they couldn’t be copy-pasted).

HTML frames were also very used at the time, but they fell out of fashion for those same reasons: performance because you’re loading many webpages instead of one, accessibility because it was near impossible to navigate the user from one frame to the other (with the keyboard, for instance), SEO because the URL of a webpage didn’t change when navigating, so some composite pages didn’t even have a navigable URL.

Early web standards
In the late 90s, a group of web developers and designers (most of them were a bit of both) started to evangelize about how it was entirely possible to make built great websites entirely with standards. The “Standard Web Project” was created in 1998 by Jeffrey Zeldman, who subsequently wrote his breakthrough book “Designing with Web Standards”. The book was a list of practical tricks to get each browsers to do what you need them to do.

Keep in mind that each browser still had a very, very different interpretation of CSS back then, so you basically had to develop one CSS per browser. Eventually, browser got more mature, and most code could gradually be mutualized for all browsers. Today, websites that don’t leverage the web standards are very rare.

Some key links from that time:

The Dao of Web Design is an article written in 2000 on A List Apart, the blog Jeffrey Zeldman founded for front-end experts to share their tricks. While most articles from back then have aged pretty badly, since browsers changed so much over the last few years, this one is still very current. It teaches people to let go of pixel-perfect, in order to embrace the goodies contained in web standards. Read it here: http://alistapart.com/article/dao
CSS Zen Garden was created by Dave Shea to showcase what CSS can do. It is basically a single HTML file, on which any one can contribute an original CSS stylesheet, to make it do interesting things. Check it out here: http://www.csszengarden.com
Float layout
As we’ve discussed, natively, HTML stacks fluid blocks vertically. People wanted to stack blocks horizontally too (next to each other), but except for positioning them as absolute (which breaks the flow of the page), the only other way to do it was to make them “float”.

The float statement, which takes left or right (or the default value none) was designed to make medias (like images) float the left or right of the text; and the text would nicely “go around” the image. But people found ways to “abuse” the float statement in order to build complex layouts. The clear statement is float‘s antagonist: it makes an element avoid to float by its previous elements.

More about float and clear: http://www.w3schools.com/css/css_float.asp

Because more recent options are not entirely mature yet, a lot of websites are still being made with floating layout.

CSS Display Table
It took long years for the W3C to have consensus on some layout specifications, and display table is one of the first ones that made it maturity. The idea is to take some HTML that doesn’t contain the <table> element, but make it behave like tables just with CSS.
It had been moderately popular, but it never rose to widespread uses, because one could not manage every layout use case this way.

CSS Flexbox
As a far more powerful alternative to CSS Display Table, CSS Flexbox has huge support from the browsers and the industry, despite the implementations in browsers not being 100% consistent in all cases. Many websites and web applications in the industry use CSS Flexbox: some mentors working at Salesforce confirmed that all applications are now built using it; another mentor working on Google Photos confirmed that it is what is being used there too. And for widespread adoption, the most used CSS frameworks are now switching to Flexbox, one by one.

Here is an excellent and fun tutorial for learning Flexbox: http://flexboxfroggy.com

The other ones?
Other CSS layout specifications are in the work at the W3C, such as CSS Grid; but none of them seem near maturity at all at this point. And it can be argued that the support CSS Flexbox is getting could actually be detrimental to them, since the industry seems gradually happy with it.

CSS Media Queries and Responsive Web Design
Another recent interesting piece of recent CSS history is the introduction of the CSS Media Queries, and the concept of Responsive Web Design.

Media queries allow to express that certain CSS rules should only be executed when certain conditions are in place (such as based on the screen’s resolution, or the number of colors a graphics card can handle). But the one condition that started to get very used, is the one allowing to only execute some CSS depending on the browser’s width. As you may have understood, this allows a single CSS codebase for a website regardless of the size of the browser, enabling and disabling some CSS rules when it passes certain width thresholds.

Do you remember Jeffrey Zeldman? (He’s the guy who founded A List Apart, the Web Standards Project, and wrote Designing with Web Standards) He’s part of the people who actually came up with the notion of Responsive Web Design, the idea to use media queries to make a single website adapt depending on the browser’s width.