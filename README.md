# python-filedump.
filedump compares the first few bytes of given files

While coding another project, I came accross a bug where my program couldn't load a certain jpg file, but was able to load other jpg files.
What made this weird is Windows was able to load and display the jpg in question.

I wanted to compare the first few bytes of the jpg in question, with the other jpg files that would load, side by side. Hence, filedump was created.

Sure enough, the jpg that would not load for me did not start like the other jpg files I had. This one started with RIFF ... WEBPVP8
While the others started with ...JFIF. And my bug was found!
