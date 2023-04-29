from security.tokens.jwt_config_shema import JWTBrewSettings, TokenLocation, CookieSameSite
from settings import main_settings

jwt_cookie_csrf = JWTBrewSettings(
    token_location={TokenLocation.COOKIES},
    cookie_samesite=CookieSameSite.LAX if main_settings.APP_MODE.PROD else CookieSameSite.NONE
)
