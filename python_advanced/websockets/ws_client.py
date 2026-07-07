#!/usr/bin/env python3
"""Minimal WebSocket client.

Connects to the echo server, sends one message, prints the response,
then lets the connection close.
"""
import asyncio
import websockets


async def client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello WebSocket")
        response = await websocket.recv()
        print(response)


if __name__ == "__main__":
    asyncio.run(client())
