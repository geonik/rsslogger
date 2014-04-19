A simple script to make log entries to an RSS feed.

Why would someone want to do this?

I don't know about someone
but I can tell you my use case was a little Raspberry Pi acting as
torrent machine. I wanted to have a simple way to push log messages
to my desktop computer and did not want to deal with the hassle of
setting up mail servers. So instead I used this approach to log messages
to an rss feed file, which I later read with a feed reader.

In my case I also did not have to use an HTTP server to read the feed since
the combination of ssh access and newsbeuter's `exec` urls allows me to read
the file without any additional setup.

Sample usage:

    rsslogger --feed-file test.rss "Test log message"

Run `rsslogger --help` to get help for all arguments.
