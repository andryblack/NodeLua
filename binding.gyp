{
  "targets": [
    {
      "target_name": "lua_host",
      "sources": [
        "src/utils.cc",
        "src/luastate.cc",
	    "src/nodelua.cc",
        "src/yajlbind.cc",

        "lua/src/lapi.c",
        "lua/src/lauxlib.c", 
        "lua/src/lbaselib.c", 
        "lua/src/lbitlib.c", 
        "lua/src/lcode.c", 
        "lua/src/lcorolib.c", 
        "lua/src/lctype.c",
        "lua/src/ldblib.c", 
        "lua/src/ldebug.c", 
        "lua/src/ldo.c", 
        "lua/src/ldump.c", 
        "lua/src/lfunc.c", 
        "lua/src/lgc.c", 
        "lua/src/llex.c", 
        "lua/src/lmathlib.c",
        "lua/src/lmem.c", 
        "lua/src/loadlib.c", 
        "lua/src/lobject.c", 
        "lua/src/lopcodes.c", 
        "lua/src/lparser.c", 
        "lua/src/lstate.c", 
        "lua/src/lstring.c",
        "lua/src/lstrlib.c", 
        "lua/src/ltable.c", 
        "lua/src/ltablib.c", 
        "lua/src/ltm.c", 
        "lua/src/lundump.c", 
        "lua/src/lvm.c", 
        "lua/src/lzio.c",
        "lua/src/linit.c",
        "lua/src/liolib.c",
        "lua/src/loslib.c",

        "yajl-2.1.0/src/yajl.c", 
        "yajl-2.1.0/src/yajl_alloc.c", 
        "yajl-2.1.0/src/yajl_buf.c", 
        "yajl-2.1.0/src/yajl_encode.c", 
        "yajl-2.1.0/src/yajl_gen.c", 
        "yajl-2.1.0/src/yajl_lex.c", 
        "yajl-2.1.0/src/yajl_parser.c",
        "yajl-2.1.0/src/yajl_tree.c"
	],
      "include_dirs": [
        "lua/src",
        "yajl-2.1.0/src/api",
        "<!(node -e \"require('nan')\")"
        ],
      "defines" : [],
      "libraries": [
        "-ldl"
	]
    }
  ]
}
