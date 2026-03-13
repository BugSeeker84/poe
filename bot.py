from __future__ import annotations

import os
from typing import AsyncIterable

import fastapi_poe as fp


class EchoTestBot(fp.PoeBot):
    async def get_response(
        self, request: fp.QueryRequest
    ) -> AsyncIterable[fp.PartialResponse]:
        user_text = request.query[-1].content if request.query else ""
        if not user_text:
            yield fp.PartialResponse(text="Send me any message and I will echo it.")
            return

        yield fp.PartialResponse(text=f"Echo: {user_text}")

    async def get_settings(self, _: fp.SettingsRequest) -> fp.SettingsResponse:
        return fp.SettingsResponse(allow_attachments=False)


def create_poe_app():
    access_key = os.getenv("POE_ACCESS_KEY")
    if access_key:
        return fp.make_app(EchoTestBot(), access_key=access_key)
    return fp.make_app(EchoTestBot())


app = create_poe_app()
