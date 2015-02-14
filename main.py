from FestivalScraper import FestivalScraper

def main():
    with open('festivals.txt') as f:
        for line in f.readlines():
            t = FestivalScraper(line)
            artits = t.get_artists()

if __name__ == "__main__":
    main()
