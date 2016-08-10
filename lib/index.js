var lua_host = null;

try{
    lua_host = require('../build/Release/lua_host');
}catch(e){
    lua_host = require('../build/Debug/lua_host');
}

module.exports = lua_host;