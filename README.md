# YAARC

Yet another accessible Reddit client

## Disclaimer

This is nowhere near complete. I started this as a private repo because I wasn't sure how I'll license it and I hate having a bunch of empty / unfinished projects on my public profile.

It seems as though this project will actually get somewhere so I decided to publish it.

Be warned though, the code will be verry messy. This is my first ever project on a bigger scale (multiple modules, UI, ETC) so I can say this without a shadow of a doubt in my mind. Oh, and friendly tip, do not look at the commit history and all the changed files unless you want to facepalm.

If you have any ideas for improvement, feel free to submit issues and PRs! I'll be grateful for any contributions and feedback.

## What is implemented so far?

I managed to successfully make a very basic authentication library which checks for a saved refresh token, and if none is found it authenticates through Reddit's API.

For now I managed to display submitions from R/Test in a list. After I implement displaying of the body text I will actually display the contents of a users front-page.

## Why?

Just because I can.

Also, it's fun and I want another project to work on.

I suppose the main reason though is a lack of an RFB like client for anything other than Windows, and I love RFB so I'll clone it my self.

## Concept

This is supposed to be a concept-clone of Reddit For Blind, which in my experience is the fastest way to browse Reddit with a screen-reader.

On top of the basic features you'd expect from a Reddit client, I'm planning on potentially adding more features such as chat integration, native video playback support, and more.

## Guess we're using WX

Originally I planned to use Pyglet and build my own UI. People have discouraged me from doing so, and for good reason.

Instead, I'll go for a compromise. I want to be able to read posts quickly and efficiently with minimal efford, so instead of displaying part of the post in the listview, I'll send the contents to the speech API directly, whilst also displaying them in an edit-box for these who prefer reading.

### UI Design

For UI design, I'm using WXGlade. The reason for that is that it's very simple to use, and certainly simpler than designing the WX code from scratch.

So far it seems to work okay for this project, so I'll probably stick with it unless I hit a massive roadblock which will force me off-of using it.

When making new UI elements, keep in mind a few things:
* Do-not make everything in to a ton of menus. This will just make the navigation more clunky than it should be.
* Design the UI with blind users in mind. Test with a screen-reader and make sure everything reads before submitting a PR.
* And finally, just stick to common UI design practices and don't stray too far off them. I'll make allowances for some uncommon things that simply work better for blind people, as this is a client made by the blind for the blind, but for the love of god don't do what Luna for Reddit did with the whole putting full-stops on buttons thing. That is not how you design user interfaces, and blind or not this is a standard.
