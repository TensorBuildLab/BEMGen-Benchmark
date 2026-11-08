"""Build RIS entries for arXiv papers from the arXiv API record (no typed metadata).
usage: python arxiv_ris.py ref_list.txt out.ris"""
import re, sys, time, urllib.request, xml.etree.ElementTree as ET
ids = sorted({m.group(1) for l in open(sys.argv[1]) for m in [re.search(r"arXiv\.(\d{4}\.\d{4,5})", l)] if m})
ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
out, seen = [], set()
STOP = {"a", "an", "the", "on", "of", "for", "and", "to", "in", "with", "is", "are", "do", "can", "how", "what", "you", "we", "your", "beyond", "towards", "toward"}
for i in range(0, len(ids), 20):
    url = "http://export.arxiv.org/api/query?max_results=50&id_list=" + ",".join(ids[i:i+20])
    xml = urllib.request.urlopen(url, timeout=60).read()
    for e in ET.fromstring(xml).findall("a:entry", ns):
        aid = re.search(r"abs/(\d{4}\.\d{4,5})", e.find("a:id", ns).text).group(1)
        title = " ".join(e.find("a:title", ns).text.split())
        authors = [a.find("a:name", ns).text for a in e.findall("a:author", ns)]
        year = e.find("a:published", ns).text[:4]
        last = authors[0].split()[-1].lower()
        word = next((w for w in re.findall(r"[a-z0-9]+", title.lower()) if w not in STOP), "x")
        key = re.sub(r"[^a-z0-9]", "", f"{last}{year}{word}")
        while key in seen: key += "b"
        seen.add(key)
        lines = ["TY  - JOUR", f"ID  - {key}"] + [f"AU  - {' '.join(a.split()[-1:])}, {' '.join(a.split()[:-1])}" for a in authors]
        lines += [f"TI  - {title}", "T2  - arXiv preprint", f"PY  - {year}", f"DO  - 10.48550/arXiv.{aid}",
                  f"UR  - https://arxiv.org/abs/{aid}", f"N1  - arXiv:{aid}; record from arXiv API {time.strftime('%Y-%m-%d')}", "ER  - ", ""]
        out.append("\n".join(lines))
    time.sleep(3)
open(sys.argv[2], "w").write("\n".join(out))
print(len(ids), "ids;", len(out), "records")
