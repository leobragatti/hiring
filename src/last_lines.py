import os
import io


def last_lines(file_name: str, buffer_size: int = io.DEFAULT_BUFFER_SIZE):
    with open(file_name, errors="ignore") as tmp_file:
        offset = 0
        tmp_file.seek(0, os.SEEK_END)
        file_size = remaining_size = tmp_file.tell()
        while remaining_size > 0:
            offset = min(file_size, (offset + buffer_size))
            tmp_file.seek(file_size - offset)
            buffer = tmp_file.read(min(remaining_size, buffer_size))
            remaining_size -= buffer_size

            rows = buffer.split("\n")
            for row in rows[::-1]:
                yield f"{row}\n"
