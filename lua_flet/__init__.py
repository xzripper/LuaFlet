"""Flet for Lua."""

from lupa import LuaRuntime

from flet import app

from importlib import import_module


LUA_FLET_VERSION = '1.0.0'

class LuaFlet:
    """LuaFlet Class."""

    lua_runtime: LuaRuntime = None
    """Lua Runtime."""

    lua_file: str = None
    """Lua File."""

    def __init__(self, lua_file: str) -> None:
        """Initialize LuaFlet."""
        self.lua_runtime = LuaRuntime()

        self.lua_file = lua_file

        self.lua_runtime.globals()['Flet'] = __import__('flet')

        def pyimport(module: str, _import: str=None, package: str=None) -> None:
            return import_module(module, package) if not _import else getattr(import_module(module, package), _import)

        self.lua_runtime.globals()['pyimport'] = pyimport

        self.lua_runtime.globals()['LUA_FLET_VERSION'] = '1.0.0'

    def run(self, **app_kwargs) -> None:
        """Run lua file."""
        with open(self.lua_file, 'r') as _lua_code:
            lua_code = _lua_code.read()

        return app(self.lua_runtime.execute(lua_code), **app_kwargs)

def run(lua_file: str, **app_kwargs) -> None:
    """Run lua file."""
    return LuaFlet(lua_file).run(**app_kwargs)
