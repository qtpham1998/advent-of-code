from collections import defaultdict
from queue import Queue
import utils


def detect_start_marker(data: str, detect_message: bool) -> int:
    distinct_count = 14 if detect_message else 4
    seen_chars = defaultdict(lambda: 0)
    marker_builder = Queue()

    for i, c in enumerate(data):
        seen_chars[c] += 1
        marker_builder.put(c)

        if seen_chars[c] > 1:
            removed = ""
            while removed != c:
                removed = marker_builder.get()
                seen_chars[removed] -= 1

        if marker_builder.qsize() == distinct_count:
            return i + 1


if __name__ == "__main__":
    data = utils.read_whole_file()
    packet_start = detect_start_marker(data, detect_message=False)
    print("Part 1: First packet marker is detected after {} characters".format(packet_start))
    message_start = detect_start_marker(data, detect_message=True)
    print("Part 2: First message marker is detected after {} characters".format(message_start))
