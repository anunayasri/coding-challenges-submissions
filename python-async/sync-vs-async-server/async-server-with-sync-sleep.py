import time

from aiohttp import web


async def handle(request):
    # Simulate 10ms workload
    time.sleep(0.01)
    return web.Response(text="Hello from async server!")


def run_async_server():
    app = web.Application()
    app.router.add_get("/", handle)
    port = 9002
    print(f"Starting async + sync server on port {port}...")
    web.run_app(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    run_async_server()
