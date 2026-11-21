import pygame
import json
import csv
import os
import time
from datetime import datetime

pygame.init()

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Input Tester")

font = pygame.font.SysFont(None, 36)

STATS_FILE = "stats.json"
CSV_FILE = "history.csv"

left_clicks = 0
right_clicks = 0
key_count = 0

current_cps = 0
current_kps = 0

click_times = []
key_times = []

typed_text = ""

key_stats = {
    "W": 0,
    "A": 0,
    "S": 0,
    "D": 0,
    "SPACE": 0,
    "ENTER": 0
}


def ensure_files():
    if not os.path.exists(STATS_FILE):
        default_stats = {
            "best_cps": 0,
            "best_kps": 0,
            "history": []
        }

        with open(STATS_FILE, "w", encoding="utf-8") as f:
            json.dump(
                default_stats,
                f,
                indent=4,
                ensure_ascii=False
            )

    if not os.path.exists(CSV_FILE):
        with open(
            CSV_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:
            writer = csv.writer(f)

            writer.writerow([
                "Time",
                "LeftClicks",
                "RightClicks",
                "KeyPresses",
                "BestCPS",
                "BestKPS"
            ])


def load_stats():
    with open(STATS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_stats():
    with open(STATS_FILE, "w", encoding="utf-8") as f:
        json.dump(
            stats,
            f,
            indent=4,
            ensure_ascii=False
        )


def export_csv():
    with open(
        CSV_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            left_clicks,
            right_clicks,
            key_count,
            stats["best_cps"],
            stats["best_kps"]
        ])


def update_cps():
    global current_cps

    now = time.time()

    click_times[:] = [
        t for t in click_times
        if now - t <= 1
    ]

    current_cps = len(click_times)

    if current_cps > stats["best_cps"]:
        stats["best_cps"] = current_cps


def update_kps():
    global current_kps

    now = time.time()

    key_times[:] = [
        t for t in key_times
        if now - t <= 1
    ]

    current_kps = len(key_times)

    if current_kps > stats["best_kps"]:
        stats["best_kps"] = current_kps


def reset_stats():
    global left_clicks
    global right_clicks
    global key_count
    global typed_text

    left_clicks = 0
    right_clicks = 0
    key_count = 0
    typed_text = ""

    for key in key_stats:
        key_stats[key] = 0


ensure_files()
stats = load_stats()

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            click_times.append(time.time())

            if event.button == 1:
                left_clicks += 1

            elif event.button == 3:
                right_clicks += 1

        elif event.type == pygame.KEYDOWN:

            key_count += 1
            key_times.append(time.time())

            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_r:
                reset_stats()

            elif event.key == pygame.K_c:
                export_csv()

            elif event.key == pygame.K_BACKSPACE:
                typed_text = typed_text[:-1]

            else:
                typed_text += event.unicode

            if event.key == pygame.K_w:
                key_stats["W"] += 1

            elif event.key == pygame.K_a:
                key_stats["A"] += 1

            elif event.key == pygame.K_s:
                key_stats["S"] += 1

            elif event.key == pygame.K_d:
                key_stats["D"] += 1

            elif event.key == pygame.K_SPACE:
                key_stats["SPACE"] += 1

            elif event.key == pygame.K_RETURN:
                key_stats["ENTER"] += 1

    update_cps()
    update_kps()

    screen.fill((20, 20, 20))

    y = 20

    lines = [
        "Input Tester",
        "",
        f"Left Clicks : {left_clicks}",
        f"Right Clicks: {right_clicks}",
        f"Total Clicks: {left_clicks + right_clicks}",
        "",
        f"Current CPS : {current_cps}",
        f"Best CPS    : {stats['best_cps']}",
        "",
        f"Current KPS : {current_kps}",
        f"Best KPS    : {stats['best_kps']}",
        "",
        f"W     : {key_stats['W']}",
        f"A     : {key_stats['A']}",
        f"S     : {key_stats['S']}",
        f"D     : {key_stats['D']}",
        f"SPACE : {key_stats['SPACE']}",
        f"ENTER : {key_stats['ENTER']}",
        "",
        "R = Reset",
        "C = Export CSV",
        "ESC = Exit",
        "",
        f"Typed: {typed_text[-40:]}"
    ]

    for line in lines:
        text = font.render(
            line,
            True,
            (255, 255, 255)
        )
        screen.blit(text, (20, y))
        y += 30

    pygame.display.flip()
    clock.tick(60)

stats["history"].append({
    "time": datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    ),
    "left_clicks": left_clicks,
    "right_clicks": right_clicks,
    "key_count": key_count,
    "best_cps": stats["best_cps"],
    "best_kps": stats["best_kps"]
})

save_stats()

pygame.quit()