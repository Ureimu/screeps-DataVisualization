const { ScreepsAPI } = require('screeps-api');
const secretInf = require('./secret');
const fs = require('fs');

// Supports @tedivm's [Unified Credentials File format](https://github.com/screepers/screepers-standards/blob/34bd4e6e5c8250fa0794d915d9f78d3c45326076/SS3-Unified_Credentials_File.md) (Pending [screepers-standard PR #8](https://github.com/screepers/screepers-standards/pull/8))
//const api = await ScreepsAPI.fromConfig('main', 'appName')
// This loads the server config 'main' and the configs section 'appName' if it exists
// config section can be accessed like this:
// If making a CLI app, its suggested to have a `--server` argument for selection
//console.log(api.appConfig.myConfigVar)

// All options are optional
const api = new ScreepsAPI(secretInf.secret);

// If you want to point to the screeps PTR (Public Test Realm),
// you can set the 'path' option to '/ptr' and it will work fine.

// Dump Memory
api.memory.get('stats',secretInf.shard)
  .then(memory => {
    fs.writeFileSync('memory.json', JSON.stringify(memory))
  })
  .catch(err => console.error(err));


// Dump Memory Path
api.memory.get('rooms.W0N0')
  .then(memory => {
    fs.writeFileSync('memory.rooms.W0N0.json', JSON.stringify(memory))
  })
  .catch(err => console.error(err));