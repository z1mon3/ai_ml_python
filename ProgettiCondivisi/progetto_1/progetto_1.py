import pandas as pd


# TEST DEI LINK AI DATASET

def test_download_dataset_anno_2017():
    df = pd.read_csv("http://www.comune.torino.it/opendata/statistica/nascite_decessi/nati_circ_17.csv", encoding="latin1")
    df = df.rename(str.strip, axis='columns')

    c = "CIRCOSCRIZIONE" in df.columns
    f = "N_FEMMINE" in df.columns
    m = "N_MASCHI" in df.columns
    return (c, f, m)


def test_download_dataset_anno_2018():
    df = pd.read_csv("http://www.comune.torino.it/statistica/dati/2018/csv/D42018.csv", sep=";")
    df = df.rename(str.strip, axis='columns')

    c = "Circoscrizione di residenza" in df.columns
    f = "Femmine" in df.columns
    m = "Maschi" in df.columns
    return (c, f, m)


def test_download_dataset_anno_2019():
    df = pd.read_csv("http://www.comune.torino.it/statistica/dati/2019/csv/D4%20Nati%20anno%202019.csv")
    df = df.rename(str.strip, axis='columns')

    c = "Circoscrizione" in df.columns
    f = "Femmine" in df.columns
    m = "Maschi" in df.columns
    return (c, f, m)


def test_download_dataset_anno_2020():
    df = pd.read_csv("http://www.comune.torino.it/statistica/dati/2020/csv/D4%20Nati%20anno%202020.csv")
    df = df.rename(str.strip, axis='columns')

    c = "Circoscrizione_residenza" in df.columns
    f = "Femmine" in df.columns
    m = "Maschi" in df.columns
    return (c, f, m)


def test_download_dataset_anno_2021():
    df = pd.read_csv("http://www.comune.torino.it/statistica/dati/2021/csv/D4%20Nati%20anno%202021.csv", sep=";")
    df = df.rename(str.strip, axis='columns')

    c = "circoscrizione" in df.columns
    f = "femmine" in df.columns
    m = "maschi" in df.columns
    return (c, f, m)




