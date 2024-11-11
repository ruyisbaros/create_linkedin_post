
import json


def process_posts(raw_file_path: str, processed_file_path: str = "data/processed_posts.json",):
    enriched_posts = []
    with open(raw_file_path) as file:
        raw_posts = json.load(file)
        # print(raw_posts)
        for post in raw_posts:
            metada = extract_metadata(post["text"])
            post_with_metada = post | metada
            enriched_posts.append(post_with_metada)
            # print(post_with_metada)
        for epost in enriched_posts:
            print(epost)


def extract_metadata(post_text: str):
    return {
        "line_count": 10,
        "language": "English",
        "tags": ["politics", "tech"],
    }


if __name__ == '__main__':
    process_posts(raw_file_path="data/raw_posts.json")
