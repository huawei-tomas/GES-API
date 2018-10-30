# GES API

This is a short example that shows how to   
1. Generate a token for your graph.
2. Start, Stop, or Execute a gremlin query on your graph through the API.

### INSTALL

You're going to want to have a file somewhere (I named my `.ges_environ` in 
current directory) with the following environmental variables

```bash
export GES_REGION=<ges_region>
export GES_USER=<ges_user>
export GES_PSSWD=<ges_psswd>
export GES_DOMAIN=<ges_domain>
export GES_PROJECTID=<ges_projectid>
```
and then you can just call `source .ges_environ` and all your variables are 
set.

Then you can generate a token with `python gen_authkey.py` and use the API
to start, stop, or test the graph with 
`python test_api.py -a [start|stop|test]`
