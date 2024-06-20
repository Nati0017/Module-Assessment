# End of Module Assessment

Want to know a secret? Lots of cool things are made by people with no development experience at all. And lots of developers built their experience by.. well, by building things.

Below is the specification for an API I like to call "cheeper". It's a Twitter clone, but with absolutely no features - no users, no logins, nothing. All you can do is send it a message, and read all the messages.

**You're going to build a cheeper client**

Your instructor will give you an API endpoint for this task.

You can POST to the endpoint at `/send_cheep` with a data body of:

```
{
  "message": "Cheep cheep!"
}
```

And you can POST to the endpoint `/get_cheeps` to get a list of cheeps from the API endpoint. That bit isn't documented though - I guess you'll just have to test the endpoint and see what comes back.

Remember: you can start by trying to do this with the curl tool. Otherwise, you're going to have to look over your notes - and probably do a lot of Googling.

Good luck!
