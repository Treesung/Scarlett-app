from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

import uvicorn

async def homepage(request):
    return JSONResponse({'As we all know': 'Your mom is gay'})

async def about(request):
    return JSONResponse({'Name ': 'Joe'})

async def contact(request):
    return JSONResponse({'email': 'joe@gmail.com.'})

app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/about', about),
    Route('/contact', contact)
])

if __name__ == "__main__":
    uvicorn.run("starlette_api:app", host="0.0.0.0", port=6969, reload=True)