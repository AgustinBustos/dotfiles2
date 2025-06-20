#!/usr/bin/env python3
"""Run IHaskell with Docker."""

import argparse
import json
import subprocess
import sys
import webbrowser
from pathlib import Path

IHASKELL_IMAGE = "ghcr.io/ihaskell/ihaskell-notebook:master"
CONTAINER_NAME = "ihaskell"
PORT = 8888

def main():
    args = parse_args()

    if args.mount_dir:
        mount_dir = Path(args.mount_dir).resolve()
        mount_flags = ["--volume", f"{mount_dir}:/home/jovyan/src"]
    else:
        mount_flags = []

    proc = subprocess.Popen([
        "docker", "run",
            "--name", CONTAINER_NAME,
            "--publish", f"{PORT}:8888",
            *mount_flags,
            IHASKELL_IMAGE,
    ])

    try:
        # wait for container
        wait_for_container()

        # open browser
        token = get_token()
        webbrowser.open_new_tab(f"http://localhost:{PORT}/lab?token={token}")

        # wait on process
        code = proc.wait()
        if code != 0:
            sys.exit(code)
    finally:
        subprocess.check_call(
            ["docker", "rm", "-f", CONTAINER_NAME],
            stdout=subprocess.DEVNULL,
        )

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        "mount_dir",
        help="The directory to mount into the container (default: don't mount anything)",
        metavar="MOUNT_DIR",
        nargs="?",
    )

    return parser.parse_args()

def wait_for_container():
    while True:
        out = subprocess.check_output(["docker", "ps", "-f", f"name={CONTAINER_NAME}", "-q"])
        if len(out) > 0:
            return

def get_token():
    while True:
        notebooks_proc = subprocess.check_output([
            "docker", "exec", CONTAINER_NAME,
            "jupyter",
            # "lab", 
            "notebook", "list", "--json",
        ])
        notebook = notebooks_proc.decode().split("\n")[0]
        if notebook:
            return json.loads(notebook)["token"]

if __name__ == "__main__":
    main()
