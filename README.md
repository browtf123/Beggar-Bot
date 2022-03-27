### To run

There are scripts to help you along.
First build the image:
`./scripts/build-docker.sh`

You will need to have a file in this directory called .env which contains json with your discord bot token, e.g.:
```
{
    "token":"yourtokenhere"
}
```

Then run the image:
`./scripts/local-run`

To enter the docker container in a shell for developer mode, call:
`./script/dev-env`