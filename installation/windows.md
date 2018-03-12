# Setup MongoDB on Windows

Recommended version is via the MSI installer

* Run MSI
* Find `C:\Program Files\MongoDB\Server\3.6\bin`
    * Add that folder to path
* Create mongo folders
    * `c:\mongodb\data` 
    * `c:\mongodb\logs`
    * `c:\mongodb\configs`
* Copy configs: [win.config](win.config)
* Test configs
* `mongod --config c:\mongodb\configs\mongo-cmd.config`
* Install as windows service (ADMIN cmd)
`"C:\Program Files\MongoDB\Server\3.6\bin\mongod.exe" --config C:\mongodb\config\mongo-service.config --install`
* Change service startup mode to manual?

See MongoDB's full instructions at:

[docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)
