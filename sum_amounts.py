from pathlib import Path

import pandas as pd


def main():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    # pd.set_option('display.max_colwidth', -1)

    frames = []
    for i in range(5, 12):
        frame = pd.read_csv(Path(f"./sources/Mangled/venmo_statement ({i}).csv"), header=1)
        frames.append(frame)

    combined = pd.concat(frames)
    print(combined[["Note", "From", "Amount (total)"]])

    # Get rid of bad characters
    amounts = combined["Amount (total)"].apply(lambda x: x.replace('+ $', ''))

    # Sum it
    print(amounts.astype("float32").sum())


if __name__ == "__main__":
    main()
