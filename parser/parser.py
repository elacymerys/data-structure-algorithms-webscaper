import csv


class CsvParser:
    @staticmethod
    def parse_to(filename, data):
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter=';')

            topic_idx = 0
            for task in data['tasks']:
                if task.id == 1:
                    topic_title = data['topics'][topic_idx].title
                    topic_idx += 1
                else:
                    topic_title = ''
                row = [topic_title, task.id, task.title, task.link]
                writer.writerow(row)
