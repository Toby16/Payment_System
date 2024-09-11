#!/usr/bin/env python3

import uvicorn
import PAYMENT

if __name__ == "__main__":
    config = uvicorn.Config("PAYMENT:app", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
