import hashlib
import time
from typing import Optional


class URLShortener:
    def __init__(self):
        self.ALLOWED_CHARS = "23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"  # без похожих символов
        self.MIN_LENGTH = 6
        self.MAX_ATTEMPTS = 3

    def _generate_hash(self, url: str, timestamp: float) -> str:
        """Generate a unique hash based on URL and timestamp."""
        combined = f"{url}{timestamp}".encode('utf-8')
        return hashlib.blake2b(combined, digest_size=8).digest()

    def _encode_base62(self, num: int) -> str:
        """Convert number to base62 string."""
        if num == 0:
            return self.ALLOWED_CHARS[0]

        arr = []
        base = len(self.ALLOWED_CHARS)
        while num:
            num, rem = divmod(num, base)
            arr.append(self.ALLOWED_CHARS[rem])
        return ''.join(reversed(arr))

    def generate_short_code(self, url: str, existing_codes: set) -> Optional[str]:
        """
        Generate a unique short code using a combination of techniques.

        Args:
            url: Original URL to shorten
            existing_codes: Set of existing short codes to check for collisions

        Returns:
            A unique short code or None if unable to generate after max attempts
        """
        timestamp = time.time()

        for attempt in range(self.MAX_ATTEMPTS):
            # Generate initial hash
            hash_bytes = self._generate_hash(url, timestamp + attempt)

            # Convert to integer and generate base62 string
            num = int.from_bytes(hash_bytes, byteorder='big')
            short_code = self._encode_base62(num)

            # Ensure minimum length
            if len(short_code) < self.MIN_LENGTH:
                short_code = short_code.ljust(self.MIN_LENGTH, self.ALLOWED_CHARS[0])

            # Trim to maximum length if needed
            short_code = short_code[:8]

            # Check for collisions
            if short_code not in existing_codes:
                return short_code

        return None
