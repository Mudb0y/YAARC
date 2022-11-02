# YAARC

Yet another accessible Reddit client

## Why?

Just because I can.

Also, it's fun and I want another project to work on.

I suppose the main reason though is a lack of an RFB like client for anything other than Windows, and I love RFB so I'll clone it my self.

## Concept

This is supposed to be a concept-clone of Reddit For Blind, which in my experience is the fastest way to browse Reddit with a screen-reader.

On top of the basic features you'd expect from a Reddit client, I'm planning on potentially adding more features such as chat integration, native video playback support, and more.

## Guess we're using WX, then

Originally I planned to use Pyglet and build my own UI. People have discouraged me from doing so, and for good reason.

Instead, I'll go for a compromise. I want to be able to read posts quickly and efficiently with minimal efford, so instead of displaying part of the post in the listview, I'll send the contents to the speech API directly, whilst also displaying them in an edit-box for these who prefer reading.