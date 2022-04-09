#!/usr/bin/env python
import gzip
import json
import os
import requests

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rrltdb.models import Tiploc


def main():

    # Check if the tiploc file exists and download if it doesn't
    if not os.path.exists("/tmp/corpus.json.gz"):
        print("Corpus file does not exist, downloading")
        nrod_user = os.getenv("NROD_USER")
        nrod_pass = os.getenv("NROD_PASS")
        corpus_uri = f"https://{nrod_user}:{nrod_pass}@datafeeds.networkrail.co.uk/ntrod/SupportingFileAuthenticate?type=CORPUS"
        corpus_dl = requests.get(corpus_uri, allow_redirects=True)
        open("/tmp/corpus.json.gz", "wb").write(corpus_dl.content)


    tiplocs_checked = 0
    tiplocs_created = 0

    engine = create_engine(os.getenv("ALEMBIC_DB_URI"))
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    tiploc_json = []

    with gzip.open("/tmp/corpus.json.gz", 'r') as tiploc_data:
        lines = tiploc_data.readlines()
        for line in lines:
            tiploc_json.append(json.loads(line))

    for tiploc_entry in tiploc_json[0]["TIPLOCDATA"]:
        """      {
        "NLC": "999815",
        "STANOX": "06221",
        "TIPLOC": "WEST530",
        "3ALPHA": "",
        "UIC": "",
        "NLCDESC": "WESTERTON SIG YH530",
        "NLCDESC16": ""
      }"""

        # Find the tiploc if it exists
        tiplocs_checked = tiplocs_checked + 1
        curr_tiploc = session.query(Tiploc).filter_by(tiploc_code=tiploc_entry["TIPLOC"])
        if curr_tiploc.count() < 1:
            tiplocks_created = tiplocs_created + 1
            new_tiploc = Tiploc()
            new_tiploc.tiploc_code = tiploc_entry["TIPLOC"]
            new_tiploc.nalco = tiploc_entry["NLC"]
            new_tiploc.stanox = tiploc_entry["STANOX"]
            new_tiploc.crs_code = tiploc_entry["3ALPHA"]
            new_tiploc.description = tiploc_entry["NLCDESC"]
            new_tiploc.tps_description = tiploc_entry["NLCDESC16"]
            session.add(new_tiploc)
            session.commit()

    print(f"Checked={tiplocs_checked} created={tiplocs_created}")


if __name__ == "__main__":
    main()
