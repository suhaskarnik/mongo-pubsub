Use Mongo DB to implement a simple pubsub architecture using a Python CLI app.

## Structure

`main.py` is the entry point



## Pre-Reqs
On Fedora, ensure you have `mongosh` installed. The default version fails due to SSH issues, so install the below. 
```bash
cat << EOF > ./mongodb-org-7.0.repo 
[mongodb-org-7.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/9/mongodb-org/7.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/server-7.0.asc(.venv) 
EOF

sudo mv ./mongodb-org-7.0.repo /etc/yum.repos.d/

sudo dnf install mongodb-mongosh-shared-openssl3.x86_64
```

Note: because we are going to deploy Mongo in a Docker container, just `mongosh` will suffice. The rest of `mongodb-org` is not required. Also, the standard version of `mongodb-mongosh` throws an SSL error. [This is why](https://jira.mongodb.org/browse/MONGOSH-1231?jql=text%20~%20%22mongodb-mongosh-shared-openssl3%22) the OpenSSL3 variant needs to be installed 

## Deploy and Run

Deploy MongoDB and test connection
```bash
docker pull mongodb/mongodb-community-server:latest
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest
mongosh --port 27017
```

Populate the MONGO_URL variable in the `.env` file 
```bash
echo "MONGO_URL=$(mongosh --eval "db.getMongo()")" > .env
```

Then initialise the database. It generates a log file in `/tmp/` with a randomised name (which is also printed to the output)
```bash
python main.py init
```

NOTE: for all of the subcommands of `main.py`, you can add the `--help` arg to get usage instructions. All options have sane defaults, so you can run the subcommand even without providing them. 

Now create two terminal sessions, one for pub and one for sub.  
Publisher:
```bash
python main.py pub
```

Subscriber:
```bash
python main.py sub
```