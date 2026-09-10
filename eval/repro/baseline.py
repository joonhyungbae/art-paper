"""Input–gold baseline, novel-overlap contamination, adjusted margins, 3-way tally.
Runs on eval/pilot Tier 1 cases using the paper's own instrumentation engine."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "eval"))
import instrumentation as I

PILOT = ROOT / "eval" / "pilot"
CASES = ["sa23-02","sa23-04","sa23-07","sa23-10","sa24-01","sa24-03","sa24-04","sa24-10",
         "sa24-12","sa24-15","sa24-18","sa25-09","sa25-11","sa25-12","sa25-14"]
CLEAN = ["sa23-10-clean","sa24-18-clean"]  # sa25-ck-clean has no gold dir
INPUT_FILES = ["documentation.md","concept_memo.md","exhibition_record.md"]
NOISE = 0.02
OUT = Path(__file__).resolve().parent / "tier1_baseline.json"

def blob(sections, kind):
    return " ".join(sections[k] for k,_,kd in I.LAYERS if kd==kind and k in sections)

def novel_overlap(recon, gold, inp, n=8):
    tr, tg, ti = I._tokens(recon), I._tokens(gold), I._tokens(inp)
    nr = I._ngrams(tr, n); ng = set(I._ngrams(tg, n)); ni = set(I._ngrams(ti, n))
    if not nr: return 0.0, 0.0
    tot = sum(nr.values())
    in_gold = sum(c for g,c in nr.items() if g in ng)
    in_gold_not_input = sum(c for g,c in nr.items() if g in ng and g not in ni)
    return round(in_gold/tot,4), round(in_gold_not_input/tot,4)

def run(case):
    d = PILOT/case
    gold = I._read(d/"gold"/"paper.md"); recon = I._read(d/"reconstruction"/"paper.md")
    inp = "\n".join(I._read(d/"input"/f) for f in INPUT_FILES)
    gs, rs = I._split_sections(gold), I._split_sections(recon)
    gT, gG, rT, rG = blob(gs,"transferable"), blob(gs,"generative"), blob(rs,"transferable"), blob(rs,"generative")
    T = I._token_jaccard(gT, rT); G = I._token_jaccard(gG, rG)
    T_in = I._token_jaccard(gT, inp); G_in = I._token_jaccard(gG, inp)
    c_rg, c_novel = novel_overlap(recon, gold, inp)
    c_ig = I._ngram_containment(inp, gold, 8)      # input 8-grams found in gold
    c_gi = I._ngram_containment(gold, inp, 8)      # gold 8-grams found in input (how much of gold is in the pack)
    anch = I.anchoring_rate(recon)
    m = round(T-G,4); m_in = round(T_in-G_in,4); m_adj = round(m-m_in,4)
    tally = "support" if m>NOISE else ("invert" if m<-NOISE else "noise")
    return dict(case=case, T=T, G=G, margin=m, T_in=T_in, G_in=G_in, margin_in=m_in, margin_adj=m_adj,
                T_resid=round(T-T_in,4), G_resid=round(G-G_in,4),
                contam_recon_in_gold=c_rg, contam_novel=c_novel, input_in_gold=c_ig, gold_in_input=c_gi,
                anchoring=anch["rate"], claims=anch["claims_detected"], tally=tally,
                gold_words=len(I._tokens(gold)), input_words=len(I._tokens(inp)), recon_words=len(I._tokens(recon)))

rows = [run(c) for c in CASES]
clean = [run(c) for c in CLEAN]
json.dump({"tier1":rows,"clean":clean}, open(OUT,"w"), indent=1)

hdr = ["case","T","G","margin","T_in","G_in","margin_in","margin_adj","T_resid","contam_recon_in_gold","contam_novel","gold_in_input","anchoring","tally"]
print("\t".join(hdr))
for r in rows+clean:
    print("\t".join(str(r[h]) for h in hdr))
import statistics as st
print("\nTier1 tally:", {k:sum(1 for r in rows if r["tally"]==k) for k in ("support","noise","invert")})
print("adj margin >noise:", sum(1 for r in rows if r["margin_adj"]>NOISE), "| >0:", sum(1 for r in rows if r["margin_adj"]>0))
print("mean T", round(st.mean(r["T"] for r in rows),3), "mean T_in", round(st.mean(r["T_in"] for r in rows),3),
      "mean G", round(st.mean(r["G"] for r in rows),3), "mean G_in", round(st.mean(r["G_in"] for r in rows),3))
print("mean margin", round(st.mean(r["margin"] for r in rows),3), "mean margin_in", round(st.mean(r["margin_in"] for r in rows),3),
      "mean margin_adj", round(st.mean(r["margin_adj"] for r in rows),3))
print("mean contam recon-in-gold", round(st.mean(r["contam_recon_in_gold"] for r in rows),4),
      "novel", round(st.mean(r["contam_novel"] for r in rows),4), "max novel", max(r["contam_novel"] for r in rows))
print("mean gold_in_input", round(st.mean(r["gold_in_input"] for r in rows),4))
a=[r["anchoring"] for r in rows if r["anchoring"] is not None]; print("anchoring mean", round(st.mean(a),3), "n", len(a), "claims", sum(r["claims"] for r in rows))

# Tier 2 tallies from aggregate JSON
t2 = json.load(open(ROOT / "corpus_expansion/selected_corpus/tier2_n23_pilot_results.json"))["tier2_n23"]
def tal(rs): return {k:sum(1 for r in rs if (r["margin"]>NOISE if k=="support" else r["margin"]<-NOISE if k=="invert" else abs(r["margin"])<=NOISE)) for k in ("support","noise","invert")}
print("\nTier2 n", len(t2), "tally", tal(t2), "elevated [0.03,0.10):", sum(1 for r in t2 if 0.03<=r["contam"]<0.10), "max contam", max(r["contam"] for r in t2))
print("Tier2 supported(sign):", sum(1 for r in t2 if r["margin"]>0))
print("Tier2 by venue:", {v:(sum(1 for r in t2 if r["case"].startswith(v) and r["margin"]>0), sum(1 for r in t2 if r["case"].startswith(v))) for v in ("isea","leo","dc")})
