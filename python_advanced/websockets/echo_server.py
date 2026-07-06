#!/usr/bin/env python3
"""Minimal WebSocket echo server.

Listens on localhost:8765, accepts multiple concurrent clients,
and echoes back any text message it receives.
"""
import asyncio
import websockets


async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())