import json
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


class ValidationException:
    @staticmethod
    async def execute(request: Request, exc: RequestValidationError):
        print(f"!!! VALIDATION ERROR !!!")
        print(json.dumps(exc.errors(), indent=2))

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"error": exc.errors()},
        )
