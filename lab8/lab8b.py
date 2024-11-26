# =========================================================================
# Type definition
# =========================================================================

# Define the type somehow...  The initial "" is simply here as a placeholder.
from cal_abstraction import *
TimeSpanSeq = []

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.

def new_time_span_seq():
    return []


def tss_is_empty(tss):
    return len(tss)==0


def tss_plus_span(tss, ts):
    for i,existing_tss in enumerate(tss):
        if ts_start(ts)<ts_start(existing_tss):
            tss.insert(i,ts)
    return tss

def tss_iter_spans(tss):
    pass


def show_time_spans(tss):
    pass


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result
