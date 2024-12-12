# =========================================================================
# Type definition
# =========================================================================

# Define the type somehow...  The initial "" is simply here as a placeholder.
from cal_abstraction import *

TimeSpanSeq = NamedTuple("TimeSpanSeq", [("timespans", List[TimeSpan])])

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.

def new_time_span_seq() -> TimeSpanSeq:
    return TimeSpanSeq(timespans=[])

def tss_is_empty(tss: TimeSpanSeq)->bool:
    return len(tss.timespans)==0

def tss_plus_span(tss:TimeSpanSeq, ts:TimeSpan)->TimeSpanSeq:
    spans=tss.timespans
    for i,existing_tss in enumerate(spans):
        if ts_start(ts)<ts_start(existing_tss):
            spans.insert(i,ts)
            break
    else:
        spans.append(ts)
    return TimeSpanSeq(timespans=spans)

def tss_iter_spans(tss:TimeSpanSeq):
    return iter(tss[0])

def show_time_spans(tss:TimeSpanSeq):
    if tss_is_empty:
        return None
    else:
        for i in tss:
            print(i)


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result
