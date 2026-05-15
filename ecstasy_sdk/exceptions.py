"""Исключения ecstasy-sdk."""

from typing import Any


class EcstasyError(Exception):
    """Базовая ошибка SDK."""


class EcstasyConfigError(EcstasyError):
    """Ошибка конфигурации SDK."""


class EcstasyTransportError(EcstasyError):
    """Ошибка транспортного уровня."""


class EcstasyTimeoutError(EcstasyTransportError):
    """Ошибка таймаута HTTP-запроса."""


class EcstasyAPIError(EcstasyError):
    """Ошибка, полученная от Ecstasy API."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        method: str,
        url: str,
        request_id: str | None = None,
        response_text: str = "",
        response_json: dict[str, Any] | list[Any] | None = None,
        problem_type: str | None = None,
        title: str | None = None,
        detail: str | None = None,
        instance: str | None = None,
        errors: Any = None,
    ) -> None:
        """Инициализирует ошибку API."""

        super().__init__(message)
        self.status_code = status_code
        self.method = method
        self.url = url
        self.request_id = request_id
        self.response_text = response_text
        self.response_json = response_json
        self.problem_type = problem_type
        self.title = title
        self.detail = detail
        self.instance = instance
        self.errors = errors


class EcstasyBadRequestError(EcstasyAPIError):
    """Ошибка 400 Bad Request."""


class EcstasyUnauthorizedError(EcstasyAPIError):
    """Ошибка 401 Unauthorized."""


class EcstasyForbiddenError(EcstasyAPIError):
    """Ошибка 403 Forbidden."""


class EcstasyNotFoundError(EcstasyAPIError):
    """Ошибка 404 Not Found."""


class EcstasyConflictError(EcstasyAPIError):
    """Ошибка 409 Conflict."""


class EcstasyValidationError(EcstasyAPIError):
    """Ошибка валидации API."""


class EcstasyServerError(EcstasyAPIError):
    """Серверная ошибка API."""


class EcstasyResponseValidationError(EcstasyError):
    """Ошибка валидации ответа API через Pydantic."""
