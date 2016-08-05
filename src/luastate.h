#ifndef LUASTATE_H
#define LUASTATE_H

#include <map>
#include <string>

#include <nan.h>

//using namespace v8;

#include "utils.h"

extern "C"{
#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>
}

class LuaState : public Nan::ObjectWrap{
 public:
  lua_State* lua_;
  std::string name_;
  
  static void Init(v8::Local<v8::Object> exports);
 
  static int CallFunction(lua_State* L);
 private:
  LuaState();
  ~LuaState();
  void close_state();

  static Nan::Persistent<v8::Function> constructor;

  typedef std::map<std::string, 
    Nan::Callback* > functions_map_t;
  functions_map_t functions;

  static NAN_METHOD(New);
  static NAN_METHOD(Close);
  static NAN_METHOD(GetName);

  static NAN_METHOD(CollectGarbageSync);
  
  static NAN_METHOD(DoFileSync);

  static NAN_METHOD(DoStringSync);

  static NAN_METHOD(SetGlobal);
  static NAN_METHOD(GetGlobal);

  static NAN_METHOD(CallGlobalSync);

  static NAN_METHOD(RegisterFunction);
};
#endif
